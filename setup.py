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
    packages=["classes"],

    # Include additional files into the package
    include_package_data=True,

    # Details
    #url="http://pypi.python.org/pypi/MyApplication_v010/",

    #
    license="LICENSE.txt",
    description="Useful towel-related stuff.",

    long_description=open("README.md").read(),

    
)