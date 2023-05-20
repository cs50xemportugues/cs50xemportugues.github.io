import openai
import time
from files_names.videos.labs import labs
import datetime
import os

openai.api_key = os.environ["CHATGPT_APIKEY"]

def translate(files, folder, language):

    for f in files:

        try:
            source_file = open(f"cs50x/content/english/{folder}/{f}.txt", "r")

            try:
                response = openai.ChatCompletion.create(
                    model="gpt-3.5-turbo",
                    messages=[
                        {"role": "system", "content": f"You are a helpful assistant that translates computer science related text from English to {language.capitalize()}. Translate the text thoroughly. Do not summarize the translation."},
                        {"role": "user", "content": f'Translate the following computer science script from English to {language.capitalize()}: "{source_file.read()}"'}
                    ],
                )

                generated_file = open(f'cs50x/content/{language}/{folder}/{f}.txt', 'w')
                generated_file.writelines(response.choices[0].message.content)

            except openai.error.InvalidRequestError:
                print(f"there was an error when translating '{f}'")
            time.sleep(20)
        except:
            pass

def translate_notes():
    translate(labs, "video_scripts", "french")

