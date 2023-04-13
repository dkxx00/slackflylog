#!/usr/bin/env python
# coding: utf-8

from setuptools import setup, find_packages
import sys


# 基於flylog, slack-client處理

PY2 = sys.version_info[0] == 2
if PY2:
    REQUIRE_PACK = ['flylog','slackclient>=1.3.2']
    __version__ = "1.0.0"

else:
    REQUIRE_PACK = ['flylog','slack_sdk>=3.19.5']
    __version__ = "3.0.0"




setup(
    name='slackflylog',
    version=__version__,
    author="dkxx00",
    author_email="hymanxx6@gmail.com",
    description="基于flylog的Slack日志发送",
    license="MIT",
    packages=find_packages(),
    install_requires=REQUIRE_PACK,
    url="https://github.com/dkxx00/slackflylog"
)


