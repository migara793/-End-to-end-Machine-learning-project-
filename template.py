import os
from pathlib import Path
import logging
logging.basicConfig(level=logging.INFO,format='[%(asctime)s]:%(message)s: ')
project_name='mlproject'
list_of_files= [ 
".github/workflows/.gitkeep", 
f"src/{project_name}/_init__.py", 
f"src/{project_name}/components/_init__.py", 
f"src/{project_name}/utils/_init_.py", 
f"src/{project_name}/utils/common.py", 
f"src/{project_name}/config/_init_.py", 
f"src/{project_name}/config/configuration.py", 
f"src/{project_name}/pipeline/_init__.py", 
f"src/{project_name}/entity/_init_.py", 
f"src/{project_name}/entity/config_entity.py", 
f"src/{project_name}/constants/_init_.py", 
"config/config.yaml", 
"params.yaml", 
"schema.yaml", 
"main.py", 
"app.py", 
"Dockerfile", 
"requirements.txt", 
"setup.py", 
"research/trials.ipynb", 
"templates/index.html"]

for filepath in list_of_files:
    filepath=Path(filepath)
    filedr,filename=os.path.split(filepath)
    
    if filedr!="":
        os.makedirs(filedr,exist_ok=True)
        logging.info(f"Creating directory;{filedr} for the file:{filename}")
    
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath)==0):
        with open(filepath,'w')as f:
            pass
            logging.info(f"Creating empty file:{filename}")
    
    else:
        logging.info(f"{filename} is already exists")


         

