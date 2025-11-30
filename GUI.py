import tkinter as tk
from game_data import GameData

#This GUI is configured to change frames according to the button presses from the player
#For each menu a frame will be created by a function and will receive his respective widgets, buttons + labels
#For each frame a function a function will be definede in order to change the frames dinamically

#this GUI was created following the tutorial "Creating Multiple Frames in Tkinter" avaiable at https://www.youtube.com/watch?v=SDNoklJcb30
#and "Create Graphical User Interfaces With Python And TKinter" avaible at https://www.youtube.com/watch?v=yQSEXcf6s2I&list=PLCC34OHNcOtoC6GglhF3ncJ5rLwQrLGnV

#This global variable will control which frame is the active frame
global current_frame


#the following functions will display each frame for each menu and the game
#the hide the current frame and the intended frame is showin, which in turns becomes the current frame
def show_main_menu():
    """This function shows the main menu where the game modes are displayed"""

    global current_frame 
    current_frame.pack_forget()
    main_menu.pack()
    current_frame = main_menu 

def show_random_nouns_frame():
    """This function shows the random game menu where the player chooses 
    how many random nouns to play"""

    global current_frame
    current_frame.pack_forget()
    random_nouns_frame.pack()
    current_frame = random_nouns_frame

def show_suffix_frame():
    """This function shows the random game menu where the player chooses
    which suffix to play"""

    global current_frame
    current_frame.pack_forget()
    suffix_frame.pack()
    current_frame = suffix_frame

def show_game_frame():
    """This function shows the random game menu where the player plays 
    the game according to type of game chosen"""

    global current_frame
    current_frame.pack_forget()
    game_frame.pack()
    current_frame = game_frame

def reset_game_frame():
    "This function clear all widgets from the game_frame"

    for widget in game_frame.winfo_children():
        widget.destroy()

#Creation of the main window
root = tk.Tk()

#Creation of the frames for each screen
main_menu = tk.Frame(root)
random_nouns_frame = tk.Frame(root)
suffix_frame = tk.Frame(root)
game_frame = tk.Frame(root)

def create_main_menu():
    """this function creates the main menu where the type of game is chosen"""

    #Top label: welcoming the player
    tk.Label(main_menu, text="Welcome to the Der Die Das Game!", font=('Arial', 18)).pack()

    tk.Label(main_menu, text="Choose your type of game:", font=('Arial', 18)).pack()

    #Buttons: choose the type of game
    tk.Button(main_menu, text="Random Nouns", font=('Arial', 16), command=show_random_nouns_frame).pack()

    tk.Button(main_menu, text="Nouns by Suffix", font=('Arial', 16), command=show_suffix_frame).pack()

    tk.Button(main_menu, text="100 Most Used Nouns", font=('Arial', 16), command=lambda: [create_game_frame('most_used', quantity=100, plays=10), show_game_frame()]).pack()

    tk.Button(main_menu, text="500 Most Used Nouns", font=('Arial', 16), command=lambda: [create_game_frame('most_used', quantity=500, plays=10), show_game_frame()]).pack()

    tk.Button(main_menu, text="1000 Most Used Nouns", font=('Arial', 16), command=lambda: [create_game_frame('most_used', quantity=1000, plays=10), show_game_frame()]).pack()

    tk.Button(main_menu, text="Survive", font=('Arial', 16), command=lambda: [create_game_frame('survive'), show_game_frame()]).pack()


def create_random_nouns_frame():
    """This function creates a frame to choose a quantity of random games to play"""

    #Top label: instruction 
    tk.Label(random_nouns_frame, text="Choose the number of nouns: ", font=('Arial', 18)).pack()

    #Buttons: shows quantity of nouns to be played
    tk.Button(random_nouns_frame, text="10", font=('Arial', 16), command=lambda: [create_game_frame('random', plays=10), show_game_frame()]).pack()
    
    tk.Button(random_nouns_frame, text="20", font=('Arial', 16), command=lambda: [create_game_frame('random', plays=20), show_game_frame()]).pack()

    tk.Button(random_nouns_frame, text="30", font=('Arial', 16), command=lambda: [create_game_frame('random', plays=30), show_game_frame()]).pack()

    tk.Button(random_nouns_frame, text="40", font=('Arial', 16), command=lambda: [create_game_frame('random', plays=40), show_game_frame()]).pack()

    tk.Button(random_nouns_frame, text="50", font=('Arial', 16), command=lambda: [create_game_frame('random', plays=50), show_game_frame()]).pack()


