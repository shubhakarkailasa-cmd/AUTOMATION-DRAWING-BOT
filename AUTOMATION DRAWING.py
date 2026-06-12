import pyautogui
import time

time.sleep(4)

print("Welcome to Automate Diagram...")

position = []

while True:
    choice = input("""
Enter the choice:
1) RECORD
2) REPLAY
3) VIEW POSITION
4) EXIT
5) SAVE THE POSITION TO FILE

Choice: """)

    if choice == "1":
        while True:
            user = input("Want to take position? (yes/no): ")

            if user.lower() != "yes":
                break

            load = pyautogui.position()
            print(load)
            position.append(load)

    elif choice == "2":
        if not position:
            print("No positions are recorded to replay.")
        else:
            print("Replaying positions...")
            for pos in position:
                pyautogui.dragTo(pos[0], pos[1], duration=2)

    elif choice == "3":
        if not position:
            print("No positions recorded.")
        else:
            print(position)

    elif choice == "4":
        print("Exiting...")
        break

    elif choice == "5":
        with open("data.txt", "w") as file:
            for pos in position:
                file.write(f"{pos[0]},{pos[1]}\n")

        print("Positions saved successfully.")

    else:
        print("Invalid input.")