#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'Shinichi Nakagawa'


class _GoogleAPI(object):

    def __init__(self, path):
        self.path = path


class GoogleDrive(_GoogleAPI):

    def write_spreadsheet(self):
        pass

    def upload(self):
        pass
