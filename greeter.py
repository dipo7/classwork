from datetime import datetime

def greet(name):
    # Get the current hour
    current_hour = datetime.now().hour
    
    # Determine the greeting based on the time of day
    if 5 <= current_hour < 12:
        greeting = "Good Morning"
    elif 12 <= current_hour < 18:
        greeting = "Good Afternoon"
    else:
        greeting = "Good Night"
    
    print(f"{greeting}, {name}!")

if __name__ == "__main__":
    name = input("Enter your name: ")
    greet(name)
