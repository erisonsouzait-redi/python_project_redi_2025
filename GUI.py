import tkinter as tk
from tkinter import ttk
import game_class

class MainMenu(tk.Frame):

    """This class creates the initial menu to choose the type of game"""

    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        #Top Labels
        self.welcome_label = tk.Label(self, text="Welcome to the Der Die Das Spiel!", font=('Arial', 18))
        self.welcome_label.grid(row=0, column=0, columnspan=1, pady=10)

        self.choose_label = tk.Label(self, text="Choose your type of game", font=('Arial', 18))
        self.choose_label.grid(row=1, column=0, columnspan=1, pady=10)

        #Buttons
        self.random_noun = tk.Button(self, text="Random Nouns", font=('Arial', 16), command=lambda: controller.show_frame(RandomMenu))
        self.random_noun.grid(row=2, column=0, columnspan=1, pady=5)

        self.by_endings = tk.Button(self, text="Nouns by endings", font=('Arial', 16), command=lambda: controller.show_frame(EndingsMenu))
        self.by_endings.grid(row=4, column=0, columnspan=1, pady=5)

        self.by_topic = tk.Button(self, text="Nouns by topic", font=('Arial', 16))
        self.by_topic.grid(row=6, column=0, columnspan=1, pady=5)


class RandomMenu(tk.Frame):

    """This class display the options for quantities of random nouns to be played"""

    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        #Label
        self.choose_label = tk.Label(self, text="Choose the number of nouns: ", font=('Arial', 18))
        self.choose_label.grid(row=0, column=0, columnspan=1, pady=10)

        #Buttons
        self.random_ten = tk.Button(self, text="10", font=('Arial', 16), command=lambda: controller.show_frame(BaseGame))
        self.random_ten.grid(row=2, column=0, columnspan=1, pady=5)

        self.random_twenty = tk.Button(self, text="20", font=('Arial', 16), command=lambda: controller.show_frame(MainMenu))
        self.random_twenty.grid(row=4, column=0, columnspan=1, pady=5)

        self.random_thirty = tk.Button(self, text="30", font=('Arial', 16), command=lambda: controller.show_frame(MainMenu))
        self.random_thirty.grid(row=6, column=0, columnspan=1, pady=5)

