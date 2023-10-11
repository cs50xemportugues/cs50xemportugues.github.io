import openai
import time
from files_names.text.specifications import specifications, specifications_part1, specifications_part2
from dotenv import load_dotenv
load_dotenv()  
import os
import sys

openai.api_key = os.getenv('CHATGPT_KEY')

def translate(files, folder, language, extension, file_description):

    for f in files:
        try:
            if folder=="manual":
                root_folder = "app/content/english"
            else:
                root_folder = "cs50x/content/english"

            if (folder=="labs_code" or folder=="psets_code"):
                source_file = open(f"{root_folder}/{folder}/{f}/{f}.{extension}", "r")
            elif (folder=="labs_checks"):
                source_file = open(f"{root_folder}/{folder}/{f}/__init__.{extension}", "r")
            else:
                source_file = open(f"{root_folder}/{folder}/{f}.{extension}", "r")


            if (extension=="py"):
                system_message = f"You are a helpful assistant that translates Python language code from English to {language.capitalize()}. Translate the function names also."
                prompt = f'Translate the following computer science {file_description} from English to {language.capitalize()}: \'{source_file.read()}\''
            elif (extension=="c"):
                system_message = f"You are a helpful assistant that translates C language code from English to {language.capitalize()}. Translate the function names also."
                prompt = f'Translate the following computer science {file_description} from English to {language.capitalize()}: \'{source_file.read()}\''
            else:
                system_message = f"You are a helpful assistant that translates computer science related content from English to {language.capitalize()}. Translate the text thoroughly. Do not summarize the translation. Do not convert HTML tags to Markdown."
                prompt = f'Translate the following computer science {file_description} from English to {language.capitalize()}: \'{source_file.read()}\''

                
            print(">>>>>>>>>> HERE 1")
            try:
                response = openai.ChatCompletion.create(
                    model="gpt-3.5-turbo",
                    messages=[
                        {"role": "system", "content": system_message},
                        {"role": "user", "content": prompt}
                    ],
                )

                print(">>>>>>>>>> HERE 2")

                print(response.choices[0].message.content)

                # It generates an html file instead of markdown because the pset page require the url_for function to properly route
                
                if folder=="psets":
                    generated_file = open(f'templates/{language}/psets/{f}.{extension}', 'w')
                    generated_file.writelines(response.choices[0].message.content)

                if folder=="manual":
                    current_directory = os.getcwd()
                    file_destination = f"{current_directory}/app/content/{language}/{folder}"
                    # Creates folder if not exists
                    if not (os.path.exists(file_destination)):
                        os.makedirs(file_destination)

                    translated_file = response.choices[0].message.content

                    # remove " at the end of file
                    if translated_file.startswith("'"):
                        translated_file = translated_file[1:]
                    if translated_file.startswith('"'):
                        translated_file = translated_file[1:]
                    # remove ' at the end of file
                    if translated_file.endswith("'"):
                        translated_file = translated_file[:-1]
                    if translated_file.endswith('"'):
                        translated_file = translated_file[:-1]

                    generated_file = open(f'{file_destination}/{f}.{extension}', 'w')
                    generated_file.writelines(translated_file)

                elif folder=="labs_code" or folder=="psets_code":

                    current_directory = os.getcwd()
                    file_destination = f"{current_directory}/cs50x/content/{language}/{folder}/{f}"

                    # Creates folder if not exists
                    if not (os.path.exists(file_destination)):
                        os.makedirs(file_destination)

                    generated_file = open(f'{file_destination}/{f}.{extension}', 'w')

                    # Replace TODO by FAZER
                    translated_file = response.choices[0].message.content.replace("TODO", "FAZER").replace("TO-DO", "FAZER")
                    translated_file.replace("int principal(", "int main(")
                    # remove ' at start of file
                    if translated_file.startswith("'"):
                        translated_file = translated_file[1:]
                    # remove ' at the end of file
                    if translated_file.endswith("'"):
                        translated_file = translated_file[:-1]

                    generated_file.writelines(translated_file)

                elif folder=="labs_checks":
                    generated_file = open(f'cs50x/content/{language}/labs_checks/{f}/__init__.{extension}', 'w')
                    generated_file.writelines(response.choices[0].message.content.replace("importar ", "import ").replace("check50.verificar", "check50.check").replace("check50.existe", "check50.exists").replace("check50.c.compila", "check50.c.compile").replace("check50.executar", "check50.run").replace(".entradas(", ".stdin(").replace(".rejeitar()", ".reject()").replace(".saída(", ".stdout(").replace(".sair(0)", ".exit(0)"))

                    source_cs50yml = open(f"cs50x/content/english/labs_checks/{f}/.cs50.yml", "r")
                    cs50yml = open(f'cs50x/content/{language}/labs_checks/{f}/.cs50.yml', 'w')
                    cs50yml.writelines(source_cs50yml.readlines())
                elif folder=="psets_code":
                    generated_file = open(f'cs50x/content/{language}/{folder}/{f}.{extension}', 'w')
                    generated_file.writelines(response.choices[0].message.content)
                else:
                    generated_file = open(f'cs50x/content/{language}/{folder}/{f}.{extension}', 'w')
                    generated_file.writelines(response.choices[0].message.content)
                
                print(">>>>>>>>>> HERE 3")

            except openai.error.InvalidRequestError:
                print(f">>>> Error: there was an error when translating '{f}'")
            time.sleep(20)
            
        except:
            print(f">>> Error: couldn't open the file '{f}'")
            pass


