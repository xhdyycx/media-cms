import json
from app.utils.mjson import JsonUtils

class ConfigConverter:
    @staticmethod
    def convert_config(config: dict) -> dict:
        """
        将配置格式从:
        {
            "CMS_DEMO0001": {
                "name": "demo",
                "private_key": "00000000000000000000000000000000"
            }
        }
        转换为:
        {
            "demo": "CMS_DEMO0001_00000000000000000000000000000000"
        }
        """
        return {
            f'{_var_var_0}_{_var_var_1["private_key"]}': _var_var_1["name"]
            for _var_var_0, _var_var_1 in config.items()
        }

if __name__ == '__main__':
    original_config = { }
    original_config = { }
    converted = ConfigConverter.convert_config(original_config)
    print(JsonUtils.to_str(converted))
    converted_list = []
    items = list(converted.items())
    for i in range(0, len(items), 50):
        converted_list.append(dict(items[i:i + 50]))
    converted = converted_list
    print(JsonUtils.to_str(converted_list))

