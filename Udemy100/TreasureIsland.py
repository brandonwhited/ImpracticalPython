print("""                                         ___.-----.______
                                   ___.-----'::::::::::::::::`---.___
                _.--._            (:::;,-----'~~~~~`----::::::::::.. `-.
   _          .'_---. `--.__       `~~'                 `~`--.:::::`..  `..
  ; `-.____.-' ' {0} ` `--._`---.____                         `:::::::: : ::
 :_^              ~   `--.___ `----.__`----.____                ~::::::.`;':
  :`--.__,-----.___(         `---.___ `---.___  `----.___         ~|;:,' : |
   `-.___,---.____     _,        ._  `----.____ `----.__ `-----.___;--'  ; :
                  `---' `.  `._    `))  ,  , , `----.____.----.____   --' :|
                        / `,--.\    `.` `  ` ` ,   ,  ,     _.--   `-----'|'
 _.~~~~~~._____    __./'_/'     :   .:----.___ ` ` ` ``  .-'      , ,  :::'
                 ///--\;  ____  :   :'    ____`---.___.--::     , ` ` ::'
                 `'           _.'   (    /______     (   `-._   `-._,-'
    ()  ()                 .-' __.-//     /_______---'       `-._   `.
  * *(o)'      ~~~        /////    `'       ~~~~~~      ~~ ______;   ::.
  `\ )( /*                `'`'                            /_______   _.'
    {()}      ,     ~~~                  ~~~~~~~~           /___.---'  --__
     !|       `                                              ~~~
  ~~~~~~~~
 ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~""")

print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 

Action_1 = input("You're at a crossroad. Where do you want to go? Type 'left' or 'right'\n").lower()

if Action_1 == "left":
    print("You move on to the dock")
    Action_2 = input ("You come to a dock, should you \"wait\" for a boat or \"swim\"?\n")   
    if Action_2 == "wait" or "Wait":
        # Game will cointinue
        print("You get on the boat and where it drops you off, ther are three doors")
        Action_3 = input("There are three doors with three different colors. Do you go through the blue,red or yellow door\n")
        if Action_3 == "blue":
            print("Congratulations, you have made to the end and survived!")
        else:
            print("You died right before salvation")
    else:
        print("You get eaten by trout when swimming")
else:
    print("You fall in hole and die") 
    
    

