import random

ran_num1 = [random.randint(0,10000) for r in xrange(100)] # v1
# ran_num1 = [4,5,3,9,2,7,1]
# ran_num2 = [random.choice([i for i in xrange(10000)]) for r in xrange(10)] # v2 

for i in range(0,len(ran_num1)):
	min = i
	max = i
	for j in range(i+1,len(ran_num1)):
		if ran_num1[j] < ran_num1[min]:
			min = j
	ran_num1[min], ran_num1[i] = ran_num1[i], ran_num1[min]
print ran_num1