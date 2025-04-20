import contextlib
from datetime import datetime
import io
import logging
import os
import zipfile
from fastapi import FastAPI, Request, File, UploadFile
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import json

from format_templates.data_table_formats import (
    BLOCK_HEADER,
    HEADER,
    BLOCK_FOOTER,
    BODY,
    FOOTER,
    MEDIA_MAP,
    REACTION_BODY,
    REACTION_CONTENT,
)

rendering_logger = logging.getLogger("rendering.error")
app = FastAPI()

# Mount static files (if needed)
app.mount("/static", StaticFiles(directory="static"), name="static")

# Set up Jinja2 templates
templates = Jinja2Templates(directory="templates")


# Load JSON data from an uploaded file
async def load_json_data(file: UploadFile):
    content = await file.read()
    return json.loads(content)


# Extract ZIP file data from an uploaded file to static folder
async def extract_zipfile_data(file: UploadFile):
    # TODO:
    # * What if static/media already exists
    # * Make media upload optional, show error if no media zip exists
    # and one is not supplied
    # * If media folder was once uploaded before
    #   * Show in html webpage that a folder already exists and
    #   empty field for zipfile upload.
    #   * Allow user an option to delete (maybe a checkmark) previous media
    #   upload and allow uploading a new one.
    content = await file.read()
    with zipfile.ZipFile(io.BytesIO(content), "r") as zip_ref:
        zip_ref.extractall(f"{os.getcwd()}/static")


async def epoch_to_datetime(epoch_time: float):
    dt_object = datetime.fromtimestamp(epoch_time / 1000.0)
    return dt_object.strftime("%b %d, %Y %I:%M:%S %p")


@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse("landing_body.html", {"request": request})


@app.post("/render", response_class=HTMLResponse)
async def render_data(
    request: Request,
    # file: UploadFile = File(...),
    json_file: UploadFile = File(
        ..., description="JSON file upload", spool_temporary_file=True
    ),
    zip_file: UploadFile = File(
        ..., description="ZIP file upload", spool_temporary_file=True
    ),
):
    output_file_name = "templates/data_table.html"
    errors = []
    try:
        with contextlib.suppress(FileNotFoundError):
            os.remove(output_file_name)
        await extract_zipfile_data(zip_file)
        loaded_data = await load_json_data(json_file)
        with open(output_file_name, "a") as data_table_file:
            data_table_file.write(BLOCK_HEADER + "\n")
            data_table_file.write(
                HEADER.format(
                    thread_name=loaded_data.get("threadName", "").split("_")[0]
                )
                + "\n"
            )
            for message in loaded_data.get("messages", []):
                reactions = []
                sender_name = message.get("senderName", "")
                for reaction in message["reactions"]:
                    reaction_content = REACTION_CONTENT.format(
                        reaction=reaction["reaction"], actor=reaction["actor"]
                    )
                    reactions.append(
                        REACTION_BODY.format(reaction_content=reaction_content)
                    )
                if message.get("type") == "text":
                    data_table_file.write(
                        BODY.format(
                            text=message.get("text", ""),
                            sender_name=sender_name,
                            timestamp=await epoch_to_datetime(message.get("timestamp")),
                            reaction_body="\n".join(reactions),
                        )
                        + "\n"
                    )
                if message.get("type") == "media":
                    for content in message["media"]:
                        try:
                            media_template, media_tag = MEDIA_MAP[
                                content["uri"].split(".")[-1]
                            ]
                            data_table_file.write(
                                media_template.format(
                                    media_tag=media_tag,
                                    uri=content["uri"][2:],
                                    sender_name=sender_name,
                                    timestamp=await epoch_to_datetime(
                                        message.get("timestamp")
                                    ),
                                    reaction_body="\n".join(reactions),
                                )
                            )
                        except KeyError as key_error:
                            errors.append(str(key_error))

            data_table_file.write(FOOTER)
            data_table_file.write(BLOCK_FOOTER)
            rendering_logger.error("\n".join(errors))
        return templates.TemplateResponse("data_table.html", {"request": request})
    except json.JSONDecodeError:
        return templates.TemplateResponse(
            "error.html", {"request": request, "error": "Invalid JSON file"}
        )
