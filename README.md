# AutoTest
基于Appium + Cucumber 自动化集成测试

cucumber feature文件如下
~~~
  Feature: 用于测试两数相加

  Background:
    Given 初始化appium

  Scenario Outline: 测试两数相加
    Given 设置数字1为"<Number1>"
    Given 隐藏键盘
    Given 设置数字2为"<Number2>"
    Given 隐藏键盘
    When 点击计算
    Then 两数相加结果为"<Result>"
    Examples:
      | Number1 | Number2 | Result |
      | 2       | 4       | 6      |
      | 5       | 8       | 13     |
~~~
