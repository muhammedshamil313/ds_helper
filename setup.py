from setuptools import setup, find_packages

setup(
    name="ds_helper",
    version="1.0.0",
    author="Your Name",
    description="A lightweight Data Science helper library for column detection, visualization, and text cleaning.",
    packages=find_packages(),
    install_requires=[
        "pandas",
        "matplotlib",
        "seaborn",
        "wordcloud",
        "nltk"
    ],
    python_requires='>=3.7',
)
