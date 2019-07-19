class Desk:  ##第一個字要大寫
	def __init__(self, color, size , rename):
		self.color = color  #第一個.color的color是自己(self)的屬性，第二個 =color的color是參數，對應上一行(__init__)的color
		self.size = size
		self.name = "DD" #增加屬性 
		self.rename = rename
		print('我被創造出來了')

	def recolor(self, re_color): #一個功能 ，裡面有兩個參數，第一個self會自己投掉，第二個要給他參數
		self.color = re_color

	def cut(self , lenx):  #一個功能
		self.lenx = lenx

	def play(self , countx):   #這個play 叫啥？  #一個功能
		self.countx = countx


d = Desk("blue" , 'big', 'Tan')
d.recolor("red") #d.recolor , Desk 這個class裡有一個叫做recolor的功能
d.cut(100)
d.play(50)

print("color = " , d.color)
print("size = ", d.size)
print("被修剪了",d.lenx,"公分")
print(d.countx)
print(d.name)
print(d.rename)