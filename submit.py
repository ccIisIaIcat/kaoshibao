import imp
from tkinter.messagebox import NO
from rsa import sign
from selenium import webdriver
from selenium.webdriver.common.by import By

import json
import re
from time import sleep

import logging
logger = logging.getLogger(__name__)
logger.setLevel(level = logging.INFO)
handler = logging.FileHandler("run.log")
handler.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)


with open('test1.json', 'r', encoding='utf8') as f:
    json_data = json.load(f)

#1.创建Chrome浏览器对象，这会在电脑上在打开一个浏览器窗口
browser = webdriver.Chrome(executable_path=r'C:\\Program Files (x86)\\Google\\Chrome\\Application\\chromedriver.exe')

#2.通过浏览器向服务器发送URL请求
browser.get("https://www.kaoshibao.com/k/3344927")
# browser.get("https://www.kaoshibao.com/k/3236269")


# #3.刷新浏览器
# browser.refresh()

#4.设置浏览器的大小
browser.set_window_size(800,800)

# 搜索按钮为 进入考试
element = browser.find_element(By.CLASS_NAME, 'go-btn').click()
sleep(3)
# 设置用户登录框，填写考试信息
element = browser.find_elements(By.TAG_NAME, 'input')

print(element)
if len(element) == 2:
    # element[0].send_keys('李岩')
    # element[1].send_keys('18801307699')
    element[0].send_keys('贾真47')
    element[1].send_keys('15901533702')

element = browser.find_element(By.CLASS_NAME, 'go-btn').click()

sleep(3)


# 下一步区块
next_preve = browser.find_element(By.CLASS_NAME, 'next-preve')
button_list = next_preve.find_elements(By.TAG_NAME, 'button')
signal = 1
while True:
    element = browser.find_elements(By.CLASS_NAME, 'qusetion-box')
    spacn = element[0].find_elements(By.TAG_NAME, 'span')
    text = element[0].text
    span = spacn[0].text
    data = text.replace(span, '')
    # print('--{}--'.format(data))
    print('####################\n')
    time_day = 4
    signal += 1
    print(signal)
    try:
        data = data.strip()
        # print('{}#'.format(data))
        logger.info('题目：{}'.format(data))
        value_data = json_data.get(data, None)
        answ = value_data['正确答案（必填）']
        print(value_data)
        print(answ)
        if answ == "错误":
            answ = "B"
        if answ == "正确":
            answ = "A"
        answ.replace("选项 ", "")
        answ_list = []
        if len(answ) == 1:
            time_day = 3
        else:
            # time_day = 7    # 多选题7秒
            time_day = 3
        for i in range(len(answ)):
            answ_list.append(answ[i])
        for a in answ_list:
            option = '选项 {}'.format(a)
            option_value = value_data[option]
            select_left = browser.find_element(By.CLASS_NAME, 'select-left')
            option_list = select_left.find_elements(By.TAG_NAME, 'span')
            key = ''
            # print(option_value)
            for option in option_list:
                key = option.text
                print(key)
                if option_value == '选项 对':
                    option_value = '正确'
                elif option_value == '选项 错':
                    option_value = '错误'
                if key == option_value:
                    logger.info('选项：{}'.format(key))
                    logger.info('答案：{}'.format(option_value))
                    logger.info('状态：True')
                    option.click()
                
        print('####################\n')
    except Exception as err:
        print("err:    !",err)
        print('未找到！', err)
        logger.error('错误信息：{}'.format(err))
    sleep(time_day)
    button_list[-1].click()
    