ReadMe
============

1. 直接运行 create_pod.py 脚本完成pod的初始创建.

2. 如果要导入工程则在podfile中增加:
pod '${PODNAME}', :path => './DevelopmentPods/${PODNAME}'
然后执行 pod install