def create_suffix_frame():
    """This function creates a frame to choose which word suffix to play"""

    #Top label: instructs the player to choose
    tk.Label(suffix_frame, text="Choose the suffix to play:", font=('Arial', 18)).pack(pady=10)

    #Creation of subframes to organise the suffixes
    row1 = tk.Frame(suffix_frame)
    row1.pack(fill='x')
    row2 = tk.Frame(suffix_frame)
    row2.pack(fill='x')
    row3 = tk.Frame(suffix_frame)
    row3.pack(fill='x')

    #1st row: 5 buttons
    tk.Button(row1, text="-a", font=('Arial', 16), command=lambda: [create_game_frame('suffix', plays=10, suffix='a'), show_game_frame()]).pack(side='left', expand=True, fill='x', padx=2, pady=5)
    tk.Button(row1, text="-ant", font=('Arial', 16), command=lambda: [create_game_frame('suffix', plays=10, suffix='ant'), show_game_frame()]).pack(side='left', expand=True, fill='x', padx=2, pady=5)
    tk.Button(row1, text="-anz", font=('Arial', 16), command=lambda: [create_game_frame('suffix', plays=10, suffix='anz'), show_game_frame()]).pack(side='left', expand=True, fill='x', padx=2, pady=5)
    tk.Button(row1, text="-ast", font=('Arial', 16), command=lambda: [create_game_frame('suffix', plays=10, suffix='ast'), show_game_frame()]).pack(side='left', expand=True, fill='x', padx=2, pady=5)
    tk.Button(row1, text="-chen", font=('Arial', 16), command=lambda: [create_game_frame('suffix', plays=10, suffix='chen'), show_game_frame()]).pack(side='left', expand=True, fill='x', padx=2, pady=5)
    

    #2nd row: 5 buttons
    tk.Button(row2, text="-ei", font=('Arial', 16), command=lambda: [create_game_frame('suffix', plays=10, suffix='ei'), show_game_frame()]).pack(side='left', expand=True, fill='x', padx=2, pady=5)
    tk.Button(row2, text="-ich", font=('Arial', 16), command=lambda: [create_game_frame('suffix', plays=10, suffix='ich'), show_game_frame()]).pack(side='left', expand=True, fill='x', padx=2, pady=5)
    tk.Button(row2, text="-icht", font=('Arial', 16), command=lambda: [create_game_frame('suffix', plays=10, suffix='icht'), show_game_frame()]).pack(side='left', expand=True, fill='x', padx=2, pady=5)
    tk.Button(row2, text="-il", font=('Arial', 16), command=lambda: [create_game_frame('suffix', plays=10, suffix='il'), show_game_frame()]).pack(side='left', expand=True, fill='x', padx=2, pady=5)
    tk.Button(row2, text="-ma", font=('Arial', 16), command=lambda: [create_game_frame('suffix', plays=10, suffix='ma'), show_game_frame()]).pack(side='left', expand=True, fill='x', padx=2, pady=5)

    #3rd row: 5 buttons
    tk.Button(row3, text="-or", font=('Arial', 16), command=lambda: [create_game_frame('suffix', plays=10, suffix='or'), show_game_frame()]).pack(side='left', expand=True, fill='x', padx=2, pady=5)
    tk.Button(row3, text="-tel", font=('Arial', 16), command=lambda: [create_game_frame('suffix', plays=10, suffix='tel'), show_game_frame()]).pack(side='left', expand=True, fill='x', padx=2, pady=5)
    tk.Button(row3, text="-um", font=('Arial', 16), command=lambda: [create_game_frame('suffix', plays=10, suffix='um'), show_game_frame()]).pack(side='left', expand=True, fill='x', padx=2, pady=5)
    tk.Button(row3, text="-ur", font=('Arial', 16), command=lambda: [create_game_frame('suffix', plays=10, suffix='ur'), show_game_frame()]).pack(side='left', expand=True, fill='x', padx=2, pady=5)
    tk.Button(row3, text="-us", font=('Arial', 16), command=lambda: [create_game_frame('suffix', plays=10, suffix='us'), show_game_frame()]).pack(side='left', expand=True, fill='x', padx=2, pady=5)
    
