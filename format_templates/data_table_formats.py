BLOCK_HEADER = """
{% extends "base.html" %}

{% block content %}
"""


HEADER = """<div class="clearfix _ikh">
        <div class="_4bl9">
            <div class="_li">
                <div class="_a705">
                    <div>
                        <div class="_3-8y _3-95 _a709">
                            <div style="background-color: #3578E5" class="_a70c"><img
                                    src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAQAAAC1+jfqAAAABGdBTUEAALGPC/xhBQAAACBjSFJNAAB6JgAAgIQAAPoAAACA6AAAdTAAAOpgAAA6mAAAF3CculE8AAAAB3RJTUUH4wUJExktKVPrMgAAAAJiS0dEAP+Hj8y/AAAAx0lEQVR42n3LsUpCYRiA4W8SZ6WmwmjxGqIgmtwDB5fwCoQgkKBuwLWpZm/gjG6tx83xtLg1lRQKNoRPaPwYlj3ryxuJEw8KMzOFe8fxk4rMpkwl5aonfylUY8nANoNlbvhPI/QlC7kPwEQX9MNY0opQN8JQTQeMQ3qyWFHWVLJvCubhBUztKWkqx4oM8Bpy0HFgiJF6hJYkDzegawKYyy0kt2HXm23e7USEtm3a8U3Pb58uI3Fm06OjWHPo2Z1T565cu1Bbty8r7oMp62N1aQAAACV0RVh0ZGF0ZTpjcmVhdGUAMjAxOS0wNS0xMFQwMjoyNTo0NS0wNzowMC7bZsEAAAAldEVYdGRhdGU6bW9kaWZ5ADIwMTktMDUtMTBUMDI6MjU6NDUtMDc6MDBfht59AAAAAElFTkSuQmCC" />
                            </div>
                            <div class="_a70d">
                                <div class="_a70e">{thread_name}</div>
                            </div>
                        </div>
                    </div>
                    <div class="_a706" role="main">
"""

IMAGE_BODY = """
                        <div class="_a6-g">
                            <div class="_2ph_ _a6-h _a6-i">{sender_name}</div>
                            <div class="_2ph_ _a6-p">
                                <div>
                                    <a target="_blank" href={{{{ url_for('static', path="{uri}") }}}}>
                                        <img src={{{{ url_for('static', path="{uri}") }}}} class="_a6_o _3-96">
                                    </a>
                                </div>
                            </div>
                            <div class="_3-94 _a6-o">
                                <div class="_a72d">{timestamp}</div>
                            </div>
                            {reaction_body}
                        </div>
"""


STREAMING_BODY = """
                        <div class="_a6-g">
                            <div class="_2ph_ _a6-h _a6-i">{sender_name}</div>
                            <div class="_2ph_ _a6-p">
                                <div>
                                    <{media_tag} src={{{{ url_for('static', path="{uri}") }}}} controls=1 class"_a6_o _3-96">
                                        <a target="_blank" href={{{{ url_for('static', path="{uri}") }}}}>
                                            Click for {media_tag}.
                                        </a>
                                    </{media_tag}>
                                </div>
                            </div>
                            <div class="_3-94 _a6-o">
                                <div class="_a72d">{timestamp}</div>
                            </div>
                            {reaction_body}
                        </div>
"""


BODY = """
                        <div class="_a6-g">
                            <div class="_2ph_ _a6-h _a6-i">{sender_name}</div>
                            <div class="_2ph_ _a6-p">
                                <div>
                                    <div>{text}</div>
                                </div>
                            </div>
                            <div class="_3-94 _a6-o">
                                <div class="_a72d">{timestamp}</div>
                            </div>
                            {reaction_body}
                        </div>
"""


REACTION_BODY = """
                                <div>
                                    <ul class="_a6-q">
                                        {reaction_content}
                                    </ul>
                                </div>
"""


REACTION_CONTENT = """
                                        <li>
                                            <span>
                                                {reaction} {actor}
                                            </span>
                                        </li>
"""


FOOTER = """
                    </div>
                </div>
            </div>
        </div>
    </div>
"""


BLOCK_FOOTER = """
{% endblock %}
"""


MEDIA_MAP = {
    "mp4": (STREAMING_BODY, "video"),
    "jpeg": (IMAGE_BODY, None),
    "webp": (IMAGE_BODY, None),
    "gif": (IMAGE_BODY, None),
    "wav": (STREAMING_BODY, "audio"),
}
