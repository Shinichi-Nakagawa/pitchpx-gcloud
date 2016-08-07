#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import logging
from enum import Enum
import click

from google import GoogleDrive

__author__ = 'Shinichi Nakagawa'


class PitchpxGcloudClient(object):

    class Mode(Enum):

        SPREADSHEET = 0

    def __init__(self, client_secret, path, mode):
        """
        init
        :param client_secret: client_secret file(full path, json)
        :param path: pitchpx datasets path(dir)
        :param mode: using gcloud service flag(spreadsheet only)
        """
        self.client_secret = client_secret
        self.mode = mode
        self.path = path
        logging.info('client_secret: {} path: {}'.format(self.client_secret, self.path))

    def run(self):
        """
        Run to process
        """
        api = GoogleDrive(self.path, self.client_secret)
        # TODO 必要が出てきたらUPLOADなどを足す
        if self.mode == self.Mode.SPREADSHEET:
            api.spread_open()
            api.spread_update()
        else:
            raise Exception('invalid Mode')


@click.command()
@click.option('--client_secret', '-c', required=True, default='./client_secret.json', help='Client Secret file(json)')
@click.option('--directory', '-d', required=True, default='.', help='Input directory path(pitchpx datasets)')
@click.option('--mode', '-m', required=True, default='spreadsheet',
              help='Convert mode(spreadsheet or csv default:spreadsheet)')
def gcloud(client_secret, directory, mode):
    """
    Google cloud
    :param client_secret:
    :param directory:
    :param mode:
    """
    logging.basicConfig(level=logging.INFO)
    # TODO 必要が出てきたらCSV UPLOADを作る
    if mode == 'spreadsheet':
        _mode = PitchpxGcloudClient.Mode.SPREADSHEET
    else:
        raise click.BadParameter('invalid to mode(value:{})'.format(mode))
    client = PitchpxGcloudClient(
        os.path.abspath(client_secret),
        os.path.abspath(directory),
        _mode
    )
    client.run()


if __name__ == '__main__':
    gcloud()