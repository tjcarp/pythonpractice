#local and global variables with same name
def spam():
	eggs = "spam local"
	print(eggs) 
	
def bacon():
	eggs = "bacon local"
	print(eggs)
	spam()
	print(eggs)
	
eggs = "global"
bacon()
print(eggs)