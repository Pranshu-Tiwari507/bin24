environment = {"A": "Dirty", "B": "Dirty"}
location = "A"
steps = 10
print("Initial Environment:", environment)
print("Initial Location:", location)
for i in range(steps):
    print("\nStep", i + 1)
    if environment[location] == "Dirty":
        print("Action: SUCK")
        environment[location] = "Clean"
    else:
        if location == "A":
            print("Action: Move to B")
            location = "B"
        else:
            print("Action: Move to A")
            location = "A"
    print("Current Location:", location)
    print("Environment:", environment)
print("\nFinal Environment:", environment)
print("Final Location:", location)
print("Program Ended.")


# environment = {"A": "Dirty", "B": "Dirty"}
# location = "A"
# print("Initial Environment:", environment)
# print("Initial Location:", location)
# step = 0
# while "Dirty" in environment.values():
#     step += 1
#     print("\nStep", step)

#     if environment[location] == "Dirty":
#         print("Action: SUCK")
#         environment[location] = "Clean"
#     else:
#         if location == "A":
#             print("Action: Move to B")
#             location = "B"
#         else:
#             print("Action: Move to A")
#             location = "A"
#     print("Current Location:", location)
#     print("Environment:", environment)
# print("\nAll squares are clean. Stopping.")
# print("Final Environment:", environment)
# print("Final Location:", location)
# print("Total steps taken:", step)