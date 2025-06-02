from . import BaseNotification

class FirebaseNotification(BaseNotification):
    def send(self, message):
        print(f'Sending firebase message: {message}')
