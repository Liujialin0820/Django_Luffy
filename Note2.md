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

