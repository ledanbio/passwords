import json
def load_settings():
    with open("settings.json", "r") as f:
        data = json.load(f)
    return data

def transfer_language(language):
    asd = 1

def writeJSON(society, login, password):
    my_dict = {
    "society": society,
    "login": login,
    "password": password
    }
    with open("data_in_json/passwords.json", "w") as f:
        json.dump(my_dict, f)

def readJSON():
    with open("settings.json", "r") as f:
        data = json.load(f)
    return data

def extractionDATA():
    data = readJSON()
    result = []
    for item in data:
        account = {
            'society': item['society'],
            'login': item['login'],
            'password': item['password']
        }
        result.append(account)
    return result