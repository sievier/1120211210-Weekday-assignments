friend_list=["马云","马化腾","王健林","李彦宏"]
print("=========2021年生日========")
for friend in friend_list:
	print("{},谢谢你给我过生日".format(friend))
print()

print("=========2022年生日========")
friend_list.append("许家印")
for friend in friend_list:
	print("{},谢谢你给我过生日".format(friend))