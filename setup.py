import sys
import setuptools

if sys.version_info < (3, 5):
    print("Unfortunately, your python version is not supported!\n"
          + "Please upgrade at least to Python 3.5!")
    sys.exit(1)

with open("README.rst", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="apk-signer",
    python_requires='>=3.5',
    version="1.1.2",
    author="ksg97031",
    author_email="ksg97031@gmail.com",
    description="Sign the apk file",
    install_requires=['click', 'androguard'],
    long_description=long_description,
    long_description_content_type="text/x-rst",
    url="https://github.com/ksg97031/apk-signer",
    packages=setuptools.find_packages(),
    entry_points={
        'console_scripts': [
            'apk-signer = apk_signer.scripts.launcher:cli'
        ],
    },
    package_data={
        "apk_signer": ["pyapksigner.jks"],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
