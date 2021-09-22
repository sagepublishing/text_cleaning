.. _Transformations:


#################
Transformations
#################


Texti supports several different text preprocessing transformations that you can mix and match for your specific needs. You can also create workflows or sequences of transformations. The table below summarizes and provides examples of current transformations in Texti. 


.. list-table:: Transformations
   :header-rows: 1

   * - Category
     - Transformation
     - Description
     - Before Tranformation
     - Input
     - After Transformation
   * - Clean
     - Strip Whitespaces
     - 
     - 
     - -
     - 
   * - Clean
     - Remove Tags
     - 
     - 
     - -
     - 
   * - Clean
     - Fix Encoding
     - 
     - 
     - -
     - 
   * - Clean
     - remove headers
     - 
     - 
     - 1
     - 
   * - Clean
     - remove footers
     - 
     - 
     - 2
     - 
   * - Filter
     - Remove punctutation
     - 
     - 
     - -
     - 
   * - Filter
     - Remove Digits
     - 
     - 
     - -
     - 
   * - Filter
     - Remove URLs
     - 
     - 
     - -
     - 
   * - Filter
     - Remove Stopwords (gensim)
     - 
     - 
     - 
     - 
   * - Filter
     - remove Short words
     - 
     - 
     - 
     - 
   * - Filter
     - remove custom stop words
     - 
     - 
     - 
     - 
   * - Filter
     - remove stopwords (nltk)
     - 
     - 
     - 
     - 
   * - Filter
     - remove custom patters
     - 
     - 
     - 
     - 
   * - Filter
     - remove stopords except
     - 
     - 
     - 
     - 
   * - Filter
     - remove punctuation except
     - 
     - 
     - 
     - 
   * - Filter
     - remove brackets
     - 
     - 
     - 
     - 
   * - Filter
     - remove diacritics
     - 
     - 
     - 
     - 
   * - Replace
     - Replace URLs with tokens
     - 
     - 
     - 
     - 
   * - Replace
     - Replace Digits with Tokens
     - 
     - 
     - 
     - 
   * - Replace
     - Replace Currency symbols with tokens
     - 
     - 
     - 
     - 
   * - Replace
     - convert word numbers
     - 
     - 
     - 
     - 
   * - Replace
     - replace hyphenated words
     - 
     - 
     - 
     - 
   * - Format
     - To lowercase
     - 
     - 
     - 
     - 
   * - Format
     - Stem words
     - 
     - 
     - 
     - 
   * - Format
     - Lemmatize sentence (nltk)
     - 
     - 
     - 
     - 
   * - Format
     - stem words (Lancaster)
     - 
     - 
     - 
     - 
   * - Format
     - Lemmatize sentence (spacy)
     - 
     - 
     - 
     - 
   * - Format
     - To Sentences
     - 
     - 
     - 
     - 
   * - Format
     - Lemmatize sentence (textblob)
     - 
     - 
     - 


If you're interested in adding to the list, consider contributing! More details in the contribute page.