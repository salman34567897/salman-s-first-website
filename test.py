"""      
Large Python Project Example
This script demonstrates:
- Classes
- File handling
- Code generation (can generate 2000+ lines)
- Real working logic
""" 

import random   
import string
import time 
 
# ------------------------------- 
# Utility Functions               
# ------------------------------- 
                                 

def random_string(length=8):
    return ''.join(random.choice(string.ascii_letters) for _ in range(length))


def delay():
    time.sleep(0.01)


# -------------------------------
# Logger Classz
# -------------------------------

class Logger:
    def __init__(self):
        self.logs = []

    def log(self, message):
        entry = f"[LOG] {message}"
        print(entry)
        self.logs.append(entry)

    def save(self, filename="logs.txt"):
        with open(filename, "w") as f:
            for log in self.logs:
                f.write(log + "\n")


# -------------------------------
# Data Manager
# -------------------------------

class DataManager:
    def __init__(self):
        self.data = {}

    def add(self, key, value):

        self.data[key] = value


    def get(self, key):

        return self.data.get(key, None)

    def delete(self, key):
        
        if key in self.data:
            del self.data[key]

    def show_all(self):
        for k, v in self.data.items():
            print(k, ":", v)


# -------------------------------
# Code Generator
# -------------------------------

class CodeGenerator:
    def __init__(self, filename="generated_code.py"):
        self.filename = filename

    def generate(self, lines=2000):
        with open(self.filename, "w") as f:
            f.write("# Auto-generated Python file\n\n")

            for i in range(lines):
                f.write(f"print('This is line {i}')\n")

        print(f"Generated {lines} lines in {self.filename}")


# -------------------------------
# Game Logic (Example)
# -------------------------------

class SimpleGame:
    def __init__(self):
        self.score = 0

    def play(self):
        print("Game Started!")
        for _ in range(10):
            num = random.randint(1, 10)
            guess = random.randint(1, 10)

            print(f"Number: {num}, Guess: {guess}")

            if num == guess:
                self.score += 10
                print("Correct!")
            else:
                print("Wrong!")

            delay()

        print("Final Score:", self.score)


# -------------------------------
# Main Application
# -------------------------------

class App:
    def __init__(self):
        self.logger = Logger()
        self.data_manager = DataManager()
        self.generator = CodeGenerator()
        self.game = SimpleGame()

    def run(self):
        self.logger.log("App started")

        # Data operations
        for i in range(20):
            key = random_string()
            value = random.randint(1, 100)
            self.data_manager.add(key, value)

        self.logger.log("Data added")
        self.data_manager.show_all()

        # Play game
        self.game.play()

        # Generate 2000 lines code
        self.generator.generate(2000)

        # Save logs
        self.logger.save()

        self.logger.log("App finished")


# -------------------------------
# Run Program
# -------------------------------

if __name__ == "__main__":
    app = App()
    app.run()

    