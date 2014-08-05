WubiLetterDistribution
---

一个用python写的五笔字母频率分布统计小脚本，可以统计用五笔全拼输入一段文本时需要按下各个键的频率分布。

####文件说明
- **stat.py** 主程序
- **wubi86.dict.txt** 五笔86版字库
- **pinyin_simp.dict.txt** 拼音字库
- **text.txt** 测试文本，《世界上下五千年——现代卷》，约18万个汉字

*字库均提取自[小狼毫][1]并经处理，只保留需要的数据*

[1]:http://code.google.com/p/rimeime "小狼毫项目主页"


*Notice: This script is used for entertainment purpose only*

Output
---
####Using Wubi
	Statistics:
	Dictinary: wubi86.dict.txt
	G	6.857%
	F	6.699%
	T	6.476%
	W	6.325%
	D	5.238%
	J	5.014%
	R	4.743%
	H	4.680%
	U	4.631%
	K	4.095%
	Y	4.063%
	N	4.010%
	P	3.545%
	Q	3.530%
	M	3.504%
	B	3.404%
	L	3.313%
	A	3.290%
	C	3.162%
	I	3.005%
	E	2.824%
	S	2.233%
	X	2.067%
	V	1.856%
	O	1.437%
	Z	0.000%

####Using Pinyin
	Statistics:
	Dictinary: pinyin_simp.dict.txt
	I	13.352%
	N	11.770%
	A	10.203%
	E	8.196%
	U	7.885%
	G	6.829%
	H	6.659%
	O	5.429%
	D	4.017%
	Z	3.440%
	J	2.835%
	S	2.741%
	Y	2.639%
	L	2.215%
	B	1.687%
	X	1.413%
	T	1.371%
	M	1.367%
	R	1.177%
	C	1.100%
	F	0.951%
	Q	0.858%
	W	0.812%
	K	0.698%
	P	0.294%
	V	0.061%
