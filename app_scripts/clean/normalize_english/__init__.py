import pandas as pd
import re


def normalize_english(inStr: str, opts: dict):
    """Normalizes enlish to the target language (UK or US) based
    on the dictionary found here: http://www.tysto.com/uk-us-spelling-list.html"""

    # import the matching table
    df = pd.read_csv("https://raw.githubusercontent.com/sagepublishing/text_cleaning/app_prototype/app_scripts/clean/normalize_english/us_uk_matching_table.csv")

    # create dictionaries (faster to iterate on)
    translate_uk_us = dict(zip(df.UK, df.US))
    translate_us_uk = dict(zip(df.US, df.UK))

    # depending on target language, search and match relevant dict
    if opts['target_language'] == "UK":
        for item in translate_us_uk.keys():
        	# the word has to be lower case to match the dictionary, but return the correct capitalization using ifelse statement
            if inStr[0].isupper():
                return re.sub(item, translate_us_uk[item], inStr.lower()).capitalize()
            else:
                return re.sub(item, translate_us_uk[item], inStr)

    elif opts['target_language'] == "US":
        for item in translate_uk_us.keys():
        	# the word has to be lower case to match the dictionary, but return the correct capitalization using ifelse statement
            if inStr[0].isupper():
                return re.sub(item, translate_uk_us[item], inStr.lower()).capitalize()
            else:
                return re.sub(item, translate_uk_us[item], inStr)
            
    else:
    	# if input is neither US nor UK, return error message
        return "Wrong input - please enter \"US\" or \"UK\"."
  