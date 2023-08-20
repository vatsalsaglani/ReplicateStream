# Replicate Stream

This repository provides an example on how one can stream responses from LLMs on replicate using Python.

## Demo

https://github.com/vatsalsaglani/ReplicateStream/assets/23306338/874f3ac8-a2ac-4801-a018-b96dbb7d2205

## Getting started

Let's look at how we can run this code and stream responses in terminal.

### Clone the repository

```
git clone https://github.com/vatsalsaglani/ReplicateStream.git
```

### Install requirements

```
pip3 install -r requirements.txt
```

### Add Replicate API token to the environment

You can create an `.env` file and add the following content or set the variable manually in the commandline or terminal.

```
REPLICATE_API_TOKEN="your_replicate_api_token"
```

### Execute

Run the `app.py` file like following with the model version to use.

```
python app.py --replicate_model_version="2a7f981751ec7fdf87b5b91ad4db53683a98082e9ff7bfd12c8cd5ea85980a52"
```

_Ask you question!_

