# Data Dev

Code for corpora cleaning and testing of modules and scripts in `python`.



## Set up in virtual environment

I recommend running the notebook in a virtual environment as it requires to install a number of packages. 

```python
# create a virtual environment
virtualenv -p python3 myenv
source venv/bin/activate

# install python kernel in venv
pip install --user ipykernel
python -m ipykernel install --user --name=myenv

# install required packages (this might take a while)
pip install -r requirements.txt

# then open the notebook with the myenv kernel
```

## Content

|          File name           | Purpose                                                      |
| :--------------------------: | ------------------------------------------------------------ |
|      exploration.ipynb       | notebook for testing, messy for now                          |
|       requirements.txt       | libraries required to run the code in exploration.ipynb      |
|  sample_pdf_french_law.pdf   | sample pdf used for testing (French Environmental Code in English) |
|  sample_xml_welsh_parl.xml   | sample xml file used for testing (welsh parliamentary proceedings) |
| transformed_welsh_parl.json  | result of transforming xml into json - welsh parl            |
| sample_pdf_afd_manifesto.pdf | more complex sample PDF (manifesto of the AFD)               |
|  sample_xml_french_parl.xml  | more complex sample XML (questions to French Parliament)     |
| transformed_french_parl.json | result of transforming xml into json - french parl           |
