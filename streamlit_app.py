import streamlit as st
import tensorflow as tf
from PIL import Image
import numpy as np

# Load model once (cached)
@st.cache_resource
def load_model():
    model = tf.keras.models.load_model("tumor_model.h5")
    return model

model = load_model()

# App title
st.title("Brain Tumor Detection")

# Upload file
uploaded_file = st.file_uploader("Upload an MRI image", type=["jpg","jpeg","png"])

if uploaded_file is not None:
    image = Image.open(uploaded_file).convert("RGB")
    st.image(image, caption="Uploaded Image", use_column_width=True)

    # Preprocess
    img = image.resize((128, 128))  
    img_array = np.array(img) / 255.0
    img_array = np.expand_dims(img_array, axis=0)

    # Predict
    prediction = model.predict(img_array)[0][0]

    if prediction > 0.5:
        st.error("Tumor Detected")
    else:
        st.success("No Tumor")
