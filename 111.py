import configparser

from telethon import TelegramClient, sync, events, TelegramClient

config = configparser.ConfigParser()
config.read("config.ini")

api_id   = config['Telegram']['api_id']
api_hash = config['Telegram']['api_hash']
username = config['Telegram']['username']

client = TelegramClient(username, api_id, api_hash)



client.start()

@client.on(events.NewMessage(chats=('nocapabnormal')))
async def normal_handler(event):

    mess_date = event.message.to_dict()['date']
    mess_id = event.message.to_dict()['id']
    print(event.message.to_dict()['message'])
    print(mess_date,mess_id)
    print('--------------------------------------')

client.run_until_disconnected()
