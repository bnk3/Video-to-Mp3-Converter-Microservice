import smtplib, os, json

from email.message import EmailMessage

def notification(message):
    try:
        message = json.loads(message)
        mp3_fid = message["mp3_fid"]
        sender_address = os.environ.get("GMAIL_ADDRESS")
        sender_password = os.environ.get("GMAIL_PASSWORD")
        reciever_address = message["username"]
        
        msg = EmailMessage()
        msg.set_content(f"mp3 file_id: {mp3_fid} is now ready!")
        
        msg["Subject"] = "MP3_DOWNLOAD"
        msg["From"] = sender_address
        msg["To"] = reciever_address
        
        session = smtplib.SMTP_SSL("smtp.gmail.com", 465)
        # session.starttls()
        session.login(sender_address, sender_password)
        session.send_message(msg, sender_address, reciever_address)
        session.quit()
        print("E-Mail Sent")
    except Exception as err:
        print(err)
        return err
        
        