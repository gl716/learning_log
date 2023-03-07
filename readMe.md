## 创建数据库
使用以下代码创建默认的`sqlite`数据库  
`python manage.py migrate`

## 添加模型后初始化表结构
`python manage.py makemigrations learning_logs`

## 执行初始化表结构
`python manage.py migrate`