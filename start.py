#!/Usr/bin/env python3
# -*- coding: UTF-8 -*-

import os
# from git.repo import Repo

# # 创建本地路径用来存放远程仓库下载的代码
# download_path = os.path.join('aha')
# # 拉取代码
# git_url = 'https://github.com/375003148/ModularizationProjectTemplate'
# Repo.clone_from(git_url,to_path=download_path,branch='master')


# ----------配置初始设置------------
username = 'ZZH'

# # 配置工程前缀
# project_prefix = ''
# while len(project_prefix)==0:
#     project_prefix = input('请输入你的工程前缀：')
#     project_prefix = project_prefix.upper().replace(' ', '')
#     print('工程前缀是' + project_prefix)
#
# # 配置工程名称
# project_name = ''
# while len(project_name)==0:
#     project_name = input('请输入你的工程名称（注意驼峰标示）：')
#     project_name = project_name.replace(' ', '')
#     print('工程名称是' + project_name)

project_name = 'EasyPaa'
project_prefix = 'EW'
project_folder = os.getcwd() + '/Template/ZZHPROJECT/'
os.system("python edit_template.py %s %s %s"%(project_name, project_prefix, project_folder))



