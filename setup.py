from setuptools import setup, find_packages

setup(
    name="openai-pricing-scraper",
    version="0.1.1",
    packages=find_packages(),
    install_requires=[
        "beautifulsoup4",
        "requests",
    ],
)
