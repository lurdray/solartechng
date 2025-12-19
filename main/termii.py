import requests

def send_whatsapp_notification(api_key: str, to: str, message: str, base_url: str = "https://api.ng.termii.com"):
    """
    Send a plain WhatsApp notification via Termii without media.
    Uses 'N-Alert' as the sender ID.

    Parameters:
        api_key  (str): Your Termii API key
        to       (str): Recipient phone number in international format
        message  (str): The message text
        base_url (str): Base URL from your Termii account (default NG endpoint)
    """
    url = f"{base_url}/api/sms/send"

    payload = {
        "to": to,
        "from": "N-Alert",     # Your WhatsApp sender ID
        "sms": message,
        "type": "plain",
        "channel": "whatsapp", # Ensures delivery via WhatsApp
        "api_key": api_key
    }

    headers = {
        "Content-Type": "application/json"
    }

    response = requests.post(url, headers=headers, json=payload)
    response.raise_for_status()
    return response.json()


# Example usage
if __name__ == "__main__":
    API_KEY = "TermiiSettings__ApiKey=TLKTE6vDixqeACH7UlNnk0phowwgGXawuKSj6Sko4CtoIKhgp8y29uGwdhl2uu"
    recipient_number = "2348148737265"
    text_message = "Hi there, testing Termii WhatsApp notification"

    result = send_whatsapp_notification(API_KEY, recipient_number, text_message)
    print(result)
