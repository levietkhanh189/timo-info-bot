# app/utils/helpers.py

import os

def get_env_variable(name: str) -> str:
    try:
        return os.environ[name]
    except KeyError:
        raise Exception(f"The environment variable {name} has not been set.")
