from py_toon_format import encode
import json

with open("places_output.json", "r") as f:
    data = json.load(f)


def json_toon_converter(data):
    return encode(data)
    #print(toon_string)
