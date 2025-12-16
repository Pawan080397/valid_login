import yaml

def read_config():
    with open("configs/config.yaml", "r") as file:
        return yaml.safe_load(file)
