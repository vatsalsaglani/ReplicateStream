from typing import List, Dict
import traceback
import requests

from parsing import parse_message
from stream import stream_data


class ReplicateStreamChatCompletion:
    def __init__(self, model_name: str, api_token: str):
        self._model = model_name
        self._token = api_token

    def _stream(self, url: str, headers: Dict):
        yield from stream_data(url, headers)

    def chat(self, system_prompt: str, history: List[Dict]):
        messages = list(map(lambda h: parse_message(h), history))
        try:
            output = requests.post(
                "https://api.replicate.com/v1/predictions",
                headers={"Authorization": f"Token {self._token}"},
                json={
                    "input": {
                        "prompt": " ".join(messages),
                        "system_prompt": system_prompt,
                        "temperature": 0.2,
                    },
                    "stream": True,
                    "version": self._model,
                },
            )
            output = output.json()
            print("Initial Response:", output)
            if not output.get("error"):
                urls = output.get("urls")
                stream_url = urls.get("stream")
                yield from self._stream(
                    stream_url,
                    {
                        "Authorization": f"Token {self._token}",
                        "Accept": "text/event-stream",
                    },
                )
            else:
                raise Exception("Error streaming response")
        except Exception as err:
            print("EXCEPTION: ", str(err))
            print("TRACEBACK: ", traceback.format_exc())
            pass
