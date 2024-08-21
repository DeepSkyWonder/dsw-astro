from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()


requirements = [
    "matplotlib",
    "ipython",
    "numpy",
    "astropy",
]


setup(
    name="dsw-astro",
    version="0.0.1",
    author="Cameron McEwing",
    author_email="deepskywonder@gmail.com",
    description="Tools for Astronomy",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/DeepSkyWonder/dsw-astro",
    install_requires=requirements,

    packages=find_packages(),
    include_package_data=True,
    package_data={"": ["dsw-astro/fitting/cepheid/data/*.fits"]},
    exclude_package_data={"": ["README.md"]},

    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.9',
)

