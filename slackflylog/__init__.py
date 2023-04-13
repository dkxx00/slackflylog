# -*- coding: utf-8 -*-
import sys

PY2 = sys.version_info[0] == 2
if PY2:
    __version__ = "1.0.0"

else:
    __version__ = "3.0.0"


from .api.log_handler import LogHandler
from .api.client import Client
from .agent.agent import Agent

# 向下兼容
FlyLogHandler = LogHandler
