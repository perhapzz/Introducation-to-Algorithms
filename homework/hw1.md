## 3.2

$B=O(A)$

NNYYN

NNYYN

NNNNN

YYNNN

YNYNY

YNYNY

## 4.5-4

不能

$a=4,\ b=2, f(n)=n^2\lg n$

猜测，
$$
T(n)\le cn^2\lg^2n
$$
证明，
$$
\begin{aligned}
T(n)&=4T(n/2)+n^2\lg n\\
&\le4c(n/2)^2\lg^2(n/2)+n^2\lg \\
&=cn^2\lg(n/2)\lg n-cn^2\lg(n/2)\lg 2+n^2\lg n\\
&=cn^2\lg^2n-cn^2\lg n\lg 2-cn^2\lg(n/2)\lg 2+n^2\lg n\\
&=cn^2\lg^2n+(1-c\lg 2)n^2\lg n-cn^2\lg(n/2)\lg2\ \ \ (c\ge1/\lg2)\\
&\le cn^2\lg^2n-cn^2\lg(n/2)\lg 2\\
&\le cn^2\lg^2 n 
\end{aligned}
$$


$T(n)=\Theta(n^2\lg^2n)$



## 4.3

### a. $T(n)=4T(n/3)+nlgn$

$a = 4, b = 3, f(n) = n\lg n,$ 由主定理 
$$
T(n) = \Theta(n^{\log_34})
$$

### b. $T(n)=3T(n/3)+n/lgn$

#### 方法1

![image-20211009202516677](/Users/panhuazheng/Desktop/zzz/算法导论/算法作业-1/image-20211009202516677.png)

​		深度为$i$的结点对应规模为$n/3^i=1$时，即$i=log_3n$时，字问题规模变为1，对应于叶结点$T(1)$。

​		每层结点数是上一层的3倍，因此深度为$i$的结点数为$3^i$。并且深度为$i$的结点对应的字问题规模为$n/3^i$，故深度为$i$的每个结点的代价为$c(n/3^i)/\lg(n/3^i)$。因此，除叶结点外，深度为i i*i*的所有结点的代价之和为$3^i·(c(n/3^i)/\lg(n/3^i))=cn/(\lg n-i·\lg 3)$。又由于深度为$i$的结点数为$3^i$，并且叶结点深度为$\log_3n$，故叶结点一共有$3^{\log_3n}=n$个，于是所有叶结点的代价和为$\Theta(n)$。

​		每一层代价加起来，得
$$
\begin{aligned}
T(n) &= \sum_{i=0}^{\log_3n-1}\frac{cn}{\lg n-i·\lg3}+\Theta(n)\\
&=cn·\sum_{i=0}^{\log_3n-1}\frac{1/\lg3}{\lg n/\lg 3-i}+\Theta(n)\\
&=\frac{cn}{\lg3}·\sum_{i=0}^{\log_3n-1}\frac{1}{\log_3n-i}+\Theta(n)\\
&=\frac{cn}{\lg3}·(\frac{1}{\log_3n}+\frac{1}{\log_3n-1}+···+1)+\Theta(n)\\
&=\frac{cn}{\lg3}·\sum_{i=1}^{\log_3n}\frac{1}{i}+\Theta(n)\\
&=\frac{cn}{\lg3}·(\ln(\log_3n)+O(1))+\Theta(n)\\
&=\Theta(n\lg\lg n)
\end{aligned}
$$


#### 方法2

猜测
$$
T(n) = \Theta(n\log_3\log_3 n)
$$
下面将这个猜测代入原递归式进行验证。我们要证明的是：存在正常数$c_1$和$c_2$，使得$c_2n\log_3\log_3 n\le T(n)\le c_1n\log_3\log_3 n$对足够大的$n$都成立。

（1） 证明存在正常数$c_1$，使得$T(n)\le c_1n\log_3\log_3n$

首先假定此上界对所有正数$m<n$都成立，特别是对于$m=\frac{n}{3}$，有$T(\frac{n}{3})\le c_1\frac{n}{3}\log_3 \log_3 \frac{n}{3}$

将其代入递归式得到
$$
\begin{aligned}
T(n)&≤3(c_1\frac{n}{3}\log_3\log_3\frac{n}{3})+\frac{n}{\lg n }\\
&=c_1n\log_3\log_3{\frac{n}3}+\frac{n}{\lg n}\\

\end{aligned}
$$
现要选取合适的$c_1$，使得不等式$c_1n\log_3\log_3{\frac{n}3}+\frac{n}{\lg n}\le c_1n\log_3\log_3n$成立。将不等式做一下变换，等价于
$$
\frac{c_1n(\log_3\log_3{n}-\log_3\log_3\frac{n}3)}{\frac{n}{\lg n}}\ge1 
$$
令
$$
f(x)=\log_3x
$$

