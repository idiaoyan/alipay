#!/usr/bin/env python
# coding: utf-8
import sys

if str(sys.version[0]) == "3":
    from unittest import mock
else:
    from mock import mock
