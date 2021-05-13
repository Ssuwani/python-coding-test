# -*- coding: utf8 -*-
# 문제번호로 푼 문제인지 확인!!
# 모든 문제 list 불러와서 경로 알려주기!!
import os
from functools import reduce
import argparse
parser = argparse.ArgumentParser()
parser.add_argument("id", help="Add user id with --id [id]")
args = parser.parse_args()
search_id = args.id
base_dir = '../'
folders = os.listdir(base_dir)
total_files = []
for folder in folders:
    # 문제를 푼 폴더
    if folder[0].isnumeric():
        files = os.listdir(os.path.join(base_dir, folder))
        total_files.append(files)
total_files = reduce(lambda x, y: x+y, total_files)
total_ids = [file.split("_")[0] for file in total_files]

if search_id in total_ids:
    print(f"{search_id} 는 이미 풀었다~")
else:
    print(f"{search_id} 이거 풀어야해..")
