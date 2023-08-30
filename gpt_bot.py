import os
import textwrap
import openai

from langchain import PromptTemplate
from langchain.llms import OpenAI, OpenAIChat

openai.api_key = os.environ.get('OPENAI_API_KEY')
# llm = OpenAIChat(model_name="gpt-3.5-turbo", temperature=0.7, stop=['\n'])

class GPTBot():
    def __init__(self):
        self.template = """
        以下は、話者Aと話者Bの対話です。

        [話者Aのプロフィール]
        {profile}
        [話者Aの性格]
        {personality}
        [対話]{history_text}
        話者B: {input_text}
        話者A: """

        self.template = textwrap.dedent(self.template)[1:]

        self.prompt = PromptTemplate(
                template=self.template,
                input_variables=['profile', 'personality', 'history_text', 'input_text']
        )

    def ret_system_utt(self, dialogue_history, input_text, prompt_id=0):
        profile = "私は北海道に住んでいます。\n私は映画を見るのが好きです。"
        personality = "開放性が低い。\n誠実性が高い。\n外向性が低い。\n協調性が低い。\n神経症傾向が高い。"

        history_text = ""
        for d in dialogue_history:
            if d['spk'] == '[SPK2]':
                spk = '話者B'
            else:
                spk = '話者A'
            history_text += f"\n{spk}: {d['utt']}"

        prompt_text = self.prompt.format(profile=profile, personality=personality, 
                history_text=history_text, input_text=input_text)
        print(f'prompt:\n{prompt_text}', flush=True)

        llm = OpenAI(model_name="gpt-4-0613", temperature=0.7, stop=['\n'], 
                request_timeout=60, max_tokens=300)
        ret = llm(prompt_text)
        return ret
