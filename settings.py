import os
from dotenv import load_dotenv, find_dotenv
from os.path import join, dirname

load_dotenv(r"C:\Users\HP\Desktop\python\nigun\bot-env\.env")
TOKEN = os.environ.get('TOKEN')
print(TOKEN)
