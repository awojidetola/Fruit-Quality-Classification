import streamlit as st
import torch
import torchvision.transforms as transforms
from torchvision import models
from PIL import Image
import numpy as np

# Load your trained model
model = models.resnet50(pretrained=True, num_classes = 1000)
model.load_state_dict(torch.load('fruit_quality_classification.pth'))
model.eval()

#model = torch.load('fruit_quality_classification.pth')
#model.eval()

# Define the image transformation
transform = transforms.Compose([
    transforms.Resize((224, 224)),
    transforms.ToTensor(),
])

def predict_image(image, model):
    image = transform(image).unsqueeze(0)
    with torch.no_grad():
        outputs = model(image)
    _, predicted = outputs.max(1)
    return predicted.item()

st.title('Fruit Image Classification')

uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

class_names = ['Healthy Apple',
 'Rotten Apple',
 'Healthy Banana',
 'Rotten Banana',
 'Healthy Ballpepper',
 'Rotten Ballpepper',
 'Healthy Carrot',
 'Rotten Carrot',
 'Healthy Cucumber',
 'Rotten Cucumber',
 'Healthy Grape',
 'Rotten Grape',
 'Healthy Guava',
 'Rotten Guava',
 'Healthy Jujube',
 'Rotten Jujube',
 'Healthy Mango',
 'Rotten Mango',
 'Healthy Orange',
 'Rotten Orange',
 'Healthy Pomegranate',
 'Rotten Pomegranate',
 'Healthy Potato',
 'Rotten Potato',
 'Healthy Strawberry',
 'Rotten Strawberry',
 'Healthy Tomato',
 'Rotten Tomato']

if uploaded_file is not None:
    image = Image.open(uploaded_file).convert("RGB")
    new_image = image.resize((350,350))
    st.image(new_image, caption='Uploaded Image')
    st.write("")

if st.button ("Submit"):
    st.write("Classifying...")
    label = predict_image(image, model)
    st.subheader(f'The image is classified as: {class_names[label]}')

st.link_button("Github Repository", "https://github.com/awojidetola/Fruit-Quality-Classification")


#if st.button('GitHub Link'):
 #   st.write("[GitHub Repository](https://github.com/awojidetola/Fruit-Quality-Classification)")
