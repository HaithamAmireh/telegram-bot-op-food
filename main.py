import os
import random

import telebot
from util import food_item, food_items_snacks, resturants_to_food, resturants_to_snacks

BOT_TOKEN = os.environ.get("BOT_TOKEN")

bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands=["food"])
def list_categories_food(message):
    bot.reply_to(
        message,
        f"These are the available Food Items: {','.join(food_items)}, use \n/Burgers \n/Pizza \n/Zarb \n/Mansaf \n/FriedChicken \n/Shawarma .",
    )


@bot.message_handler(commands=["snacks"])
def list_categories_snack(message):
    bot.reply_to(
        message,
        f"These are the available snack Items: {','.join(food_items_snacks)}, use \n/IceCream \n/BubbleTea \n/Juice .",
    )


@bot.message_handler(commands=food_items + food_items_snacks)
def get_place(message):
    resturant = select_at_random(message.text[1:])
    bot.reply_to(message, str(resturant))


@bot.message_handler(commands=["start", "hello"])
def send_welcome(message):
    bot.reply_to(
        message,
        "Hey there!, Welcome to OP Food Stupid.\n These are the available commands \n/food \n/snacks",
    )


@bot.message_handler(func=lambda msg: True)
def echo_all(message):
    bot.reply_to(message, f"{message.text} is not a command. Check /start")


def select_at_random(food_item):
    if food_item in resturants_to_food:
        return resturants_to_food[food_item][
            random.randint(0, len(resturants_to_food[food_item]) - 1)
        ]


bot.infinity_polling()
