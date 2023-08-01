# name_list=["Passerby A","Passerby B","Passerby C"]
# year_list=["Tiger","Sheep"]
# for name in name_list:
#     for year in year_list:
#         message_content=f"""
#         We are delighted to acknowledge you that
#         in the golden year of {name},
#         {year} has been selected to be the representatives of ou communitity"""
#         print(message_content)
# gpa_dict={"小明":3.251,"小红":3.245,"小白":2.253,"小李":2.594}
# for name, gpa in gpa_dict.items():
#     print(f"{name}你好，你的当前绩点为：{gpa:.4f}")
#
# def calculate_sector_1(central_angle,radius_1):
#     return central_angle/360*1.0*3.14*radius_1**2
# print(calculate_sector_1(160,30))
#
# import statistics
# print(statistics.median([69,18,-54,181,99]))

# class CuteAssCat:
#     def __init__(self,name,color,age,personality):
#         self.name=name
#         self.color=color
#         self.age=age
#         self.personality=personality
#     def CatPrint(self):
#         print(f"""Cat's name:{self.name}\nCat's color:{self.color}""")
#     def Think(self,content):
#         print(f"The cat named {self.name} plans to do {content} later.")
# 
# class Student:
#     def __init__(self,name,number):
#         self.name=name
#         self.number=number
#         self.grades={"语文":0,"数学":0,"英语":0}
# 
#     def PrintGrade(self):
#         print(f"{self.name} {self.number}的成绩为：")
#         for course in self.grades:
#             print(f"{course}:{self.grades[course]}分")
# Student1=Student("小曾","191547")
# Student1.PrintGrade()
# Student1.name="zeng"
# Student1.PrintGrade()

# class Employee:
#     def __init__(self,name,id):
#         self.name=name
#         self.id=id
#     def print_info(self):
#         print("姓名："+name+"\t工号："+id)
#
# class FullTimeEmployee(Employee):
#     def __init__(self,monthly_salary,name,id):
#         super().__init__(name,id)
#         self.monthly_salary=monthly_salary
#     def calculate_monthly_pay(self):
#         return self.monthly_salary
#
# class PartTimeEmployee(Employee):
#     def __init__(self,daily_salary,days,name,id):
#         super().__init__(name,id)
#         self.daily_salary=daily_salary
#         self.work_days=days
#     def calculate_monthly_pays(self):
#         return self.daily_salary*self.work_days

# with open(".\data.txt","r",encoding="utf-8") as f:
#     line = f.readline()
#     while line !="" :
#         print(line)
#         line=f.readline()

# with open(".\poem.txt","w",encoding="utf-8") as g:
#     g.write("我欲乘风归去，\n")
#     g.write("又恐琼楼玉宇，\n")
#     g.write("高处不胜寒。")
#
# with open(".\poem.txt","r+",encoding="utf-8") as h:
#     h.write("\n起舞弄清影\n")
#     h.write("何似在人间。")
#     content=h.read()
#     print(content)
#
# try:
#     user_weight=float(input("请输入您的体重（单位：kg）："))
#     user_height=float(input("请输入您的身高（单位：m）："))
#     user_BMI=user_weight/(user_height)**2
# except ValueError:
#     print("输入不为合理数字，请重新运行程序并输入正确的数字。")
# except ZeroDivisionError:
#     print("身高不能为0，请重新运行程序并输入正确的数字")
# except:
#     print("程序发生未知错误，请重新运行")
# else:
#     print("您的BMI值为："+str(user_BMI))
# finally:
#     print("程序运行结束")

# import unittest
# from pyny import my_adder
# from pyny import my_divider
# from pyny import  my_multiplyer
#
# class TestMyAdder(unittest.TestCase):
#     def test_my_adder(selfs):
#         assert my_adder(3,5)==8
#
#     def test_my_divider(self):
#         self.assertEqual(my_divider(4,2),2)
#
#     def test_my_multiplyer(self):
#         self.assertEqual(my_multiplyer(3,5),15)

# from bs4 import BeautifulSoup
# import requests
# Head={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"}
#
# for start_num in range(0,250,25):
#     Resource=requests.get(f"https://movie.douban.com/top250?start={start_num}",headers=Head)
#     Content=Resource.text
#     Soup=BeautifulSoup(Content,"html.parser")
#     all_titles=Soup.findAll("span",attrs={"class":"title"})
#     for title in all_titles:
#         Chinese_Title=title.string
#         if "/" not in Chinese_Title:
#             print(Chinese_Title)

from bs4 import BeautifulSoup
import requests
Head={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"}


Request=requests.get(f"http://books.toscrape.com",headers=Head)
Content=Request.text
Soup=BeautifulSoup(Content,"html.parser")
all_Catalogue=Soup.findAll("ul")
for Catalogue in all_Catalogue:
    Titles=Catalogue.findAll("li")
    for title in Titles:
        for TITs in title:
            print(TITs.string)