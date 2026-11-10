import json

class JsonUtils:
    @staticmethod
    def to_str(data_input) -> str:
        if not data_input:
            return ''
        return json.dumps(data_input, ensure_ascii=False, default=str)
    @staticmethod
    def json_to_dict(data_input) -> dict:
        if not data_input:
            return {}
        return json.loads(data_input)

if __name__ == '__main__':
    print(JsonUtils.json_to_dict('{"a": 1, "b": 2}'))

