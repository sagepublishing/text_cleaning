# Current alternatives



## Table of alternatives

What academics use for now and the associated shortcomings. Just for quick overview, can be linked to larger research / documents if needed. 



|   Name   |                 Link                 | Language |                              +                               |            -             |
| :------: | :----------------------------------: | :------: | :----------------------------------------------------------: | :----------------------: |
| Quanteda | https://github.com/quanteda/quanteda |    R     | All basic processing steps via simple functions + descriptive statistics + models. Models run fast. Good documentation. | Requires knowledge of R. |
| TidyText |                                      |    R     |                                                              |                          |
|  NLPTK   |                                      |  Python  |                                                              |                          |
|    tm    |                                      |    R     |                                                              |                          |
| stringr  |                                      |    R     |                                                              |                          |
|  spaCy   |                                      |  Python  |                                                              |                          |



## Random thoughts on this

* None of those packages provide simple ways to extract features eg. get all domain names of links, this still requires writing custom regular expressions which can be time consuming / frustrating (because high cost for a task that should be simple).
* Those tools do what you ask expressively, no recommendations / insights, e.g. forgetting to lowercase, or certain words are mispelled so cannot be matched etc. 