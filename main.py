print("** Welcome to the Convenience Store Chatbot! **")
print("   -----------------------------------------")
name = input("What might your name be? ")

age = input("And how old are you? ")

print("Good day " + name + ", It's a pleasure to meet you!")
print("")
print("Here are some options you may choose from: ")
print("1. Store Hours")
print("2. Store Locations")
print("3. Avaliable Items")
print("4. Exit Chatbot")

user_choice = int(input("Now, what may I help you with " + name + "? "))

if user_choice == 4:
    print("Very well. See you later!")
