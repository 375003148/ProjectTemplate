#!/Usr/bin/env python3
# -*- coding: UTF-8 -*-

import os
import re
import io


# 在指定的目录dir_path下创建一个pod文件夹，并配置初始文件
def new_pod(dir_path, podname):
    # 创建文件夹
    pod_path = os.path.join(dir_path, podname)
    if os.path.exists(pod_path):
        print_warning('该目录下已经存在同名文件，请处理')
        return
    else:
        os.makedirs(pod_path)

    # 生成对应的podspec文件
    spec_path = os.path.join(dir_path, 'PODNAME.podspec')
    new_spec_path = os.path.join(pod_path, podname+'.podspec')
    f = io.open(spec_path, 'r+')
    content = f.read()
    new_content = content.replace('${PODNAME}', podname)
    f.close()

    # 打开一个文件只用于写入。如果该文件已存在则打开文件，并从开头开始编辑，即原有内容会被删除。如果该文件不存在，创建新文件。
    newfile = open(new_spec_path, 'w')
    newfile.write(new_content)
    newfile.close()


def print_warning(s):
    print("\033[1;31;m!!!!!!!!!!!!!!!!!!!!! %s !!!!!!!!!!!!!!!!!!!!!\033[0m" % s)


def print_important_mes(s):
    print("\033[1m********************* %s *********************\033[0m" % s)


# 配置pod名称 input只适用python3
pod_name = ''
while len(pod_name) == 0:
    pod_name = input('请输入你的pod名称：')
    print('你的pod名称是：' + pod_name)

# 开始配置pod模块
new_pod(sys.argv[0], pod_name)
