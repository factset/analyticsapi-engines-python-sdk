# coding: utf-8

"""
    Engines API

    Allow clients to fetch Analytics through APIs.  # noqa: E501

    The version of the OpenAPI document: v3:[pa,spar,vault,pub,quant,fi,axp,afi,npo,bpm,fpo,others],v1:[fiab]
    Contact: api@factset.com
    Generated by: https://openapi-generator.tech
"""


from setuptools import setup, find_packages  # noqa: H301

NAME = "fds.analyticsapi.engines"
VERSION = "5.7.0-rc.1"
# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools

REQUIRES = [
  "urllib3 >= 1.25.3",
  "python-dateutil",
  "fds.protobuf.stach.extensions < 2.0.0",
]

setup(
    name=NAME,
    version=VERSION,
    description="Engines API",
    author="FactSet Research Systems",
    author_email="api@factset.com",
    url="https://github.com/factset/analyticsapi-engines-python-sdk",
    keywords=["OpenAPI", "OpenAPI-Generator", "Engines API"],
    python_requires=">=3.6",
    install_requires=REQUIRES,
    packages=find_packages(exclude=["test", "tests"]),
    include_package_data=True,
    license="Apache License, Version 2.0",
    long_description="""\
    Allow clients to fetch Analytics through APIs.  # noqa: E501
    """
)
