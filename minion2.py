import os
import subprocess
import readline
import random
import base64 
import binascii
import re



# Define colors
DARKGRAY = '\033[1;30m'
RED = '\033[0;31m'
LIGHTRED = '\033[1;31m'
GREEN = '\033[0;32m'
YELLOW = '\033[1;33m'
BLUE = '\033[0;34m'
PURPLE = '\033[0;35m'
LIGHTPURPLE = '\033[1;35m'
CYAN = '\033[0;36m'
WHITE = '\033[1;37m'
SET = '\033[0m'

COLORS = [DARKGRAY, RED, LIGHTRED, GREEN, YELLOW, BLUE, PURPLE, LIGHTPURPLE, CYAN, WHITE]

def print_figlet(text):
    color = random.choice(COLORS)
    os.system(f'figlet -f big "{text}" | sed "s/^/{color}/" | sed "s/$/{SET}/"')

def completer(text, state):
    options = [i for i in os.listdir('.') if i.startswith(text)]
    if state < len(options):
        return options[state]
    else:
        return None
        

def check_figlet_installed():
    try:
        subprocess.run(['figlet', '-v'], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        print("Figlet is installed!")
    except subprocess.CalledProcessError:
        print("Figlet is not installed. Please install it using your package manager (e.g., apt-get install figlet).")

check_figlet_installed()

    
    




readline.set_completer(completer)
readline.parse_and_bind('tab: complete')

def main_menu():
    while True:
        print_figlet("MINION")
        print(f"{YELLOW}Created by TTEH{SET}")
        print(f"[{RED}!] legal disclaimer: Usage of minion for attacking targets without prior mutual consent is illegal. It is the end user's responsibility to obey all applicable local, state, and federal laws. Developers assume no liability and are not responsible for any misuse or damage caused by this program.{SET}")
        print("\nMain Menu")
        print("1.  Nmap")
        print("2.  Gobuster")
        print("3.  SMB")
        print("4.  SQLmap")
        print("5.  Search Exploit-db")
        print("6.  ExifTool")
        print("7.  Binwalk")
        print("8.  Log Analysis")
        print("9.  Cryptography")
        print("10. Exit")
        choice = input("How can MINION help? : ")

        if choice == '1':
            nmap_menu()
        elif choice == '2':
            gobuster_menu()
        elif choice == '3':
            smb_menu()
        elif choice == '4':
            sqlmap_menu()
        elif choice == '5':
            exploit_db_menu()
        elif choice == '6':
            exiftool_menu()
        elif choice == '7':
            binwalk_menu()
        elif choice == '8':
            log_analysis_menu()
        elif choice == '9': 
            cryptography_menu() 
        elif choice == '10': 
             exit()
        else:
            print(f"{LIGHTRED}Invalid selection: Returning to main menu{SET}")
            
def nmap_menu():
    while True:
        print_figlet("Nmap Menu")
        IP = input("Enter IP Address: ")
        print("\n1. Slow but detailed")
        print("a. Slow & output to file")
        print("\n2. Normal with scripts")
        print("b. Normal & output to file")
        print("\n3. Normal without scripts (this is faster)")
        print("c. Normal without scripts & output to file")
        print("\n4. Fast but loud (might miss open ports)")
        print("d. Fast, loud, & output to file")
        print("\n5. Back")
        print("6. Exit")
        speed = input("Please select the speed : ")

        if speed == '1':
            os.system(f"nmap -v -A -p- -T4 {IP}")
        elif speed == 'a':
            os.system(f"nmap -A -p- -T4 {IP} -oN {IP}.slow")
        elif speed == '2':
            os.system(f"nmap -n -v -sV -sC -p- -T4 {IP}")
        elif speed == 'b':
            os.system(f"nmap -n -sV -sC -p- -T4 {IP} -oN {IP}.normal")
        elif speed == '3':
            os.system(f"nmap -n -v -sS -p- --min-rate 1000 {IP}")
        elif speed == 'c':
            os.system(f"nmap -n -sS -p- --min-rate 1000 {IP} -oN {IP}.no_script")
        elif speed == '4':
            os.system(f"nmap -n -v -sV -sC -p- --min-rate 5000 {IP}")
        elif speed == 'd':
            os.system(f"nmap -n -sV -sC -p- --min-rate 5000 {IP} -oN {IP}.fast")
        elif speed == '5':
            main_menu()
        elif speed == '6':
            exit()
        else:
            print(f"{LIGHTRED}Invalid selection: Returning to Nmap menu{SET}")

def gobuster_menu():
    while True:
        print_figlet("Gobuster Menu")
        IP = input("Enter IP Address: ")
        print("\n1. Small wordlist")
        print("2. Medium wordlist")
        print("3. Large wordlist")
        print("4. Back")
        print("5. Exit")
        size = input("Select wordlist size : ")

        if size == '1':
            os.system(f"gobuster dir --url http://{IP}/ --wordlist /usr/share/wordlists/dirbuster/directory-list-2.3-small.txt -x php")
        elif size == '2':
            os.system(f"gobuster dir --url http://{IP}/ --wordlist /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt")
        elif size == '3':
            os.system(f"gobuster dir --url http://{IP}/ --wordlist /usr/share/wordlists/seclists/Discovery/DNS/subdomains-top1million-20000.txt")
        elif size == '4':
            main_menu()
        elif size == '5':
            exit()
        else:
            print(f"{LIGHTRED}Invalid selection: Returning to Gobuster menu{SET}")
            
def smb_menu():
    while True:
        print_figlet("SMB Menu")
        IP = input("Enter IP Address: ")
        print("\n1. List Shares")
        print("2. Test for Uncredentialed Access")
        print("3. Access with Credentials")
        print("4. Back")
        print("5. Exit")
        access = input("How can MINION help? : ")

        if access == '1':
            os.system(f"smbclient -N -L \\\\{IP}\\")
        elif access == '2':
            share = input("Share Name : ")
            os.system(f"smbclient \\\\{IP}\\{share}")
        elif access == '3':
            share = input("Share Name : ")
            uname = input("Username : ")
            os.system(f"smbclient \\\\{IP}\\{share} -U {uname}")
        elif access == '4':
            main_menu()
        elif access == '5':
            exit()
        else:
            print(f"{LIGHTRED}Invalid selection: Returning to SMB menu{SET}")
            
            
def sqlmap_menu():
    while True:
        print_figlet("SQLmap Menu")
        print("1. Detect SQL injection flaws")
        print("2. Check For Cookie Vulnerabilities")
        print("3. Get Cookie Shell")
        print("4. Back")
        print("5. Exit")
        choice = input("How can MINION help? : ")

        if choice == '1':
            url = input("Enter URL: ")
            os.system(f"sqlmap -u {url}")
        elif choice == '2':
            url = input("Enter URL: ")
            cookie = input("Enter PHPSESSID: ")
            os.system(f"sqlmap -u {url} --cookie='PHPSESSID={cookie}'")
        elif choice == '3':
            url = input("Enter URL: ")
            cookie = input("Enter PHPSESSID: ")
            os.system(f"sqlmap -u {url} --cookie='PHPSESSID={cookie}' --os-shell")
        elif choice == '4':
            main_menu()
        elif choice == '5':
            exit()
        else:
            print(f"{LIGHTRED}Invalid selection: Returning to SQLmap menu{SET}")


def exploit_db_menu():
    while True:
        print_figlet("Exploit-db Menu")
        print("1. Search")
        print("2. Back")
        print("3. Exit")
        choice = input("How can MINION help? : ")

        if choice == '1':
            search = input("What would you like to search for?: ")
            os.system(f"searchsploit {search}")
        elif choice == '2':
            main_menu()
        elif choice == '3':
            exit()
        else:
            print(f"{LIGHTRED}Invalid selection: Returning to Exploit-db menu{SET}")


def exiftool_menu():
    while True:
        print_figlet("ExifTool Menu")
        print("1. Extract metadata from an image")
        print("2. Back")
        print("3. Exit")
        choice = input("How can MINION help? : ")

        if choice == '1':
            image_path = input("Enter the path to the image: ")
            os.system(f"exiftool {image_path}")
        elif choice == '2':
            main_menu()
        elif choice == '3':
            exit()
        else:
            print(f"{LIGHTRED}Invalid selection: Returning to ExifTool menu{SET}")
           
def binwalk_menu():
    while True:
        print_figlet("Binwalk Menu")
        print("1. Analyze a file")
        print("2. Extract from a file")
        print("3. Back")
        print("4. Exit")
        choice = input("How can MINION help? : ")

        if choice == '1':
            file_path = input("Enter the path to the file: ")
            os.system(f"binwalk {file_path}")
        elif choice == '2':
            file_path = input("Enter the path to the file: ")
            os.system(f"binwalk --dd='.*' {file_path}")
        elif choice == '3':
            main_menu()
        elif choice == '4':
            exit()
        else:
            print(f"{LIGHTRED}Invalid selection: Returning to Binwalk menu{SET}")

def log_analysis_menu():
    while True:
        print_figlet("Log Analysis Menu")
        print("1. Filter logs by keyword")
        print("2. Sort logs")
        print("3. Extract specific fields")
        print("4. Combine functions")
        print("5. Back")
        print("6. Exit")
        choice = input("How can MINION help? : ")

        if choice == '1':
            log_path = input("Enter the path to the log file (e.g., /var/log/syslog): ")
            keyword = input("Enter the keyword to filter by (e.g., ERROR): ")
            output_option = input("Output to file? (yes/no): ").lower()
            try:
                if output_option == 'yes':
                    output_file = input("Enter the path for the output file (e.g., /path/to/output.txt): ")
                    os.system(f"cat {log_path} | grep '{keyword}' > {output_file}")
                else:
                    os.system(f"cat {log_path} | grep '{keyword}'")
            except Exception as e:
                print(f"{LIGHTRED}Error: {str(e)}. Please ensure the log file path and keyword are correct.{SET}")
        elif choice == '2':
            log_path = input("Enter the path to the log file (e.g., /var/log/syslog): ")
            output_option = input("Output to file? (yes/no): ").lower()
            try:
                if output_option == 'yes':
                    output_file = input("Enter the path for the output file (e.g., /path/to/output.txt): ")
                    os.system(f"cat {log_path} | sort > {output_file}")
                else:
                    os.system(f"cat {log_path} | sort")
            except Exception as e:
                print(f"{LIGHTRED}Error: {str(e)}. Please ensure the log file path is correct.{SET}")
        elif choice == '3':
            log_path = input("Enter the path to the log file (e.g., /var/log/syslog): ")
            field = input("Enter the field number to extract (e.g., 1): ")
            output_option = input("Output to file? (yes/no): ").lower()
            try:
                if output_option == 'yes':
                    output_file = input("Enter the path for the output file (e.g., /path/to/output.txt): ")
                    os.system(f"cat {log_path} | cut -d' ' -f{field} > {output_file}")
                else:
                    os.system(f"cat {log_path} | cut -d' ' -f{field}")
            except Exception as e:
                print(f"{LIGHTRED}Error: {str(e)}. Please ensure the log file path and field number are correct.{SET}")
        elif choice == '4':
            log_path = input("Enter the path to the log file (e.g., /var/log/syslog): ")
            functions = input("Enter the functions to combine (e.g., 'grep keyword | sort | cut -d\" \" -f1-3'): ")
            output_option = input("Output to file? (yes/no): ").lower()
            try:
                if output_option == 'yes':
                    output_file = input("Enter the path for the output file (e.g., /path/to/output.txt): ")
                    os.system(f"cat {log_path} | {functions} > {output_file}")
                else:
                    os.system(f"cat {log_path} | {functions}")
            except Exception as e:
                print(f"{LIGHTRED}Error: {str(e)}. Please ensure the log file path and functions are correct.{SET}")
        elif choice == '5':
            main_menu()
        elif choice == '6':
            exit()
        else:
            print(f"{LIGHTRED}Invalid selection. Please select a valid option from the menu.{SET}")
            


def detect_base(input_string):
    try:
        # Check for Base64
        if re.match(r'^[A-Za-z0-9+/=]+$', input_string):
            base64_bytes = input_string.encode('utf-8')
            base64.decodebytes(base64_bytes)
            return "Base64"
    except binascii.Error:
        pass

    try:
        # Check for Base32
        if re.match(r'^[A-Z2-7]+=*$', input_string):
            base32_bytes = input_string.encode('utf-8')
            base64.b32decode(base32_bytes)
            return "Base32"
    except binascii.Error:
        pass

    try:
        # Check for Hexadecimal (with or without '0x' prefix)
        if re.match(r'^(0x)?[0-9A-Fa-f]+$', input_string):
            int(input_string, 16)
            return "Hexadecimal"
    except ValueError:
        pass

    try:
        # Check for Binary
        if re.match(r'^[01 ]+$', input_string):
            return "Binary"
    except ValueError:
        pass

    return "Unknown encoding"
    
 

def cryptography_menu():
    while True:
        print_figlet("Cryptography Menu")
        print("1. Detect encoding of a string")
        print("2. Back")
        print("3. Exit")
        choice = input("How can MINION help? : ")

        if choice == '1':
            input_string = input("Enter the string to detect its encoding: ")
            encoding = detect_base(input_string)
            print(f"The encoding is: {encoding}")                  
        elif choice == '2':
            main_menu()
        elif choice == '3':
            exit()
        else:
            print(f"{LIGHTRED}Invalid selection: Returning to Cryptography menu{SET}")


      
            
            

if __name__ == "__main__":
    main_menu()

