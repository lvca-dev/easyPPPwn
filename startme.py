import subprocess

def display_menu():
    print("select interface:")
    print("1. eth0")
    print("2. enp0s3")

def run_eth0():
    command = "sudo python3 pppwn.py --interface=eth0 --fw=1100"
    try:
        subprocess.run(command, shell=True, check=True)
        print("Command executed successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Failed to execute command: {e}")

def run_enp0s3():
    command = "sudo python3 pppwn.py --interface=enp0s3 --fw=1100"
    try:
        subprocess.run(command, shell=True, check=True)
        print("Command executed successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Failed to execute command: {e}")

def main():
    while True:
        display_menu()
        choice = input("Enter your choice (1-2): ")
        
        if choice == '1':
            run_eth0()
        elif choice == '2':
            run_enp0s3()
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
