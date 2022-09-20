from setuptools import setup , find_packages

with open('README.md','r', encoding='utf8') as f:
    LONG_DESCRIPTION=f.read()

AUTHOR='nitesh kumar gupta'
EMAIL='guptanitesh2711@gmail.com'
__version__='0.0.1'


setup(name='deep_classifier',
author=AUTHOR,
author_email=EMAIL,
license='MIT',
version=__version__,
#install_requires=['tensorflow','pandas','numpy','matplotlib'],
packages=find_packages(where="src"),
long_description=LONG_DESCRIPTION,
url='https://github.com/niteshgupta2711/dvc_ineuron',
package_dir={"": "src"},
project_urls={'Bug Tracker ': 'https://github.com/niteshgupta2711/dvc_ineuron'},
)