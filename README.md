# RAG using Haystack AI

Tried learning the Haystack AI (`v2.x`) by building a Local RAG using Ollama and `phi3` (for speed on Windows machine). We are using the [`bilgeyucel/seven-wonders`](https://huggingface.co/datasets/bilgeyucel/seven-wonders) datasets from 🤗Hugging Face.

## Getting Started

```bash
git clone git@github.com:mayeenulislam/haystack-ai.git && cd haystack-ai

conda create -n haystack python=3.11 -y

conda activate haystack

pip install -r requirements.txt

# alternatively...
# pip install haystack-ai datasets ollama-haystack gradio

ollama run phi3 # necessary?
```

### Running the Application

```bash
python app.py # will download the data and train
```

## Credits

[**Haystack AI: Production-ready RAG with Custom Data made easy!**](https://www.youtube.com/watch?v=8qqaqefugWQ) (Based on `v1.x`)<br/>
Mervin Praison
