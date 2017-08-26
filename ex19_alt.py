def cheese_and_crackers(cheese_count, boxes_of_crackers):
	print "You have %d cheeses!" % cheese_count
	print "You have %d boxes of crackers!" % boxes_of_crackers
	print "Man that's enough for a party!"
	print "Get a blanket.\n"

print "How much cheese do you have?"
amount_of_cheese = int(raw_input())

print "And how much boxes of crackers do you have?"
amount_of_crackerboxes = int(raw_input())

cheese_and_crackers(amount_of_cheese, amount_of_crackerboxes)

