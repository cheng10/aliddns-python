import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="aliddns-python",
    version="0.0.1",
    author="cheng10",
    author_email="cheng10@ualberta.ca",
    description="A Dynamic DNS tool for alicloud",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/cheng10/aliddns-python",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)