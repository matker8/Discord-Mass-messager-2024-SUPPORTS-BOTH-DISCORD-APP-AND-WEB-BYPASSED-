import pyautogui
import time

def autotyper():
    # Get the text to be sent
    text = input("Enter the text you want to send: ")

    # Get the number of times to send the text
    num_times = int(input("Enter the number of times to send the text: "))

    # Get the delay between messages in seconds
    delay = float(input("Enter the delay between messages in seconds: "))

    # Confirm the settings
    print(f"Text: {text}")
    print(f"Number of times: {num_times}")
    print(f"Delay: {delay} seconds")
    confirm = input("Confirm? (y/n): ")

    if confirm.lower() == "y":
        # Switch to the Discord window
        print("Switching to Discord window...")
        pyautogui.press('win')
        pyautogui.typewrite('discord')
        pyautogui.press('enter')
        time.sleep(2)

        # Send the text
        for _ in range(num_times):
            pyautogui.typewrite(text)
            pyautogui.press('enter')
            time.sleep(delay)

        print("Done!")

    else:
        print("Cancelled.")

def raid_discord_server():
    # Get the number of users to raid with
    num_users = int(input("Enter the number of users to raid with: "))

    # Get the delay between users in seconds
    delay = float(input("Enter the delay between users in seconds: "))

    # Confirm the settings
    print(f"Number of users: {num_users}")
    print(f"Delay: {delay} seconds")
    confirm = input("Confirm? (y/n): ")

    if confirm.lower() == "y":
        # Switch to the Discord window
        print("Switching to Discord window...")
        pyautogui.press('win')
        pyautogui.typewrite('discord')
        pyautogui.press('enter')
        time.sleep(2)

        # Raid the server
        for _ in range(num_users):
            pyautogui.typewrite("@everyone")
            pyautogui.press('enter')
            time.sleep(delay)

        print("Done!")

    else:
        print("Cancelled.")

def main_menu():
    print("Main Menu:")
    print("1. Spam a Discord server")
    print("2. Raid a Discord server")
    print("3. Quit")

    choice = input("Enter your choice: ")

    if choice == "1":
        autotyper()
    elif choice == "2":
        raid_discord_server()
    elif choice == "3":
        print("Goodbye!")
    else:
        print("Invalid choice. Please try again.")
        main_menu()

if __name__ == "__main__":
    main_menu()