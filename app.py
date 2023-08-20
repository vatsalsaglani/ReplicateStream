import os
import argparse
from time import sleep

from chat import ReplicateChatCompletion
from configs import *

parser = argparse.ArgumentParser(description="Replicate stream completion")

parser.add_argument(
    "--replicate_model_version",
    default="58d078176e02c219e11eb4da5a02a7830a283b14cf8f94537af893ccff5ee781",
    help="Version of the replicate model which supports streaming.",
)


def clear_terminal():
    os.system("cls" if os.name == "nt" else "clear")


args = parser.parse_args()

model_version = args.replicate_model_version

# print(f'MODEL VERSION: {model_version}')

completion = ReplicateChatCompletion(
    model_version,
    REPLICATE_API_TOKEN,
)

messages = []
system_prompt = """You are a helpful, respectful and honest assistant. Always answer as helpfully as possible, while being safe. Your answers should not include any harmful, unethical, racist, sexist, toxic, dangerous, or illegal content. Please ensure that your responses are socially unbiased and positive in nature.

If a question does not make any sense, or is not factually coherent, explain why instead of answering something not correct. If you don't know the answer to a question, please don't share false information."""

while True:
    inp = input("\nEnter message: ").rstrip().lstrip()
    if inp:
        messages.append({"role": "user", "content": inp})
    if len(inp) > 2:
        inp = inp[-1:]
        answer = ""
        for ans in completion.chat(system_prompt, messages):
            answer += ans
            clear_terminal()
            print(answer, end="", flush=True)
            sleep(0.1)
        messages.append({"role": "model", "content": inp})
