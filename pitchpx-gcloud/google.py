#!/usr/bin/env python
# -*- coding: utf-8 -*-

import yaml
import glob
import logging
import os


import gspread
from oauth2client.service_account import ServiceAccountCredentials

__author__ = 'Shinichi Nakagawa'


class _GoogleAPI(object):
    """
    Google API Client base class
    """

    SERVICE_NAME = None
    VERSIONS = None

    def __init__(self, path, client_secret, setting_file='/setting.yml'):
        """
        Google API Client
        :param path:
        :param client_secret:
        :param setting_file:
        """
        self.setting = yaml.load(open(''.join([os.path.abspath('.'), setting_file]), 'r'))
        self.client_secret = client_secret
        self.path = path
        self.credentials = self.get_credentials()

    def get_credentials(self):
        """
        get credential
        :return: credentials
        """
        return ServiceAccountCredentials.from_json_keyfile_name(
            filename=self.client_secret,
            scopes=self.setting['gcloud']['scopes']
        )


class GoogleDrive(_GoogleAPI):

    def __init__(self, path, client_secret, setting_file='/setting.yml'):
        """
        Google API Client
        :param path:
        :param client_secret:
        :param setting_file:
        """
        super(GoogleDrive, self).__init__(path, client_secret, setting_file)
        self.gc = gspread.authorize(self.credentials)
        self.sh = self.spread_open()

    def spread_open(self):
        """
        Open Spread sheet
        """
        return self.gc.open(self.setting['gcloud']['spreadsheet']['name'])

    def spread_update(self):
        """
        Open Spread update
        """
        for row in glob.glob('{}/{}*'.format(self.path, self.setting['config']['file_prefix'])):
            logging.info(row)
