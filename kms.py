# prerequisites:
# have python3, pip (sudo apt-get install python3-pip), setuptools (python3 -m install setuptools)
#
# 1. install boto3
#
# for python3:
#    python3 -m pip install boto3

import boto3
import os

# VARS
# read access key from env vars
access_key = os.environ['AWS_ACCESS_KEY']
# read access key from env vars
access_secret_key = os.environ['AWS_SECRET_KEY']
# set the region
region = 'us-east-1'

# KMS SETUP
kms = boto3.client('kms', region_name=region, aws_access_key_id=access_key, aws_secret_access_key=access_secret_key)
# cretate KMS key in advance in the region you set before (in the AWS console), name it for example 'tempKey'

# KMS ENCRYPTION
key_id = 'alias/tempKey'
# here is some stuff to encrypt
database_password = 'flagship-player-dispatch-agile-agenda-flanking-karma'
result=kms.encrypt(KeyId=key_id, Plaintext=database_password)
# >>> 'CiphertextBlob': b'\x01\x02\x02\x00xe\x95BB\xd3\xb7\xbb\x92\x01I\xe0\xf1\xdd\xd5E\xda\x06?\xef@\\0\x7fz2_"Ckx\x1f\\\x01\xce94\x84\x99\xa2\x97\x8f\x0e\x89\x1b\xdb\x8a\xb7\xa2\xf4\x00\x00\x00\x950\x81\x92\x06\t*\x86H\x86\xf7\r\x01\x07\x06\xa0\x81\x840\x81\x81\x02\x01\x000|\x06\t*\x86H\x86\xf7\r\x01\x07\x010\x1e\x06\t`\x86H\x01e\x03\x04\x01.0\x11\x04\x0c\xf4\xe4\xab\xf6\x87=\x02K\xda+ky\x02\x01\x10\x80O\x0b\xef\xe3:f\x13V\x91\x0e\xe2\xc0\x01\x9a\xe3>\xd6\x8c\xf9\x04\x88\xcd&\xbc\x90\xben\xa7\xf9w\xe6\xb1p\xec$r\xf3\xce\x8c\xab\xfa\x10\x96X\xe7\xc5\xd8\x8aV\x05\x83\x8b\xe3\x19?\x1a\xdf\xe84\xbfj1\xec\x9bUe\xcb\x88\xcb\x08t\x9e\xd3\xeb5\x96\x12\xb0vz', 'KeyId': 'arn:aws:kms:us-east-1:XXXXXXXXXXXX:key/XXXXXXXXXXXXXXX', 'EncryptionAlgorithm': 'SYMMETRIC_DEFAULT', 'ResponseMetadata': {'RequestId': 'XXXXXXXXXXXXXXXXX', 'HTTPStatusCode': 200, 'HTTPHeaders': {'x-amzn-requestid': 'XXXXXXXXXXXXXXXX', 'cache-control': 'no-cache, no-store, must-revalidate, private', 'expires': '0', 'pragma': 'no-cache', 'date': 'Tue, 26 Nov 2019 16:45:41 GMT', 'content-type': 'application/x-amz-json-1.1', 'content-length': '425'}, 'RetryAttempts': 0}}
encrypted_password = result['CiphertextBlob']
# >>> b'\x01\x02\x02\x00xe\x95BB\xd3\xb7\xbb\x92\x01I\xe0\xf1\xdd\xd5E\xda\x06?\xef@\\0\x7fz2_"Ckx\x1f\\\x01\xce94\x84\x99\xa2\x97\x8f\x0e\x89\x1b\xdb\x8a\xb7\xa2\xf4\x00\x00\x00\x950\x81\x92\x06\t*\x86H\x86\xf7\r\x01\x07\x06\xa0\x81\x840\x81\x81\x02\x01\x000|\x06\t*\x86H\x86\xf7\r\x01\x07\x010\x1e\x06\t`\x86H\x01e\x03\x04\x01.0\x11\x04\x0c\xf4\xe4\xab\xf6\x87=\x02K\xda+ky\x02\x01\x10\x80O\x0b\xef\xe3:f\x13V\x91\x0e\xe2\xc0\x01\x9a\xe3>\xd6\x8c\xf9\x04\x88\xcd&\xbc\x90\xben\xa7\xf9w\xe6\xb1p\xec$r\xf3\xce\x8c\xab\xfa\x10\x96X\xe7\xc5\xd8\x8aV\x05\x83\x8b\xe3\x19?\x1a\xdf\xe84\xbfj1\xec\x9bUe\xcb\x88\xcb\x08t\x9e\xd3\xeb5\x96\x12\xb0vz'

# KMS DECRYPTION
decrypt_result = kms.decrypt(CiphertextBlob=encrypted_password)
# >>> {'KeyId': 'arn:aws:kms:us-east-1:XXXXXXXXXXX:key/XXXXXXXXXXXXXXXXXX', 'Plaintext': b'flagship-player-dispatch-agile-agenda-flanking-karma', 'EncryptionAlgorithm': 'SYMMETRIC_DEFAULT', 'ResponseMetadata': {'RequestId': 'XXXXXXXXXXXXXXXXXXXXXXX', 'HTTPStatusCode': 200, 'HTTPHeaders': {'x-amzn-requestid': 'XXXXXXXXXXXXXXXXXXXX', 'cache-control': 'no-cache, no-store, must-revalidate, private', 'expires': '0', 'pragma': 'no-cache', 'date': 'Tue, 26 Nov 2019 16:48:23 GMT', 'content-type': 'application/x-amz-json-1.1', 'content-length': '216'}, 'RetryAttempts': 0}}
decrypt_result['Plaintext']
# b'flagship-player-dispatch-agile-agenda-flanking-karma'
decrypt_result['Plaintext'].decode('utf-8')
# 'flagship-player-dispatch-agile-agenda-flanking-karma'
