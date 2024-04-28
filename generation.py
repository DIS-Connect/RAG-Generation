from openai import OpenAI
from secret import api_key

class ChatBot():


    def __init__(self):
        self.openai_client = OpenAI(api_key=api_key)
        # self.openai_client.api_key = api_key

        
        

    def answer_question(self, question, model, conversation):

        ######### Promt engineering and Retrieval here ##############

        prompt_text = "Please answer this question of the user: \n" + question

        ############################################################
        openai_connected = False
        if not openai_connected:
            return "LLM connection is not implemented yet"


        response = self.openai_client.chat.completions.create(
            model=model,
            response_format={ "type": "json_object" },
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": "Who won the world series in 2020?"}
            ]
        )
        return response.choices[0].message.content
