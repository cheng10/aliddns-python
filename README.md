# aliddns-python

A simple dynamic DNS tool for alicloud DNS.

[![image](https://img.shields.io/pypi/status/aliddns-python)](https://pypi.org/project/aliddns-python/)
[![image](https://img.shields.io/pypi/v/aliddns-python.svg)](https://pypi.org/project/requests/)
[![image](https://img.shields.io/pypi/l/aliddns-python.svg)](https://pypi.org/project/aliddns-python/)
[![image](https://img.shields.io/pypi/pyversions/aliddns-python.svg)](https://pypi.org/project/aliddns-python/)
[![image](https://img.shields.io/github/contributors/cheng10/aliddns-python.svg)](https://github.com/cheng10/aliddns-python/graphs/contributors)

## Installation

```shell
pip install --upgrade aliddns-python
```

## Quickstart

```shell
# update the given domain name DNS record with current public ip
python -m aliddns.ddns --key=<ACCESS_KEY> --secret=<SECERT_KEY> --record=www.yourdomain.com
```

## Usage

### Job Scheduling

```shell
# update dns record every 5 mins using cron job
# use `crontab -e` to edit the crob job
# m h  dom mon dow   command
*/5 * * * python -m aliddns.ddns --key=<ACCESS_KEY> --secret=<SECERT_KEY> --record=www.yourdomain.com
```

## References

- [Offical Alicloud DNS API](https://help.aliyun.com/document_detail/124923.html)
- [Dynamic DNS using Alibaba Cloud DNS API](https://www.alibabacloud.com/blog/Dynamic-DNS-using-Alibaba-Cloud-DNS-API_459542)
- [Alicloud OpenAPI Explorer](https://api.aliyun.com/)

## LICENSE

```text
Copyright (c) 2019 cheng10

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```
