# name = input("May I know your name? ")
# print("Hello " + name + "!")
# print(len(name))

print("Welcome to the tip calculator.")
bill = int(input("What is the total bill? "))
people = int(input("How many people to split the bill? "))
while True:
    tip = int(input("What percentage tip would you like to give? 10,12 or 15? "))
    if tip in (10,12,15): break
    else: print("be wise")
split_bill = (bill + bill*tip/100)/people
split_bill = "{:.2f}".format(split_bill)                #will always show upto 2 decimal even if its 0
print("Each person should pay: " + str(split_bill))

###from ascii.co/art
print("\n\nHidden door")
print("""
88888888888888888888888888888888888888888888888888888888888888888888888
88.._|      | `-.  | `.  -_-_ _-_  _-  _- -_ -  .'|   |.'|     |  _..88
88   `-.._  |    |`!  |`.  -_ -__ -_ _- _-_-  .'  |.;'   |   _.!-'|  88
88      | `-!._  |  `;!  ;. _______________ ,'| .-' |   _!.-'     |  88
88..__  |     |`-!._ | `.| |_______________||."'|  _!.;'   |     _|..88
88   |``"..__ |    |`";.| '|_|TNTNTNTNTNT|_|'| _!-|   |   _|..-|'    88
88   |      |``--..|_ | `;!|l|TNTNTNTNTNT|l|.''   |_..!-'|     |     88
88   |      |    |   |`-,!_|_|TNTNTNTNTNT|_||.!-;'  |    |     |     88
88___|______|____!.,.!,.!,!|o|TNTNTNTNTNT|o|,!,.!.,.!..__|_____|_____88
88      |     |    |  |  | |_|TNTNTNTNTNT|_|| |   |   |    |      |  88
88      |     |    |..!-;''|l|TP'YNTNTNTN|l| |`-..|   |    |      |  88
88      |    _!.--'  | _!,"|_|o * oTNTNTN|_||!._|  `'-!.._ |      |  88
88     _!.-'|    | _."|  !;|o|Tb,dNTNTNTN|o|`.| `-._|    |``-.._  |  88
88..--'     |  _.''|  !-| !|_|TNTNTNTNTNT|_|.|`-. | ``._ |     |``"..88
88   |      |.|    |.|  !| |l|TNTNTNTNTNT|l||`. |`!   | `".    |     88
88   |  _.-'  |  .'  |.' |/|_|TNTNTNTNTNT|_|! |`!  `,.|    |-._|     88
88  _!"'|     !.'|  .'| .'|[@]TNTNTNTNTNT[@] \|  `. | `._  |   `-._  88
88-'    |   .'   |.|  |/| /                 \|`.  |`!    |.|      |`-88
88      |_.'|   .' | .' |/                   \  \ |  `.  | `._    |  88
88     .'   | .'   |/|  /                     \ |`!   |`.|    `.  |  88
88  _.'     !'|   .' | /                       \|  `  |  `.    |`.|  88
88888888888888888888888888888888888888888888888888888888888888888888888
""")
# print(round(8/3))      #rounds the float to nearest integer
# print(round(8/3,2))    #rounds the float to 2 decimals
# print(8//3)            #chops off the decimal part & it is an integer
