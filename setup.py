from setuptools import setup , find_packages

AUTHOR='nitesh kumar gupta'
EMAIL='guptanitesh2711@gmail.com'
__version__='0.0.1'


setup(name='deep classifier',
author=AUTHOR,
author_email=EMAIL,
license='MIT',
version=__version__,
install_requires=['tensorflow','pandas','numpy','matplotlib'],
packages=find_packages(where='src'))