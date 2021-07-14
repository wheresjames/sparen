#!/usr/bin/python3

from setuptools import setup

def readConfig(fname):
    cfg = {}
    with open(fname) as f:
        lines = f.readlines()
        for line in lines:
            parts = line.strip().replace("\t", " ").split(" ")
            k = parts.pop(0).strip()
            cfg[k] = " ".join(parts).strip()
    return cfg

cfg = readConfig('./sparen/PROJECT.txt')

setup(
    name=cfg['name'],
    version=cfg['version'],
    description=cfg['description'],
    url=cfg['url'],
    author=cfg['author'],
    author_email=cfg['email'],
    license=cfg['license'],
    packages=[cfg['name']],
    include_package_data = True
)
