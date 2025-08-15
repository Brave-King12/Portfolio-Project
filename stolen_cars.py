stolen_cars = ["2022wx1678", "Joe Carthy", "08612356",
               "2021d5667", "Mary Smith", "087889988",
               "2023kl3434", "John Doe", "0798765432",
               "2019bb2345", "John Paw", "0709988776"]
while True:
    user_input = input("Enter car registration, owner name, or phone number ('Q' or 'q' to quit): ").lower()
    if user_input == 'q':
        break
    found = False
    i = 0
    while i < len(stolen_cars):
        if user_input in [stolen_cars[i].lower(), stolen_cars[i+1].lower(), stolen_cars[i+2].lower()]:
            print(f"Car stolen: \nRegistration: {stolen_cars[i]}\nOwner: {stolen_cars[i+1]}\nPhone: {stolen_cars[i+2]}")
            found = True
            break
        i += 3
    if not found:
        print("Car not stolen.")