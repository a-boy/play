# SVG 全面教程

## 1. SVG 简介
SVG(Scalable Vector Graphics)是一种基于XML的矢量图形格式，可以在不损失质量的情况下任意缩放。

## 2. 基础语法
```xml
<svg width="200" height="200" xmlns="http://www.w3.org/2000/svg">
  <rect x="10" y="10" width="100" height="100" fill="red" />
</svg>
```
[SVG演练场](https://developer.mozilla.org/en-US/play)

## 3. 基本形状
### 3.1 矩形
```xml
<rect x="10" y="10" width="100" height="50" fill="blue" stroke="black" stroke-width="2"/>
```

### 3.2 圆形
```xml
<circle cx="50" cy="50" r="40" fill="green"/>
```

## 4. 路径绘制
```xml
<path d="M10 10 L100 10 L100 100 Z" fill="none" stroke="black"/>
```

## 5. 渐变效果
```xml
<defs>
  <linearGradient id="grad1" x1="0%" y1="0%" x2="100%" y2="0%">
    <stop offset="0%" style="stop-color:rgb(255,255,0);stop-opacity:1" />
    <stop offset="100%" style="stop-color:rgb(255,0,0);stop-opacity:1" />
  </linearGradient>
</defs>
<rect x="10" y="10" width="200" height="100" fill="url(#grad1)" />
```

## 6. 滤镜效果
```xml
<defs>
  <filter id="blur">
    <feGaussianBlur in="SourceGraphic" stdDeviation="5" />
  </filter>
</defs>
<rect x="10" y="10" width="100" height="100" fill="blue" filter="url(#blur)"/>
```

## 7. 动画效果
```xml
<rect x="10" y="10" width="50" height="50" fill="red">
  <animate attributeName="x" from="10" to="200" dur="3s" repeatCount="indefinite"/>
</rect>
```

## 8. 实际应用案例
### 8.1 简单图标
```xml
<svg width="100" height="100">
  <circle cx="50" cy="50" r="40" fill="yellow" stroke="black" stroke-width="2"/>
  <circle cx="35" cy="40" r="5" fill="black"/>
  <circle cx="65" cy="40" r="5" fill="black"/>
  <path d="M30 70 Q50 90 70 70" fill="none" stroke="black" stroke-width="2"/>
</svg>
```

### 8.2 复杂图形
```xml
<svg width="200" height="200">
  <path d="M20,20 L180,20 L180,180 L20,180 Z M40,40 L160,40 L160,160 L40,160 Z" 
        fill="none" stroke="black" stroke-width="2"/>
  <circle cx="100" cy="100" r="30" fill="red"/>
  <line x1="100" y1="40" x2="100" y2="160" stroke="blue" stroke-width="2"/>
  <line x1="40" y1="100" x2="160" y2="100" stroke="blue" stroke-width="2"/>
</svg>
```
## 参考资料
1. [MDN SVG参考](https://developer.mozilla.org/en-US/docs/Web/SVG)
2. [Inkscape 绘图软件](https://inkscape.org/zh-hans/)