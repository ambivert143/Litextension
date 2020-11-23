"""
Cho trước 2 số y, x (y > x). Bây h cần tăng x để đạt được giá trị bằng y. Có 2 cách thay đổi giá trị của x:
	- tăng gấp đôi x
	- bớt x đi 1 đơn vị
Tìm số bước nhỏ nhất để x = y.
"""


"""leaves = {x: []}

def bfs(leaves):
	pass
while y not in leaves:
	new_leaves = {}
	for x in leaves:
		new_leaves[2*x] = leaves[x] + ['*2']
		new_leaves[x-1] = leaves[x] + ['-1']
	leaves = new_leaves

print(leaves[y])"""


"""def timbuoc(x, y):
	if x == y:
		return x
	elif (x < y ):
		return 2*x
	else:
		return (x-1)"""

def main(x, y):
	leaves = {x: []}
	while y not in leaves:
		new_leaves = {}
		for x in leaves:
			new_leaves[2*x] = leaves[x] + ['*2']
			new_leaves[x-1] = leaves[x] + ['-1']
		leaves = new_leaves
	print(leaves[y])