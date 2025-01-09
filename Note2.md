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

# 跨域

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