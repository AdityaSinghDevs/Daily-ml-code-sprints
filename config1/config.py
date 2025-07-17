import os
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("API_KEY")
api2=os.getenv("KEY2")
print(api_key)
print(api2)
