# Distributed Denial of Service Telegram Bot

import telebot
import threading
import time

API_TOKEN = '7981467842:AAFYTLyCYLY6WokzyA2lq0m3vEZBcXS-OmE'
bot = telebot.TeleBot(API_TOKEN)

active_attacks = {}

def attack(target):
    while active_attacks.get(target):
        # Simulate sending requests to the target
        print(f"Attacking {target}...")
        time.sleep(1)

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "Welcome! Use /attack <target> to start an attack and /stop <target> to stop it.")

@bot.message_handler(commands=['attack'])
def attack_command(message):
    target = message.text.split()[1]
    if target not in active_attacks:
        active_attacks[target] = True
        threading.Thread(target=attack, args=(target,)).start()
        bot.reply_to(message, f"Started attacking {target}.")
    else:
        bot.reply_to(message, f"Already attacking {target}.")

@bot.message_handler(commands=['stop'])
def stop_command(message):
    target = message.text.split()[1]
    if target in active_attacks:
        active_attacks[target] = False
        del active_attacks[target]
        bot.reply_to(message, f"Stopped attacking {target}.")
    else:
        bot.reply_to(message, f"Not attacking {target}.")

bot.polling()
