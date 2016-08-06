#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import yaml

__author__ = 'Shinichi Nakagawa'


class _GoogleAPI(object):

    def __init__(self, path, setting_file='/setting.yml'):
        self.setting = yaml.load(open(self.DELIMITER.join([os.path.abspath(__file__), setting_file]), 'r'))
        self.path = path


class GoogleDrive(_GoogleAPI):

    def write_spreadsheet(self):
        pass

    def upload(self):
        pass
