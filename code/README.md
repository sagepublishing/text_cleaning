# Code and testing



Code for corpora cleaning and testing of modules and scripts in `python`.



## Set up in virtual environment

```python
# create a virtual environment
virtualenv -p python3 myenv
source venv/bin/activate

# set working directory
pip install --user ipykernel
python -m ipykernel install --user --name=myenv

# install required packages
cd code
pip install -r requirements.txt

# then open the notebook with the myenv kernel
```

