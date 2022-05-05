import yaml
import json

with open("sample2.yaml", 'r') as Yaml_Input, open("sample1.json", "w") as JSON_Output:
    try:
        yamlObject = yaml.safe_load(Yaml_Input) # yamlObject will be a list or a dict
        print(type(yamlObject))
        json.dump(yamlObject, JSON_Output)
    except:
        print("Error in yaml File")