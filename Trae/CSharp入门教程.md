# C# 编程入门教程

## 目录
1. [C#简介](#c简介)
2. [开发环境搭建](#开发环境搭建)
3. [基础语法](#基础语法)
4. [变量和数据类型](#变量和数据类型)
5. [运算符](#运算符)
6. [控制流程](#控制流程)
7. [数组和集合](#数组和集合)
8. [面向对象编程基础](#面向对象编程基础)
9. [常用类库](#常用类库)

## C#简介
C#是由微软开发的一种面向对象的编程语言，它继承了C++的强大功能，同时提供了更简单易用的语法。C#主要用于开发：
- Windows桌面应用程序
- Web应用程序
- 移动应用程序
- 游戏开发（Unity3D）
- 企业级应用程序

## 开发环境搭建
1. 下载安装Visual Studio（推荐使用Visual Studio Community版本）
2. 在安装时选择".NET开发"工作负载
3. 安装完成后创建第一个控制台应用程序

## 基础语法
### 第一个C#程序
```csharp
using System;

namespace HelloWorld
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("Hello World!");
        }
    }
}
```

### 基本语法规则
- 大小写敏感
- 所有语句以分号(;)结束
- 程序从Main方法开始执行
- 花括号{}定义代码块

## 变量和数据类型
### 基本数据类型
```csharp
int number = 10;              // 整数
double price = 23.99;         // 双精度浮点数
char grade = 'A';             // 字符
string name = "张三";         // 字符串
bool isValid = true;          // 布尔值
```

### 变量声明和初始化
```csharp
// 声明变量
int age;

// 声明并初始化
string city = "北京";

// var关键字（类型推断）
var count = 100;              // 自动推断为int类型
var message = "Hello";        // 自动推断为string类型
```

## 运算符
### 算术运算符
```csharp
int a = 10;
int b = 3;

int sum = a + b;      // 加法
int diff = a - b;     // 减法
int product = a * b;  // 乘法
int quotient = a / b; // 除法
int remainder = a % b;// 取余
```

### 比较运算符
```csharp
bool isEqual = (a == b);     // 等于
bool notEqual = (a != b);    // 不等于
bool greater = (a > b);      // 大于
bool less = (a < b);         // 小于
```

## 控制流程
### if-else条件语句
```csharp
int score = 85;

if (score >= 90)
{
    Console.WriteLine("优秀");
}
else if (score >= 60)
{
    Console.WriteLine("及格");
}
else
{
    Console.WriteLine("不及格");
}
```

### switch语句
```csharp
char grade = 'B';

switch (grade)
{
    case 'A':
        Console.WriteLine("优秀");
        break;
    case 'B':
        Console.WriteLine("良好");
        break;
    case 'C':
        Console.WriteLine("及格");
        break;
    default:
        Console.WriteLine("不及格");
        break;
}
```

### 循环语句
```csharp
// for循环
for (int i = 0; i < 5; i++)
{
    Console.WriteLine($"第{i+1}次循环");
}

// while循环
int count = 0;
while (count < 3)
{
    Console.WriteLine("while循环");
    count++;
}

// foreach循环
string[] fruits = {"苹果", "香蕉", "橙子"};
foreach (string fruit in fruits)
{
    Console.WriteLine(fruit);
}
```

## 数组和集合
### 数组
```csharp
// 声明并初始化数组
int[] numbers = {1, 2, 3, 4, 5};

// 创建指定大小的数组
string[] names = new string[3];
names[0] = "张三";
names[1] = "李四";
names[2] = "王五";
```

### List集合
```csharp
using System.Collections.Generic;

// 创建List集合
List<string> cities = new List<string>();

// 添加元素
cities.Add("北京");
cities.Add("上海");

// 访问元素
Console.WriteLine(cities[0]);

// 遍历集合
foreach (string city in cities)
{
    Console.WriteLine(city);
}
```

## 面向对象编程基础
### 类的定义
```csharp
public class Student
{
    // 字段
    private string name;
    private int age;

    // 属性
    public string Name
    {
        get { return name; }
        set { name = value; }
    }

    public int Age
    {
        get { return age; }
        set { age = value; }
    }

    // 构造函数
    public Student(string name, int age)
    {
        this.name = name;
        this.age = age;
    }

    // 方法
    public void Study()
    {
        Console.WriteLine($"{name}正在学习");
    }
}
```

### 对象的创建和使用
```csharp
// 创建对象
Student student = new Student("张三", 18);

// 访问属性
Console.WriteLine($"姓名：{student.Name}");
Console.WriteLine($"年龄：{student.Age}");

// 调用方法
student.Study();
```

## 常用类库
### 字符串处理
```csharp
string text = "Hello, C#";

// 字符串长度
int length = text.Length;

// 字符串分割
string[] words = text.Split(',');

// 字符串替换
string newText = text.Replace("Hello", "Hi");

// 字符串查找
bool contains = text.Contains("C#");
```

### 日期时间处理
```csharp
// 获取当前日期时间
DateTime now = DateTime.Now;

// 格式化日期
string dateStr = now.ToString("yyyy-MM-dd");

// 日期计算
DateTime tomorrow = now.AddDays(1);
DateTime nextMonth = now.AddMonths(1);
```

### 文件操作
```csharp
using System.IO;

// 读取文件
string content = File.ReadAllText("test.txt");

// 写入文件
File.WriteAllText("output.txt", "Hello, C#");

// 检查文件是否存在
bool exists = File.Exists("test.txt");
```

## 总结
本教程介绍了C#编程的基础知识，包括：
- 基本语法和数据类型
- 控制流程语句
- 数组和集合的使用
- 面向对象编程基础
- 常用类库的使用

通过学习这些基础知识，你已经可以开始编写简单的C#程序了。要成为一名优秀的C#开发者，还需要：
1. 多练习，编写更多的代码
2. 学习更多高级特性（如委托、事件、LINQ等）
3. 了解.NET框架的其他组件
4. 实践实际项目开发

祝你学习愉快！