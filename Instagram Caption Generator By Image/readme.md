# CaptionCraft

## Overview

**CaptionCraft** is a web-based application that leverages Google’s Generative AI (Gemini model) and Streamlit for building an interactive platform. This application takes user inputs, including a text prompt and an image, and generates content using the **Gemini-1.5-flash** model.

In this case, **CaptionCraft** is designed specifically as an **Instagram Caption Generator**, helping users create captivating and artistic captions that pair well with their photos. The generated captions can reflect various themes like nature, emotions, self-reflection, and more.

The following documentation details the setup and functioning of the CaptionCraft project, explaining each step and component involved in the application. Additionally, example use cases are provided to demonstrate how the application generates Instagram captions based on user prompts.

---

## Prerequisites

To run this project locally, ensure you have the following installed:

- Python 3.7+
- `pip` package manager
- Google Generative AI API access (with a valid API key)
- Required Python libraries: `google-generativeai`, `streamlit`, `Pillow`, `python-dotenv`

---

## Environment Setup

### Step 1: Install Dependencies

Install the required libraries via `pip`:

```bash
pip install google-generativeai streamlit pillow python-dotenv
```

### Step 2: Configure API Key

To interact with the Google Generative AI service, you need an API key. Store the API key in a `.env` file as follows:

```bash
# .env file
API_KEY=your_google_genai_api_key
```

### Step 3: Loading Environment Variables

The project uses `dotenv` to load environment variables. The following line loads the API key from the `.env` file:

```python
from dotenv import load_dotenv
load_dotenv()
```

---

## Components and Code Breakdown

### 1. **Google Generative AI Setup**

The application integrates with the **Google Generative AI** service. First, the API key is retrieved from environment variables, and the **Gemini-1.5-flash** model is configured:

```python
import os
import google.generativeai as genai

# Configure the Google GenAI with your API key
genai.configure(api_key=os.getenv("API_KEY"))

# Load the generative model
model = genai.GenerativeModel("gemini-1.5-flash")
```

### 2. **Streamlit User Interface**

Streamlit powers the user interface. The main structure includes a text input, image uploader, and a button to generate responses from the AI model.

- **Setting up Streamlit Configuration:**

```python
st.set_page_config(page_title="Gen AI")
st.header("Gen AI Application")
```

- **Input Fields:**

1. **Text Prompt Input:**

```python
input = st.text_input("Input Prompt", key="input")
```

This allows the user to enter a prompt that will be sent to the AI model for generating content.

2. **Image Uploader:**

```python
upload_img = st.file_uploader("Choose an Image..", type=["jpg", "png", "jpeg"])
```

The user can upload an image, which is processed using the `Pillow` library (`PIL`).

- **Image Display:**

```python
if upload_img is not None:
    image = Image.open(upload_img)
    st.image(image, caption="Uploaded Image")
```

This snippet displays the uploaded image along with a caption.

### 3. **Content Generation Function**

The main functionality of the application is encapsulated in the `get_res` function:

```python
def get_res(input, image):
    if input != "":
        response = model.generate_content([input, image])
        return response.text
```

This function sends the user's input (prompt and image) to the AI model and retrieves a generated response.

### 4. **Generating the Response**

When the user clicks the **Generate Response** button, the application sends the input data to the AI model and returns the generated content:

```python
submit = st.button("Generate Response from prompt")

if submit:
    response = get_res(input, image)
    st.subheader("Response")
    st.write(response)
```

---

## How to Run the Application

1. Make sure all dependencies are installed and your API key is configured in the `.env` file.
2. Run the Streamlit application using the following command:

```bash
streamlit run app.py
```

3. Open the provided local address in a browser, and you should see the user interface for CaptionCraft.

---

## Features

- **Text Input**: Users can enter a text prompt for the AI model to generate content.
- **Image Upload**: Users can upload an image (in `jpg`, `png`, or `jpeg` format) to be processed along with the text prompt.
- **AI Response**: When the user submits the input, the Google Generative AI model generates a response that combines the text prompt and image context.

---

## Example Use Cases

### 1. **Instagram Caption Generator (Nature, Emotions, Self-Reflection)**

**Prompt**:  
Create a short, poetic Instagram caption that combines elements of nature, emotions, and self-reflection. The caption should evoke a sense of wonder and connection, using metaphorical language and vivid imagery. It should be concise yet impactful, leaving the reader with a feeling of inspiration or curiosity.

**Image**:  
A serene sunset over a forest or a misty mountain landscape.

**Generated Caption**:  
"Beneath the amber skies, I lose myself in the whispers of the trees. Each breath of wind carries a story, a quiet reminder that even in stillness, the soul grows wild."

### 2. **Travel Adventure Caption**

**Prompt**:  
Write an adventurous Instagram caption that reflects the thrill of exploring new places and the joy of being free-spirited. Include references to the open road, distant horizons, and a sense of excitement for the unknown.

**Image**:  
A long, winding road through a desert or a coastal highway.

**Generated Caption**:  
"Chasing the horizon, where the sun meets the sea and every turn holds a new story. The road ahead is endless, just like the adventures waiting to unfold."

### 3. **Motivational Fitness Caption**

**Prompt**:  
Create a powerful, motivational Instagram caption focused on strength, perseverance, and personal growth. Use metaphors related to fitness and self-discipline, and leave the reader feeling empowered.

**Image**:  
A person lifting weights in the gym or running on a trail.

**Generated Caption**:  
"With each rep, I build more than muscle. I forge resilience, break barriers, and push past limits. Strength isn’t just physical—it’s the power of the mind to rise above every challenge."

### 4. **Fashion Aesthetic Caption**

**Prompt**:  
Generate a trendy Instagram caption that highlights the beauty of fashion, creativity, and individuality. Use expressive language to emphasize style and confidence.

**Image**:  
A stylish outfit or a person walking down a fashion-forward street.

**Generated Caption**:  
"Strutting through life with bold colors and bolder dreams. Fashion isn’t just what you wear—it’s how you paint the world with your personality."

---

## Conclusion

CaptionCraft is a powerful tool for generating creative Instagram captions tailored to various themes and moods. By utilizing Google’s **Generative AI** model and combining text prompts with images, users can generate thoughtful, engaging captions for their posts. This application streamlines the process of caption creation, allowing users to focus more on sharing their stories.

---

## Troubleshooting

1. **Invalid API Key**: Ensure your API key is correct and stored in the `.env` file. Verify that `dotenv` successfully loads it.
2. **Image Upload Issues**: Ensure that the image format is one of the supported types (`jpg`, `png`, `jpeg`). If the image does not display, check the file size and format.