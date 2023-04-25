from guitar import Guitar

guitar1 = Guitar("Gibson L-5 CES", 1922, 16035.40)
guitar2 = Guitar("Another Guitar", 2013, 500)
assert guitar1.get_age() == 101
assert guitar2.get_age() == 10
print("Gibson L-5 CES get_age() - Expected 101. Got", guitar1.get_age())
print("Another Guitar get_age() - Expected 10. Got", guitar2.get_age())


assert guitar1.is_vintage() == True
assert guitar2.is_vintage() == False
print("Gibson L-5 CES is_vintage() - Expected True. Got", guitar1.is_vintage())
print("Another Guitar is_vintage() - Expected False. Got", guitar2.is_vintage())
