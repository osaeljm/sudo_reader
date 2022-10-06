#! /usr/bin/env python

from setuptools import setup

setup(
   name='parsrepo',
   version='0.1.2',
   description='Python script that parses and generate a report of sudoers file.',
   long_description=open("README.md").read(),
   long_description_content_type="text/mardown",
   #entry_points={"console_scripts:["parsrepo=parsrepo.type:find_alias"]"},
   author='Osael Jimenez',
   author_email='osa092@gmail.com',
   license='Apache License',
   packages=['parsrepo'],  # would be the same as name
   install_requires=['typer', 'os', 're','openpyxl', 'getpass', 'rich'], #external packages acting as dependencies
)