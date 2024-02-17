#!/usr/local/bin/gpp/venv/bin/python3
import argparse
import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(
    api_key="sk-BbVzUw3MPu6BPkesXt0GTBiDRGXYjLBx",
    base_url="https://api.proxyapi.ru/openai/v1",
)

def main():
    parser = argparse.ArgumentParser(description='Утилитиа gpt-3.5-turbo')
    parser.add_argument('prompt', type=str, help='Ваш запрос')

    args = parser.parse_args()
    chat_completion = client.chat.completions.create(
        model="gpt-3.5-turbo", messages=[{"role": "user", "content": args.prompt}]
    )

    print(chat_completion.choices[0].message.content)

if __name__ == '__main__':
    main()
