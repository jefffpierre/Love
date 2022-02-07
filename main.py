# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
combine = name1 + name2
lower = combine.lower()

t = lower.count("t")
r = lower.count("r")
u = lower.count("u")
e = lower.count("e")

true = t + u + r + e

l = lower.count("l")
o = lower.count("o")
v = lower.count("v")
e = lower.count("e")

love = l + o + v + e

score = int(str(true) + str(love))

if (score < 10) or (score > 90):
    print(f"Your score is {score}, you go together like coke and mentos.")
elif (score >= 40) and (score <= 50):
    print(f"Your score is {score}, you are alright together.")
else:
    print(f"Your score is {score}.")

