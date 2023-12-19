import datetime
import random
import tkinter as tk


def get_date_string(days_left):
  """Returns a string in the format month/day/year given the number of days left."""

  current_date = datetime.date.today()
  date_in_future = current_date + datetime.timedelta(days=days_left)

  return date_in_future.strftime("%m/%d/%Y")

# Other functions in the code go here

#create a function called status(). It should print the food you have left by accessing the global food variable. Same thing for health, days_left, and distance_left
def status():
    global food_left, health_left, days_left, distance_left
    print(food_left)
    print(health_left)
    print(days_left)
    print(distance_left)

# Create function to update game status
def update_game_status():
    global game_status_text, distance_left, food_left, health_left, days_left
    date_string = get_date_string(days_left)
    game_status_text.set(f"Distance left: {distance_left}, Food left: {food_left}, Health: {health_left}, Date: {date_string}")


#create a function called travel(). No parameters. Should subtract a random amount (between 10 and 15) from the global distance_left variable. It should also consume 5 lb of food and decrease the days_left
def travel():
    global distance_left, food_left, days_left
    distance_left -= random.randint(10,15)
    food_left -= 5
    days_left -= 1
    update_game_status()

#create a function called rest(). No parameters. Should add 1 to your global health variable. It should also consume 5 lb of food and decrease the days_left
def rest():
    global health_left, food_left, days_left
    health_left += 1
    food_left -= 5
    days_left -= 1
    update_game_status()

#create a function called hunt(). No parameters. Should add a random lb of food (between 0 and 20) to the global food variable. It should also consume 5 lb of food and decrease the days_left
def hunt():
    global food_left, days_left
    food_obtained = random.randint(0,20)
    food_left += food_obtained
    food_left -= 5
    days_left -= 1
    print(f"You obtained {food_obtained} lb of food.")
    update_game_status()

#create a function called check_food(). No parameters. Checks if the user has food. If the user does not have food, decrease health by 1. 
def check_food():
    global food_left, health_left

    if food_left <= 0:
        health_left -= 1
        print("You don't have enough food. Your health decreases by 1.")
    update_game_status()


#create a function called check_win(distance_left,food,health,days_left). If there's no distance left to go, and the user has at least 1 health and has not run out of days, return True. Else, return False. 
def check_win():
    return distance_left <= 0 and health_left >= 1 and days_left >= 1

#create a function called check_lose(distance_left,food,health,days_left). If health is less than 1 or days_left is less than 1, return True. Else, return False
def check_lose():
    return health_left < 1 or days_left < 1

#quit function
def quit_game():
    global gameover, app 
    gameover = True
    app.destroy()

#create a function called help(). It should print the different options the user has and what each option does. 
def help():
    print("Options:")
    print("  - travel: Travel a random distance and consume food")
    print("  - rest: Rest and increase health while consuming food")
    print("  - hunt: Hunt for food and consume food")
    print("  - status: Print the remaining food, health, distance, and days")
    print("  - help: Print available options")
    print("  - quit: Quit the game")



if __name__ == '__main__':
    #In this space, print some directions for the user along with a welcome message.
    print('Welcome to the Oregon Trail! You have 305 days to get to Oregon.')

    x = input("Type 'Start' to begin: ")

    if x != "Start":
        print("Bye")
    else:
        distance_left = 2
        food_left = 50
        health_left = 5
        days_left = 305
        gameover = False
        # GUI 
        app = tk.Tk()
        app.title("Oregon Trail")
      # Create game status text field
        game_status_text = tk.StringVar()
        game_status_label = tk.Label(app, textvariable=game_status_text)
        game_status_label.pack()

      # Create date string label
        date_string_label = tk.Label(app, textvariable=game_status_text)
        date_string_label.pack()

      # Update game status text
        update_game_status()

        # Create action buttons
        travel_button = tk.Button(app, text="Travel", command=travel)
        travel_button.pack()

        rest_button = tk.Button(app, text="Rest", command=rest)
        rest_button.pack()

        hunt_button = tk.Button(app, text="Hunt", command=hunt)
        hunt_button.pack()

        status_button = tk.Button(app, text="Status", command=status)
        status_button.pack()

        quit_button = tk.Button(app, text="Quit", command=quit_game)
        quit_button.pack()

        # Create game status text field
        game_status_text = tk.StringVar()
        game_status_label = tk.Label(app, textvariable=game_status_text)
        game_status_label.pack()

        update_game_status()

        while not gameover:
            user = input("\nWhat do you want to do with your turn? ")
            if user == "travel" or user == "Travel":
                travel()
            elif user == "rest" or user == "Rest":
                rest()
            elif user == "hunt" or user == "Hunt":
                hunt()
            elif user == "help" or user == "Help":
                help()
            elif user == "quit" or user == "Quit":
                quit_game()
            elif user == "status" or user == "Status":
                status()
            else:
                print("Invalid option. Type 'help' to check the available options.")

            if check_win():
                print("\nCongratulations! You have reached Oregon!")
                gameover = True
            elif check_lose():
                print("\nYou lost the game. Better luck next time!")
                gameover = True

            check_food()
            app.update()
            update_game_status()

        app.mainloop()