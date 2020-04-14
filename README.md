## Python CLI Template
### Runtime Requirements  
[Python 3.6+](https://www.python.org/downloads/)  
[PIP package manager](https://pip.pypa.io/en/stable/installing/)  
[virtualenv](https://virtualenv.pypa.io/en/latest/)  
### Set up and Run  
1. From the project root folder, create a Python 3.6+ virtual environment  
`$ virtualenv --python=python3 env`  
2. Activate the virtual environment  
`$ source env/bin/activate`  
3. Install the project dependencies  
`$ pip install -r requirements.txt`  
4. Copy the configuration from from  
`data/configuration/no_key_example.yml`  
to  
`data/configuration/dev.yml`  
5. Update the `data/configuration/dev.yml` file with Box Platform application JWT keys and set the seed related attibutes  
6. Run the command line interface menu to see the available commands  
`$ python src/cli/main.py` 
7. Run the foo command to build a datetime chunked Box environment  
 `$ python src/cli/main.py foo`  