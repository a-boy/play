JavaScript 作为一门不断发展的编程语言，持续引入新功能和语法以提升开发者的编码效率和编程体验。以下是 ES6（ES2015）之后 JavaScript 陆续推出的一些新特性：

### ES6（ES2015）
- **块级作用域变量**
    - `let` 和 `const` 用于声明块级作用域变量。`let` 声明的变量可以重新赋值，而 `const` 声明的常量一旦赋值就不能再重新赋值。
    ```javascript
    {
      let localVar = 'I am local';
      const constantVar = 42;
    }
    // 这里无法访问 localVar 和 constantVar
    ```
- **箭头函数**
    - 提供了更简洁的函数定义语法，并且没有自己的 `this`、`arguments`、`super` 或 `new.target`。
    ```javascript
    const numbers = [1, 2, 3];
    const squared = numbers.map(num => num * num);
    ```
- **模板字符串**
    - 使用反引号（`）来定义，可以包含变量和表达式，使用 `${}` 语法嵌入变量。
    ```javascript
    const name = 'John';
    const greeting = `Hello, ${name}!`;
    ```
- **解构赋值**
    - 可以从数组或对象中提取值并赋值给变量。
    ```javascript
    const [first, second] = [1, 2];
    const { city, country } = { city: 'New York', country: 'USA' };
    ```
- **类和继承**
    - 引入了 `class` 关键字来定义类，使用 `extends` 关键字实现继承。
    ```javascript
    class Animal {
      constructor(name) {
        this.name = name;
      }
      speak() {
        console.log(`${this.name} makes a noise.`);
      }
    }
    class Dog extends Animal {
      speak() {
        console.log(`${this.name} barks.`);
      }
    }
    ```

### ES2016
- **指数运算符**
    - 引入了 `**` 作为指数运算符，用于计算一个数的幂。
    ```javascript
    const result = 2 ** 3; // 结果为 8
    ```
- **`Array.prototype.includes`**
    - 用于判断数组是否包含某个特定的值，返回一个布尔值。
    ```javascript
    const arr = [1, 2, 3];
    const hasTwo = arr.includes(2); // true
    ```

### ES2017
- **`async/await`**
    - 用于处理异步操作，使异步代码看起来更像同步代码，提高了代码的可读性和可维护性。
    ```javascript
    async function fetchData() {
      try {
        const response = await fetch('https://api.example.com/data');
        const data = await response.json();
        return data;
      } catch (error) {
        console.error(error);
      }
    }
    ```
- **`Object.values` 和 `Object.entries`**
    - `Object.values` 返回一个给定对象所有可枚举属性的值组成的数组，`Object.entries` 返回一个给定对象自身可枚举属性的键值对数组。
    ```javascript
    const obj = { a: 1, b: 2 };
    const values = Object.values(obj); // [1, 2]
    const entries = Object.entries(obj); // [['a', 1], ['b', 2]]
    ```

### ES2018
- **异步迭代器和 `for - await - of`**
    - 允许异步遍历可迭代对象。
    ```javascript
    async function* asyncGenerator() {
      let i = 0;
      while (i < 3) {
        yield await new Promise(resolve => setTimeout(() => resolve(i++), 100));
      }
    }
    (async () => {
      for await (const num of asyncGenerator()) {
        console.log(num);
      }
    })();
    ```
- **Rest/Spread 属性**
    - 扩展了对象的 Rest 和 Spread 语法，允许在对象解构和对象字面量中使用。
    ```javascript
    const { a, ...rest } = { a: 1, b: 2, c: 3 };
    const newObj = { ...rest, d: 4 };
    ```

### ES2019
- **`Array.prototype.flat` 和 `Array.prototype.flatMap`**
    - `flat` 方法用于将多维数组扁平化，`flatMap` 是 `map` 和 `flat` 的组合。
    ```javascript
    const nestedArray = [1, [2, [3]]];
    const flattened = nestedArray.flat(2); // [1, 2, 3]
    const numbers = [1, 2, 3];
    const result = numbers.flatMap(num => [num * 2]); // [2, 4, 6]
    ```
- **`Object.fromEntries`**
    - 将键值对数组转换为对象。
    ```javascript
    const entries = [['a', 1], ['b', 2]];
    const obj = Object.fromEntries(entries); // { a: 1, b: 2 }
    ```

### ES2020
- **`BigInt`**
    - 引入了一种新的数字类型，用于表示任意大的整数。
    ```javascript
    const bigNumber = 123456789012345678901234567890n;
    ```
- **`Promise.allSettled`**
    - 等待所有的 Promise 都完成（无论是成功还是失败），并返回一个包含每个 Promise 结果的数组。
    ```javascript
    const promises = [Promise.resolve(1), Promise.reject(new Error('Error'))];
    Promise.allSettled(promises).then(results => console.log(results));
    ```

### ES2021
- **逻辑赋值运算符**
    - 包括 `&&=`、`||=` 和 `??=`，结合了逻辑运算符和赋值运算符。
    ```javascript
    let a = 0;
    a ||= 5; // 如果 a 为假值，则将 5 赋值给 a
    ```
- **`String.prototype.replaceAll`**
    - 用于替换字符串中所有匹配的子字符串。
    ```javascript
    const str = 'Hello, World!';
    const newStr = str.replaceAll('o', 'e'); // 'Helle, Werld!'
    ```

### ES2022
- **类的私有方法和属性**
    - 使用 `#` 符号定义类的私有方法和属性。
    ```javascript
    class MyClass {
      #privateProperty = 42;
      #privateMethod() {
        return this.#privateProperty;
      }
      publicMethod() {
        return this.#privateMethod();
      }
    }
    ```
- **`Object.hasOwn`**
    - 用于检查对象是否具有指定的自有属性。
    ```javascript
    const obj = { a: 1 };
    const hasProp = Object.hasOwn(obj, 'a'); // true
    ```

### ES2023
- **数组和类型化数组的新方法**
    - `toReversed`、`toSorted`、`toSpliced` 和 `with` 等方法，这些方法返回一个新的数组，而不会改变原数组。
    ```javascript
    const arr = [1, 2, 3];
    const reversed = arr.toReversed(); // [3, 2, 1]
    ```
- **WeakMap 和 WeakSet 的键可以是任何原始值**
    - 之前 WeakMap 和 WeakSet 的键只能是对象，现在可以使用原始值作为键。 