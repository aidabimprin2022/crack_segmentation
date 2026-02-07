"""
Example inference script for crack segmentation in images of historic churches.

The script loads a pre-trained TorchScript model, applies the required
ImageNet normalization, and produces a binary crack segmentation mask.

Please, download the model from the following Google Drive link:
    https://drive.google.com/file/d/13AvEer_20VIG60lp6pryh0vJZdHE7njk/view?usp=sharing
"""

import cv2
import torch
import torchvision.transforms.v2 as transforms
import numpy as np

# ImageNet normalization parameters used during training
IMAGENET_MEAN = [0.485, 0.456, 0.406]
IMAGENET_STD = [0.229, 0.224, 0.225]

# Input image and output mask paths
IMAGE_PATH = "sample_image.jpg"
OUTPUT_PATH = "sample_image_mask.png"

# Load the pre-trained TorchScript model in inference mode
net = torch.jit.load("crack_segmentation_unet.pt", map_location="cpu")
net.eval()

# Define the preprocessing pipeline required by the model
preprocess = transforms.Compose([
    transforms.ToImage(),
    transforms.ToDtype(torch.float32, scale=True),
    transforms.Normalize(
        mean=IMAGENET_MEAN, 
        std=IMAGENET_STD
    ),
])

# Read input image from disk
img = cv2.imread(IMAGE_PATH)
if img is None:
    raise FileNotFoundError(f"Image not found: {IMAGE_PATH}")

# Convert image from BGR (OpenCV default) to RGB
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# Apply preprocessing and add batch dimension
x = preprocess(img).unsqueeze(0) 

# Perform inference
with torch.inference_mode():
    y = net(x)
    y = torch.sigmoid(y)

# Convert output to a NumPy array
mask = y.squeeze().cpu().numpy() 

# Binarize the probability map
binary_mask = (mask > 0.5).astype(np.uint8) * 255

# Save the resulting segmentation mask
cv2.imwrite(OUTPUT_PATH, binary_mask)

print(f"Segmentation saved to: {OUTPUT_PATH}")
