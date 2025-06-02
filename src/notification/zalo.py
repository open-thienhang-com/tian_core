from . import BaseNotification

class ZaloNotification(BaseNotification):
    def send(self, message):
        print(f'Sending zalo message: {message}')