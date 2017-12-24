import os
import sys
import argparse
from pathlib import Path
import subprocess
from collections import defaultdict

from as232.gitannex import annex_info
from as232.gitannex import make_whereis_data
from as232.gitannex import getkey, parse_key

parser = argparse.ArgumentParser()
parser.add_argument('dirname', default='.', nargs='*')
args = parser.parse_args()


def get_checksums(filelist):
    checksums = defaultdict(list)
    for fdata in filelist:
        ck = fdata['checksum']
        checksums[ck].append(fdata)
    return checksums

def get_common_sizes(sizes):
    data = dict()
    for s in sizes:
        if len(sizes[s]) > 1:
            data[s] = sizes[s]
    return data


def find_dupes(sizes):
    dupes = defaultdict(list)
    cs = get_common_sizes(sizes)
    cs_keys = list(cs.keys())
    cs_keys.sort()
    for cskey in cs_keys:
        cks = get_checksums(cs[cskey])
        for ck in cks:
            if len(cks[ck]) > 1:
                for fdata in cks[ck]:
                    dupes[ck].append(fdata)
    return dupes

def handle_directory(dirname, sizes, filelist):
    wd = Path(dirname)
    for path in wd.rglob('*'):
        if path.is_file() and path.is_symlink():
            key = path.resolve().name
            data = parse_key(key)
            data['file'] = path
            filelist.append(data)
            sizes[data['size']].append(data)

def main():
    sizes = defaultdict(list)
    filelist = []
    for dirname in args.dirname:
        handle_directory(dirname, sizes, filelist)
    dupes = find_dupes(sizes)
    for ck in dupes:
        for fdata in dupes[ck]:
            print(fdata['file'])
        print('')
    return 0

