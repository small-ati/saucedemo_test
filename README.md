# 电商网站的selenium POM实战

## 项目简介
可以测试https://www.saucedemo.com/网站登录、加入一个商品后、断言购物车数量。本项目目前会有些局限性。

## 功能列表
- 登录网站、断言登录后网站页面
- 加入一个指定商品、断言购物车数量是否为1

## 技术栈
- Python 3
- Selenium
- pytest
- POM（页面对象模型）
- Git

## 项目结构
- `test_saucedemo.py`：测试文件
- `saucedemo_obj.py`: 分装定位函数
- `README.md`：项目说明

## 如何运行
1. 安装依赖：`pip install selenium pytest`
2. 将匹配 Edge 版本的 `msedgedriver.exe` 放在项目文件夹根目录下
3. 在项目文件夹终端输入：`pytest -v`

## 作者
陈天泰（自学 Python 自动化测试，正在转行中）