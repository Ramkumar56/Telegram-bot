from telegram import *
from telegram.ext import *
from timeandtable import *


bot=Bot("1636584404:AAES2UcLnb-Qfh3BxkGZvXKw5nPDe6pAlTM")
#print(bot.get_me())

updater=Updater("1649812724:AAF_qLhkCyUF_5giRNJK5hKZieWBh3ssDb4",use_context=True)

dispatcher=updater.dispatcher

def test_function(update:Update,context:CallbackContext):
	bot.send_message(
	
	        chat_id=update.effective_chat.id,
	        text="Hello,Have a nice day",
	        )
	       
start_value=CommandHandler('hi',test_function)

dispatcher.add_handler(start_value)

def test_function1(update:Update,context:CallbackContext):
	bot.send_message(
	
	        chat_id=update.effective_chat.id,
	        text="https://meet.google.com/dom-xbpm-usd",
	        )
	       
start_value1=CommandHandler('cd',test_function1)

dispatcher.add_handler(start_value1)

#print(bot.get_me())

def test_function2(update:Update,context:CallbackContext):
	bot.send_message(
	
	        chat_id=update.effective_chat.id,
	        text="https://meet.google.com/row-hszw-ckx",
	        )
	       
start_value2=CommandHandler('ml',test_function2)

dispatcher.add_handler(start_value2)

#print(bot.get_me())

def test_function3(update:Update,context:CallbackContext):
	bot.send_message(
	
	        chat_id=update.effective_chat.id,
	        text="https://teams.microsoft.com/l/meetup-join/19%3a3af7fa1cb2864576bf2a31367912d701%40thread.tacv2/1609836209655?context=%7b%22Tid%22%3a%22a1a25784-a9a3-463c-b172-e33616c44667%22%2c%22Oid%22%3a%22906361ce-eb56-4bb7-ba54-885c8174a1a6%22%7d",
	        )
	       
start_value3=CommandHandler('erp',test_function3)

dispatcher.add_handler(start_value3)

#print(bot.get_me())

def test_function4(update:Update,context:CallbackContext):
	bot.send_photo(
	
	        chat_id=update.effective_chat.id,
	        photo="AgACAgUAAxkBAAOCYF2ae_rBlgfltRNpJe_-u-GITaIAAhGuMRtsJ-lW-szHh-QNPJ-9guxudAADAQADAgADeQADCSUDAAEeBA",
	        )
	       
start_value4=CommandHandler('ftt',test_function4)

dispatcher.add_handler(start_value4)

#print(bot.get_me())

def test_function5(update:Update,context:CallbackContext):
	bot.send_message(
	
	        chat_id=update.effective_chat.id,
	        text=table(),
	        )
	       
start_value5=CommandHandler('tt',test_function5)

dispatcher.add_handler(start_value5)

#print(bot.getme())

def test_function6(update:Update,context:CallbackContext):
	bot.send_message(
	
	        chat_id=update.effective_chat.id,
	        text=check(),
	        )
	       
start_value6=CommandHandler('now',test_function6)

dispatcher.add_handler(start_value6)

#print(bot.getme())

def test_function7(update:Update,context:CallbackContext):
	bot.send_message(
	
	        chat_id=update.effective_chat.id,
	        text=nextcl(),
	        )
	       
start_value7=CommandHandler('next',test_function)

dispatcher.add_handler(start_value7)

#print(bot.getme())

updater.start_polling()
