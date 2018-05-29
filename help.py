def help():
    print ("What type of help do you need?")
    print ("1. Backstory")
    print ("2. Objective")
    print ("3. Pokemon")
    print ("4. Sidequests")
    command = input()
    if command == '1':
        for dialogue in gameinfo1:

