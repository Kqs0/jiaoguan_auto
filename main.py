#! /usr/bin/env python
# -*- coding: utf-8 -*-
import os

if __name__ == '__main__':
    # 根据result目录下的文件生成allure测试报告html文件
    os.system("allure generate ./reports -o ./html --clean")
