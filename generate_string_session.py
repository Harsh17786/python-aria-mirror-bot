from pyrogram import Client

API_KEY = int(input("Enter API KEY: 1570274"))
API_HASH = input("Enter API HASH: d463fbcaa44274b3e969028dd570d3ab")
with Client(':memory:', api_id=API_KEY, api_hash=API_HASH) as app:
    print(app.export_session_string())
