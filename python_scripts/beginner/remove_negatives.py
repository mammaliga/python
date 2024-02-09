
def remove_negatives(lst):
	return list(filter(lambda num: num >= 0, lst))


print(remove_negatives([-1,3,4,-99]))     #[3,4]

print(remove_negatives([-7,0,1,2,3,4,5]))      #[0, 1, 2, 3, 4, 5]

print(remove_negatives([50,60,70]))   #[50,60,70]