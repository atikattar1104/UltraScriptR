from os.path import exists

def main():
     print("\n Welcome to Script File Generator\n")
     print(" Select your option\n")
     print(" 1. Create UNIX/Linux shell script file")
     print(" 2. Create Powershell script file")
     print(" 3. Create Command Prompt Batch script file")
     print(" 4. Create Command Prompt CMD script file")
     print(" 5. Append new line of script code")
     print("\n 6. Exit")
     print()
     option = input("\n Your option: ")
     if option == "1":
          print("\nCreating UNIX/Linux shell script file")
          fname0 = input("\n Enter the file name you want: ")
          str0 = input("\n Enter your script's first line here: ")
          unix(fname0, str0)
          print("\n In UNIX/Linux shell scripts, There is a line called SheBang line at the start of the file. By default, It is #!/bin/bash , And it is written in this generated file. You can customize that line according to your need, Using any text editor.")
          print("\n To add more lines in scripts, use 5. Append new line of script code option in first menu")
     elif option == "2":
          print("\nCreating Powershell script file")
          fname1 = input("\n Enter the file name you want: ")
          str1 = input("\n Enter your script's first line here: ")
          powershell(fname1, str1)
          print("\n To add more lines in scripts, use 5. Append new line of code option in first menu")
     elif option == "3":
          print("\nCreating Command Prompt Batch script file")
          fname2 = input("\n Enter the file name you want: ")
          str2 = input("\n Enter your script's first line here: ")
          batch(fname2, str2)
          print("\n To add more lines in scripts, use 5. Append new line of code option in first menu")
     elif option == "4":
          print("\nCreating Command Prompt CMD script file")
          fname3 = input("\n Enter the file name you want: ")
          str3 = input("\n Enter your script's first line here: ")
          cmd(fname3, str3)
          print("\n To add more lines in scripts, use 5. Append new line of code option in first menu")
     elif option == "5":
          print("\n Note: Your file must be present where this script is saved. If it is not, Please provide complete file path of your file.")
          fname4 = input("\n Enter your file's name: ")
          str4 = input("\n Enter your script's line you want to append: ")
          append(fname4, str4)
     elif option == "6":
          exit()
     else:
          print("\n Invalid option")

def unix(fname0, str0):
     f = open(fname0+".sh", "w")
     f.write("#!/bin/bash\n")
     f.write(str0+"\n")
     f.close()
     return True

def powershell(fname1, str1):
     f = open(fname1+".ps1", "w")
     f.write(str1+"\n")
     f.close()
     return True

def batch(fname2, str2):
     f = open(fname2+".bat", "w")
     f.write(str2+"\n")
     f.close()
     return True

def cmd(fname3, str3):
     f = open(fname3+".cmd", "w")
     f.write(str3+"\n")
     f.close()
     return True

def append(fname4, str4):
     existance = exists(fname4)
     if existance == True:
          f = open(fname4, "a")
          f.write(str4+"\n")
          print("\n Your new script line has been appended in your file")
          f.close()
     else:
          print("File not found. Please try again!")
     return True


if __name__ == "__main__":
     main()

