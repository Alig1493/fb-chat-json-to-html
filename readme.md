# FB Chat JSON to HTML

![FB Chat JSON to HTML](image.png)

A simple tool to convert Facebook chat JSON files into a readable HTML format. This project is designed to make it easier to browse and analyze your Facebook chat history in a user-friendly interface.

## Features

- Converts Facebook chat JSON files into clean, readable HTML.
- Preserves message timestamps, sender names, and message content.
- Supports media files by linking them to the HTML output.
- Lightweight and easy to use.

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/your-username/fb-chat-json-to-html.git
    ```
2. Navigate to the project directory:
    ```bash
    cd fb-chat-json-to-html
    ```
3. Set up a virtual environment:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```
4. Install dependencies using `pip-tools`:
    ```bash
    pip install pip-tools
    pip-compile requirements.in
    pip install -r requirements.txt
    ```

## Usage

1. Export your Facebook chat data as a JSON file from Facebook's data download tool.
2. Place the JSON file in the project directory.
3. If your chat includes media files, upload them as a zipped folder. Extract the contents of the zip file into the `static` folder in the project directory. The HTML output will link to these media files.
4. Run the conversion script:
    ```bash
    node convert.js your-chat-file.json
    ```
5. Open the generated `output.html` file in your browser to view the chat.

## Running the Server

To start the server for development or production, use the following commands:

### Development Server
Run the FastAPI development server:
```bash
uvicorn app.main:app --reload
```
Refer to the [FastAPI documentation](https://fastapi.tiangolo.com/) for more details on running and configuring the development server.

### Production Server
Run the FastAPI production server:
```bash
uvicorn app.main:app --host 0.0.0.0 --port 8000
```
Refer to the [FastAPI deployment documentation](https://fastapi.tiangolo.com/deployment/) for best practices and deployment options.

## Contributing

Contributions are welcome! Feel free to submit issues or pull requests to improve the project.

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.