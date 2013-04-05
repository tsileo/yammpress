import os
import sys
from setuptools import setup

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = "yammpress",
    version = "0.1.0",
    author = "Thomas Sileo",
    author_email = "thomas.sileo@gmail.com",
    description = "",
    license = "MIT",
    keywords = "blog blogging engine yaml markdown",
    url = "https://github.com/tsileo/yammpress",
    py_modules=['yammpress'],
    long_description= read('README.rst'),
    install_requires=[
        "komandr", "pyyaml", "python-slugify", "markdown2", "pymongo", "python-dateutil"
        ],
    entry_points={'console_scripts': ["yammpress = yammpress:main"]},
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Topic :: Text Processing",
        "Topic :: Utilities",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
    ],
    scripts=["yammpress.py"],
#    zip_safe=False,
)
