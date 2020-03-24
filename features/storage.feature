Feature: 用于测试通用数据存储接口

  Background:
    Given 初始化appium

  Scenario Outline: 测试通用数据接口
    Given 设置节点路径为"<Name>"
    Given 隐藏键盘
    Given 选择节点操作为"<Opt>"
    Given 选择节点类型为"<Type>"
    Given 设置节点值为"<Value>"
    Given 隐藏键盘
    When 执行接口
    Then 执行结果为"<Result>"
    Examples:
      | Name | Opt | Type    | Value | Result |
      | A/B  | Put | Int     | 10    | 成功     |
      | C    | Put | String  | test  | 成功     |
      | D    | Put | Boolean | false | 成功     |