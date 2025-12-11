from setuptools import find_packages, setup
from typing import List
import os

HYPHEN_DOT_E = "-e ."
def get_req(file_path:str)->List[str]:
    """This fn will return the list of requirements
    """
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [each_req.replace("\n","")
                        for each_req in requirements]
        ##We need to remove this -e . cause this just
        # triggers the setup.py, its not a module.
        if HYPHEN_DOT_E in requirements:
            requirements.remove(HYPHEN_DOT_E)
    return requirements

setup(
    name="AI_and_ML_project_1",
    version='0.0.1',
    author="Arman",
    author_email='armanixofficial01@gmail.com',
    packages=find_packages(),
    install_requires = get_req(os.path.join(os.path.dirname(__file__),'requirements.txt')) 
    # 
    #               
    ##INSTED OF THIS['numpy', "pandas", "seaborn"], WE CHOOSE
    #GET REQUIREMENTS
)
