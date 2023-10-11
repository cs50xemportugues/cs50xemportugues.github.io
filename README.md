# CS50x Website Builder

This project uses ChatGPT to translate the content from Harvard University's CS50 course, and then uses Flask to build the content into a set of static files that can be hosted on Github Pages.

This program has been used to build the websites for the Portuguese, French, and Spanish versions of the course:

- [CS50x em Português](https://cs50xemportugues.github.io/)
- [CS50x en Français](https://cs50xenfrancais.github.io/)
- [CS50x en Español](https://cs50xenespanol.github.io/)

But it can be used to translate the course to any language!

## Translating the Content

The course content to be translated can be divided into 3 groups: Video content, Text content, and Code content.

- Video content
  - Lectures
  - Sections
  - Shorts
  - Walkthroughs
    - Labs
    - Psets
- Text content
  - Manual
  - Style Guide
  - Slides
    - Lectures
    - Shorts
    - Walkthroughs
  - Notes
  - Specifications
    - Labs
    - Psets
  - Website pages
    - Certificate
    - FAQs
    - Homepage
    - Academic Honesty
    - Final Project
    - Office Hours
    - Sections
    - Seminars
    - Staff
    - Syllabus
    - Thanks
- Code content
  - Source code
    - Lectures
    - Labs
    - Psets
  - Checks
    - Labs
    - Psets

### Chat GPT Limitations

ChatGPT limits the number of words that can be translated in one api call, therefore some of the content has to be divided into multiple files so that they can be translated and then reassembled together in the correct order once translated.

### Adapting the translated content

It is important to differentiate when it is better to use an English term instead of the translation

### How to translate the content

The script `translate.py` is the program used to translate the content. To translate a group of content into a specific language, run the following command:

`python translate.py CONTENT_TYPE LANGUAGE`

where `CONTENT_TYPE` is the type of content to be translate (notes, psets, specifications, etc) and `LANGUAGE` is language the content will be translated to, eg. Portuguese.

The argument `CONTENT_TYPE` can be one of the following options:

- `labs_checks`
- `labs_code`
- `labs_scripts`
- `labs_specifications`
- `lectures_code`
- `lectures_scripts`
- `lectures_slides`
- `notes`
- `psets`
- `psets_checks`
- `psets_code`
- `psets_specifications`
- `shorts_scripts`
- `shorts_slides`
- `walkthroughs_scripts`
- `walkthroughs_slides`
- `additional_pages`

The translated content will be stored at `cs50x/content/LANGUAGE`. These translated files will then be used to build the course website using Frozen-Flask.

## Setup

### Courses

Each course/section is contained in a module/package:

- `app`: Core tools like Manual Pages, Help50, and more
- `cs50x`: Introduction to Computer Science
- `python`: Introduction to Programming with Python
- `web`: Web Programming with Python and JavaScript
- `ai`: Introduction to Artificial Intelligence with Python
- `sql`: Introduction to Databases with SQL
- `cybersecurity`: Introduction to Cybersecurity
- `games`: Introduction to Game Development
- `business`: Computer Science for Business Professionals
- `law`: Computer Science for Lawyers
- `technology`: Understanding Technology

### Environment Variables

Create a `.env` file and include the following environment variables:

- `COURSE_LANGUAGE`: The language of the course to visualize the website (portuguese, spanish, or french)
- `CHATGPT_KEY`: Your ChatGPT API key

## Building the Project

After translating the content, run the following command to build (freeze) the project in a set of static files:

`python freeze.py`

This will create a folder called `build_LANGUAGE` (e.g. `build_portuguese`) that contains the files that compose the website. You can host it on Github Pages.
