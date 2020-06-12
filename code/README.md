# Code and testing



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

# install required packages
cd code
pip install -r requirements.txt

# then open the notebook with the myenv kernel
```

