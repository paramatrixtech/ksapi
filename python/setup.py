# coding: utf-8

from setuptools import setup, find_packages # noqa: H301

NAME = "ks-api-client"
VERSION = "1.1.0"
# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools http://pypi.python.org/pypi/setuptools

REQUIRES = ["certifi>=14.05.14", "six >= 1.10", "python_dateutil >= 2.5.3", "urllib3 > 1.15", "python-socketio[client]==5.3.0","requests==2.26.0", "python-dotenv==0.19.2"]

setup(
    name=NAME,
    version=VERSION,
    description="KS Trade API&#39;s",
    author="KS-Trade API",
    author_email="team@xyz.org",
    url="",
    keywords=["KS-Trade API", "KS Trade API's"],
    install_requires=REQUIRES,
    packages=find_packages(exclude=["test", "tests"]),
    include_package_data=True,
    long_description="""\
    """
)
