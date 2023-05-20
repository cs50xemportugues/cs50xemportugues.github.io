from flask import Flask, render_template
from cs50x import cs50x
import os
from cs50x.content.french.language import menu as menu_french
from cs50x.content.portuguese.language import menu as menu_portuguese
from cs50x.content.spanish.language import menu as menu_spanish
from cs50x.content.english.language import menu as menu_english

from cs50x.content.french.language import specifications_urls as specifications_urls_french
from cs50x.content.portuguese.language import specifications_urls as specifications_urls_portuguese
from cs50x.content.spanish.language import specifications_urls as specifications_urls_spanish
from cs50x.content.english.language import specifications_urls as specifications_urls_english

app = Flask(__name__)
app.config["FREEZE_DESTINATION"] = os.environ["COURSE_LANGUAGE"]

if os.environ["COURSE_LANGUAGE"] == "portuguese":
    app.config["FREEZER_DESTINATION"] = "portuguese"
    app.config["LANGUAGE"] = "portuguese"
    app.config["ASIDE_BG_COLOR"] = "green"
    app.config["LANGUAGE_MENU"] = menu_portuguese
    app.config["SPECIFICATION_URLS"] = specifications_urls_portuguese

elif os.environ["COURSE_LANGUAGE"] == "spanish":
    app.config["FREEZER_DESTINATION"] = "spanish"
    app.config["LANGUAGE"] = "spanish"
    app.config["ASIDE_BG_COLOR"] = "red"
    app.config["LANGUAGE_MENU"] = menu_spanish
    app.config["SPECIFICATION_URLS"] = specifications_urls_spanish

elif os.environ["COURSE_LANGUAGE"] == "french":
    app.config["FREEZER_DESTINATION"] = "french"
    app.config["LANGUAGE"] = "french"
    app.config["ASIDE_BG_COLOR"] = "blue"
    app.config["LANGUAGE_MENU"] = menu_french
    app.config["SPECIFICATION_URLS"] = specifications_urls_french

elif os.environ["COURSE_LANGUAGE"] == "english":
    app.config["FREEZER_DESTINATION"] = "english"
    app.config["LANGUAGE"] = "english"
    app.config["ASIDE_BG_COLOR"] = "black"
    app.config["LANGUAGE_MENU"] = menu_english
    app.config["SPECIFICATION_URLS"] = specifications_urls_english


app.register_blueprint(cs50x, url_prefix='/2023')

if __name__ == '__main__':
    app.run()
