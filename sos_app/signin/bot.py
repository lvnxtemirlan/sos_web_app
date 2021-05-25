import requests
from decouple import config

TELEGRAM_API_TOKEN = config("TELEGRAM_API_TOKEN")


class Alerter:
    def __init__(self, chat_id):
        self.chat_id = chat_id
        self.api_token = TELEGRAM_API_TOKEN

    def send_message(self, msg):

        payload = {
            "chat_id": self.chat_id,
            "text": msg,
            "parse_mode": "HTML"
        }

        return requests.post(f"https://api.telegram.org/bot{self.api_token}/sendMessage", data=payload).status_code

    def send_photo(self, msg, image_path):

        payload = {
            "chat_id": self.chat_id,
            "text": msg,
            "caption": msg,
            "parse_mode": "markdown"
        }
        with open(image_path, "rb") as image_file:
            response = requests.post(f"https://api.telegram.org/bot{self.api_token}/sendPhoto", data=payload, files={"photo": image_file})
        return response