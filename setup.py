from setuptools import setup,find_packages
from typing import List

def get_requirements(file:str)-> List[str]:
    HYPEN_E_DOT = '-e .'
    libraries=[]

    with open (file) as file_obj:
        libraries = file_obj.readlines()
        libraries = [req.replace('\n','') for req in libraries] 

        if HYPEN_E_DOT in libraries:
            libraries.remove(HYPEN_E_DOT)
    return libraries
setup(

    name='Nifty_50_Forcasting',
    version=1.0,
    author="Aniket_Kumar",
    author_email="aniketue175011ece@gmail.com",
    packages=find_packages(),
    install_requires = get_requirements('requirements.txt')
    
    
)