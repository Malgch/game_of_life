from abc import ABC, abstractmethod

class IMessageService(ABC):
    @abstractmethod
    def send(self, message, recipient):
        pass

class EmailService(IMessageService):
    def send(self, message, recipient):
        print(f"Sending email: {message} to {recipient}")

class SMSService(IMessageService):
    def send(self, message, recipient):
        print(f"Sending SMS: {message} to {recipient}")

class NotificationService:
    def __init__(self, message_service: IMessageService):
        self.message_service = message_service

    def send_notification(self, recipient, message):
        self.message_service.send(message, recipient)