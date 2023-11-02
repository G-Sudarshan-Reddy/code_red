from setuptools import find_packages, setup
from typing import List

hypen = '-e .'
def get_req(file_path:str)->List[str]:
    
    requirements = []
    with open('requirements.txt') as file_obj:
        requirements=file_obj.readlines()
        requirements = [req.replace("\n","") for req in requirements ]

        if hypen in requirements:
            requirements.remove(hypen)

    return requirements
 

setup(
name = 'code_red',
version = '0.0.1',
author='sudarshan',
author_email = 'sudarshangopal10@gmail.com',
packages = find_packages(),
install_requires= get_req('requirements.txt')
)