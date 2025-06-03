import setuptools

with open("README.md", "r",encoding="utf-8") as f:
    long_description = f.read()
    
    
__version__ = "0.1.0"

REPO_NAME = "TEXT-SUMMARIZATION"
AUTHOR_NAME = "Yash-2815"
SRC_REPO = "TextSummarizer"
AUTHOR_MAIL = "yaswanthbadeti09@gmail.com"

setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_NAME,
    author_email=AUTHOR_MAIL,
    description="Text Summarization tool using BERT model",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Yash-2815/TEXT-SUMMARIZATION",
    project_urls={
        "Bug Tracker": "https://github.com/Yash-2815/TEXT-SUMMARIZATION/issues",
    },
    packages=setuptools.find_packages(where="src"),
    package_dir={"": "src"},
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)