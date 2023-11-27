from .translate import translate
from concatenate_files import concat_files
from ..files_names import specifications, specifications_part1, specifications_part2

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