class EndingsMenu(tk.Frame):

    """This class display the screen with the game based on the ending of the nouns"""

    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        #Label
        self.choose_label = tk.Label(self, text="Choose the noun ending to train", font=('Arial', 18))
        self.choose_label.grid(row=0, column=0, columnspan=5, pady=10)

        #1st row
        self.ant_button = tk.Button(self, text="-ant", font=('Arial', 16), command=lambda: controller.show_frame(BaseGame))
        self.ant_button.grid(row=1, column=0, padx=2, pady=5, sticky="ew")

        self.ast_button = tk.Button(self, text="-ast", font=('Arial', 16), command=lambda: controller.show_frame(BaseGame))
        self.ast_button.grid(row=1, column=1, padx=2, pady=5, sticky="ew")

        self.ich_button = tk.Button(self, text="-ich", font=('Arial', 16), command=lambda: controller.show_frame(BaseGame))
        self.ich_button.grid(row=1, column=2, padx=2, pady=5, sticky="ew")

        self.ig_button = tk.Button(self, text="-ig", font=('Arial', 16), command=lambda: controller.show_frame(BaseGame))
        self.ig_button.grid(row=1, column=3, padx=2, pady=5, sticky="ew")

        self.ismus_button = tk.Button(self, text="-ismus", font=('Arial', 16), command=lambda: controller.show_frame(BaseGame))
        self.ismus_button.grid(row=1, column=4, padx=2, pady=5, sticky="ew")

        #2 nd row
        self.ling_button = tk.Button(self, text="-ling", font=('Arial', 16), command=lambda: controller.show_frame(BaseGame))
        self.ling_button.grid(row=2, column=0, padx=2, pady=5, sticky="ew")

        self.or_button = tk.Button(self, text="-or", font=('Arial', 16), command=lambda: controller.show_frame(BaseGame))
        self.or_button.grid(row=2, column=1, padx=2, pady=5, sticky="ew")

        self.us_button = tk.Button(self, text="-us", font=('Arial', 16), command=lambda: controller.show_frame(BaseGame))
        self.us_button.grid(row=2, column=2, padx=2, pady=5, sticky="ew")

        self.a_button = tk.Button(self, text="-a", font=('Arial', 16), command=lambda: controller.show_frame(BaseGame))
        self.a_button.grid(row=2, column=3, padx=2, pady=5, sticky="ew")

        self.anz_button = tk.Button(self, text="-anz", font=('Arial', 16), command=lambda: controller.show_frame(BaseGame))
        self.anz_button.grid(row=2, column=4, padx=2, pady=5, sticky="ew")

        #3rd row
        self.enz_button = tk.Button(self, text="-enz", font=('Arial', 16), command=lambda: controller.show_frame(BaseGame))
        self.enz_button.grid(row=3, column=0, padx=2, pady=5, sticky="ew")

        self.ei_button = tk.Button(self, text="-ei", font=('Arial', 16), command=lambda: controller.show_frame(BaseGame))
        self.ei_button.grid(row=3, column=1, padx=2, pady=5, sticky="ew")

        self.ie_button = tk.Button(self, text="-ie", font=('Arial', 16), command=lambda: controller.show_frame(BaseGame))
        self.ie_button.grid(row=3, column=2, padx=2, pady=5, sticky="ew")

        self.heit_button = tk.Button(self, text="-heit", font=('Arial', 16), command=lambda: controller.show_frame(BaseGame))
        self.heit_button.grid(row=3, column=3, padx=2, pady=5, sticky="ew")

        self.keit_button = tk.Button(self, text="-keit", font=('Arial', 16), command=lambda: controller.show_frame(BaseGame))
        self.keit_button.grid(row=3, column=4, padx=2, pady=5, sticky="ew")

        #4th row
        self.ik_button = tk.Button(self, text="-ik", font=('Arial', 16), command=lambda: controller.show_frame(BaseGame))
        self.ik_button.grid(row=4, column=0, padx=2, pady=5, sticky="ew")

        self.sion_button = tk.Button(self, text="-sion", font=('Arial', 16), command=lambda: controller.show_frame(BaseGame))
        self.sion_button.grid(row=4, column=1, padx=2, pady=5, sticky="ew")

        self.tion_button = tk.Button(self, text="-tion", font=('Arial', 16), command=lambda: controller.show_frame(BaseGame))
        self.tion_button.grid(row=4, column=2, padx=2, pady=5, sticky="ew")

        self.sis_button = tk.Button(self, text="-sis", font=('Arial', 16), command=lambda: controller.show_frame(BaseGame))
        self.sis_button.grid(row=4, column=3, padx=2, pady=5, sticky="ew")

        self.tat_button = tk.Button(self, text="-tät", font=('Arial', 16), command=lambda: controller.show_frame(BaseGame))
        self.tat_button.grid(row=4, column=4, padx=2, pady=5, sticky="ew")

        #5th row
        self.ung_button = tk.Button(self, text="-ung", font=('Arial', 16), command=lambda: controller.show_frame(BaseGame))
        self.ung_button.grid(row=5, column=0, padx=2, pady=5, sticky="ew")

        self.ur_button = tk.Button(self, text="-ur", font=('Arial', 16), command=lambda: controller.show_frame(BaseGame))
        self.ur_button.grid(row=5, column=1, padx=2, pady=5, sticky="ew")

        self.schaft_button = tk.Button(self, text="-schaft", font=('Arial', 16), command=lambda: controller.show_frame(BaseGame))
        self.schaft_button.grid(row=5, column=2, padx=2, pady=5, sticky="ew")

        self.chen_button = tk.Button(self, text="-chen", font=('Arial', 16), command=lambda: controller.show_frame(BaseGame))
        self.chen_button.grid(row=5, column=3, padx=2, pady=5, sticky="ew")

        self.lein_button = tk.Button(self, text="-lein", font=('Arial', 16), command=lambda: controller.show_frame(BaseGame))
        self.lein_button.grid(row=5, column=4, padx=2, pady=5, sticky="ew")

        #6th row
        self.icht_button = tk.Button(self, text="-icht", font=('Arial', 16), command=lambda: controller.show_frame(BaseGame))
        self.icht_button.grid(row=6, column=0, padx=2, pady=5, sticky="ew")

        self.il_button = tk.Button(self, text="-il", font=('Arial', 16), command=lambda: controller.show_frame(BaseGame))
        self.il_button.grid(row=6, column=1, padx=2, pady=5, sticky="ew")

        self.it_button = tk.Button(self, text="-it", font=('Arial', 16), command=lambda: controller.show_frame(BaseGame))
        self.it_button.grid(row=6, column=2, padx=2, pady=5, sticky="ew")

        self.ma_button = tk.Button(self, text="-ma", font=('Arial', 16), command=lambda: controller.show_frame(BaseGame))
        self.ma_button.grid(row=6, column=3, padx=2, pady=5, sticky="ew")

        self.ment_button = tk.Button(self, text="-ment", font=('Arial', 16), command=lambda: controller.show_frame(BaseGame))
        self.ment_button.grid(row=6, column=4, padx=2, pady=5, sticky="ew")

        #7th row
        self.tel_button = tk.Button(self, text="-tel", font=('Arial', 16), command=lambda: controller.show_frame(BaseGame))
        self.tel_button.grid(row=7, column=0, padx=2, pady=5, sticky="ew")

        self.tum_button = tk.Button(self, text="-tum", font=('Arial', 16), command=lambda: controller.show_frame(BaseGame))
        self.tum_button.grid(row=7, column=1, padx=2, pady=5, sticky="ew")

        self.um_button = tk.Button(self, text="-um", font=('Arial', 16), command=lambda: controller.show_frame(BaseGame))
        self.um_button.grid(row=7, column=2, padx=2, pady=5, sticky="ew")




