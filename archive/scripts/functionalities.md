# List of functionalities

Brainstorm for functionalities. Based on experience + existing tools + research papers. 

[TOC]

> **Steps of text analysis:** 
>
> *From Text as Data (Benoit, 2019)*
>
> 1. Selecting texts and defining the corpus.
>
> 2. Converting of texts into a common electronic format.
> 3. Defining documents and choosing the unit of analysis
> 4. Defining and refining features.
> 5. Converting of textual features into a quantitative matrix.
> 6. Analyzing the (matrix) data using an appropriate statistical procedure. 7. Interpreting and reporting the results. 
>
> > **For inspiration:**
> >
> > * In R: Quanteda, TidyText, tm, stringr
> >
> > * In Python: NLTK, spaCy



## Loading text data

* Character vector
* .txt and .json
* Other file types (.docx, .pdf etc.)
* APIs
* Websites
* Load straight from cloud / websites (esp. if files are large)



## Mining text

* Extract the title, author, headers etc.
* Extract blocks of text with associated metadata
* Get encoding right
* Extract tables
* Extract noise (e.g. footer, reference numbers etc.)



## Basic cleaning

* Lowercase, strip line breaks and spaces
* Remove or extract numbers and punctuation
* Handle special symbols
* Replace special features by a token
* Handle unicode issues
* Remove stopwords according to different dictionaries



## Advanced cleaning and tagging

* Identify other languages
* Clean URLs
* Clean and extract text from HTML / CSS / JS
* Correct spelling mistakes / identifies potential mistakes and improper capitalization

* Speech tagging

* Co-reference resolution

* Collocation extraction

* Identify non common words (e.g. people / locations / domain names etc.)

* Conversion between US and UK english

  

## Pre-analysis preparation

* Tokenize
* Stem or lemmatize
* Create document-term matrices
* Group document-term matrices
* Weighted schemes for matrix
* Add covariates



## Descriptive statistics

* Word count
* Top features
* Readability
* Lexical diversity



## Contextualization

* Use external dictionaries

  
