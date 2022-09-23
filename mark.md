（命令行最前面显示venv即说明在虚拟环境中）
1.进入虚拟环境命令
venv\scripts\activate
2.退出虚拟环境命令
deactivate
3.命令创建文件
mkdir + 文件名

4.static可以存放一些静态文件，如图片、css样式文件等等

5.数据库
* 用户名：root 密码：123456
* 启动服务net start mysql
* mysql路径 E:\softwareinstall_C\mysql
* [报错]当出现1045报错，先打开cmd，输入mysql -u root -p,不用输入密码，直接enter，输入use mysql，
  再输入ALTER USER 'root'@'localhost' IDENTIFIED WITH mysql_native_password BY '123456'修改密码就行了
* 
6.安装flask-sqlalchemy
为了简化数据库操作，我们将使用 SQLAlchemy——一个 Python 数据库工具（ORM，即对象关系映射）。
借助 SQLAlchemy，你可以通过定义 Python 类来表示数据库里的一张表（类属性表示表中的字段 / 列），
通过对这个类进行各种操作来代替写 SQL 语句。这个类我们称之为模型类，类中的属性我们将称之为字段。

7.Flask-为什么会启动两次
原因：
当调用app.run()的时候，用到了Werkzeug库，它会生成一个子进程，当代码有变动的时候它会自动重启
如果在run（）里加入参数 use_reloader=False，就会取消这个功能，当然，在以后的代码改动后也不会自动更新了。

8.[报错]'FLASK_ENV' is deprecated and will not be used in Flask 2.3. Use 'FLASK_DEBUG' instead.
在.flaskenv文件内，将FLASK_ENV=development，修改为FLASK_DEBUG=development


