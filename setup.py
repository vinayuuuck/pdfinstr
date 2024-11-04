from setuptools import setup, find_packages

with open("requirements.txt", "r", encoding="utf-8") as fh:
    requirements = fh.read()

setup(
    name="pdfinstr-cli",
    description="Print pdf content to std out",
    long_description="Print pdf content to std out",
    version="1.0.0",
    author="Vinayak Singh Bhadoriya",
    author_email="vinayaksbhadoriya@gmail.com",
    scripts=["scripts/pdfinstr"],
    packages=find_packages("src"),
    install_requires=[requirements],
    package_dir={"": "src"},
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
    ],
)
