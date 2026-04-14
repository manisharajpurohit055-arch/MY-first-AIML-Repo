#condition
print(2<3)
print(2==3)
print(9!=8)
print(8<9)
print(8<=8)
print(8>66)
print(99>=16)

#conditional statement 
#if statement 
def evaluate_temp(temp):
    msg="normal"
    if(temp>38):
        msg="fever!"
        return msg
#calling func
print(evaluate_temp(108))

#if else statemnet 
def evalu_temp(temp):
    if(temp<38):
        msg="Normal temp"
    else:
        msg="fever!"
    return msg
print(evalu_temp(39))
print(evalu_temp(32))

#if elif(if else) else statement

def e_temp(temp):
    if(temp>38):
        msg="fever!"
    elif(temp>35):
        msg="normal temp"
    else:
        msg="low temp"
    return msg
print(e_temp(30))
