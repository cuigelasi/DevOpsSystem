# DevOps 实战

## 设置django和mysql容器密码
```shell
passwd
Newpassword: 123qwe
Retype new password: 123qwe

```
## 创建utf-8字符集数据库
```shell
mysql -ucgls -p123qwe
CREATE DATABASE db_name DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci;
```

## django数据库同步操作
```
# 建立相应的migrations目录，并记录下所有的关于modes.py的改动，这时还未保存到数据库
python manage.py makemigrations
# 将改动作用到数据库文件，比如新建table，更新table
python manage.py migrate
```

## 运行django工程
```
# 运行django工程，指定ip和port，便于web调试
python manage.py runserver <ip>:<port>
```

## 创建web app
```
python manage.py startapp web
```

## 创建超级用户
```
python manage.py createsuperuser
```

## django2.02 + markdown 打造bolg界面
```
#前端显示
#需要额外安装：
python -m pip install markdown
yum -y install python-pygments
python -m pip install Pygments==1.4
#获取代码高亮css
pygmentize -S default -f html -a .codehilite > code.css

#后台录入
1.安装django-mdeditor app
python -m pip install django-mdeditor
2.settings.py的INSTALLED_APPS中添加’mdeditor’
3.添加路径设置到setting
MEDIA_ROOT = os.path.join(BASE_DIR, 'uploads')  #uploads必须存在，且在项目目录下
MEDIA_URL = '/media/'                           #你上传的文件和图片会默认存在/uploads/editor下
4.添加url
```


