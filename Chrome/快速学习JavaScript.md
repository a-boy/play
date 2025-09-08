# 快速学习JavaScript

```JavaScript
[0,null,undefined,"",NaN,  Infinity,[],{}].map(Boolean)
//(8)[false,  false,  false,  false,  false,  true,   true,  true]
[0,null,undefined,"",NaN,  Infinity,[],{}].map(Number)
//(8) [0, 0, NaN, 0, NaN, Infinity, 0, NaN]

typeof(null)   //'object'
typeof(0)      //'number'
typeof(NaN) //'number'
typeof(undefined)    //'undefined'
typeof([0])    //'object'
typeof(Array)  //'function'
typeof(Array[6]) //'undefined'
```

```JavaScript
Array.of(7); // [7]
Array(7); // array of 7 empty slots

Array(6).keys().toArray()  //(6) [0, 1, 2, 3, 4, 5]
[...Array(6).keys()]   //(6) [0, 1, 2, 3, 4, 5]
[...Array(6).keys()].slice(2)  //(4) [2, 3, 4, 5]
Array.from(Array(5).keys()) //(5) [0,  1,  2,  3,  4]
Array.from({length: 5}, (_, i) => i);

const range = (start, stop, step=1) => Array.from({ length: (stop - start-1) / step + 1}, (_, i) => start + (i * step));

const range = (start, stop, step=1) =>
  Array.from(
    { length: Math.ceil((stop - start) / step) },
    (_, i) => start + i * step,
 );

const range = (start, stop, step = 1) =>
  Array(Math.ceil((stop - start) / step)).fill(start).map((v, i) => v+ i * step);
range(0,4) //(4) [0, 1, 2, 3]

[1,2,3]*2  //NaN
[1,2,3]+2  //'1,2,32'

fruit1='apple'
obj={[fruit1]:'苹果'}  // {apple: '苹果'}
obj={[{o:1}]:'苹果'}   // {[object Object]: '苹果'}
```

```JavaScript
'A'.charCodeAt(0)    //65
String.fromCharCode(66)  //'B'
Array.from(Array(5).keys())
String.fromCharCode(...range(65,65+26)) //'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
```


```JavaScript
null | 'a' // 0
null || 'a' // 'a'
null && 'a'  // null
1 && 'a' // 'a'

a=null
a?.__proto__ //undefined

a=1
a?.__proto__
// Number {0, toExponential: ƒ, toFixed: ƒ, toPrecision: ƒ, toString: ƒ, …}

```


```JavaScript
+[]    //0
!![]    //true
!!+[]  //false
[1]+1 //'11'
+([1]+1) //11
+[1]+1 //2

~~'2.78'  //2
~~'-2.78'  //-2
parseInt('-2.78') //-2
Math.floor(-2.78) //-3
+'-2.78'  //-2.78
Number('-2.78') //-2.78
!!'2.78' //true

parseInt(8e3) //8000
parseInt(8e30) //8
Number(8e30)  //8e+30
parseInt(0.0000008)  //8
0.0000008  //8e-7
parseInt(0.000008) //0

0xff  //255
0b110 //6
~0b110  //-7
0o12  //10
~10    //-11  x不大时 ~x === -(x+1)
2n**31n-1n //2147483647n
2^3  == 0b10^0b11 == 1
```


```JavaScript

'美丽'.fontcolor('#0ff')  // '<font color="#0ff">美丽</font>'
'美丽'.link('beauty')   // '<a href="beauty">美丽</a>'
'美丽'.repeat(3) // '美丽美丽美丽'
tempGirls = Array(3).fill("girl", 0);  //(3) ['girl', 'girl', 'girl']

```


```JavaScript
Array.from("foo")  //(3) ['f', 'o', 'o']
Array.from([1, 3, 5], (x) => x*x) //(3) [1, 9, 25]
```


### JavaScript生成HTML表格

