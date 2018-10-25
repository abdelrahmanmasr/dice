def authentication(username, password):
    print("Inside authentication function")
    with open("credintials.txt") as file:
        saved_credintials = file.readlines()
        print (saved_credintials)
    for saved_credintial in saved_credintials:
        name = username +" " +password +"\n"
        if name == saved_credintial:
            print("authenticated")

authentication("mohammed", "mohammed234")

authentication("Abdelrahman", "Daabis")
list = [1, 2, 3]



















# TODO: create a function that returns a random number between 1 and 6. use random module in python
