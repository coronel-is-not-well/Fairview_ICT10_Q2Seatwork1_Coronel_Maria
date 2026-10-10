from pyscript import document,display

def Submit(e):

    Members = ["Sabine Shark", "Dylan Dove", "Tanya Tiger", "Ramone Ram", "Kirsten Kangaroo", "Atrisha Alpaca", "Lance Lion", "Sean Seal", "Diego Dog", "Maria Mouse", "Edrian Elephant", "Eliana Eagle", "Raven Raven", "Annika Ant", "Amanda Axolotl", "Sunny Sheep", "Rodolfo Rat", "Maiselle Macaw", "Matt Monkey", "Andre Armadillo", "Anissa Albatross", "Frances Fox", "Ynigo Yak", "Zack Zebra", "Rohan Rabbit", "Jhoana Jaguar"] # names of 10 Ruby <3

    NameF = document.getElementById("FName").value # getting the value of the input of the first name

    NameL = document.getElementById("LName").value # getting the value of the input of the first name

    Members_new = NameF.capitalize() + " " + NameL.capitalize() # combining them and making them capitalized with a space


    Message = f"Congratulations {Members_new}! You are part of the Maria Mouse Clubhouse." if Members_new in Members else f"Sorry {Members_new}, your name is not on the list." # checking if the members new is in the list of members

    display(Message, target="output1") # making it seen

