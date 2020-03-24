import sys
import unittest
from behave import *
from appium import webdriver
from time import sleep
import sys

sys.path.append(r"./storage")
from storage import StorageManager

storage = StorageManager()
storage.setUp()


@given('初始化appium')
def step_初始化appium(context):
    pass

@given('设置数字1为"{number}"')
def step_设置数字1为(context, number):
    et_number = storage.getDriver().find_element_by_id('com.itpiggy.adddemo:id/et_number1')
    et_number.click()
    et_number.clear()
    et_number.send_keys(number)


@given('设置数字2为"{number}"')
def step_设置数字2为(context, number):
    et_number = storage.getDriver().find_element_by_id('com.itpiggy.adddemo:id/et_number2')
    et_number.click()
    et_number.clear()
    et_number.send_keys(number)

@when('点击计算')
def step_点击计算(context):
    storage.getDriver().find_element_by_id('com.itpiggy.adddemo:id/btn_add').click()


@then('两数相加结果为"{result}"')
def step_两数相加结果为(context, result):
    etResult = storage.getDriver().find_element_by_id('com.itpiggy.adddemo:id/tv_result')
    text = etResult.text
    storage.assertEqual(result, text)


@given('隐藏键盘')
def step_隐藏键盘(context):
    storage.getDriver().hide_keyboard()
