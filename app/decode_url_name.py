#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
    Create by Alex Cao on 2019-09-17
"""
import argparse
import os
import sys
from urllib.parse import unquote


def decode_directory_files(folder):
    folder = os.path.expanduser(folder) if folder[0] == '~' else folder
    if not os.path.isdir(folder):
        print('not a folder')
    elif os.path.isfile(folder):
        decode_file(os.path.basename(folder), os.path.dirname(folder), 1)
    else:
        for i, f in enumerate(os.listdir(folder), 1):
            decode_file(f, folder, i)
    return ''


def decode_file(f, folder, i):
    before = os.path.join(folder, f)
    after = os.path.join(folder, unquote(f))
    print("{}. {} --> {}".format(i, before, after))
    try:
        os.rename(before, after)
    except Exception as e:
        print(e)
        exit(0)


parser = argparse.ArgumentParser(description='将URLEncode编码的文件名解码为正常字符')
parser.add_argument('folder', nargs=1,
                    type=str, help='需要解码文件所在的目录')

if __name__ == '__main__':
    args = parser.parse_args()
    folder = getattr(args, 'folder')[0]
    decode_directory_files(folder)
    # args = sys.argv
    # if args[0] == '-h':
    # decode_directory_files('~/Downloads')
