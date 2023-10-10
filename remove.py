import os

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
]

current_directory = os.getcwd()

for f in manual:
    source_file = open(f"app/content/portuguese/manual/{f}.md", "r")

    content = source_file.read()

    # remove ' (or "") at the end of file
    if content.startswith("'"):
        content = content[1:]
    if content.startswith('"'):
        content = content[1:]
    # remove ' (or "") at the end of file
    if content.endswith("'"):
        content = content[:-1]
    if content.endswith('"'):
        content = content[:-1]

    generated_file = open(f"app/content/portuguese/manual/{f}.md", 'w')
    generated_file.writelines(content)
