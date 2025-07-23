import time
import json
import requests

TELEGRAM_TOKEN = "7938938048:AAF66EPJDsgu_QIbfofEePsc6q4P-f_UQ1c"
CHAT_ID = "6588203945"

def send_telegram_message(message):
    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
    payload = {"chat_id": CHAT_ID, "text": message}
    requests.post(url, data=payload)

def check_vfs_appointment():
    # Simulation de vérification (à remplacer avec code réel)
    return True  # Simule qu'un créneau est trouvé

def main():
    with open("config.json", "r", encoding="utf-8") as f:
        config = json.load(f)
    
    while True:
        if check_vfs_appointment():
            send_telegram_message(f"[RDV DISPONIBLE] Bonjour {config['nom']}, un rendez-vous est disponible !")
            break
        time.sleep(60)  # Attendre 1 minute avant une nouvelle vérification

if __name__ == "__main__":
    main()