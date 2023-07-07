from setuptools import setup,find_packages
from typing import List


HYPER_E_DOT = '-e .'
def get_requirements(filepath: str) -> List[str]:
    
    '''This function will return a list of requirements'''
    requirement = []
    with open(filepath) as file_obj:
        requirement = file_obj.readlines()
        requirement = [req.replace('\n', '') for req in requirement]
        
        if HYPER_E_DOT in requirement:
            requirement.remove(HYPER_E_DOT)
            
    return requirement


setup(
    name='mlproject',
    version='0.0.1',
    author='Srimam',
    author_email='srimam@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt'),
)