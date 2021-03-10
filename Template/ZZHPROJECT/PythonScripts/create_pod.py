#!/Usr/bin/env python3
# -*- coding: UTF-8 -*-

import os
# import re
import io
import sys


# 在工程的根目录的DevelopmentPods生成一个一个新的pod文件夹
def create_new_pod(podname):
    # 创建pod初始相关文件
    print()
    print_important_mes('***************')
    print_important_mes('开始创建pod库文件')
    pod_home_name = 'DevelopmentPods'
    pod_path = os.path.join(project_folder, pod_home_name, podname)
    if os.path.exists(pod_path):
        print_warning('该目录下已经存在同名文件，请处理')
        return
    else:
        os.makedirs(pod_path)
    # 生成对应的podspec文件
    spec_path = os.path.join(script_folder, 'PODNAME.podspec')
    new_spec_path = os.path.join(pod_path, podname+'.podspec')
    f = io.open(spec_path, 'r+')
    content = f.read()
    new_content = content.replace('${PODNAME}', podname)
    f.close()
    # 打开一个文件只用于写入。如果该文件已存在则打开文件，并从开头开始编辑，即原有内容会被删除。如果该文件不存在，创建新文件。
    newfile = io.open(new_spec_path, 'w')
    newfile.write(new_content)
    newfile.close()
    print_important_mes('创建pod库文件成功')
    print_important_mes('***************')

    # 修改podfile
    print()
    print_important_mes('*****************')
    print_important_mes('正在修改podfile文件')
    mark = "${ZZHPODNAME}"  # 这个字符串就是插入位置的标记
    podfile_path = os.path.join(project_folder, 'podfile')
    f = io.open(podfile_path, 'r+')
    content = f.read()
    f.seek(0, 0)
    f.truncate()
    pos = content.find(mark)
    if pos != -1:
        place_str = "  pod '%s', :path => './%s/%s'" % (podname, pod_home_name, podname)
        place_index = pos+len(mark)
        content = content[:place_index] + '\n' + place_str + content[place_index:]
        f.write(content)
        f.close()
        print_important_mes('podfile文件修改成功')
        print_important_mes('*****************')
    else:
        f.close()
        print_warning('podfile中未找到${ZZHPODNAME}，修改podfile失败')
        return
    # pod install
    print()
    print_important_mes('**************')
    print_important_mes('pod installing')
    os.chdir(project_folder)
    os.system('pod install --verbose --no-repo-update')


def print_warning(s):
    print("\033[1;31;m!!!!!!!!!!!!!!!!!!!!! %s !!!!!!!!!!!!!!!!!!!!!\033[0m" % s)


def print_important_mes(s):
    print("\033[1m********************* %s *********************\033[0m" % s)


# 脚本所在目录
script_folder = os.path.dirname(sys.argv[0])
# 工程根目录
project_folder = os.path.dirname(script_folder)

# 配置pod名称 input只适用python3
pod_name = ''
while len(pod_name) == 0:
    pod_name = input('请输入你的pod名称：').replace(" ", "").replace("\t", "").strip()
pod_name = pod_name[:1].upper() + pod_name[1:]
print('你的pod名称是：' + pod_name)

# 开始配置pod模块
create_new_pod(pod_name)
