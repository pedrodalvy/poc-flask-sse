# Flask SSE Proof of Concept

This project serves as a Proof of Concept (POC) to validate the use of Server-Sent Events (SSE) with Flask. It's a simple and straightforward implementation, demonstrating how to establish a persistent connection where the server pushes updates to the client.

-   Demonstrates a basic SSE implementation.
-   Uses Flask to create a simple web server.
-   Shows the current date and time, updated every second.

## 🚀 Getting Started

These instructions will get you a copy of the project up and running on your local machine.

### Prerequisites

-   Python 3.x
-   Poetry (for dependency management)

### Installation

1.  Clone the repository:

    ```bash
    git clone git@github.com:pedrodalvy/poc-flask-sse.git
    cd poc-flask-sse
    ```

2.  Install dependencies using Poetry:

    ```bash
    poetry install
    ```

### Running the Application

-   To start the application, run the following command:

    ```bash
    flask run
    ```

-   This will start the Flask development server on `http://localhost:5000`.

## 🔍 Example Usage

The application exposes a single endpoint that streams the current date and time. The updates are sent every second.

### Validating with cURL

You can validate the SSE stream using `curl` in your terminal:

```bash
curl -N http://localhost:5000
```

**Expected Output:**

| Output                | Description                                      |
|:----------------------|:-------------------------------------------------|
| `2023-10-27 10:30:00` | The current date and time, updated every second. |
| `2023-10-27 10:30:01` | ...                                              |
| `2023-10-27 10:30:02` | ...                                              |

The `-N` flag ensures that `curl` doesn't buffer the output, allowing you to see each update as it is received.

### Endpoint Details

| Endpoint | Method | Description                                                                   |
|:---------|:-------|:------------------------------------------------------------------------------|
| `/`      | GET    | Streams the current date and time, updating the content every second via SSE. |

## 🛠️ Additional Notes

-   This project is a basic POC and doesn't include any tests.
-   No additional libraries outside of Flask's built-in capabilities were used.
-   The core of the application is contained in a single file, `app.py`.
