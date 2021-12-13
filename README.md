# MCunicode字体放缩

[![GitHub license](https://img.shields.io/github/license/sch246/MCunicode)](https://github.com/sch246/MCunicode/blob/master/LICENSE)
[![standard-readme compliant](https://img.shields.io/badge/readme%20style-standard-brightgreen.svg?style=flat-square)](https://github.com/RichardLitt/standard-readme)

将我的世界的unicode字体格式转化为bitmap格式，并且进行放缩的资源包

## 内容列表

- [背景](#背景)
- [安装](#安装)
- [使用](#使用)
    - [生成器](#生成器)
- [维护者](#维护者)
- [使用许可](#使用许可)

## 背景


我们都知道bitmap和ttf都是可以用height和ascent控制高度和偏移的

如果想要更大的英文字体什么的只需要改这两个参数就行，非常简单

但中文不行，中文在unicode里，而unicode是没有这两个参数的

稍微翻一翻原版资源包就会发现，mc的unicode也是bitmap，甚至和其它bitmap的图片放在一起

所以咱们把legacy_unicode用一堆bitmap替换掉，应该也能显示出来

写脚本替换即可

## 安装


### 这玩意不需要安装)

点击[这里](https://codeload.github.com/sch246/MCunicode/zip/refs/heads/master)下载源代码

然后解压到资源包文件夹就行了

## 使用


默认提供的范围只有1.16的2,3,4,5,6,7,8,9,16,24,32的放大，否则请自己拓展

最简单直接的方式就是打开资源包，assets\size\font\下

随便复制一份

改成你想改的名字,然后把所有的height和ascent都替换了

否则，确保你安装了python

- 仅放缩字体

运行newsize.py

![](https://s4.ax1x.com/2021/12/13/oLgVln.png)

- 放缩并设置偏移

运行newsize_s.py

![](https://s4.ax1x.com/2021/12/13/oLgZyq.png)



### 生成器

本资源包只准备了1.16的unicode图片

但是也可以使用其它同样格式的图片

替换/textures/font和/textures/font_plus，然后重新生成即可

>运行high_png.py可以将/font_plus/下的字体高度变为256格以适应向上偏移，如果要使用newsize_s.py并且载入高度为256的图片，请确保/font_plus/下的图片是处理过的

## 维护者


[@sch246](https://github.com/sch246)

## 使用许可


[TML](LICENSE)
