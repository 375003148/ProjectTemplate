#!/Usr/bin/env python3
# -*- coding: UTF-8 -*-

import os
import shutil
import sys


def start():
    # 配置工程前缀
    current_dir = os.path.dirname(sys.argv[0])
    os.chdir(current_dir)
    project_prefix = ''
    while len(project_prefix) == 0:
        project_prefix = input('请输入你的工程前缀：').upper().replace(" ", "").replace("\t", "").strip()
        print('工程前缀是：' + project_prefix)
    # 配置工程名称
    project_name = ''
    while len(project_name) == 0:
        project_name = input('请输入你的工程名称（注意驼峰标示）：').replace(" ", "").replace("\t", "").strip()
        print('工程名称是：' + project_name)
    # 检查当前目录是否已经有了同名文件或文件夹
    checkpath = os.path.join(current_dir, project_name)
    if os.path.exists(checkpath):
        print_warning('脚本当前目录已存在同名文件，请处理后再操作')
        return

    # 拉取代码
    tmpdir = 'pwlptauv94543890322340'
    git_url = 'git://github.com/375003148/ProjectTemplate.git'
    print()
    print_important_mes('git clone 拉取模板')
    os.system('git clone %s %s' % (git_url, tmpdir))
    if os.path.exists(os.path.join(current_dir, tmpdir, 'start.py')):
        print_important_mes('拉取成功')
        print()
    else:
        print_warning('git clone 失败')
        print()
        return

    # 调用 edit_template.py进行工程修改
    os.chdir(tmpdir)
    project_folder = os.path.join(current_dir, tmpdir, 'Template', 'ZZHPROJECT')
    os.system("python edit_template.py %s %s %s" % (project_name, project_prefix, project_folder))

    # 配置完成之后将工程移动到最外面,删除多余的东西
    shutil.move(os.path.join(current_dir, tmpdir, 'Template', project_name), current_dir)
    shutil.rmtree(os.path.join(current_dir, tmpdir))
    print()
    print_important_mes('***************')
    print_important_mes('恭喜你，全部成功啦')
    print_important_mes('***************')


def print_warning(s):
    print("\033[1;31;m!!!!!!!!!!!!!!!!!!!!! %s !!!!!!!!!!!!!!!!!!!!!\033[0m" % s)


def print_important_mes(s):
    print("\033[1m********************* %s *********************\033[0m" % s)


start()
