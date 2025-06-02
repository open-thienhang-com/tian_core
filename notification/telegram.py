import requests
import time

TOKEN = '7847847200:AAFWYAA_RBR5d3Vex5kDDVP34rMFVokZfgw'  # Replace with your actual bot token
BASE_URL = f'https://api.telegram.org/bot{TOKEN}'


def send(message: str):
    """Get the chat ID of the last message sent to the bot."""
    url = f'{BASE_URL}/getUpdates'
    response = requests.get(url)
    data = response.json()
    print(data)
    # Check if there are any new messages
    if 'result' in data and data['result']:
        for update in data['result']:
            if 'message' not in update:
                continue
            chat_id = update['message']['chat']['id']
            url = f'{BASE_URL}/sendMessage'
            payload = {'chat_id': chat_id, 'text': message}
            requests.post(url, data=payload)
    else:
        print("No messages found.")
        return None

        
class Telegrambot:
    def __init__(self):
        self.offset = None

    def run(self):
        """Main loop to check for new messages and respond."""
        offset = None
        while True:
            updates = self.get_updates(offset)

            if 'result' in updates:
                for update in updates['result']:
                    offset = update['update_id'] + 1
                    if 'message' in update:
                        chat_id = update['message']['chat']['id']
                        text = update['message'].get('text', '')

                        # Respond to /start command
                        if text == '/start':
                            self.send_message(chat_id, "Hello! Welcome to the bot.")
                        else:
                            # Echo any other message
                            self.send_message(chat_id, f"You said: {text}")

            # Delay between requests to avoid hitting Telegram’s API too frequently
            time.sleep(1)
    
    def get_updates(offset=None):
        """Get updates from Telegram to check for new messages."""
        url = f'{BASE_URL}/getUpdates'
        params = {'timeout': 100, 'offset': offset}
        response = requests.get(url, params=params)
        return response.json()

    def send_message(chat_id, text):
        """Send a message to a Telegram chat."""
        url = f'{BASE_URL}/sendMessage'
        payload = {'chat_id': chat_id, 'text': text}
        requests.post(url, data=payload)