import timeit

def t1():
	li = []
	for i in range(10000):
		li.append(i)


def t2():
	li = []
	for i in range(1000):
		li = li + [i]

def t3():
	[i for i in range(1000)]


def t4():
	li = list(range(1000))

def t5():
	li = []
	for i in range(1000):
		li.insert(0,i)
time1 = timeit.Timer("t1()","from __main__ import t1")
time2 = timeit.Timer("t2()","from __main__ import t2")
time3 = timeit.Timer("t3()","from __main__ import t3")
time4 = timeit.Timer("t4()","from __main__ import t4")
time5 = timeit.Timer("t5()","from __main__ import t5")


print("app",time1.timeit(1000),"seconds")
print("ins",time5.timeit(1000),"seconds")
print("[]  ",time2.timeit(1000),"seconds")
print("for  in",time3.timeit(1000),"seconds")
print("list",time4.timeit(1000),"seconds")