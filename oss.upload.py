# -*- coding: utf-8 -*-

import sys
import oss2

# 设置用户配置
if ( len(sys.argv) > 5 ):
    #设置用户的AccessKeyId
    access_key_id = sys.argv[1].encode('utf-8').decode('utf-8')
    #设置用户的AccessKeySecret
    access_key_secret = sys.argv[2].encode('utf-8').decode('utf-8')
    #设置用户的Endpoint
    endpoint = sys.argv[3].encode('utf-8').decode('utf-8')
    #设置用户的BucketName
    bucket_name = sys.argv[4].encode('utf-8').decode('utf-8')
    #设置用户的本地文件
    local_file = sys.argv[5].encode('utf-8').decode('utf-8')
    #设置用户的远程文件
    oss_file = sys.argv[6].encode('utf-8').decode('utf-8')
else:
    print("Example: python %s AccessKeyId AccessKeySecret Endpoint BucketName /data/backup.zip backup.zip" % sys.argv[0])
    exit()

auth = oss2.Auth(access_key_id, access_key_secret)
bucket = oss2.Bucket(auth, endpoint, bucket_name)

def percentage(consumed_bytes, total_bytes):
    if total_bytes:
        rate = int(100 * (float(consumed_bytes) / float(total_bytes)))
        print('\r{0}% '.format(rate), end='')
        sys.stdout.flush()

oss2.resumable_upload(bucket, oss_file, local_file, store=oss2.ResumableStore(root='/tmp'), progress_callback=percentage)
