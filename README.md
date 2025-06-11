# Video Submission Service to n8n

This project is a simple FastAPI application that provides an endpoint to post a video file and forward it to a pre-configured n8n webhook to get some information eyraction out of the video.

## Prerequisites

*   Python 3.8+
*   pip

## Setup

1.  **Clone the repository (if you haven't already):**
    ```bash
    git clone <your-repository-url>
    cd n8n_video_procrssor
    ```

2.  **Create and activate a virtual environment (recommended):**
    ```bash
    python -m venv venv
    # On Windows
    venv\Scripts\activate
    # On macOS/Linux
    source venv/bin/activate
    ```

3.  **Install dependencies:**
    Create a `requirements.txt` file with the following content:
    ```txt
    fastapi
    uvicorn[standard]
    requests
    python-multipart
    ```
    Then run:
    ```bash
    pip install -r requirements.txt
    ```

4.  **Configure n8n Webhook URL:**
    The application expects the n8n webhook URL. It's currently hardcoded in `video_extraction.py`. For better practice, consider using an environment variable.

## Running the Application

Use Uvicorn to run the FastAPI application:
```bash
uvicorn video_extraction:app --reload
```
The application will typically be available at `http://127.0.0.1:8000`.

## Usage

### Submit a Video

*   **Endpoint:** `POST /submit-video/`
*   **Request Type:** `multipart/form-data`
*   **Form Data:**
    *   `video`: The video file to upload.

**Example using cURL:**
```bash
curl -X POST -F "video=@/path/to/your/video.mp4" http://127.0.0.1:8000/submit-video/
```

The response will be the JSON response from the n8n workflow if successful, or an error message.

### Video processing json 
The json file for the n8n workflow. Import it in the n8n to have the workflow directly on your canvas