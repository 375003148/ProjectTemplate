#!/Usr/bin/env python3
# -*- coding: UTF-8 -*-

import os
import re
import sys
import io


# 配置模板工程
def config_template(pro_folder):
    # 修改工程名称
    if len(os.path.basename(pro_folder)) == 0:
        pro_folder = os.path.dirname(pro_folder)
    _rename_project(pro_folder, old_project_name, new_project_name)
    pro_folder = os.path.dirname(pro_folder) + '/' + new_project_name

    # 替换其它内容
    replaceitems = {
        'ZZHAppDelegate': 'EWAppDelegate',
        'ZZHViewController': 'EWViewController',
    }
    for olditem, newitem in replaceitems.items():
        _rename_project(pro_folder, olditem, newitem)

    print()
    print_important_mes('工程配置完成')
    print('工程目录：' + pro_folder)
    return pro_folder


# 递归替换指定路径下的所有目录和文件的名称和内容中的字符串（包括路径指定的这个根目录）
def _rename_project(path, old, new):
    # 如果是文件则修改内容后重命名。
    if os.path.isfile(path):
        if path[-3:] != '.py':
            # 替换文件内容
            _replace_content(path, old, new)
            # 替换文件名称
            _rename(path, old, new)
    # 如果是目录，遍历所有的内容进行递归操作
    elif os.path.isdir(path):
        # 替换文件夹名称
        path = _rename(path, old, new)
        # 继续递归
        files = os.listdir(path)
        for item in files:
            newpath = os.path.join(path, item)
            _rename_project(newpath, old, new)
    else:
        print_warning('路径不正确：'+path)


# 修改文件或目录名称
def _rename(path, old_name, new_name):
    filename = os.path.basename(path)
    dirname = os.path.dirname(path)
    newpath = path
    if old_name in filename:
        tmp = filename.replace(old_name, new_name)
        newpath = os.path.join(dirname, tmp)
        os.rename(path, newpath)
    return newpath


# 替换文件内容中的字符串
def _replace_content(file_path, old_string, new_string):
    # 打开文件  r+: 可读可写，若文件不存在，报错。 ignore是忽略error
    f = io.open(file_path, 'r+', errors='ignore')
    # f = open(file_path, 'r+', errors='ignore')
    content = f.read()
    new_content = re.sub(old_string, new_string, content)
    # 清空文件内容
    f.seek(0, 0)
    f.truncate()
    # 书写新的内容
    f.write(new_content)
    f.close()


# pod init
def pod_install():
    print()
    print_important_mes('pod installing')
    print_important_mes('**************')
    os.chdir(project_folder)
    os.system('pod install --verbose --no-repo-update')


def print_warning(s):
    print("\033[1;31;m!!!!!!!!!!!!!!!!!!!!! %s !!!!!!!!!!!!!!!!!!!!!\033[0m" % s)


def print_important_mes(s):
    print("\033[1m********************* %s *********************\033[0m" % s)


# 基本参数
old_project_name = 'ZZHPROJECT'
new_project_name = sys.argv[1]
new_project_prefix = sys.argv[2]
project_folder = sys.argv[3]

# 配置模板工程
project_folder = config_template(project_folder)

# 操作cocopods
pod_install()
