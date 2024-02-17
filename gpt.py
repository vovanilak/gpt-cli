import os
import typer
from typing_extensions import Annotated
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

models = {
    "gpt-3.5-turbo-0125": {
        "input_price": 0.144,
        "output_price": 0.432,
    },
    "gpt-3.5-turbo-1106": {
        "input_price": 0.3,
        "output_price": 0.6,
    },
    "gpt-3.5-turbo-0613": {
        "input_price": 0.43,
        "output_price": 0.58,
    },
    "gpt-3.5-turbo-16k-0613": {
        "input_price": 0.86,
        "output_price": 1.15,
    },
    "gpt-4": {
        "input_price": 8.64,
        "output_price": 17.28,
    },
    "gpt-4-1106-preview": {
        "input_price": 2.88,
        "output_price": 8.64,
    },
}

client = OpenAI(
    api_key=os.getenv("OPENAI_TOKEN"),
    base_url="https://api.proxyapi.ru/openai/v1"
)

def main(
    prompt: Annotated[str, typer.Argument()] = None,
    model: Annotated[str, typer.Option(help='Set a model. To get list of commands enter "--list"')] = "gpt-3.5-turbo-0125",
    limit: Annotated[int, typer.Option(help='Set a limit of tokens')] = 50,
    list: Annotated[bool, typer.Option(help='List of models')] = False
    ):
    if list:
        for k, v in models:
            print(k)
            print(v)
    elif prompt:
        chat_completion = client.chat.completions.create(
            model=model,
            messages=[{"role": "user", "content": prompt}],
            max_tokens=limit
        )
        print(chat_completion.choices[0].message.content)
    else:
        pr = input(f'{model} > ')
        while pr not in ("!", "ё"):
            chat_completion = client.chat.completions.create(
                model=model,
                messages=[{"role": "user", "content": pr}],
                max_tokens=limit
            )
            print(chat_completion.choices[0].message.content)
            pr = input(f'{model} > ')

if __name__ == "__main__":
    typer.run(main)

