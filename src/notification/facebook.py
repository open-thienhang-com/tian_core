from . import BaseNotification

class FacebookNotification(BaseNotification):
    def send(self, message):
        print(f'Sending facebook message: {message}')