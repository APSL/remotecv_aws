# coding: utf-8

# Based on thumbor-community thumbor aws_s3 loader
# Use of this source code is governed by the MIT license that can be
# found in the LICENSE file.

from boto3.session import Session

class Bucket(object):
    """
    This handles all communication with AWS API
    """
    _bucket      = None
    _local_cache = dict()

    def __init__(self, bucket, region, accessKeyId, secretAccessKey):
        """
        Constructor
        :param string bucket: The bucket name
        :param string region: The AWS API region to use
        :param string accessKeyId: The AWS access key ID for accessing the bucket
        :param string secretAccessKey: The AWS secret access key for accessing the bucket
        :return: The created AWS client for the bucket 
        """
        self._bucket = bucket
        
        session = Session(
                        aws_access_key_id=accessKeyId,
                        aws_secret_access_key=secretAccessKey,
                        region_name=region
                  )

        self._client = session.resource('s3')

    def get(self, path):
        """
        Returns object at given path
        :param string path: Path or 'key' to retrieve AWS object
        """

        file_path = self._client.Bucket(self._bucket).Object(path).get()

        return file_path['Body'].read()
        

