#!/Usr/bin/env python3
# -*- coding: UTF-8 -*-

import os
import re

# 在指定的目录dir_path下创建一个pod文件夹，并配置初始文件
def new_pod(dir_path, podname):
    # 创建文件夹
    pod_path = os.path.join(dir_path, podname)
    if os.path.exists(pod_path):
        print('警告已经存在了')
    else:
        os.makedirs(pod_path)

    # 生成对应的podspec文件
    spec_path = os.path.join(dir_path, 'PODNAME.podspec')
    new_spec_path = os.path.join(pod_path, podname+'.podspec')
    # f = open(spec_path, 'r+', errors='ignore')
    f = open(spec_path, 'r+')
    content = f.read()
    new_content = content.replace('${PODNAME}', podname)
    # new_content = re.sub('${PODNAME}', podname, content)
    print(new_content)
    f.close()

    # 打开一个文件只用于写入。如果该文件已存在则打开文件，并从开头开始编辑，即原有内容会被删除。如果该文件不存在，创建新文件。
    newfile = open(new_spec_path, 'w')
    newfile.write(new_content)
    newfile.close()





# 配置pod名称 input只适用python3
pod_name = ''
while len(pod_name)==0:
    pod_name = input('请输入你的pod名称：')
    print('你的pod名称是：' + pod_name)

# 开始配置pod模块
cwd = os.getcwd()
new_pod(cwd, pod_name)







    




