# aliddns-python

An easy-to-use dynamic DNS(DDNS) tool for Alibaba Cloud.

[![image](https://img.shields.io/pypi/status/aliddns-python)](https://pypi.org/project/aliddns-python/)
[![image](https://img.shields.io/pypi/v/aliddns-python.svg)](https://pypi.org/project/aliddns-python/)
[![image](https://img.shields.io/pypi/l/aliddns-python.svg)](https://pypi.org/project/aliddns-python/)
[![image](https://img.shields.io/pypi/pyversions/aliddns-python.svg)](https://pypi.org/project/aliddns-python/)
[![image](https://img.shields.io/github/contributors/cheng10/aliddns-python.svg)](https://github.com/cheng10/aliddns-python/graphs/contributors)

## Use Cases

You have domain names hosted in Alibaba Cloud, and you want to setup DDNS.
DDNS is pretty usefull when you have public but dynamic IP from your ISP.
Some advanced home routers support DDNS of many kinds out of box,
but many cheap or old ones do not. This easy to use script allows you to setup
up Alicloud DDNS sync on your home PC or any python-enabled devices.

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

## Documentation

### Get Your Access Keys from Alibaba Cloud

![how-to-get-access-key](https://user-images.githubusercontent.com/10646050/61933480-9038de00-afb8-11e9-9bfd-3cd8f21d0ecd.png)

```text
Getting a key pair is easy, and lets you to use more API features apart from the DNS one.

In order to get one, log into your Alibaba Cloud console and in the top navigation bar, hover with your mouse in your email address and click "accesskeys" as illustrated below.

<https://www.alibabacloud.com/blog/Dynamic-DNS-using-Alibaba-Cloud-DNS-API_459542>
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
