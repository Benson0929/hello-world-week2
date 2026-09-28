# Assignment 3 - Story Algorithm

# User inputs
name = input("What is your name? ")
activity = input("What activity did you do? ")
friendCount = int(input("How many friends were with you? "))
occasion = input("What was the occasion? ")
funAnswer = input("Was it fun? (yes/no) ")

# Variables with different data types
wasFun = (funAnswer == "yes")

# Convert the number to a string for concatenation
friendCountString = str(friendCount)

# Create the story using concatenation
story = name + " had a " + activity + " with " + friendCountString + " friends during the " + occasion + "."

# Output
print(story)
print("Was it fun?", wasFun)