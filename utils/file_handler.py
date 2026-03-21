import json

def export_to_json(data, filepath):
    if data is None:
        print("Nothing to export!")
        return None
    try:
        with open(filepath, mode="w") as file:
            json.dump(data, file, indent=4)
    except FileNotFoundError:
        print("File Not Found.")