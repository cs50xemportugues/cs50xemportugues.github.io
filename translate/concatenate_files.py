FOLDER_CONTENT = "content"
MARKDOWN_EXTENSION = ".md"

def concat_files(course, input_filenames, folder, language):
    with open(f"{course}/{FOLDER_CONTENT}/{language}/{folder}/{input_filenames[0][0:-1]}{MARKDOWN_EXTENSION}", 'w') as outfile:
        for fname in input_filenames:
            with open(f"{course}/{FOLDER_CONTENT}/{language}/{folder}/{fname}.md") as infile:
                for line in infile:
                    outfile.write(line)
            outfile.write("\n\n")

def concat_files_notes(course, input_filenames, folder, language):
    with open(f"{course}/{FOLDER_CONTENT}/{language}/{folder}/{input_filenames[0][0:1]}{MARKDOWN_EXTENSION}", 'w') as outfile:
        for fname in input_filenames:
            with open(f"{course}/{FOLDER_CONTENT}/{language}/{folder}/{fname}") as infile:
                for line in infile:
                    outfile.write(line)
            outfile.write("\n\n")
