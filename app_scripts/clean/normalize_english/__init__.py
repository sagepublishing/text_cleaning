import pandas as pd

def normalize_english(inStr: str, opts: dict):
	"""Normalizes enlish to the target language (UK or US) based
	on the dictionary found here: http://www.tysto.com/uk-us-spelling-list.html"""

	# import the matching table
	df = pd.read_csv("us_uk_matching_table.csv")

	# create dictionaries (faster to iterate on)
	translate_uk_us = dict(zip(df.UK, df.US))
	translate_us_uk = dict(zip(df.US, df.UK))

	# get target language inputted by user
	target = opts['target_language']

	# depending on target language, search and match relevant dict
	if target == "UK":
		for item in translate_us_uk.keys():
			string = re.sub(item, translate_us_uk[item], inStr)
		return string

	elif target =="US":
		for item in translate_uk_us.keys():
			string = re.sub(item, translate_uk_us[item], inStr)
		return string