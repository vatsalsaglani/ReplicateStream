import json
import requests
from typing import Dict


def stream_data(url, headers: Dict):
    with requests.get(url, headers=headers, stream=True) as response:
        if response.status_code != 200:
            raise Exception(
                "Failed to connect with status code: ", response.status_code
            )

        errored = False
        for line in response.iter_lines():
            line = line.decode("utf-8")
            if line.startswith("data: "):
                data = line.split("data: ")[-1]
                if data.startswith("{"):
                    error = json.loads(data)
                    if error:
                        if errored and "detail" in error:
                            raise Exception(error.get("detail"))
                        elif "reason" in error:
                            raise Exception(error.get("reason"))
                yield data
            elif line.startswith("event: "):
                event = line.split("event: ")[-1]
                if event == "done":
                    return
                elif event == "error":
                    errored = True
