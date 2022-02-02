lottery="hello coders"
print("Choose a character of the world",lottery,"to win the lottery.")
inp=input(" ")
if inp==lottery[0].lower() or inp==lottery[1].lower() or inp==lottery[4].lower() or inp==lottery[6].lower() or inp==lottery[8].lower():
    print("You win the lottery")
else:
    print("You lose the lottery")