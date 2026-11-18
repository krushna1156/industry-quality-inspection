import cv2
import numpy as np

def preprocess_image(image_bytes: bytes) -> tuple:
    """
    OpenCV preprocessing routine: decodes, resizes, normalizes, 
    and applies thresholding/edge filtering for CNN feature extraction.
    """
    # Convert bytes to numpy array
    nparr = np.frombuffer(image_bytes, np.uint8)
    img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
    
    if img is None:
        raise ValueError("Invalid image data")
        
    # Resize to standard CNN input size
    img_resized = cv2.resize(img, (224, 224))
    
    # Grayscale conversion
    gray = cv2.cvtColor(img_resized, cv2.COLOR_BGR2GRAY)
    
    # Apply Thresholding & Canny Edge Filtering (as per resume)
    _, thresh = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)
    edges = cv2.Canny(gray, 100, 200)
    
    # Normalization (0-1 scale) for variable lighting inputs
    normalized_img = img_resized.astype('float32') / 255.0
    
    return normalized_img, edges
