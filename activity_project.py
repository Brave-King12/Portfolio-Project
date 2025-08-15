activity = input("Do you want to eat or play? ")

if activity == "play":
    sports = input("Do you want to play badminton or swimming? ")
    
    if sports == "badminton":
        age = int(input("How old are you? "))
        
        if 11 <= age < 30:
            print("Go to the traning ground.") 
        elif age < 11:
            print("You are too young to play badminton.")
        else:
            print("You are too old to play badminton.")
    
    elif sports == "swimming":
        print("Go to the swimming pool.")

    else:
        print("Go to the sports room and decide.")
        
elif activity == "eat":
    food = input("Do you prefer Burmese food or European Food ? ")
    
    if food == "Burmese":
        Burmese_food = input("Do you want Mohinga or Coconut Noodle? ")
        print(f"Your order for {Burmese_food} is confirmed.")
    
    elif food == "European":
        order_steak = input("Only Beef Steak are available. Do you want to order? (yes/no) ")
        
        if order_steak == "yes":
            print("Your steak order is confirmed.")
        else:
            print("Thank you, See you next time.")
    
    else:
        print("Invalid choice. Please choose either Burmese or European Foods.")
        
else:
    print("Invalid choice. Please choose either 'eat' or 'play'.")
