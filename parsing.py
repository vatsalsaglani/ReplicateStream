from typing import Dict

Llama_Begin = "[INST]"
Llama_End = "[/INST]"


def parse_message(message: Dict):
    if message.get("role") == "user":
        return f"{Llama_Begin} {message.get('content')} {Llama_End}"
    else:
        return message.get("content") if message.get("content") else ""
