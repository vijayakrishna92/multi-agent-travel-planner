from py_toon_format import encode
import json

# with open("researcher_output.json", "r") as f:
#     data = json.load(f)


def json_toon_converter(data):
    return encode(data)
