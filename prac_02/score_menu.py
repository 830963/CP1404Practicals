import random
def check_score(score ):
    if 0 <= score <= 100:
        if score < 50:
            return "Bad" 
        elif 90 > score >= 50:
            return "Passable" 
        elif score >= 90:
            return "Excellent" 

    else:
        return "Invalid score" 

inp = int(input("Please enter your score "))
print(check_score(inp))



print("Random score " , check_score(random.randint(0,100)))
