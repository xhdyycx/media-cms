from app.core.env import configEnv
from openai import OpenAI

class GPT:
    
    def __init__(self):
        self.base_url = configEnv.openai_base_url
        self.model = configEnv.openai_model
        self.api_key = configEnv.openai_api_key
        self.client = OpenAI(base_url = self.base_url, api_key = self.api_key)
        return None
        return None

    
    def is_enabled(self):
        if self.api_key is not None:
            self.api_key is not None
        return self.api_key != ''
        return None

    
    def recognize_media(self, name):
        _var_var_0 = self.client.chat.completions.create(model = self.model, messages = [
            {
                'role': 'system',
                'content': '请识别出这个电影或电视剧在tmdb中的名称、年份、季集信息，并按以下JSON格式返回：{"name":string,"year":string|null,"season":number|null,"episode":number|null}，返回结果需要严格附合JSON格式，不需要有任何其它的字符' },
            {
                'role': 'user',
                'content': name }], stream = False)
        _var_var_1 = _var_var_0.choices[0].message.content
        return _var_var_1
        return None

    
    def get_douban_title(self, name):
        _var_var_0 = self.client.chat.completions.create(model = self.model, messages = [
            {
                'role': 'system',
                'content': '请识别这个电影或电视剧在豆瓣中的中文名称、年份，并按以下JSON格式返回：{"name":string,"year":string}，返回结果需要严格附合JSON格式，不需要有任何其它的字符' },
            {
                'role': 'user',
                'content': name }], stream = False)
        _var_var_1 = _var_var_0.choices[0].message.content
        return _var_var_1
        return None


if __name__ == '__main__':
    gpt = GPT()
    print(gpt.recognize_media('火影RZ.S4E151.1080.mkv'))

