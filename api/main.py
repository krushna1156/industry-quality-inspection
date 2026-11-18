from fastapi import FastAPI, UploadFile, File, HTTPException
from utils.preprocess import preprocess_image
from models.inference import QualityInspectionModel
import uvicorn

app = FastAPI(
    title="Industrial Quality Inspection API",
    description="Low-latency API for automated visual inspection using CNNs and OpenCV."
)

# Initialize deep learning model
inspection_model = QualityInspectionModel()

@app.get("/")
def health_check():
    return {"status": "Active", "message": "API endpoints are fully containerized and running."}

@app.post("/predict/")
async def predict_defect(file: UploadFile = File(...)):
    """
    Receives an industrial production item image, applies OpenCV preprocessing,
    and returns a CNN inference result.
    """
    if not file.content_type.startswith("image/"):
        raise HTTPException(status_code=400, detail="Invalid file format. Please upload an image.")
        
    try:
        image_bytes = await file.read()
        
        # Apply normalization, thresholding, edge filtering
        processed_img, _ = preprocess_image(image_bytes)
        
        # Run CNN inference
        result = inspection_model.predict(processed_img)
        
        return {
            "filename": file.filename,
            "prediction": result
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
