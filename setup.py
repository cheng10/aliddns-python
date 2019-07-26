import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="aliddns-python",
    version="0.1.2",
    author="cheng10",
    author_email="cheng10@ualberta.ca",
    description="A Dynamic DNS(DDNS) tool for alicloud",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/cheng10/aliddns-python",
    packages=setuptools.find_packages(),
    install_requires=[
        'docopt',
        'requests',
        'aliyun-python-sdk-core',
        'aliyun-python-sdk-alidns',
    ],
    classifiers=[
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)