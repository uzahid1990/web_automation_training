import json
import os


cur_path = os.path.dirname(__file__)
config_file_path = os.path.relpath('../resources/config.json', cur_path)

# this class is written to get json object to parse as per their needs
class JsonParser:

    def read_json(self, param_key):
        json_file = self.json_file_path()
        with open(json_file) as f:
            data = json.load(f)
        param_list = []
        json_content = json.dumps(data)
        # print(type(json_content))
        json_1 = json.loads(json_content)
        for value in json_1[param_key].values():
            for i in value.values():
                param_list.append(i)
        return param_list

    @staticmethod
    def json_file_path():
        path = config_file_path
        return path
