# UltraScriptR

# Video Demo: https://youtu.be/oD9IGqwKtGM

# Description:

This is my CS50P final project. My python program creates script files, which are used to implement scripting languages in various operating systems and scripting programs. It is intended for beginners of shell scripting in Windows(Batch scripting, CMD scripting), UNIX/Linux(Bash, Zsh, Default shell i.e. `sh`, etc. ), and many more. But, Can be used by anyone, as desired.


# Why the world needs my project?

There is a history behind it. When i started to learn linux, and it's basic commands, shell scripting, etc, I found out that creating a shell script is a best option for multitasking and useful when you have to type long commands (like starting a vnc server with specific resolution and desktop environment or connecting to a specific ssh server which you regularly connect to by using various options). But, Rather than changing various programs to create a shell script file, Why there is no program which will do all at once, without leaving it? This is where, The concept of this program is born.

Later, I also found that some of my friends see shell scripting as a difficult concept. So, I have decided to help them (and many other shell scripting beginners worldwide) to achieve the success and mastery in shell scripting. And, This is my first step towards it.


# Additional skills i required/acquired and topics i researched for this project:

1) Linux shell scripting.

2) File extensions of Windows Batch file, CMD file, Powershell file, and other scripting files.

3) Understanding of How python creates a new file when trying to open a non-existing file in write mode.


# Files included in the project:

1) `UltraScriptR.py` is the main file, which should be executed, in order to run the project.


2) `Test_UltraScriptR.py` is the file, which contains test functions for the `UltraScriptR.py` file, which should be executed using `pytest`.


3) `Requirements.txt` is the file, which contains names of external packages required by the project.


# Functions included in `UltraScriptR.py` file:

1) `main()` contains code for

```

1) Asking user to select file type they want using {if...else} decision controller.

2) Asking user to enter a file name of their file (which is to be generated) and first line of script they want to add.

3) Calling the required function according to the chosen file type.

```

2) `unix()` contains code for

```

1) Generating script file for UNIX/Linux terminal script, ending with `.sh` file extension.

2) Adding the standard Bash initial line and first line of script which user provided in `main()`, in generated file.

```

3) `powershell()` contains code for

```

1) Generating script file for Windows Powershell terminal script, ending with `.ps1` file extension.

2) Adding the first line of script which user provided in`main()`, in generated file.

```

4) `batch()` contains code for

```

1) Generating script file for Windows Command Prompt batch script, ending with `.bat` file extension.

2) Adding the first line of script which user provided in `main()`, in generated file.

```

5) `cmd()` contains code for

```

1) Generating script file for Wimdows Command Prompt CMD script, ending with `.cmd` file extension.

2) Adding the first line of script which user provided in `main()`, in generated file.

```

6) `append()` contains code for

```

1) Checking if the file name, provided by the user, exists or not.

2) Appending a new line of script in the script file, if exists.

```


# Functions included in `Test_UltraScriptR.py` file:

1) `main()` contains code for

```

Calling test functions to test the functions from `UltraScriptR.py` file.

```

2) `test_unix()` contains code for

```

Testing `unix()` function of `UltraScriptR.py` file, using `assert` keyword.

```

3) `test_powershell()` contains code for

```

Testing `powershell()` function of `UltraScriptR.py` file, using `assert` keyword.

```

4) `test_batch()` contains code for

```

Testing `batch()` function of `UltraScriptR.py` file, using `assert` keyword.

```

5) `test_cmd()` contains code for

```

Testing `cmd()` function of `UltraScriptR.py` file, using `assert` keyword.

```

6) `test_append()` contains code for

```

Testing `append()` function of `UltraScriptR.py` file, using `assert` keyword.

```

