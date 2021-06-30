#Simple Python Script To Create a brute Force number Password File :)
#Banner
print("\033[1;34;40m _  __                 _                  __  __ ")
print("\033[1;35;40m| |/ /_ __ _   _ _ __ | |_ ___  _ __      \ \/ / ")
print("\033[1;32;40m| ' /| '__| | | | '_ \| __/ _ \| '_ \ _____\  / ")
print("\033[1;36;40m| . \| |  | |_| | |_) | || (_) | | | |_____/  \ ")
print("\033[1;31;40m|_|\_\_|   \__, | .__/ \__\___/|_| |_|    /_/\_\ ")
print("\033[1;33;40m           |___/|_| ")
print("\033[1;30;40m\n Brute Force number password file maker")
#File name
fname = str(input("\033[1;36;40mPlease input a file name:"))
#start with
rfrom = int(input("\nRange From:"))
#End at
rend = int(input("\nRange end:"))
print("\n\nCreating.....\n\n")
for i in range (rfrom,rend):
   #Convert 'i' int into string
   b = str(i)
   file = open(fname,'a')
   file.write("\n"+b)
print("Done....!")