from distutils.core import setup

setup(
    # Application name:
    name="LogParser",

    # Version number (initial):
    version="0.1.0",

    # Application author details:
    author="Alexandre Carrillo",
    author_email="alexandre.carrillo@e-campus.uab.cat",

    # Packages
    packages=["lparser"],

    # Include additional files into the package
    include_package_data=True,

    
    #
    license="LICENSE.txt",
    

    long_description=open("README.md").read(),

    
)
