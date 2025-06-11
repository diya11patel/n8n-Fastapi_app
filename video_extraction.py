from fastapi import FastAPI, File, UploadFile, HTTPException

from fastapi.responses import JSONResponse
import requests
import httpx
import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
logger.addHandler(logging.StreamHandler())



app = FastAPI()


N8N_WEBHOOK_URL = "Your url"

@app.post("/submit-video/")
async def submit_video(video: UploadFile = File(...)):
    # Prepare the video file for sending
    logger.info(f"Reading video {video.filename}")
    files = {
        "Video": (video.filename, await video.read(), video.content_type)
    }

    try:
        logger.info("Submitting video to n8n")
        # Call n8n workflow via form trigger
        response = requests.post(N8N_WEBHOOK_URL, files=files)
        logger.info("n8n workflow triggered")
        # If failed, return error response
        if response.status_code != 200:
            return JSONResponse(
                status_code=response.status_code,
                content={
                    "error": "n8n workflow failed",
                    "details": response.text
                }
            )

        # Return parsed JSON response from n8n
        return JSONResponse(content=response.json())

    except Exception as e:
        return JSONResponse(
            status_code=500,
            content={"error": "Internal Server Error", "details": str(e)}
        )


# @app.post("/upload-video/")
# async def gitupload_video(video: UploadFile = File(...)):
#     # Optionally, save the video temporarily or process it
#     # For triggering n8n, you can use an HTTP request
#     try:
#         # Trigger n8n workflow (see next section)
#         response = await trigger_n8n_workflow(video)
#         return response
#     except Exception as e:
#         raise HTTPException(status_code=500, detail=str(e))
    

# async def trigger_n8n_workflow(video: UploadFile):
#     async with httpx.AsyncClient() as client:
#         files = {'video': (video.filename, await video.read(), video.content_type)}
#         response = await client.post(N8N_WEBHOOK_URL, files=files)
#         return response.json()
    


