import random

rock = '''
                                        _________
         \                              /\| | | |
         \                            / /|_|_|_|
          \                           \        |
            (  ( ) ) ( )  )            \_______/
           ( ( ( ( )  )  ) )           /______/
          ( ( )) ) (   ) ( ( )        /       /
          ( (__.-.___.-.__) )        /       /
           /---._.---._.---\        /       /
           \||   '/  '   ||/       /       /
            |||  (_     |||       /       /
             || ///\\\  ||\______/       /
        ___/ ||||\__/|||||/             /
       /   \   ||||||||  /             /
      /     \   ||||||  /        _____/
'''

paper = ''' _ __   __ _ _ __   ___ _ __
| '_ \ / _` | '_ \ / _ \ '__|
| |_) | (_| | |_) |  __/ |
| .__/ \__,_| .__/ \___|_|
| |         | |
|_|         |_|              '''

scissor = '''
 _        ,/'
  (_).  ,/'
   _  ::
  (_)'  `\.
           `\. '''

li = [rock, paper, scissor]
user_choice = int(input("enter '0' for rock, '1' for paper, '2' for scissors: "))
if user_choice >= 3 or user_choice < 0:
    print("invalid choice")
else:
    print(li[user_choice])

    comp_choice = random.randint(0, 2)
    print("computer chooses: ")
    print(li[comp_choice])

    if user_choice == 0 and comp_choice == 2:
        print("you win!!")
    elif comp_choice == 0 and user_choice == 2:
        print("you lose")
    elif user_choice < comp_choice:
        print("you lose")
    elif user_choice > comp_choice:
        print("you win")
    elif user_choice == comp_choice:
        print("draw")
