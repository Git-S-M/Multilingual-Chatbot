
from get_response import *

bot_name = "Assistant"
print("Un assistant virtuel est là pour répondre à toutes vos questions au sujet du Coronavirus. Ecrivez 'stop' pour quitter la discussion.")

while(english==1):
    sentence = input("Vous: ")
    if sentence == 'stop':
        break
    print(bot_name + ': ' + get_response(sentence))

while(french==1):
    sentence = input("Vous: ")
    if sentence == 'stop':
        break
    print(bot_name + ': ' + get_response_1(sentence)) 