from setuptools import setup, find_packages
AUTHOR='NItesh Kumar Gutpta'
EMAIL='guptanitesh2711@gmail.com'
INSTALL_REQUIRES=['sklearn','numpy','dvc','tensorflow']




setup(author=AUTHOR,
author_email=EMAIL,
install_requires=INSTALL_REQUIRES,
packages=find_packages())