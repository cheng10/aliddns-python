"""
Update alicloud dns record.

Usage: ddns.py (--record=<record>) [--ip=<ip>] [--key=<key>] [--secret=<secret>]

Options:
    -h --help                             show this help message and exit.
    --version                             show version and exit.
    --record=<record>                     subdomain name to update, eg: `www.cheng10.cc`
    --ip=<ip>                             ip, default to current public ip.
    --key=<key>                           alicloud access key.
    --secret=<secret>                     alickoud access secret.

Install:
pip install docopt, requests, aliyun-python-sdk-core, aliyun-python-sdk-alidns

Tested on:
aliyun-python-sdk-alidns==2.0.10
aliyun-python-sdk-core==2.13.5
"""
import sys
import json
import logging
from logging.config import dictConfig

import requests
from docopt import docopt

from aliyunsdkcore.client import AcsClient
from aliyunsdkcore.acs_exception.exceptions import ClientException
from aliyunsdkcore.acs_exception.exceptions import ServerException
from aliyunsdkalidns.request.v20150109.DescribeSubDomainRecordsRequest import DescribeSubDomainRecordsRequest
from aliyunsdkalidns.request.v20150109.UpdateDomainRecordRequest import UpdateDomainRecordRequest


QUERY_IP_URL = 'http://cheng10.cc/ip'
logger = logging.getLogger(__name__)
dictConfig({
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'standard': {
            'format': '%(asctime)s[%(levelname)s]%(name)s[%(lineno)s]: %(message)s'  # NOQA E502
        },
    },
    'handlers': {
        'default': {
            'level': 'INFO',
            'formatter': 'standard',
            'class': 'logging.StreamHandler',
            'stream': 'ext://sys.stdout',  # Default is stderr
        },
    },
    'loggers': {
        '': {  # root logger
            'handlers': ['default'],
            'level': 'INFO',
            'propagate': True
        },
    }
})


def get_sub_domain_records(client, subdomain_name):
    """subdomain_name: eg. `www.cheng10.cc`, `home.cheng10.cc`
    """
    request = DescribeSubDomainRecordsRequest()
    request.set_accept_format('json')

    request.set_SubDomain(subdomain_name)

    response = client.do_action_with_exception(request)
    res = json.loads(str(response, encoding='utf-8'))
    record_info = res['DomainRecords']['Record'][0]
    logger.debug(f'record found: {record_info}')
    return record_info
    # sample response data
    """
    {
        "PageNumber": 1,
        "TotalCount": 1,
        "PageSize": 20,
        "RequestId": "19A7E4EB-A57E-4312-8E7E-5BB18A0FBD39",
        "DomainRecords": {
            "Record": [
                {
                    "RR": "home",
                    "Status": "ENABLE",
                    "Value": "21341234123.zicp.vip",
                    "Weight": 1,
                    "RecordId": "1784730000000",
                    "Type": "CNAME",
                    "DomainName": "cheng10.cc",
                    "Locked": false,
                    "Line": "default",
                    "TTL": 600
                }
            ]
        }
    }
    """

def update_domain_record(client, record_info, ip):
    if target_ip == record_info['Value']:
        logger.info('target ip not modified, not updating record.')
        return

    request = UpdateDomainRecordRequest()
    request.set_accept_format('json')

    request.set_RecordId(record_info['RecordId'])
    request.set_RR(record_info['RR'])
    request.set_Type("A")
    request.set_Value(ip)

    response = client.do_action_with_exception(request)
    res = json.loads(str(response, encoding='utf-8'))
    logger.info(f'record updated: {res}')
    return res


def get_public_ip():
    res = requests.get(QUERY_IP_URL)
    ip = str(res.content, encoding='utf-8').strip('\n')
    logger.info(f'public ip checked: {ip}')
    return ip


if __name__ == '__main__':
    args = docopt(__doc__, version='1.0.0')
    logger.debug(args)
    client = AcsClient(args['--key'], args['--secret'], 'cn-hangzhou')
    record_info = get_sub_domain_records(client, args['--record'])
    logger.info(f'domain record to update: \n{record_info}')
    target_ip = args.get('--ip') or get_public_ip()
    res = update_domain_record(client, record_info, target_ip)
    if not res:
        sys.exit()
    record_info = get_sub_domain_records(client, args['--record'])
    logger.info(f'updated domain record: \n{record_info}')
