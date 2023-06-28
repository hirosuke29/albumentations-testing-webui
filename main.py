import json

import albumentations as albu
import numpy as np
import streamlit as st
from PIL import Image
from streamlit_ace import st_ace


def load_default_albu_json() -> str:
  with open("default_albu.json", "r") as f:
    return f.read()


def main():
  st.title("Albumentations testing Web UI")

  st.header("Input your Albumentations json")
  default_albu_json: str = load_default_albu_json()
  content = st_ace(value=default_albu_json, language="json", tab_size=2, theme="monokai", placeholder="Write your albumentations json here")
  albu_transform_dict: dict[str, any] = json.loads(content)
  albu_transform = albu.from_dict(albu_transform_dict)

  st.header("Upload your image")
  uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "png"])
  if uploaded_file is not None:
    st.image(uploaded_file, caption="Uploaded Image")
    image: Image.Image = Image.open(uploaded_file)
    st.write(f"width: {image.size[0]}, height: {image.size[1]}, channels: {len(image.getbands())}")

    transformed_image_array = albu_transform(image=np.array(image))["image"]
    st.image(transformed_image_array, caption="Transformed Image", clamp=True)
    st.write(f"width: {transformed_image_array.shape[1]}, height: {transformed_image_array.shape[0]}, channels: {transformed_image_array.shape[2]}")
  
    st.button("Re-transform", on_click=None)

if __name__ == "__main__":
  main()