def concat_files(input_filenames, folder, language):
    with open(f"cs50x/content/{language}/{folder}/{input_filenames[0][0:-1]}.md", 'w') as outfile:
        for fname in input_filenames:
            with open(f"cs50x/content/{language}/{folder}/{fname}.md") as infile:
                for line in infile:
                    outfile.write(line)
            outfile.write("\n\n")

def concat_files_notes(input_filenames, folder, language):
    with open(f"cs50x/content/{language}/{folder}/{input_filenames[0][0:-2]}.md", 'w') as outfile:
        for fname in input_filenames:
            with open(f"cs50x/content/{language}/{folder}/{fname}.md") as infile:
                for line in infile:
                    outfile.write(line)
            outfile.write("\n\n")

def translate_specifications(language):
    translate(specifications, "specifications", language, "md", "Markdown file")

def translate_specifications_part1(language):
    translate(specifications_part1, "specifications", language, "md", "Markdown file")

def translate_specifications_part2(language):
    translate(specifications_part2, "specifications", language, "md", "Markdown file")

def translate_specifications_divided_part1(language):

    bulbs_files = [
        "bulbs1",
        "bulbs2",
        "bulbs3",
        "bulbs4",
    ]

    caesar_files = [
        "caesar1",
        "caesar2",
        "caesar3",
        "caesar4",
        "caesar5",
        "caesar6",
    ]
    
    cash_files = [
        "cash1",
        "cash2",
    ]
    
    filter_less_files = [
        "filter_less1",
        "filter_less2",
        "filter_less3",
        "filter_less4",
        "filter_less5",
    ]
    
    filter_more_files = [
        "filter_more1",
        "filter_more2",
        "filter_more3",
        "filter_more4",
        "filter_more5",
        "filter_more6",
    ]
    
    inheritance_files = [
        "inheritance1",
        "inheritance2",
    ]

    mario_less_files = [
        "mario_less1",
        "mario_less2",
        "mario_less3",
    ]

    population_files = [
        "population1",
        "population2",
    ]
    
    readability_files = [
        "readability1",
        "readability2",
        "readability3",
        "readability4",
        "readability5",
    ]
    
    recover_files = [
        "recover1",
        "recover2",
    ]
    
    reverse_files = [
        "reverse1",
        "reverse2",
        "reverse3",
        "reverse4",
        "reverse5"
    ]
    
    runoff_files = [
        "runoff1",
        "runoff2",
        "runoff3",
        "runoff4",
    ]
    
    smiley_files = [
        "smiley1",
        "smiley2",
    ]

    speller_files = [
        "speller1",
        "speller2",
        "speller3",
        "speller4",
        "speller5",
    ]
    
    substitution_files = [
        "substitution1",
        "substitution2",
    ]
    
    tideman_files = [
        "tideman1",
        "tideman2",
        "tideman3",
        "tideman4",
    ]
    
    wordle50_files = [
        "wordle501",
        "wordle502",
        "wordle503",
        "wordle504",
    ]

    volume_files = [
        "volume1",
        "volume2"
    ]
    
    files = volume_files +bulbs_files + cash_files + caesar_files + filter_less_files + filter_more_files + inheritance_files + mario_less_files + population_files + readability_files + recover_files + reverse_files + runoff_files + smiley_files + speller_files + substitution_files + tideman_files + wordle50_files 

    translate(files, "specifications", language, "md", "Markdown file")

    concat_files(bulbs_files, "specifications", language)
    concat_files(cash_files, "specifications", language)
    concat_files(caesar_files, "specifications", language)
    concat_files(filter_less_files, "specifications", language)
    concat_files(filter_more_files, "specifications", language)
    concat_files(inheritance_files, "specifications", language)
    concat_files(mario_less_files, "specifications", language)
    concat_files(population_files, "specifications", language)
    concat_files(readability_files, "specifications", language)
    concat_files(recover_files, "specifications", language)
    concat_files(reverse_files, "specifications", language)
    concat_files(runoff_files, "specifications", language)
    concat_files(smiley_files, "specifications", language)
    concat_files(speller_files, "specifications", language)
    concat_files(substitution_files, "specifications", language)
    concat_files(tideman_files, "specifications", language)
    concat_files(wordle50_files, "specifications", language)
    concat_files(volume_files, "specifications", language)

