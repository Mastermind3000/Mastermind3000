print("Welcome to WhoAmI")
print("rate the following statements from 1 to 10")
q1=10-int(input("Im often dissatisfied with my self "))
q2=10-int(input("Its hard for me to make friends "))
q3=10-int(input("I feel extremly anxious infront of others "))
test_score=q1+q2+q3



print (test_score)
personality=int(input("If your testscore is higher than 15 type 1 if not type 2 "))

if personality==2:
    print("introvert")
else:
    print("extrovert")





