from flask import Flask
from flask_sqlalchemy import SQLAlchemy  # 导入扩展类
from flask import request

# flask全局应用对象
app = Flask(__name__)
# 设置数据库连接地址
# 拼接配置dialect + driver://username:passwor@host:port/database
DB_URI = 'mysql+pymysql://root:123456@localhost:3306/test'
app.config['SQLALCHEMY_DATABASE_URI'] = DB_URI

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # 是否追踪数据库修改，一般不开启, 会影响性能 # 关闭对模型修改的监控
app.config['SQLALCHEMY_ECHO'] = False  # 是否显示底层执行的SQL语句,记录打印SQL语句用于调试的, 一般设置为False, 不然会在控制台输出一大堆的东西
# 在扩展类实例化前加载配置
db = SQLAlchemy(app)  # 初始化扩展，传入程序实例 app
# 执行原生SQL语句, 测试下能不能查询到结果
sql = 'select * from menulist'
result = db.session.execute(sql)
print(result.fetchall())


@app.route('/fans', methods=['GET', 'POST'])
def get_fans():
    if request.method == 'POST':
        return 'czy from POST'
    else:
        return 'czy from GET'
    return '10000'


@app.route('/userprofile')
def get_userprofile():
    name = request.args.get('name', '')
    print(name)
    return dict(name='czy', age=25)


if __name__ == '__main__':
    app.run()
