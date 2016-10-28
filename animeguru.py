#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  animeguru.py
#  
#  Copyright 2016 facorrea <facorrea@inf.ufpel.edu.br>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
# 

"""
You have to set your own TOKEN ID to run this bot;
Also you need to set an user ID to test the running bot
"""

ADMINID = 211237132
TOKEN = "211346378:AAEQbLgvduLDfMLPvqe9hprfBDAHuJHkcCI"

from twx.botapi import TelegramBot, ReplyKeyboardMarkup


"""
BOT SUMMONING
"""

def main(args):
	bot = TelegramBot(TOKEN)
	bot.update_bot_info().wait()
	print(bot.username) + " is running on Telegram now!"

	"""
	Send a message to a user
	"""
	user_id = int(ADMINID)

	result = bot.send_message(user_id, 'Hello, goshujin-sama! I am running OK, here, you may... t-test me...').wait()
	#print(result)

	""" 
	Get updates sent to the bot
	"""
	updates = bot.get_updates().wait()
	#for update in updates:
		#print(update)


if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