def translate_specifications_divided_part2(language):

    birthdays_files = [
        "birthdays1",
        "birthdays2"
    ]

    worldcup_files = [
        "worldcup1",
        "worldcup2",
        "worldcup3",
        "worldcup4",
        "worldcup5",
        "worldcup6"
    ]

    readability_files = [
        "python_readability1",
        "python_readability2",
        "python_readability3",
        "python_readability4"
    ]

    dna_files = [
        "dna1",
        "dna2",
        "dna3",
        "dna4"
    ]

    movies_files = [
        "movies1",
        "movies2",
        "movies3",
    ]

    homepage_files = [
        "homepage1",
        "homepage2",
        "homepage3"
    ]

    finance_files = [
        "finance1",
        "finance2",
        "finance3",
        "finance4",
        "finance5",
        "finance6",
        "finance7",
        "finance8",
    ]

    songs_files = [
        "songs1",
        "songs2",
        "songs3"
    ]
    
    files = songs_files + birthdays_files+ worldcup_files + readability_files + dna_files + movies_files + homepage_files + finance_files

    translate(files, "specifications", language, "md", "Markdown file")

    concat_files(songs_files, "specifications", language)
    concat_files(birthdays_files, "specifications", language)
    concat_files(worldcup_files, "specifications", language)
    concat_files(readability_files, "specifications", language)
    concat_files(dna_files, "specifications", language)
    concat_files(movies_files, "specifications", language)
    concat_files(homepage_files, "specifications", language)
    concat_files(finance_files, "specifications", language)

