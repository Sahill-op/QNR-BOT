from telethon.sessions import StringSession
from telethon.sync import TelegramClient


print(
    """QNR SESSION"""
)

print("\n • Telethon Session •")

print("\n\nEnter Your Valid Details To Continue!\n\n")

        
APP_ID = int(input("\nEnter APP ID here: "))
API_HASH = input("\nEnter API HASH here: ")


try:
   with TelegramClient(StringSession(), APP_ID, API_HASH) as QNR:
       print("\nSTRING SESSION GENERATE SUCCESSFULLY CHECK SAVED MASSAGE")
       QNR.send_message("me", f"QNR SESSION :\n\n{QNR.session.save()}\n\nDo not share this anywhere!!")
       
except Exception as e:
    print(f"{e}")
