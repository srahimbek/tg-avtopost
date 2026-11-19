# avtopost sozlamalari
import os

TIMEZONE = "Asia/Dubai"
POST_HOURS = (9, 16)

CHANNELS = os.environ.get("CHANNELS", "").split(",")
BOTS = os.environ.get("BOTS", "").split(",")

USDT_WALLET = os.environ.get("USDT_WALLET")
CONTACT_EMAIL = os.environ.get("CONTACT_EMAIL")