$$
f'(x)=\frac{1}{x\ln3}
$$

由拉格朗日中值定理，$\exists \eta \in(\log_3n-1, \log_3n)$，
$$
{\log_3\log_3n-\log_3\log_3{\frac{n}{3}}}=\frac{f(\log_3n)-f(\log_3n-1)}{\log_3n-(\log_3n-1)}=f'(\eta)
$$
则，
$$
\begin{aligned}
\frac{c_1n(\log_3\log_3{n}-\log_3\log_3\frac{n}3)}{\frac{n}{\lg n}} &\ge \frac{c_1\frac{1}{(\log_3n)\ln3}}{\frac{1}{\lg n}}\\
&=c_1\frac{\lg n}{(\log_3n)\ln3}\\
&=\frac{c_1 \lg3}{\ln3}\frac{\log_3n}{\log_3n}\\
&=\frac{c_1 \lg 3}{\ln 3}
\end{aligned}
$$
显然，只要取$c_1\ge\frac{ln3}{lg3}$，不等式成立，此时$T(n)\ge c_1n\log_3\log_3n$成立

（2）  证明存在正常数$c_2$，使得$T(n)\ge c_2n\log_3\log_3n$对足够大的$n$都成立

证明与上文类似，最终得到只要取$c_2\le\frac{ln3}{lg3}$，就能使不等式$T(n)\ge c_2n\log_3\log_3n$成立

### c. $T(n)=4T(n/2)+n^2\sqrt{n}$

根据主定理
$$
T(n) = \Theta(n^{2.5})
$$


### d. $T(n)=3T(n/3-2)+n/2$

n足够大时，原式转化为
$$
T(n) = 3T(\frac{n}{3})+\frac{n}{2}
$$
根据主定理
$$
T(n) = \Theta(n\lg n)
$$

### e. $T(n)=2T(n/2)+n/lgn$

与b同理，$T(n)=\Theta(n\lg \lg n)$

### f. $T(n)=T(n/2)+T(n/4)+T(n/8)+n$

#### 方法1

![image-20211009204314996](/Users/panhuazheng/Desktop/zzz/算法导论/算法作业-1/image-20211009204314996.png)
$$
\begin{aligned}
T(n)& = n(\frac{7}{8}+\frac{49}{64}+···+(\frac{7}{8})^k)\\
&=n·(7-(\frac{7}{8})^n)\\
&=\Theta(n)
\end{aligned}
$$

#### 方法2

猜测：
$$
T(n)\le cn
$$
证明
$$
\begin{aligned}
T(n) &= T(\frac{n}{2})+T(\frac{n}{4})+T(\frac{n}{8})+n\\
&\le \frac{cn}2+\frac{cn}4+\frac{cn}8+n\\
&=(\frac{8}7c+1)n
\end{aligned}
$$
当$c\ge8$时,
$$
T(n) \le(\frac{7}8c+1)n\le cn
$$
同理证明下界，
$$
T(n)\ge cn
$$

### g. $T(n)=T(n-1)+1/n$

$$
T(n)=T(0)+\sum_{i=1}^{n}{\frac{1}{i}}
$$

研究调和级数的前n项和为：
$$
H_n = \sum_{i=1}^n{\frac{1}{i}}
$$
定义如下函数：
$$
h(x)=\frac{1}{i+1},\ \  i<x\le i+1
$$
可以找到$h(x)$的上下界函数
$$
\overline{h}=
\begin{cases}
1\ \ 0<x<1\\
\frac{1}{x}\ \ x\ge1
\end{cases}
$$

$$
\underline{h} = \frac{1}{1+x}
$$

则，
$$
H_n=\int_0^n{h(x)}dx
$$
且
$$
\int_0^n{\underline{h}(x)dx} \le H_n \le \int_0^n{\overline{h}(x)dx}
$$
即
$$
\ln(n+1) \le H_n \le 1+\ln(n)
$$
因此
$$
T(n) = \Theta(lgn)
$$
### h. $T(n)=T(n-1)+lgn$

$$
T(n) = T(0)+\sum_{i=1}^n{lgi}
$$

研究对数数列的前 n 项和：
$$
log(n!) = log(1)+log(2)+···+log(n)
$$
定义如下函数：
$$
a(x) = log(i+1),\ \ i<x\le i+1
$$
可以找到$a(x)$的上下界为：
$$
\underline{a}(x)=
\begin{cases}
0\ \ \ \ \ \ \ \ \  \ 0<x<1\\
log(x) \ \ x\ge 1
\end{cases}
$$

$$
\overline{a}=log(x+1)
$$

