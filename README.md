
# GithubAIPy

They released this recently, so why not make a wrapper of it, to use everywhere !

A Python package to interact with GitHub AI models. Easily authenticate and query AI models using a simple and intuitive interface.

## Installation

Install the package via pip:

```bash
pip install GithubAIPy
```

# Quick Guide: Get GitHub Bearer Token Using Chrome DevTools
Go to:
https://github.com/marketplace/models/azure-openai/gpt-4o/playground.

Open DevTools: F12 → Network tab.

Send a message in the playground.

In DevTools, find the completions request → check Headers → copy the Authorization: Bearer <token> value.

⚠️ Warning: Keep your token private! 

To use it, just put the full cookie with bearer before !
# Usage
## Authentication
authenticate using your GitHub Bearer token:

```py
from GithubAIPy import login

login("your_bearer_token_here")

```

## Querying a Model
Use the ask function to send a query to a specific AI model:

```python

from GithubAIPy import ask

response = ask("Meta-Llama-3-70B-Instruct", "What is the capital of France?")
print(response)

```
## Streaming Responses
Ask function supports streaming responses for real-time interaction:
```
response = ask("Meta-Llama-3-70B-Instruct", "Explain quantum computing in simple terms.", stream=True)
```

# Supported AI Models

Below is a list of supported AI models. You can use any of these models with the ask function.

## Supported AI Models

Below is a list of supported AI models. You can use any of these models with the `ask` function.

| Model Name                  | | | 
|-----------------------------|-----------------------------|-----------------------------|
| gpt-4o                      | gpt-4o-mini                 | o1-mini                     |
| o1-preview                  | o3-mini                     | text-embedding-3-large      |
| text-embedding-3-small      | Phi-3.5-MoE-instruct        | Phi-3.5-mini-instruct       |
| Phi-3.5-vision-instruct     | Phi-3-medium-128k-instruct  | Phi-3-medium-4k-instruct    |
| Phi-3-mini-128k-instruct    | Phi-3-mini-4k-instruct      | Phi-3-small-128k-instruct   |
| Phi-3-small-8k-instruct     | Phi-4                       | AI21-Jamba-1.5-Large        |
| AI21-Jamba-1.5-Mini         | Codestral-2501              | Cohere-command-r            |
| Cohere-command-r-08-2024    | Cohere-command-r-plus       | Cohere-command-r-plus-08-2024|
| Cohere-embed-v3-english     | Cohere-embed-v3-multilingual| DeepSeek-R1                 |
| Llama-3.2-11B-Vision-Instruct| Llama-3.2-90B-Vision-Instruct| Llama-3.3-70B-Instruct      |
| Meta-Llama-3.1-405B-Instruct| Meta-Llama-3.1-70B-Instruct | Meta-Llama-3.1-8B-Instruct  |
| Meta-Llama-3-70B-Instruct   | Meta-Llama-3-8B-Instruct    | Ministral-3B                |
| Mistral-Large-2411          | Mistral-Nemo                | Mistral-large               |
| Mistral-large-2407          | Mistral-small               | jais-30b-chat               |
# Examples
Example 1: Simple Query
```python

response = ask("gpt-4o", "What is the meaning of life?")
print(response)

```

# Example 2: Streaming Response
```python

response = ask("Meta-Llama-3-70B-Instruct", "Explain the theory of relativity.", stream=True)
```


Example 3: Using a Different Model

```python

response = ask("Mistral-Large-2411", "Write a Python function to calculate the Fibonacci sequence.")
print(response)

```

# Contributing
Contributions are welcome! If you'd like to contribute, please follow these steps:

Fork the repository.

Create a new branch (git checkout -b feature/YourFeatureName).

Commit your changes (git commit -m 'Add some feature').

Push to the branch (git push origin feature/YourFeatureName).

Open a pull request.

# License
This project is licensed under the MIT License. See the LICENSE file for details.

Support
For issues or feature requests, please open an issue on the GitHub repository.



