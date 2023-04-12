#!/usr/bin/env python
# coding: utf-8

from setuptools import setup, find_packages
import sys

PY2 = sys.version_info[0] == 2

# 基於flylog, slack-client處理
if PY2:
    require_pack = ['slackclient==1.3.2']
else:
    require_pack = ['slack_sdk==3.19.5']

setup(
    name='slackflylog',
    version="0.0.1",
    author="dkxx00",
    author_email="hymanxx6@gmail.com",
    description="基于flylog的Slack日志发送",
    license="MIT",
    packages=find_packages(),
    install_requires =require_pack,
    url="https://github.com/dkxx00/slackflylog"
)


