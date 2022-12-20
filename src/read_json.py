import json

def read(path):
    f = open(path)
    return json.load(f)

if __name__ == "__main__":
    d=read("../ext/secret.json")
    print(d)
    print(d["token"])