import os
folder = '1_수학'

# 1. [미로탐색 - 그래프탐색](./8_그래프탐색/2178_미로탐색.py) Silver I
# 2. [A-B - 수학](./1_수학/1001_A-B.py) Bronze V
# 3. [AxB - 수학](./1_수학/10998_AxB.py) Bronze V
for index, file in enumerate(os.listdir(folder)):
    filename = file.split("_")[1].split(".")[0]
    print(f"{index+1}. [{filename} - {folder[2:]}](./{folder}/{file})")