# 数据格式:
#  姓名, 考号, 地理成绩, 生物成绩

# 使用方法：
#     准备好输入文件numbers.txt(内部是所需查询的学生的学号)
#     运行此程序
#     通过Excel把输出的output.csv转换成excel表格

from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

# 初始化浏览器控制器
browser = webdriver.Chrome()

# 打开输入文件
input_file = open("./numbers.txt", "r", encoding='UTF-8')
# 打开输出文件
output_file = open("./output.csv", "a+", encoding='UTF-8')

num = ""

while True:
    num = input_file.readline()
    if num == "": break
    num = num.split("\n")[0]

    browser.get("http://112.53.84.147:83/2022zkcx")
  
    # 把学号输入网站
    browser.find_element(By.NAME, "key").send_keys(num)
    browser.find_element(By.NAME, "B12").click()

    sleep(2)
    name = browser.find_element(By.XPATH, "/html/body/table[2]/tbody/tr/td[2]/font/table[1]/tbody/tr/td[3]/font/b").text
    
    # 读取成绩
    geography = browser.find_element(By.XPATH, "/html/body/table[2]/tbody/tr/td[2]/font/table[2]/tbody/tr[5]/td[1]").text
    biology = browser.find_element(By.XPATH, "/html/body/table[2]/tbody/tr/td[2]/font/table[2]/tbody/tr[5]/td[2]").text

    output_file.write("{}, {}, {}, {}\n".format(name.split("：")[1], num, geography, biology))

browser.close()
