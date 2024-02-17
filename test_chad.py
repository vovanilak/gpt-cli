"""Пример работы с чатом через gigachain"""
from langchain.schema import HumanMessage, SystemMessage
from langchain.chat_models.gigachat import GigaChat
import os
from dotenv import load_dotenv

load_dotenv()

# Авторизация в сервисе GigaChat
chat = GigaChat(credentials=os.getenv('GIGA_TOKEN'),
                verify_ssl_certs=False)

messages = [
    #SystemMessage(
    #    content="Ты бот-программист, который помогает пользователю с программированием на python"
    #)
]

while(True):
    # Ввод пользователя
    user_input = input("User: ")
    messages.append(HumanMessage(content=user_input))
    res = chat(messages)
    messages.append(res)
    # Ответ сервиса
    print("Bot: ", res.content)