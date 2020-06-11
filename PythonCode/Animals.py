#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 引用yaml类
import yaml

# 创建一个类（Animal）【动物类】，类里有属性（名称，颜色，年龄，性别），类方法（会叫，会跑）
class Animal:
    # 定义属性
    def __init__(self, name, color, age, gender):
        self.name = name
        self.color = color
        self.age = age
        self.gender = gender

    # 定义类方法：会叫
    def can_yell(self):
        print('会叫')

    # 定义类方法：会跑
    def can_run(self):
        print('会跑')


# 创建子类【猫】，继承【动物类】
# - 复写父类的__init__方法，继承父类的属性，
# - 添加一个新的属性，毛发=短毛，
# - 添加一个新的方法， 会捉老鼠，
# - 复写父类的‘【会叫】的方法，改成【喵喵叫】
class Cat(Animal):
    # 复写父类的__init__方法，并添加新的属性
    def __init__(self, name, color, age, gender):
        self.name = name
        self.color = color
        self.age = age
        self.gender = gender
        self.hair = '短毛'

    # 定义类方法：会捉老鼠
    def can_catch_mouse(self):
        print(f'姓名：{self.name} ,颜色：{self.color} ,年龄：{self.age} ,性别：{self.gender}，毛发:{self.hair}，捉到了老鼠')

    # 复写父类的‘【会叫】的方法，改成【喵喵叫】
    def can_yell(self):
        print(f'{self.name} ，喵喵叫')


# 创建子类【狗】，继承【动物类】，
# - 复写父类的__init__方法，继承父类的属性，
# - 添加一个新的属性，毛发 = 长毛，
# - 添加一个新的方法， 会看家，
# - 复写父类的【会叫】的方法，改成【汪汪叫】
class Dog(Animal):
    # 复写父类的__init__方法，并添加新的属性
    def __init__(self, name, color, age, gender):
        self.name = name
        self.color = color
        self.age = age
        self.gender = gender
        self.hair = '长毛'

    # 定义类方法：会看家
    def can_watch_house(self):
        print(f'姓名：{self.name} ,颜色：{self.color} ,年龄：{self.age} ,性别：{self.gender}，毛发:{self.hair}，会看家')

    # 复写父类的‘【会叫】的方法，改成【汪汪叫】
    def can_yell(self):
        print(f'{self.name} ，汪汪叫')


# 使用yaml参数化
if __name__ == '__main__':
    with open('AnimalsData.yml', encoding='utf-8') as f:
        data = yaml.safe_load(f)

# 创建一个猫猫实例
# - 调用捉老鼠的方法
# - 打印【猫猫的姓名，颜色，年龄，性别，毛发，捉到了老鼠】。
cat = Cat(data['Cat']['name'], data['Cat']['color'], data['Cat']['age'], data['Cat']['gender'])
# yaml锚点默认值用法
# cat = Cat(data['default']['name'], data['default']['color'], data['default']['age'], data['default']['gender'])
cat.can_catch_mouse()

# 创建一个狗狗实例
# - 调用【会看家】的方法
# - 打印【狗狗的姓名，颜色，年龄，性别，毛发】。
dog = Dog(data['Dog']['name'], data['Dog']['color'], data['Dog']['age'], data['Dog']['gender'])
# yaml锚点默认值用法
# dog = Dog(data['default']['name'], data['default']['color'], data['default']['age'], data['default']['gender'])
dog.can_watch_house()





