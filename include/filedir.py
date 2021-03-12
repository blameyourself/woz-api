import json
def dirFile():
    try:
        with open('/serverConfig/config.json') as config_file:
            config = json.load(config_file)

            return config
    except FileNotFoundError:
        with open('include/localConfig/config.json') as config_file:
            config = json.load(config_file)

            return config