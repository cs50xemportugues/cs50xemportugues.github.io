import os
from .types import TypeCourse, TypeLanguage, TypeContent

def generate_system_message(extension: str, language: TypeLanguage):
    SYSTEM_MESSAGE_PYTHON = f"You are a helpful assistant that translates Python language code from English to {language.capitalize()}. Translate the function names also."
    SYSTEM_MESSAGE_C = f"You are a helpful assistant that translates C language code from English to {language.capitalize()}. Translate the function names also."
    SYSTEM_MESSAGE_MARKDOWN = f"You are a helpful assistant that translates computer science related content from English to {language.capitalize()}. Translate the text thoroughly. Do not summarize the translation. Do not convert HTML tags to Markdown."

    if (extension=="py"):
        return SYSTEM_MESSAGE_PYTHON
    elif (extension=="c"):
        return SYSTEM_MESSAGE_C
    else:
        return SYSTEM_MESSAGE_MARKDOWN

def generate_prompt(file_description: str, language: TypeLanguage, source_file):
    return f'Translate the following computer science {file_description} from English to {language.capitalize()}: {source_file.read()}'

def generate_prompt_notes(file_description: str, language: TypeLanguage, source_file):
    return f'Translate the following computer science {file_description} from English to {language.capitalize()}: \'{source_file}\''

def remove_leading_and_trailing(translated_content):
    """
    Removes unwanted leading and trailing characters
    """
    # remove " at the end of file
    if translated_content.startswith("'"):
        translated_content = translated_content[1:]
    if translated_content.startswith('"'):
        translated_content = translated_content[1:]
    # remove ' at the end of file
    if translated_content.endswith("'"):
        translated_content = translated_content[:-1]
    if translated_content.endswith('"'):
        translated_content = translated_content[:-1]
    return translated_content

def replace_incorrect_translations(translated_content):
    translated_content.replace("TODO", "FAZER")
    translated_content.replace("TO-DO", "FAZER")
    translated_content.replace("int principal(", "int main(")
    return translated_content

def replace_incorrect_translations_checks(translated_content):
    translated_content.replace("importar ", "import ")
    translated_content.replace("check50.verificar", "check50.check")
    translated_content.replace("check50.existe", "check50.exists")
    translated_content.replace("check50.c.compila", "check50.c.compile")
    translated_content.replace("check50.executar", "check50.run")
    translated_content.replace(".entradas(", ".stdin(")
    translated_content.replace(".rejeitar()", ".reject()")
    translated_content.replace(".saída(", ".stdout(")
    translated_content.replace(".sair(0)", ".exit(0)")
    return translated_content

def generate_file(
        course: TypeCourse,
        folder: TypeContent,
        f: str,
        language: TypeLanguage,
        extension: str,
        translated_content: str):
    
    current_directory = os.getcwd()

    if folder=="psets":
        new_file = open(f'templates/{language}/psets/{f}.{extension}', 'w')
        new_file.writelines(translated_content)

    if folder=="manual":
        
        file_destination = f"{current_directory}/app/content/{language}/{folder}"

        # Creates folder if not exists
        if not (os.path.exists(file_destination)):
            os.makedirs(file_destination)

        translated_content = remove_leading_and_trailing(translated_content)

        new_file = open(f'{file_destination}/{f}.{extension}', 'w')
        new_file.writelines(translated_content)

    elif folder=="labs_code" or folder=="psets_code":

        file_destination = f"{current_directory}/{course}/content/{language}/{folder}/{f}"

        # Creates folder if not exists
        if not (os.path.exists(file_destination)):
            os.makedirs(file_destination)

        new_file = open(f'{file_destination}/{f}.{extension}', 'w')
        translated_content = replace_incorrect_translations(translated_content)
        translated_content = remove_leading_and_trailing(translated_content)
        new_file.writelines(translated_content)

    elif folder=="labs_checks" or folder=="psets_checks":

        file_destination = f"{current_directory}/{course}/content/{language}/{folder}/{f}"
        
        # Creates folder if not exists
        if not (os.path.exists(file_destination)):
            os.makedirs(file_destination)

        generated_file = open(f'{course}/content/{language}/{folder}/{f}/__init__.{extension}', 'w')

        generated_file.writelines(replace_incorrect_translations_checks(translated_content))

        source_cs50yml = open(f"{course}/content/english/{folder}/{f}/.cs50.yml", "r")
        cs50yml = open(f'{course}/content/{language}/{folder}/{f}/.cs50.yml', 'w')
        cs50yml.writelines(source_cs50yml.readlines())

    elif folder=="psets_code":
        new_file = open(f'{course}/content/{language}/{folder}/{f}.{extension}', 'w')
        new_file.writelines(translated_content)

    elif folder=="notes":
        file_destination = f"{current_directory}/{course}/content/{language}/{folder}"

        print(">>> File destination: ", file_destination)

        # Creates folder if not exists
        if not (os.path.exists(file_destination)):
            os.makedirs(file_destination)

        generated_file = open(f'{file_destination}/{f}', 'a')
        generated_file.writelines("\n\n"+translated_content)
    else:
        generated_file = open(f'{course}/content/{language}/{folder}/{f}.{extension}', 'w')
        generated_file.writelines(translated_content)
