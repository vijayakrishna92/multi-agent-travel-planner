
from py_toon_format import encode, decode
import json

with open("places_output.json", "r") as f:
    data = json.load(f)


# Convert to TOON
toon_string = encode(data)
print('toon',toon_string)

# Convert back to Python dict
original_data = decode(toon_string)