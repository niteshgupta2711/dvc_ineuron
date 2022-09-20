import os
from pathlib import Path
package_name='DEEP_Classifier'

list_of_files=['.github/workflows/.gitkeep',
f'src/{package_name}/__init__.py',
'tests/__init__.py',
'tests/unit/__init__.py', # testing a single component
'tests/integration/__init__.py', # testing multiple components
'config/config.yaml',
'dvc.yaml',
'params.yaml',
'init_setup.sh',
'requirements.txt',
'setup.py',
'setup.cfg',
'pyproject.toml',
'tox.ini',
'notebooks/trials.ipynb',
'.gitignore',
'requirements_dev.txt',
]

if __name__=='__main__':
    for file_path in list_of_files:
        file_path=Path(file_path)
        dir, file= os.path.split(file_path)
        if dir=='':
            dir='./'
        os.makedirs(dir, exist_ok=True)
        if (not os.path.exists(os.path.join(dir,file))) or os.path.getsize(os.path.join(dir,file))==0:
            with open(os.path.join(dir,file),'w') as f1:
                pass
