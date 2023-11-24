import json
import requests
import datetime
import openai

class ultraChatBot():
    def __init__(self, json):
        self.json = json
        self.dict_messages = json['data']
        self.ultraAPIUrl = 'https://api.ultramsg.com/instance69299/'
        self.token = 'k29irlpc49wq5r4q'
        # Replace 'YOUR_OPENAI_API_KEY' with your actual OpenAI API key
        openai.api_key = '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'

    def send_requests(self, type, data):
        url = f"{self.ultraAPIUrl}{type}?token={self.token}"
        headers = {'Content-type': 'application/json'}
        answer = requests.post(url, data=json.dumps(data), headers=headers)
        return answer.json()

    def generate_openai_response(self, prompt):
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": prompt},
            ],
            timeout=12000
        )
        return response['choices'][0]['message']['content'].strip()

    def send_message(self, chatID, text):
        data = {"to": chatID, "body": text}
        answer = self.send_requests('messages/chat', data)
        return answer

    def send_openai_message(self, chatID, prompt):
        response = self.generate_openai_response(prompt)
        return self.send_message(chatID, response)

    def Processingـincomingـmessages(self):
        if self.dict_messages != []:
            message = self.dict_messages
            text = message['body']
            if not message['fromMe']:
                chatID = message['from']
                return self.send_openai_message(chatID, text)
            else:
                return 'NoCommand'