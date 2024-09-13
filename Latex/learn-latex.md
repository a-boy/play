$A_{bc}^{def}$ $\sqrt[3]{5} \ 45^{\circ}$
$x= \qquad 1$

$\binom{n}{2}$ ${n\choose 2}$

$\dfrac{\pi^2}{6}$ $\tfrac{\pi^2}{6}$

$\bigodot \oplus \leq \leqslant \gg \equiv \sim \approx \varoiint \oint \cap \cup \wedge \vee \subset \supseteq $ 

$\$ \# \% \& \_{}  \backslash \textbackslash @$

$\parallelogram \angle \perp \infty \hbar \exist \forall \partial \varnothing \Delta \nabla \square \circ \bullet$

$ \cdot \quad \cdots \vdots \ddots $

$\lim_{n\to\infty} \lim\limits_{n\to\infty} { \displaystyle \int_{0}^{+\infty} }$ $\sum_{n=1}^{\infty}{n^2}$  

$\left( \right), \left[ \right] \left\{ \right\},\left| \right| \bigg( \bigg)，\Bigg( \Bigg)$

$\left\{\dfrac{\pi^2}{6}\right.$

$$\begin{equation} \label{aaa1}
\begin{split}
&\ x^4+2x^3+11x^2+18x+18 \\
=&\ (x^2+2x+2)(x^2+9)
\\
=&\ (x^2+x+3)^2+(2x+3)^2
\end{split}
\end{equation}$$

用\label{aaa1}给公式加标签，然后用\ref{aaa1}引
用公式 (的编号)，\pageref{aaa1}引用公式所在的页
码。\usepackage{hyperref} 可以让生成的 PDF 文件
带有书签以及可点击跳转的超链接，比如公式 (1)，(2).

$$\begin{align*}
2x+3 &= 5678y-8765z &+ 20 \\
5x &= y+z &+ 33334444
\end{align*}$$

$$\begin{align*}
\begin{cases}
2x+3y=7 \\
3x+5y=8
\end{cases}
\end{align*}$$

`align(*),alignat(*),flalign(*)
equation(*), gather(*),multline(*)`

$$\begin{pmatrix}
a_{11} & a_{12} \\
a_{21} & a_{22} \\\end{pmatrix}$$

pmatrix vmatrix Vmatrix bmatrix Bmatrix matrix

插入表格：
$$\begin{tabular}{|c|c|}
\hline
1 & 2 \\
\hline
3 & 4 \\
\hline
\end{tabular}$$

插入图片：
$$\usepackage{graphicx}
\begin{figure}\centering
\includegraphics[width=
0.3\linewidth]{ 图 片 名 }
\caption{ 图 片 标 题 }
\label{xxx1}
\end{figure}$$

$\textcolor{red}{ 设置 }·$

带编号列表：
$$\usepackage{enumerate}
\begin{enumerate}[(1)]
\item
有 界 变 差 函 数
\item
可 测 函 数
\end{enumerate}$$

不带编号列表：
$$\begin{itemize}
\item 控 制 收 敛 定 理
\item Levi 引理和 Fatou 引理
\end{itemize}$$

空格与空白：
```
负空格 \! 
窄空格\, 
中等空格 \: 
宽空格 \; 
词间空格 \
四倍空格 \quad
八倍空格 \qquad
注意，“词间空格”的斜杠后有一个看不见的空格。
取消首行缩进：\noindent
水平空白
\hspace{±2cm}
垂直空白
\vspace{±2cm}```
```

