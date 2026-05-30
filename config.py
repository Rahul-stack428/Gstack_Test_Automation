import os
from dotenv import load_dotenv

load_dotenv()

USERNAME = os.getenv("GSTACK_USERNAME")
PASSWORD = os.getenv("GSTACK_PASSWORD")
BASE_URL = os.getenv("BASE_URL")
ROLE = "Platform Admin"