class BaseGame(tk.Frame):

    """This class show the screen to play a game of random nouns"""

    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        self.random_game = game_class.Game()
        self.nouns_list = self.random_game.random_nouns()
        self.current_index = 0

        #Top Label
        self.choose_label = tk.Label(self, text="Choose the correct article to the following noun in the Nominativ: ", font=('Arial', 18))
        self.choose_label.grid(row=0, column=0, columnspan=1, pady=10)
        
        #this label shows the current noun to be tested
        self.noun_label = tk.Label(self, text=self.nouns_list[0][1], font=('Arial', 18))
        self.noun_label.grid(row=2, column=0, columnspan=1, pady=10)

        #Buttons
        self.der_button = tk.Button(self, text="Der", font=('Arial', 16), command=lambda: self.button_click("Der"))
        self.der_button.grid(row=4, column=0, columnspan=1, pady=5)

        self.die_button = tk.Button(self, text="Die", font=('Arial', 16), command=lambda: self.button_click("Die"))
        self.die_button.grid(row=6, column=0, columnspan=1, pady=5)

        self.das_button = tk.Button(self, text="Das", font=('Arial', 16), command=lambda: self.button_click("Das"))
        self.das_button.grid(row=8, column=0, columnspan=1, pady=5)
        
        #Bottom Label
        self.result_label = tk.Label(self, text="", font=('Arial', 18))
        self.result_label.grid(row=10, column=0, columnspan=1, pady=10)

    def button_click(self, response):

        """Checks the anwer and proceeds to the next noun on the list"""

        current_noun = self.nouns_list[self.current_index]
        
        #check if the answer matches the article of the noun
        if response == current_noun[0]:
            self.result_label.config(text="That's Correct!", fg="green")
            #points logics here
        else:
            self.result_label.config(text="That's wrong...!", fg="red")
            #points logic here
        
        #Goes to the next noun on the list
        self.current_index += 1
        
        #check if there are more nouns and update with the next noun
        if self.current_index < len(self.nouns_list):
            next_noun = self.nouns_list[self.current_index][1]
            self.noun_label.config(text=next_noun)
        else:
            #List of nouns is finished
            self.noun_label.config(text="Game Complete!")
            self.result_label.config(text="Well done! You finished all nouns.", fg="blue")
            #Disable buttons
            self.der_button.config(state='disabled')
            self.die_button.config(state='disabled')
            self.das_button.config(state='disabled')

class GameGUI(tk.Tk):

    """This class receives all the other screens to navigate on all other menu screens"""

    def __init__(self):
        super().__init__()
        self.title("Der Die Das Spiel")
        self.geometry("500x500")

        #Container for all screens
        container = ttk.Frame(self)
        container.pack(fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        # Dictionary to hold all the frames
        self.frames = {}

        #Create all screens
        for F in (MainMenu, RandomMenu, BaseGame, EndingsMenu):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")
        
        self.show_frame(MainMenu)
    
    #This function shows a specific frame
    def show_frame(self, frame_class):
        frame = self.frames[frame_class]
        frame.tkraise()


# Initiate the Game
if __name__ == "__main__":
    game = GameGUI()
    game.mainloop()