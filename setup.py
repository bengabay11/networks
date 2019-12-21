import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="network-scrips",
    version="0.0.1",
    author="Ben Gabay",
    author_email="ben.gabay38@example.com",
    description="Useful network scripts",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/bengabay11/network-scripts",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ]
)
