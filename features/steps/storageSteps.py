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
storage.getDriver().find_element_by_id('com.haier.uhome.uplus.storage.test.client:id/btn_manual_test').click()


@given('初始化appium')
def step_初始化appium(context):
    pass

@given('设置节点路径为"{name}"')
def step_设置节点路径为(context, name):
    et_name = storage.getDriver().find_element_by_id('com.haier.uhome.uplus.storage.test.client:id/et_name')
    et_name.click()
    et_name.clear()
    et_name.send_keys(name)


@given('选择节点类型为"{type}"')
def step_选择节点类型为(context, type):
    storage.getDriver().find_element_by_id(
        'com.haier.uhome.uplus.storage.test.client:id/upstorage_sp_node_type').click()
    type__format = 'new UiSelector().text("{type}")'.format(type=type)
    storage.getDriver().find_element_by_android_uiautomator(type__format).click()


@given('选择节点操作为"{opt}"')
def step_选择节点操作为(context, opt):
    storage.getDriver().find_element_by_id('com.haier.uhome.uplus.storage.test.client:id/upstorage_sp_opt').click()
    opt__format = 'new UiSelector().text("{opt}")'.format(opt=opt)
    storage.getDriver().find_element_by_android_uiautomator(opt__format).click()


@given('设置节点值为"{value}"')
def step_设置节点值为(context, value):
    et_value = storage.getDriver().find_element_by_id('com.haier.uhome.uplus.storage.test.client:id/et_value')
    et_value.click()
    et_value.clear()
    et_value.send_keys(value)


@when('执行接口')
def step_执行接口(context):
    storage.getDriver().find_element_by_id('com.haier.uhome.uplus.storage.test.client:id/btn_exec').click()


@then('执行结果为"{result}"')
def step_执行结果为(context, result):
    etResult = storage.getDriver().find_element_by_id('com.haier.uhome.uplus.storage.test.client:id/et_result')
    context.etResult = etResult
    text = etResult.text
    if result == '成功':
        result = 'true'
    else:
        result = 'false'
    storage.assertEqual(result, text)


@given('隐藏键盘')
def step_隐藏键盘(context):
    storage.getDriver().hide_keyboard()
