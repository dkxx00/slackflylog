#!/usr/bin/env python
# coding: utf-8

from setuptools import setup, find_packages
import sys


# 基於flylog, slack-client處理
import io
import os
import re

PY2 = sys.version_info[0] == 2
if PY2:
    REQUIRE_PACK = ['slackclient==1.3.2']

else:
    REQUIRE_PACK = ['slack_sdk==3.19.5']



def read(*names, **kwargs):
    with io.open(
        os.path.join(os.path.dirname(__file__), *names),
        encoding=kwargs.get("encoding", "utf8")
    ) as fp:
        return fp.read()



def find_version(*file_paths):
    version_file = read(*file_paths)
    version_match = re.search(r"^__version__ = ['\"]([^'\"]*)['\"]", version_file, re.M)
    if version_match:
        return version_match.group(1)
    raise RuntimeError("Unable to find version string.")


setup(
    name='slackflylog',
    version=find_version('slackflylog', '__init__.py'),
    author="dkxx00",
    author_email="hymanxx6@gmail.com",
    description="基于flylog的Slack日志发送",
    license="MIT",
    packages=find_packages(),
    install_requires =REQUIRE_PACK,
    url="https://github.com/dkxx00/slackflylog"
)


