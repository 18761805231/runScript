## 使用需知

程序需要以管理员身份运行

### 依赖

爱思助手及苹果设备，python3.7及Pyhook3(如果使用get_position_v2.py)

### 文件说明

该脚本就个按键精灵，分两部分组成，第一部分是记录按键信息，第二部分是运行模拟脚本

1.记录按键位置有两个版本v1，v2，其中v2需要安装Pyhook3

2.运行start_run.py后，只需将虚拟定位界面打开，之后就不用管了，跑完再手动终止程序就行

### 使用方法
1. 爱思助手虚拟定位需要收藏一个坐标位置，作为基准点
2. 使用get_position.py记录按键位置，只需要记录一圈就好，从收藏坐标开始出发，在结束前选中收藏坐标完成最后一次修改，进行矫正。该步骤只需要在最开始记录一次，以后就不用了
3. 爱思助手虚拟定位，先模拟轨迹使创高体育进入虚拟定位状态
4. 选中收藏坐标进行矫正，开始运行start_run.py，运动已开始
5. 当运动完成后，手动终止脚本，预计8分钟左右完成，不手动就自己在改下，我懒
6. 完成