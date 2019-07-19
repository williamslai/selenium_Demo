class Player:
	def __init__(self, name, ap, hp):
		print("我的名字是", name, "& 攻擊力是", ap)
		self.ap = ap
		self.name = name
		self.hp = hp

	def attack(self, target):
		print(self.name , "attack" , target.name)
		target.hp = target.hp - self.ap

	def heal(self, target):
		#self.target = target
		print(self.name, "heal", target.name)
		#print("我是self(p1)",self.hp)
		self.hp = target.hp + self.ap
		#target.hp = target.hp + self.ap

##上面寫要用的功能
##============
##下面用上面寫的功能


p1 = Player('勇者', 1, 100)
p2 = Player("魔王", 2, 100)
p1.attack(p2)#P1攻擊P2
print(p2.hp,"剩餘血量等於", p2.hp) #印出P2被P1攻擊後的剩餘血量。

p2.attack(p1)
print(p1.name,"剩餘血量等於", p1.hp)

p1.heal(p1) # p1生命力 = p2的生命力 + p1的ap，100+1
p2.heal(p2) # p2生命力 = p1的生命力 + p2的ap，100+2
print(p1.name,"增加後的血量等於",p1.hp)#101
print(p2.name,"增加後的血量等於",p2.hp)#102

