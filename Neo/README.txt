Neo's Escape - Technical Documentation

Student: Hezekiah Watson

School: National Louis University

Course: CSS-225

Instructor: Nathan Braun

Where the Code hosted: https://github.com/flemcorp-cloud/NEO 

External Services
This game does not rely on any external services, APIs, or cloud-based platforms. All logic and gameplay are handled locally within the Python scripts.

Languages and Technologies
•	Programming Language: Python
•	Technologies Used: Python Standard Library
•	Random Module: Used to generate AI choices in the Rock, Paper, Scissors game.
•	Command Line Interface (CLI): The game runs as a terminal-based application.

System Requirements and Supported Applications
Minimum System Requirements:
•	Operating System: Windows, macOS, or Linux
•	Python Version: Python 3.6+
•	Memory: At least 100MB free RAM
•	Storage: At least 10MB free disk space
•	Processor: Any modern x86-64 CPU

Supported Applications:
•	Any terminal or command-line interface that can execute Python scripts.
•	Python interpreter installed on the system.

Coding/Naming Conventions
•	File Names: Use snake_case (e.g., main.py, character.py, play_rps.py).
•	Function Names: Defined using lowercase with underscores (e.g., play_rps(), chapter_1()).
•	Class Names: Use PascalCase (e.g., Character).
•	Variable Names: Use lowercase with underscores (e.g., wins, losses).
•	Comments and Documentation: Each file contains an author’s name, last edit date, along with docstrings and comments.

How to Run/Build/Deploy the Program
1.	Ensure that Python 3.6 or later is installed on the system.
2.	Open a terminal or command prompt.
3.	Navigate to the directory containing the game files.
4.	Run the following command: python main.py
5.	Follow the on-screen instructions to play the game.

Deployment:
•	Since this is a standalone Python script, it does not require complex deployment steps.
•	For sharing, the entire folder containing main.py and other scripts can be distributed.
•	If packaging as an executable, tools like pyinstaller can be used.

Overview of the Architecture
Modules:
•	main.py: Contains the game loop and manages the flow between chapters.
•	character.py: Defines the Character class used in the game.
•	play_rps.py: Handles the Rock, Paper, Scissors game logic.
•	chapter_1.py to chapter_5.py: Each file represents a chapter in the game and calls play_rps() for interactions.

Flow of Execution:
1.	main.py initializes the game and the player character.
2.	It loops through chapters (chapter_1.py to chapter_5.py), calling their respective functions.
3.	Each chapter presents a scenario and initiates a Rock, Paper, Scissors challenge (play_rps.py).
4.	Based on the game outcomes, wins, losses, and draws are tracked.
5.	At the end of all chapters, the game summarizes the player’s performance and determines if they have won or lost the game.

How to Start the Program (Start the Game)
•	Download the files & run with python main.py
•	Run main.py in a terminal or command prompt: python main.py
•	The game will introduce the main character and start Chapter 1.
•	The player will be prompted to play Rock, Paper, Scissors against the AI.
•	The game will progress through chapters based on the outcomes of the matches.
•	After all chapters, the game will display the final results.
•	The game will end, and the user can press Enter to exit.