则，
$$
A_n=\int_0^n{a(x)dx}
$$
且，
$$
\int_0^n{\underline{a}(x)dx} \le A_n \le \int_0^n{\overline{a}(x)dx}
$$
积分可得，
$$
nlog(n)-n\le A_n\le (n+1)log(n+1)-n
$$
因此
$$
T(n) = \Theta(nlgn)
$$
### i. $T(n)=T(n-2)+1/lgn$

与前两题同理，研究对数积分$li(x)$，当$x\rightarrow\infty$时，函数有如下渐近表现：
$$
li(x) = O(\frac{x}{ln(x)})
$$
(其完整的渐近展开式为$li(x) = \frac{x}{lnx}\sum_{k=0}^\infty\frac{k!}{(lnx)^k}$)

不难验证：
$$
\sum_{i=1}^n\frac{1}{\lg i} \ge \frac{n}{\lg n}
$$
因此
$$
T(n) = \Theta(\frac{n}{lgn})
$$

### j. $T(n)=\sqrt{n}T(\sqrt{n})+n$

#### 方法1

$$
\frac{T(n)}{n}=\frac{\sqrt n}{n} T(\sqrt n)+1= \frac{T(\sqrt n)}{\sqrt n}+1
$$

设$Y(k) = \frac{T(n)}{n}$，得
$$
Y(k)=Y(\sqrt k)+1
$$
令$m = \lg k, k=2^m$，得
$$
Y(2^m)=T(2^{\frac{m}{2}})+1
$$
重命名$S(m)=Y(2^m)$，得
$$
S(m)=S(\frac{m}{2})+1
$$
根据主方法 case2，
$$
a = 1,\ b=2,\ f(m)=1\\
n^{\log_ba} = n^{\log_21}=1
$$
$f(n)$在多项式意义上等于$n^{\log_ba}$

因此，$T(n)=\Theta(\lg m) =\Theta(\lg\lg k)=\Theta(n\lg\lg n)$

#### 方法2

猜测，
$$
T(n)=\Theta(n\lg \lg n)
$$
证明，
$$
\begin{aligned}
T(n)&\le \sqrt{n}c\sqrt{n}\lg \lg \sqrt{n}+n\\
&=cn\lg\lg\sqrt{n}+n\\
&=cn\lg\lg n-cn\lg2+n\\
&=cn\lg\lg n+(1-c\lg 2)n\\
&\le cn\lg\lg n
\end{aligned}
$$
只要取$c\ge\frac{1}{\lg 2}$，不等式成立

同理可证下界



## 4.5

#### a. 

​	与好芯片数量等同的坏芯片可以对好芯片报告坏，对坏芯片报告好，这样好坏最终无法分辨。

#### b. 

##### 步骤1:

​	（若n为奇，则从中拿出一个芯片A）随机两两配对测试

##### 步骤2:

​	仅当互报为好时，任留其中一块，其余情况都扔

​	【讨论原先为奇数的情况】

​	（1）当剩余总数是偶数时，把A放回。此时要么好的芯片数和坏的芯片数一样，A是好的芯片；要么好的芯片比坏芯片多偶数个，此时不论A是好是坏，把它加入集合也能保证好的芯片数大于坏的芯片数。

​	（2）当总数是奇数时，就不放回了，因为好的芯片数必然大于坏的芯片数。

步骤3:

​	重复执行直到只剩1个 

#### c.

$$
T(n)\le T(⌈n/2⌉)+⌊n/2⌋ 
$$

根据主方法，
$$
T(n) =O(n)
$$

## 7.1-1

⟨13,19,9,5,12,8,7,4,21,2,6,11⟩

⟨13,19,9,5,12,8,7,4,21,2,6,11⟩

⟨13,19,9,5,12,8,7,4,21,2,6,11⟩

⟨9,19,13,5,12,8,7,4,21,2,6,11⟩

⟨9,5,13,19,12,8,7,4,21,2,6,11⟩

⟨9,5,13,19,12,8,7,4,21,2,6,11⟩

⟨9,5,8,19,12,13,7,4,21,2,6,11⟩

⟨9,5,8,7,12,13,19,4,21,2,6,11⟩

⟨9,5,8,7,4,13,19,12,21,2,6,11⟩

⟨9,5,8,7,4,13,19,12,21,2,6,11⟩

⟨9,5,8,7,4,2,19,12,21,13,6,11⟩

⟨9,5,8,7,4,2,6,12,21,13,19,11⟩

⟨9,5,8,7,4,2,6,11,21,13,19,12⟩

## References：

对数积分：

https://baike.baidu.com/item/%E5%AF%B9%E6%95%B0%E7%A7%AF%E5%88%86/10413446#4

https://en.m.wikipedia.org/wiki/Logarithmic_integral_function

