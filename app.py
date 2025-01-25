from time import sleep
from datetime import datetime
from typing import Generator

from flask import Flask, Response

app = Flask(__name__)

SSE_DATE_FORMAT = '%Y-%m-%d %H:%M:%S'
SSE_INTERVAL_SECONDS = 1


@app.route('/sse/current-time', methods=['GET'])
def stream_server_sent_events() -> Response:
    """
    Endpoint for streaming Server-Sent Events (SSE) with the current time.

    Returns:
        Response: HTTP response in text/event-stream format
    """
    return Response(
        generate_sse_data(),
        mimetype='text/event-stream',
        headers={'Cache-Control': 'no-cache'}
    )


def generate_sse_data() -> Generator[str, None, None]:
    """
    Generates continuous SSE data with the current time formatted.

    Yields:
        str: SSE events in the format 'data: <timestamp>\n\n'
    """
    while True:
        current_time = datetime.now().strftime(SSE_DATE_FORMAT)
        yield f'data: {current_time}\n\n'
        sleep(SSE_INTERVAL_SECONDS)


if __name__ == "__main__":
    app.run()