def translate_notes(language):

    notes0 = [
        "0_a",
        "0_b",
        "0_c",
        "0_d",
        "0_e",
        "0_f",
        "0_g",
    ]

    notes1 = [
        "1_a",
        "1_b",
        "1_c",
        "1_d",
        "1_e",
        "1_f",
        "1_g",
        "1_h"
    ]

    notes2 = [
        "2_a",
        "2_b",
        "2_c",
        "2_d",
        "2_e",
        "2_f",
    ]

    notes3 = [
        "3_a",
        "3_b",
        "3_c",
        "3_d",
        "3_e",
        "3_f"
    ]

    notes4 = [
        "4_a",
        "4_b",
        "4_c",
        "4_d",
        "4_e",
    ]

    notes5 = [
        "5_a",
        "5_b",
        "5_c",
    ]

    notes6 = [
        "6_a",
        "6_b",
        "6_c",
        "6_d",
        "6_e",
    ]

    notes7 = [
        "7_a",
        "7_b",
        "7_c",
        "7_d",
        "7_e",
        "7_f",
    ]

    notes8 = [
        "8_a",
        "8_b",
        "8_c",
        "8_d",
        "8_e",
        "8_f",
        "8_g",
        "8_h",
        "8_i",
    ]

    notes9 = [
        "9_a",
        "9_b",
        "9_c",
        "9_d",
        "9_e",
        "9_f",
        "9_g",
        "9_h",
    ]

    #files = notes0 + notes1 + notes2 + notes3+ notes4+ notes5+ notes6+ notes7+ notes8+ notes9
    files =  notes7+ notes8+ notes9

    translate(files, "notes", language, "md", "Markdown file")

    #concat_files_notes(notes0, "notes", language)
    #concat_files_notes(notes1, "notes", language)
    concat_files_notes(notes2, "notes", language)
    concat_files_notes(notes3, "notes", language)
    concat_files_notes(notes4, "notes", language)
    concat_files_notes(notes5, "notes", language)
    concat_files_notes(notes6, "notes", language)
    concat_files_notes(notes7, "notes", language)
    concat_files_notes(notes8, "notes", language)
    concat_files_notes(notes9, "notes", language)
    
def translate_psets(language):
    psets = ["2", "3", "4", "5", "6", "7", "8", "9"]
    translate(psets, "psets", language, "html", "HTML file")

def translate_psets_code(language):
    psets_code = ["bulbs", "caesar", "cash", "credit", "plurality", "readability", "recover", "reverse", "runoff", "substitution", "tideman", "wordle"]
    translate(psets_code, "psets_code", language, "c", "C language code")

# TODO
def translate_labs_checks(language):
    #checks = ["population", "scrabble", "smiley"]
    translate(["smiley", "population"], "labs_checks", language, "py", "Python code")

def translate_labs_code(language):
    code = ["inheritance", "scrabble", "volume"]
    translate(code, "labs_code", language, "c", "C code")
    
def translate_manual(language):

    manual = [
        "atof",
        "atoi",
        "atol",
        "ceil",
        "fclose",
        "floor",
        "fopen",
        "fprintf",
        "fread",
        "free",
        "fscanf",
        "fwrite",
        "get_char",
        "get_double",
        "get_float",
        "get_int",
        "get_long",
        "get_string",
        "isalnum",
        "isalpha",
        "isblank",
        "isdigit",
        "islower",
        "ispunct",
        "isspace",
        "isupper",
        "log2",
        "malloc",
        "pow",
        "printf",
        "random",
        "realloc",
        "round",
        "scanf",
        "sprintf",
        "sqrt",
        "srandom",
        "strcasecmp",
        "strcasestr",
        "strcmp",
        "strcpy",
        "strlen",
        "strstr",
        "time",
        "tolower",
        "toupper",
    ]


    manual = [
        "scanf",
    ]
    
    translate(manual, "manual", language, "md", "Markdown file")


if sys.argv[1] != "notes" and sys.argv[1] == "specifications" and sys.argv[1] == "psets":
    print("Usage: python translate.py CONTENT_TYPE LANGUAGE")
    print("CONTENT_TYPE can be one of the following: notes, psets, or specifications")
    sys.exit()    
else:
    print(f"Translating content to {sys.argv[2]}.")
    if sys.argv[1] == "notes":
        translate_notes(sys.argv[2])
    elif sys.argv[1] == "specifications":
        translate_specifications(sys.argv[2])
        translate_specifications_part1(sys.argv[2])
        translate_specifications_part2(sys.argv[2])
        translate_specifications_divided_part1(sys.argv[2])
        translate_specifications_divided_part2(sys.argv[2])
    elif sys.argv[1] == "psets":
        translate_psets(sys.argv[2])
    elif sys.argv[1] == "labs_code":
        translate_labs_code(sys.argv[2])
    elif sys.argv[1] == "psets_code":
        translate_psets_code(sys.argv[2])
    elif sys.argv[1] == "labs_checks":
        translate_labs_checks(sys.argv[2])
    elif sys.argv[1] == "manual":
        translate_manual(sys.argv[2])