```JavaScript
function createTable(objectArray, fields, fieldTitles) {
  let body = document.getElementsByTagName('body')[0];
  let tbl = document.createElement('table');
  let thead = document.createElement('thead');
  let thr = document.createElement('tr');
  fieldTitles.forEach((fieldTitle) => {
    let th = document.createElement('th');
    th.appendChild(document.createTextNode(fieldTitle));
    thr.appendChild(th);
  });
  thead.appendChild(thr);
  tbl.appendChild(thead);

  let tbdy = document.createElement('tbody');
  let tr = document.createElement('tr');
  objectArray.forEach((object) => {
    let tr = document.createElement('tr');
    fields.forEach((field) => {
      var td = document.createElement('td');
      td.appendChild(document.createTextNode(object[field]));
      tr.appendChild(td);
    });
    tbdy.appendChild(tr);    
  });
  tbl.appendChild(tbdy);
  body.appendChild(tbl)
  return tbl;
}

createTable([
  {name: 'Banana', price: '3.04'},
  {name: 'Orange', price: '2.56'},
  {name: 'Apple', price: '1.45'}
],
['name', 'price'], ['Name', 'Price']);
```

### HTML表格数据来自js数组

```html
<table border="2">
  <thead class="thead-dark">
    <tr>
      <th scope="col">Tour</th>
      <th scope="col">Day</th>
      <th scope="col">Time</th>
    </tr>
  </thead>
  <tbody id="tableBody">
                                    
  </tbody>
</table>
<script>
const data = [{Name:'Sydney', Day: 'Monday', Time: '10:00AM'},{Name:'New York', Day: 'Monday',Time: '11:00AM'},]; // any json data or array of objects

const tableData = data.map(value => {
  return (
    `<tr>
       <td>${value.Name}</td>
       <td>${value.Day}</td>
       <td>${value.Time}</td>
    </tr>`
  );
}).join('');

const tableBody = document.querySelector("#tableBody");
tableBody.innerHTML = tableData;
</script>
```

### ["1", "2", "3"].map(parseInt)
考虑下例：  
["1", "2", "3"].map(parseInt);  

我们期望输出 [1, 2, 3], 而实际结果是 [1, NaN, NaN].

parseInt 函数通常只使用一个参数，但其实可以传入两个参数。第一个参数是表达式，第二个参数是解析该表达式的基数。当在 Array.prototype.map 的回调函数中使用 parseInt 函数时，map 方法会传递 3 个参数：元素,索引,数组
parseInt 函数会忽略第三个参数，但是不会忽略第二个参数！这可能会导致一些问题。

```JavaScript
// parseInt(string, radix) -> map(parseInt(value, index))
/* 第一次迭代 (index 是 0): */ parseInt("1", 0); // 1
/* 第二次迭代 (index 是 1): */ parseInt("2", 1); // NaN
/* 第三次迭代 (index 是 2): */ parseInt("3", 2); // NaN

//下面让我们来讨论解决方案：

const returnInt = (element) => parseInt(element, 10);
["1", "2", "3"].map(returnInt); // [1, 2, 3]
// 实际结果是一个数字数组（如预期）

// 与上面相同，但使用简洁的箭头函数语法
["1", "2", "3"].map((str) => parseInt(str)); // [1, 2, 3]

// 实现上述目标更简单的方法，同时避免了“骗招”：
["1", "2", "3"].map(Number); // [1, 2, 3]

// 但与 parseInt() 不同，Number() 还会返回一个浮点数或（解析）指数表示法：
["1.1", "2.2e2", "3e300"].map(Number); // [1.1, 220, 3e+300]

// 为了进行比较，如果我们对上面的数组使用 parseInt():
["1.1", "2.2e2", "3e300"].map((str) => parseInt(str)); // [1, 2, 3]
```

```js
0.4641571044921875.toString(2)
parseInt('0111011011010011',2)==0b0111011011010011  //30419

```


```js
const arrayLike = {
  length: 3,
  unrelated: "foo",
  0: 5,
  2: 4,
  3: 3, // ignored by with() since length is 3
};
console.log(Array.prototype.with.call(arrayLike, 0, 1));
// [ 1, undefined, 4 ]

```
