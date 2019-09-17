#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
    Create by Alex Cao on 2019-09-17
"""
import argparse
import os
from urllib.parse import unquote

parser = argparse.ArgumentParser(description='将URLEncode编码的文件名解码为正常字符')
parser.add_argument('file_or_folder', nargs=1, default=os.getcwd(),
                    type=str, help='需要解码文件或其所在的目录')


def decode_directory_files(folder):
    folder = os.path.expanduser(folder) if folder[0] == '~' else folder  # 获取绝对路径
    if not (os.path.isdir(folder) or os.path.isfile(folder)):
        parser.print_usage()
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


if __name__ == '__main__':
    args = parser.parse_args()
    decode_directory_files(getattr(args, 'file_or_folder')[0])
