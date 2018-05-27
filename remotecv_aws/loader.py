# coding: utf-8

# Based on thumbor-community thumbor aws_s3 loader
# Use of this source code is governed by the MIT license that can be
# found in the LICENSE file.

from bucket import Bucket
import os

def load_sync(path):
    """
    Loads image from S3
    :param string path: Path to load
    """
    bucket = os.environ.get('AWS_LOADER_BUCKET')
    region = os.environ.get('AWS_REGION', 'eu-west-1')
    accessKeyId = os.environ.get('AWS_ACCESS_KEY_ID')
    secretAccessKey = os.environ.get('AWS_SECRET_KEY_ID')
    endPoint = os.environ.get('AWS_END_POINT')
    bucket_loader = Bucket(bucket, region, accessKeyId, secretAccessKey, endPoint)

    return bucket_loader.get(path)