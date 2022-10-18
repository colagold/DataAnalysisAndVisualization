import  yaml
import  json

'''
:return
'''
def read_json_to_dict(path)->dict:
    with open(path,encoding="utf-8") as f:
        return json.load(f)  # 返回的就是字典

def read_yaml_to_dict(path)->dict:
    with open(path,encoding="utf-8") as f:
        return yaml.full_load(f)

def json_to_yaml(path):
    with open(path,encoding="utf-8") as f:
        y=yaml.dump(json.load(f))  # 返回的是yaml
        print("yaml.dump(json.load(f)) type:",type(y))
    return y



if __name__=="__main__":
    js_path="../data/read_file_test/test_json.json"
    yaml_path="../data/read_file_test/pmf.yaml"
    print("Json To Dict: ",read_json_to_dict(js_path))
    print("YAML To Dict: ",read_yaml_to_dict(yaml_path))
    print("Json TO Yaml: ",json_to_yaml(js_path))
