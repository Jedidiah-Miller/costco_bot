from twilio.rest import Client
from endpoints import product_page
import secrets  # from secrets.py in this folder


class Twilio:

    def __init__(self):
        self.client = self.setup_twilio_client()

    def setup_twilio_client(self):
        return Client(secrets.TWILIO_ACCOUNT_SID, secrets.TWILIO_AUTH_TOKEN)

    def send_notification(self):
        self.client.messages.create(
            messaging_service_sid=secrets.MESSAGING_SERVICE_SID,
            body=f"Callaway Golf Clubs are in stock! -- open --  {product_page}",
            to=secrets.MY_PHONE_NUMBER
        )
