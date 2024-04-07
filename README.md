# 1. 项目说明

​	本项目为SRTP项目《后疫情时代中美青少年网络用语分》的在线情感可视化网站，核心功能为中英文词语情感可视化展示。



​	项目主要基于Django框架搭建，通过Mysql进行数据存储。



# 2. 使用说明

- 首先安装所需依赖库：django，pillow，js2py，django，mysqlclient，urlilb3，fake_useragent等库。
- 然后再修改setting中的mysql数据库配置连接到一个新的用于存放账号信息的一个数据库上。

- 最后按照正常的Django项目启动流程即可正常运行：
  - `python manage.py makemigrations`
  - `python manage.py migrate`
  - `python manage.py migrate`（第二次执行效果为向绑定的数据库插入管理员账号：用户名Admin、密码123）
  - `python manage.py runserver 8080`



# 3. 效果展示

**登陆页面**

![](.\md_pic\登陆效果图.png)

**核心功能（中英文情感倾可视化向对比分析）页面**

![](.\md_pic\核心功能示例.png)