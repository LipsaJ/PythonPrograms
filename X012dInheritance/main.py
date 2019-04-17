from enemy import VampireKing
#
# random_monster = Enemy("Basic", 10, 2)
# print(random_monster)
# random_monster.take_damage(2)
# print(random_monster)
# random_monster.take_damage(7)
# print(random_monster)
# random_monster.take_damage(9)
# print(random_monster)
#
# from enemy import Troll, Vampire
# # this is overloading , first one is having no argument, n3xt 3 and last one 2
# # in java you write three constructors - overloaded method but in python it doesnt have that concept
# # tha last writen method is considered
#
# ugly_troll = Troll("Pug")
# print("ugly troll - {}".format(ugly_troll))
#
# another_troll = Troll("Ugh")
# print("Another troll - {}".format(another_troll))
#
# talented_troll = Troll("fig")
# print(talented_troll)
#
# ugly_troll.grunt()
# another_troll.grunt()
# talented_troll.grunt()
#
# ugly_troll.take_damage(2)
# print(ugly_troll)
#
# liff_v = Vampire("Liff")
# print(liff_v)
# hanz_v = Vampire("Hanzz")
# print(hanz_v)
#
# liff_v.take_damage(3)
# hanz_v.take_damage(13)
# print(hanz_v)
#
# print("-"*40)
# another_troll.take_damage(30)
# print(another_troll)
#
# while liff_v._alive:
#     # if not liff_v.dodges():
#     liff_v.take_damage(1)
#     print(liff_v)

vamp = VampireKing("Drac")
print(vamp)

vamp.take_damage(14)
print(vamp)