# willl be resp in creating ml applcation as a package we can deploy in pypy so that anyone can use it 
# this link has more info : https://stackoverflow.com/questions/1471994/what-is-setup-py
from setuptools import find_packages,setup


HYPHEN_E_DOT = '-e .'

def get_requirements(file_path):

    '''
     This function will return the list of requirements
    '''

    with open(file_path) as file :
    
     requirements_list = file.readlines()
     requirements_list = [req.replace("\n","") for req in requirements_list]
    
    # The hyphen e . is used to automaticaly run the setup.py file through requirements.txt
    if HYPHEN_E_DOT in requirements_list:
        requirements_list.remove(HYPHEN_E_DOT)

              
    return requirements_list

setup(

    name = 'end_to_end_mlproject',
    version= '0.0.1',
    author= 'Swarup',
    author_email="swarupyeole11@gmail.com",
    # this find packages will look for all the folders with __init__ file and try to build it 
    packages=find_packages(),
    install_requires = get_requirements('requirements.txt')

)

# print(get_requirements('requirements.txt'))