from setuptools import find_packages, setup
import pathlib
import os


setup(
    name = "MultiStageClustering",
    version = "0.0.1",
    author = "Ishita Roy,  Rama Chaitanya Karanam",
    author_email = "ramachaitanya0@gmail.com",
    description = 'Multi Stage Clustering',
    # long_description = readme,
    long_description_content_type = 'text/markdown',
    url = "https://github.com/ramachaitanya0/two_stage_clustering ",

    classifiers = [ 
        "Programming Language :: Python :: 3 ",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ] ,
    

    license='MIT',
    packages = ["MultiStageClustering"],
    # install_requires = [ 'pandas','numpy','sklearn>=0.22.1']
)

