# Importing required Libraries
from datasets import load_dataset
from haystack import Document
from haystack.document_stores.in_memory import InMemoryDocumentStore # Store in memory
from haystack.components.retrievers import InMemoryBM25Retriever # Retriever
from haystack.components.builders import PromptBuilder
from haystack_integrations.components.generators.ollama import OllamaGenerator
from haystack import Pipeline

# Load dataset and create documents
# load_dataset() is easy way to load a CSV file
dataset = load_dataset("bilgeyucel/seven-wonders", split="train")

# Change according to the CSV columns
docs = [Document(content=doc["content"], meta=doc["meta"]) for doc in dataset]

# Initialize document store and write documents
# Any vector database can be incorporated her
document_store = InMemoryDocumentStore()
document_store.write_documents(docs)

# Initialize retriever
# Retrieve the query from the document store
retriever = InMemoryBM25Retriever(document_store)

# Define the Prompt template
template = """
Given the following information, answer the question.

Context:
{% for document in documents %}
    {{ document.content }}
{% endfor %}

Question: {{question}}

Answer:
"""

# Initialize the Prompt builder
prompt_builder = PromptBuilder(template=template)

# Initialize Ollama Generator
generator = OllamaGenerator(
    model="phi3",
    url="http://localhost:11434/api/generate",
    generation_kwargs={
        "num_predict": 100,
        "temperature": 0.9
    }
)

# Haystack
# Create and configure Pipelines
basic_rag_pipeline = Pipeline()

basic_rag_pipeline.add_component("retriever", retriever)
basic_rag_pipeline.add_component("prompt_builder", prompt_builder)
basic_rag_pipeline.add_component("llm", generator)

basic_rag_pipeline.connect("retriever", "prompt_builder.documents")
basic_rag_pipeline.connect("prompt_builder", "llm")

# Run the pipeline with a sample question
question = "What does Rhodes Statue look like?"
response = basic_rag_pipeline.run(
    {
        "retriever": {"query": question},
        "prompt_builder": {"question": question}
    }
)

print(response["llm"]["replies"][0])
