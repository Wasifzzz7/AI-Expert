print("Welcome to WasifAI")
print("Hey I'm a ChatBOT Developed by Wasif! What is Your name?")

name = input("> ")

print(f" Nice to meet you {name}")
print("How are you feeling today (good/bad)?")

feelings = input("> ")

if feelings == "good":
    print(f"Glad to hear that {name}")
elif feelings == "bad":
    print(f"I'm sorry to hear that! Hope things will be better soon")
else:
    print("It can happen somethimes") 

print("What is your favourite sports? (football/cricket)")

sports = input("> ")

print(f"Wow! That's great I love {sports} too!")

if sports == "football":
    print("Who is your favourtie footballer?")
elif sports == "cricket":
    print("Who is your favourite cricketer?")

favouriteplayer = input("> ")

print(f"Wow! He is great I like {favouriteplayer} too")
