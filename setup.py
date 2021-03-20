import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="oxshare", # Replace with your own username
    version="0.0.1",
    author="Eric Shen",
    author_email="shenyu@hotmail.com",
    description="a utility for crawling financial data.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Shen-Yu/oxshare",
    project_urls={
        "Bug Tracker": "https://github.com/Shen-Yu/oxshare/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "oxshare"},
    packages=setuptools.find_packages(where="oxshare"),
    python_requires=">=3.6",
)