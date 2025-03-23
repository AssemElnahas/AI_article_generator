# AI Article Generator

## Description
The AI Article Generator is a Streamlit-based web application that generates AI-written articles based on a given topic. It uses the `transformers` library with the GPT-2 model to create text-based content.

## Features
- Accepts a topic input from the user.
- Generates AI-written content based on the given topic.
- Displays the generated article within the Streamlit UI.

## Installation
To run this project, make sure you have Python installed along with the required dependencies.

### Install dependencies:
```bash
pip install streamlit transformers torch
```

## Usage
Run the application using Streamlit:
```bash
streamlit run ai_article_generator.py
```

Enter a topic in the text input field and click the "Generate Article" button to generate an AI-written article.

## Requirements
- Python 3.x
- `streamlit`
- `transformers`
- `torch`

## Notes
- The application uses the GPT-2 model, which might generate text that requires manual review.
- To improve results, you can fine-tune the model or use a more advanced model like GPT-3 or GPT-4.

## License
This project is open-source and can be modified or extended as needed.

