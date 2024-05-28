#!/usr/bin/env python
# -*- coding:utf-8 -*-
#  
#   Author  :   hxflove521
#   Date    :   2024-05-28 12:12
#   Desc    :   获取GitHub相关域名对应的最新IP

import ipaddress
import time

import dns.resolver

# modify_by_yourself
GITHUB_URLS = [
    'alive.github.com', 'api.github.com', 'assets-cdn.github.com',
    'avatars.githubusercontent.com', 'avatars0.githubusercontent.com',
    'avatars1.githubusercontent.com', 'avatars2.githubusercontent.com',
    'avatars3.githubusercontent.com', 'avatars4.githubusercontent.com',
    'avatars5.githubusercontent.com', 'camo.githubusercontent.com',
    'central.github.com', 'cloud.githubusercontent.com', 'codeload.github.com',
    'collector.github.com', 'desktop.githubusercontent.com',
    'favicons.githubusercontent.com', 'gist.github.com',
    'github-cloud.s3.amazonaws.com', 'github-com.s3.amazonaws.com',
    'github-production-release-asset-2e65be.s3.amazonaws.com',
    'github-production-repository-file-5c1aeb.s3.amazonaws.com',
    'github-production-user-asset-6210df.s3.amazonaws.com', 'github.blog',
    'github.com', 'github.community', 'github.githubassets.com',
    'github.global.ssl.fastly.net', 'github.io', 'github.map.fastly.net',
    'githubstatus.com', 'live.github.com', 'media.githubusercontent.com',
    'objects.githubusercontent.com', 'pipelines.actions.githubusercontent.com',
    'raw.githubusercontent.com', 'user-images.githubusercontent.com',
    'vscode.dev', 'education.github.com'
]

def validIp(ipaddr):
    try:
        ip = ipaddress.ip_address(ipaddr)
        return True
    except ValueError:
        return False

def nslookup(domain, record_type) -> str|bool:
    dns_resolver = dns.resolver.Resolver()
    answers = dns_resolver.resolve(domain, record_type)
    for answer in answers:
        if not validIp(answer):
            return False
        return f'{answer}\t{domain}\n'

def main():
    with open("github.host","w") as hw:
        hw.write(f"# Update time {time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))}\n")
        for domain in GITHUB_URLS:
            host_ip = nslookup(domain,"A")
            if host_ip: 
                hw.write(host_ip)


if __name__ == '__main__':
    main()

