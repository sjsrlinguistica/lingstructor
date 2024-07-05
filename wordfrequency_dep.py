import subprocess

def install_dependency(package):
    try:
        subprocess.check_call(['pip', 'install', package])
    except Exception as e:
        print(f"An error occurred while installing {package}: {e}")

# Check if the dependency is installed
try:
    import wordfreq
except ImportError:
    print("The 'wordfreq' module is not installed.\n")
    #request user input on whether to install the module
    install = input("Would you like to install the 'wordfreq' module? (y/n): ")
    #declare a boolean for valid_input
    valid_input = False
    while valid_input == False:
        if install.lower() == 'y':
            install_dependency('wordfreq') # Install the dependency
            valid_input = True
        elif install.lower() == 'n':
            print("The 'wordfreq' module is required for this program to run. Exiting...")
            exit()
        else: #prompt input again
            print("Invalid input. Please enter 'y' or 'n'.")
