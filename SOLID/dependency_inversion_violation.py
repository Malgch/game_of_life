class EmailService:
    def send_email(self, email, message):
        print("Sending email to {0}".format(email))

class SMSService:
    def send_sms(self, phone_number, message):
        print("Sending SMS to {0}".format(phone_number))

class NotificationService:
    def __init__(self):
        self.email_service = EmailService()
        self.sms_service = SMSService()

    def send_notification(self, recipient, message, method):
        if method == "email":
            self.email_service.send_email(recipient, message)
        elif method == "sms":
            self.sms_service.send_sms(recipient, message)