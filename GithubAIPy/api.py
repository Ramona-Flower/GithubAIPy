import requests
import json

class GithubAIPy:
    def __init__(self):
        self.bearer_token = None
        self.headers = {
            "Content-Type": "application/json",
            "Accept": "text/event-stream",
            "Cache-Control": "no-cache",
        }

    def login(self, bearer_token):
        """Set the bearer token for authentication."""
        self.bearer_token = bearer_token
        self.headers["Authorization"] = f"{self.bearer_token}"

    def ask(self, model, question, stream=False):
        """
        Send a question to the specified model.
        
        Args:
            model (str): The name of the AI model to use.
            question (str): The question or prompt to send.
            stream (bool): If True, streams the response in real-time. Defaults to False.
        
        Returns:
            str: The full response from the model.
        """
        if not self.bearer_token:
            raise ValueError("Bearer token is not set. Please call login() first.")

        url = "https://models.inference.ai.azure.com/chat/completions"
        data = {
            "model": model,
            "messages": [{"role": "user", "content": question}],
            "max_tokens": 2048,
            "temperature": 0.8,
            "top_p": 0.1,
            "stream": stream,  # Use the stream parameter
        }

        response = requests.post(url, headers=self.headers, json=data, stream=stream)

        if response.status_code == 200:
            if stream:
                full_response = ""
                for line in response.iter_lines():
                    if line:
                        decoded_line = line.decode("utf-8").strip()
                        if decoded_line.startswith("data:"):
                            json_content = decoded_line[5:].strip()
                            if json_content == "[DONE]":
                                continue  # Ignore the [DONE] message
                            try:
                                json_data = json.loads(json_content)
                                if "choices" in json_data and json_data["choices"]:
                                    delta = json_data["choices"][0].get("delta", {})
                                    if "content" in delta:
                                        text_chunk = delta["content"]
                                        full_response += text_chunk  # Append to full response
                                        print(text_chunk, end="", flush=True)  # Stream in real-time
                            except json.JSONDecodeError:
                                print("\nError decoding JSON:", decoded_line)
                print()  # Add a newline after streaming
                return full_response
            else:
                # Non-streaming response
                json_data = response.json()
                if "choices" in json_data and json_data["choices"]:
                    return json_data["choices"][0]["message"]["content"]
                else:
                    return None
        else:
            print(f"Error: {response.status_code}, {response.text}")
            return None


# Create a singleton instance of GithubAIPy
github_ai = GithubAIPy()

# Expose the login and ask functions
def login(bearer_token):
    github_ai.login(bearer_token)

def ask(model, question, stream=False):
    return github_ai.ask(model, question, stream)