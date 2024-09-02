import os
from pathlib import Path

project_name = "rohlik_forecasting"
list_of_files = [
                 f"{project_name}/__init__.py",
                 f"{project_name}/compoments/__init__.py",
                 f"{project_name}/compoments/data_ingestion.py",
                 f"{project_name}/compoments/data_transformation.py",
                 f"{project_name}/compoments/data_validation.py",
                 f"{project_name}/compoments/model_evaluation.py",
                 f"{project_name}/compoments/model_trainer.py",
                 f"{project_name}/compoments/model_pusher.py",
                 f"{project_name}/configuration/__init__.py",
                 f"{project_name}/constants/__init__.py",
                 f"{project_name}/entities/__init__.py",
                 f"{project_name}/entities/config_entity.py",
                 f"{project_name}/entities/artifact_entity.py",
                 f"{project_name}/exception/__init__.py",
                 f"{project_name}/logger/__init__.py",
                 f"{project_name}/pipeline/__init__.py",
                 f"{project_name}/pipeline/training_pipeline.py",
                 f"{project_name}/pipeline/prediction_pipeline.py",
                 f"{project_name}/utils/__init__.py",
                 f"{project_name}/utils/main_utils.py",
                 "app.py",
                 "requirements.txt",
                 "Dockerfile",
                 ".dockerignore",
                 "demo.py",
                 "setup.py",
                 "config/model.yaml",
                 "config/schema.yaml"
]
                 
for filepath in list_of_files:
   filepath = Path(filepath)
   filedir,filename = os.path.split(filepath)
   if filedir!="":
       os.makedirs(filedir,exist_ok=True)
   if(not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
       with open(filepath, "w") as f:
           pass
   else:
       print(f"File {filepath} already exists")