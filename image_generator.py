import streamlit as st
import torch
from diffusers import StableDiffusionPipeline

st.set_page_config(
    page_title="AI Image Generator",
    page_icon="🎨"
)

st.title("🎨 AI Image Generator")
st.write("Enter a description and generate an image using AI.")

@st.cache_resource
def load_model():
    pipe = StableDiffusionPipeline.from_pretrained(
        "segmind/tiny-sd",
        torch_dtype=torch.float32
    )
    pipe = pipe.to("cpu")
    return pipe

pipe = load_model()

prompt = st.text_input(
    "Enter your image description:",
    placeholder="Example: A cute cat sitting in a garden"
)

if st.button("Generate Image 🚀"):
    if prompt.strip() == "":
        st.warning("Please enter a description.")
    else:
        with st.spinner("Generating image... Please wait ⏳"):
            image = pipe(
                prompt,
                num_inference_steps=15,
                guidance_scale=7.5
            ).images[0]

        st.success("Image generated successfully! 🎉")
        st.image(image, caption=prompt, use_container_width=True)