game_data = GameData()

#game frame 
def create_game_frame(game_mode= str, **kwargs):
    """This function creates the frame for the game to be played and controls the 
    progress of the game according with the type of game"""

    current_index = 0 
    streak = 0 

    #creation of the list of nouns according to the type of game
    nouns_list = game_data.create_game_nouns_list(game_mode, plays= kwargs.get('plays'), suffix= kwargs.get('suffix'))

    current_noun = nouns_list[current_index]
    
    #Top Label: instruction to the player
    tk.Label(game_frame, text="Nominativ: Choose the correct article: ", font=('Arial', 18)).pack()
    
    noun_label = tk.Label(game_frame, text=current_noun[1], font=('Arial', 18))
    noun_label.pack()

    def disable_buttons():
        """This function disable all buttons"""
        der_button.config(state='disabled')
        die_button.config(state='disabled')
        das_button.config(state='disabled')
        hint_button.config(state='disabled')
    
    #nested function to check if the answer matches the article of the noun
    def button_click(response):
        """This function to check the player's answer after pressing Der, Die or Das Button and advances the game"""
        nonlocal current_index, current_noun, streak

        if response == game_data.convert_genus_to_article(current_noun[0]): #(e.g. 'Das' == 'Das' ??)
            result_label.config(text="That's Correct!", fg="green")
            hint_label.config(text="")
            streak += 1
            if game_mode == 'survive':
                streak_label.config(text=f'Streak: {streak}')
        else:
            result_label.config(text=f"Wrong... The correct article is: {game_data.convert_genus_to_article(current_noun[0])}", fg="red")
            hint_label.config(text="")
            if game_mode == 'survive':
                #Player did not survive...
                noun_label.config(text="")
                result_label.config(text="Game Over", fg="blue")
                streak_label.config(text=f'Streak {streak}')
                hint_label.config(text="")
                disable_buttons()
        
        #increses to proceed to the next noun
        current_index += 1
        
        #check if there are more nouns and update with the next noun
        if current_index < len(nouns_list):
            current_noun = nouns_list[current_index]
            noun_label.config(text=current_noun[1])
        else:
            #List of nouns is finishedc
            streak_label.config(text=f'{game_data.generate_game_conclusion_message(streak, nouns_list)} Result: {streak}/{len(nouns_list)}', fg="blue")
            
            disable_buttons()

    #Buttons: all buttons call the nested function button_click, passing Der, Die or Das as a response
    der_button = tk.Button(game_frame, text="Der", font=('Arial', 16), command=lambda: button_click("Der"))
    der_button.pack()

    die_button = tk.Button(game_frame, text="Die", font=('Arial', 16), command=lambda: button_click("Die"))
    die_button.pack()

    das_button = tk.Button(game_frame, text="Das", font=('Arial', 16), command=lambda: button_click("Das"))
    das_button.pack()

    #Bottom Label: used as a way to show the player if the answer is correct or wrong
    result_label = tk.Label(game_frame, text="", font=('Arial', 18))
    result_label.pack()

    streak_label = tk.Label(game_frame, text="", font=('Arial', 18))
    streak_label.pack()

    def hint_button_click():
        """This function gives the player a text hint to help the player decide wich answer to choose"""

        hint_label.configure(text=game_data.provide_hint(current_noun[1]))

    hint_button = tk.Button(game_frame, text="Hint", font=('Arial', 16), command=hint_button_click)
    hint_button.pack()

    hint_label = tk.Label(game_frame, text="", font=('Arial', 12))
    hint_label.pack()

    back_button = tk.Button(game_frame, text="Main Menu", font=('Arial', 16), command=lambda: [show_main_menu(), reset_game_frame()])
    back_button.pack()

#initiate the GUI
current_frame = main_menu
create_main_menu()
create_random_nouns_frame()
create_suffix_frame()

main_menu.pack()

root.wm_maxsize(500,500)
root.wm_minsize(500,500)
root.title("Der Die Das Game")
root.mainloop()