# coding: utf-8

# Based on thumbor-community thumbor aws_s3 loader
# Use of this source code is governed by the MIT license that can be
# found in the LICENSE file.

import botocore.session

class Bucket(object):
    """
    This handles all communication with AWS API
    """
    _bucket      = None
    _region      = None
    _local_cache = dict()

    def __init__(self, bucket, region):
        """
        Constructor
        :param string bucket: The bucket name
        :param string region: The AWS API region to use
        :return: The created bucket
        """
        self._bucket = bucket
        self._region = region
        session = None or botocore.session.get_session()
        self._client = session.create_client('s3', region_name=self._region, endpoint_url=None)

    def get(self, path):
        """
        Returns object at given path
        :param string path: Path or 'key' to retrieve AWS object
        """
        file_path = self._client.get_object( Bucket=self._bucket, Key=path)
        return file_path['Body'].read()
        

