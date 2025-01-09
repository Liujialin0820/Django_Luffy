#  1.11 项目初始化~数据库配置 

## 创建用户防止跑路

```sql
create user luffy_user identified by 'luffy';
grant all privileges on luffy.* to 'luffy_user'@'%';
flush privileges;
```

## 使用pymysql 取代之前的sql包 提升性能

在项目主模块的 `luffyapi/__init__.py`中导入pymysql

```python
import pymysql

pymysql.install_as_MySQLdb()
```

## 跨域

```python
pip install django-cors-headers
```

添加应用

```python
INSTALLED_APPS = (
    ...
    'corsheaders',
    ...
)
```

中间件设置【必须写在第一个位置】

```python
MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    ...
]
```

添加白名单

```python
# CORS组的配置信息
CORS_ORIGIN_WHITELIST = (
    '127.0.0.1:5173',
)
CORS_ALLOW_CREDENTIALS = False  # 允许ajax跨域请求时携带cookie
```

![1557455675163](C:/Users/mrliu/OneDrive%20-%20UWA/Documents/Jialin/Study/%E8%B7%AF%E9%A3%9E%E5%AD%A6%E5%9F%8E%E5%9C%A8%E7%BA%BF%E6%95%99%E8%82%B2%E5%B9%B3%E5%8F%B0/%E7%AC%AC1%E7%AB%A0/2/assets/1557455675163.png)



完成了上面的步骤，我们就可以通过后端提供数据给前端使用ajax访问了。





# 第2章  网站首页模块开发

## 轮播图功能实现

前面已经安装了，如果没有安装则需要安装

```shell
pip install pillow
```



### 上传文件相关配置

settings.py

```python
# 访问静态文件的url地址前缀
STATIC_URL = '/static/'
# 设置django的静态文件目录
STATICFILES_DIRS = [
    os.path.join(BASE_DIR,"static")
]

# 项目中存储上传文件的根目录[暂时配置]，注意，uploads目录需要手动创建否则上传文件时报错
MEDIA_ROOT=os.path.join(BASE_DIR,"uploads")
# 访问上传文件的url地址前缀
MEDIA_URL ="/media/"

```



在django项目中转换上传文件的Url地址，总路由urls.py新增代码：

```python
from django.urls import re_path
from django.conf import settings
from django.views.static import serve

urlpatterns = [
  	...
    re_path(r'media/(?P<path>.*)', serve, {"document_root": settings.MEDIA_ROOT}),
]
```

### 注册home子应用

注册home子应用，因为子应用的位置发生了改变，所以为了原来子应用的注册写法，所以新增一个导包路径：

```python
# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# 新增一个系统导包路径
import sys
sys.path.insert(0,os.path.join(BASE_DIR,"apps"))



INSTALLED_APPS = [
	# 注意，加上drf框架的注册	
    'rest_framework',
    
    # 子应用
    'home',

]
```



### 新建开发分支进行独立开发

接下来,我们完成的功能[轮播图]这些,建议采用开发分支来完成,所以我们可以通过以下命令,复刻一份代码[也就是新建一个分支]出来进行独立开发.这样的话,就不会影响到线上的主干代码!!!

```
# 新建一个分支 
git branch 分支名称

# 查看所有分支
git branch

# 切换分支[-b表示新建分支的同时并切换到新分支]
git checkout -b 分支名称

# 删除分支
git branch -d 分支名称
```

接下来,我们可以创建一个dev开发分支并在开发分支下干活!

```
git branch dev
git checkout dev
```



#### 创建轮播图的模型

home/models.py

```python
from django.db import models

# Create your models here.
class Banner(models.Model):
    """轮播广告图模型"""
    # 模型字段
    title = models.CharField(max_length=500, verbose_name="广告标题")
    link = models.CharField(max_length=500, verbose_name="广告链接")
    # upload_to 设置上传文件的保存子目录
    image_url =  models.ImageField(upload_to="banner", null=True, blank=True, max_length=255, verbose_name="广告图片")
    remark = models.TextField(verbose_name="备注信息")
    is_show = models.BooleanField(default=False, verbose_name="是否显示")
    orders = models.IntegerField(default=1, verbose_name="排序")
    is_deleted = models.BooleanField(default=False, verbose_name="是否删除")

    # 表信息声明
    class Meta:
        db_table = "ly_banner"
        verbose_name = "轮播广告"
        verbose_name_plural = verbose_name

    # 自定义方法[自定义字段或者自定义工具方法]
    def __str__(self):
        return self.title
```



