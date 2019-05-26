import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="teichicrypt",
    version="1.1.0",
    author="Teichi",
    author_email="tobias@teichmann.top",
    description="self build crypting algorithm",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/tobi08151405/crypt",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU GENERAL PUBLIC LICENSE",
        "Operating System :: OS Independent",
    ],
)

