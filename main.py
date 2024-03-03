#homework page 58
def fc(x):
   if x < 0 :
       return ("error")
   else:
       return x*fc (x-1)
x = int(input("x:"))

#toturial
#term one
print("term 1")
aes1 = int(input(" score aes1"))
maths1 = int(input("score maths1"))
physics1 = int(input("score physics1"))
computer_programming1 = int(input("score computer_programming1"))



aes2 = int(input("score aes "))
maths2 = int(input("score maths2  "))
physic2 = int(input("score physic2 "))
computer_programming2 = int(input("score computer_programming2"))




print("term 3")

aes3 = int(input(" score aes3 "))
maths3 = int(input(" score maths3 "))
physics3 = int(input(" score physics3 "))
creative_design = int(input("score creative_design "))

avg = (aes1+maths1+physics1+computer_programming1+aes2+maths2+physic2+computer_programming2+aes3+maths3+physics3+creative_design)/12
avgmath= (maths2+maths3)/2

if aes1 > 40 and maths1 > 40 and physics1 > 40 and computer_programming1 > 40 and aes2 > 40 and maths2 > 40 and physic2 > 40 and computer_programming2 > 40 and aes3 > 40 and maths3 > 40 and physics3 > 40 and creative_design > 40 :
    print("you pass")
elfi:
    print("you fail")