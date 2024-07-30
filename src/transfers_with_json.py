import json
def load_settings():
    with open("settings.json", "r") as f:
        data = json.load(f)
    return data


def transfer_language(language):
    asd = 1