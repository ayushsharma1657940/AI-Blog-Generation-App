import streamlit as st
import os
from google import genai
from openai import OpenAI
from apikey import openai_api_key

# Set API key (better: use env variable)
os.environ["GEMINI_API_KEY"] = "AIzaSyC7ggUBC_Z5v2GqGAmm_ChLB6rJLV6VJzU"

client = genai.Client()
client02 = OpenAI(api_key=openai_api_key)

st.set_page_config(layout="wide")
st.title("Blogcraft: Your AI Writing Companion")

with st.sidebar:
    st.title("Input Your Blog Details")
    blog_title = st.text_input("Blog Title")
    keywords = st.text_area("Keywords (comma-separated)")
    num_words = st.slider("Number of Words", 250, 1000, 250)
    num_image=  st.number_input("Number of images",min_value=1,max_value=5,step = 1)
    submit_button = st.button("Generate Blog")

if submit_button:
    prompt = f"""
    generate a comprehensive ,engaging blog post relevent to the given title {blog_title} and keywords {keywords} . Make sure to incorporate these keywords in the blog post .the blog should be approximately {num_words} words in length , suitable for an online audience .Ensure the content is original,informative and maintains a consistent tone throughout
    """

    response = client.models.generate_content(
        model="models/gemini-2.5-flash",
        contents=prompt
    )
    response01 =  client02.images.generate(model="dall-e-2",
                                           prompt="cat",size = "1024x1024",
                                           
                                           n=1,)
    
    image_url =  response01.data[0].url
    
    st.image(image_url,caption="Generated Image")
    st.title("your blog post:")

    st.write(response.text)
for m in client.models.list():
    print(m.name)
