# List of text cleaning scripts



[TOC]

## Basic cleaning steps

Modules that contain a set of functions and that can be imported and used in Python.



### clean-text

* **Description**: Data on the Web and elsewhere is often dirty. Clean your text with `clean-text` to create normalized text representations. 
* **Type**: Python module

* **Link**: https://github.com/jfilter/clean-text
* **License**: Apache
* **Languages supported**: English and German
* **Functionalities**:
  * Fix unicode errors ()
  * Translate to closest ASCII representation
  * Lowercase text
  * Strip line breaks
  * Replace URLs with a special token
  * Replace email addresses with a special token
  * Replace phone numbers with a special token
  * Replace numbers with a special token
  * Replace digits with a special token
  * Replace currency symbols with a special token
  * Remove punctuation



### textcleaner

* **Description**: Text-Cleaner is a utility library for text-data pre-processing. Use it before passing the text data to a model.
* **Type**: Python module

* **Link**: https://github.com/YugantM/textcleaner
* **License**: MIT
* **Languages supported**: English and German
* **Functionalities**:
  * main_cleaner to do all the below in one call ! or
  * remove unnecessary blank lines
  * stip out a perticular character or default one
  * transfer all characters to lowercase if needed
  * remove numbers, symblos and stop-words from the whole text
  * tokenize the text-data on one call
  * stemming & lemmatization powered by NLTK

