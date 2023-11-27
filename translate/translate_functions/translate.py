import openai
import time
from dotenv import load_dotenv
load_dotenv()  
import os
from generate import generate_file, generate_prompt, generate_system_message, generate_prompt_notes
from ..types import TypeCourse, TypeLanguage, TypeContent
from typing import List

openai.api_key = os.getenv('CHATGPT_KEY')

def get_chatgpt_translation(system_message: str, prompt: str):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": system_message},
            {"role": "user", "content": prompt}
        ],
    )
    translated_content = response.choices[0].message.content
    return translated_content

def get_translation_and_generate_file(system_message, prompt, course, folder, f, language, extension):
    try:
        translated_content = get_chatgpt_translation(system_message, prompt)
        generate_file(course, folder, f, language, extension, translated_content)
    except openai.error.InvalidRequestError:
        print(f">>>> Error: there was an error when translating '{f}'")
    time.sleep(20)


def translate(
        course: TypeCourse,
        files: List[str],
        folder: TypeContent,
        language: TypeLanguage,
        extension: str,
        file_description: str):
    
    FOLDER_NOTES = "notes"
    FOLDER_LABS_CODE = "labs_code"
    FOLDER_PSETS_CODE = "psets_code"
    FOLDER_LABS_CHECKS = "labs_checks"
    FOLDER_PSETS_CHECKS = "psets_checks"

    # Defines root folder
    if folder=="manual":
        root_folder = "app/content/english"
    else:
        root_folder = f"{course}/content/english"

    system_message = generate_system_message(extension, language)
    prompt = generate_prompt(file_description, language, source_file)

    for f in files:
        try:
            if (folder==FOLDER_NOTES):
                source_file = open(f"{root_folder}/{folder}/{f}", "r")
                notes_chunks = source_file.read().split("\n## ")
                for chunk in notes_chunks:
                    prompt = generate_prompt_notes(file_description, language, "\n## "+chunk)
                    get_translation_and_generate_file(system_message, prompt, course, folder, f, language, extension)
            else:
                if (folder==FOLDER_LABS_CODE or folder==FOLDER_PSETS_CODE):
                    source_file = open(f"{root_folder}/{folder}/{f}/{f}.{extension}", "r")
                elif (folder==FOLDER_LABS_CHECKS or folder==FOLDER_PSETS_CHECKS):
                    source_file = open(f"{root_folder}/{folder}/{f}/__init__.{extension}", "r")
                else:
                    source_file = open(f"{root_folder}/{folder}/{f}.{extension}", "r")
                get_translation_and_generate_file(system_message, prompt, course, folder, f, language, extension)
        except:
            print(f">>> Error: couldn't open the file '{f}'")
            pass
