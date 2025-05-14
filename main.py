import os
from fastapi import FastAPI, File, UploadFile
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
from service import PaddyPredictionService
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI()

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Initialize the prediction service
prediction_service = PaddyPredictionService()

@app.get("/")
async def root():
    return {"message": "Paddy Disease Prediction API is running"}

@app.post("/predict/disease")
async def predict_disease(file: UploadFile = File(...)):
    try:
        contents = await file.read()
        result = prediction_service.predict_disease(contents)
        return result
    except Exception as e:
        logger.error(f"Error in disease prediction: {str(e)}")
        return {"error": str(e)}

@app.post("/predict/variety")
async def predict_variety(file: UploadFile = File(...)):
    try:
        contents = await file.read()
        result = prediction_service.predict_variety(contents)
        return result
    except Exception as e:
        logger.error(f"Error in variety prediction: {str(e)}")
        return {"error": str(e)}

@app.post("/predict/age")
async def predict_age(file: UploadFile = File(...)):
    try:
        contents = await file.read()
        result = prediction_service.predict_age(contents)
        return result
    except Exception as e:
        logger.error(f"Error in age prediction: {str(e)}")
        return {"error": str(e)}

if __name__ == "__main__":
    # Get port from environment variable or use default
    port = int(os.getenv("PORT", 8000))
    # Run the server
    uvicorn.run(app, host="0.0.0.0", port=port)
