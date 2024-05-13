# Hangman Game

# Table of Contents
- [Description of Project](#description-of-project)
- [Installation instructions](#installation-instructions)
- [Usage instructions](#usage-instructions)
- [File structure of the project](#file-structure-of-the-project)
- [License information](#license-information)

<a name="Description-of-project"></a>

# Description of Project:
Hangman is a classic game in which a player thinks of a word and the other player tries to guess that word within a certain amount of attempts.
This is an implementation of the Hangman game, where the computer thinks of a word and the user tries to guess it. 

<a name="Installation-instructions"></a>
# Installation instructions
Setting up (recommended in Linux or MacOS)

__Linux__

- Open PowerShell or Windows Command Prompt in **administrator** mode by right-clicking and selecting "Run as administrator"
- Enter the wsl --install command, which will enable features to run WSL and will install the Ubuntu distribution of Linux
![image](https://github.com/Aspiringdeveloper123/hangman785/assets/43377891/a4a8d6d7-288c-42ea-a58d-96182a2cec40)
- To ensure the operating system is up to date, run the following code

![image](https://github.com/Aspiringdeveloper123/hangman785/assets/43377891/22c93a13-a35a-4c58-b5b4-0ffa5c889b9f)
- Install miniconda (an open source environment and package manager) which includes conda, Python, the packages they depend on and other useful packages:

![image](https://github.com/Aspiringdeveloper123/hangman785/assets/43377891/48b7c006-c8dd-4a01-92b4-52bd96c21349)

After running the last command, close your terminal and open a new one, for the changes to take place

- Installing Python

![image](https://github.com/Aspiringdeveloper123/hangman785/assets/43377891/261819d6-2b76-4a56-8da8-1b4e4381834e)

Make sure to press 'Y' when the 'Do you want to continue?' question comes up.

- Installing VS Code - a free source code editor that fully supports Python and has other useful features e.g debugging, syntax highlighting etc

![image](https://github.com/Aspiringdeveloper123/hangman785/assets/43377891/458cf968-0252-41d3-a97a-c1bc7ae93316)

Open up VS Code

- Installing VS Code extensions provides an interative way of running Python code. To install any extension, go on VS Code, and click on 'Extensions', and from the menu, we will install Python and Jupyter

<a name="Usage-instructions"></a>

# Usage instructions
## How to play
1. Clone or download the repository to your local machine.
2. Open a terminal or command prompt and navigate to the directory where the main.py file is located.
3. Run the main.py file in a Python environment by entering the following command: python main.py
4. The game will choose a random word from the ``` list_of_fruits ```  and display the word as a series of dashes, representing the letters in the word.
5. Guess one letter at a time by typing it into the command prompt and pressing Enter
6. If the letter is in the word, it will be revealed in the correct position(s) in the word.
7. If the letter is not in the word, you will lose one life, where if you have more than 0 lives, you will be prompted to guess again
8. If you have already guessed the same letter, you will be prompted to guess again
9. If you don't have any more lives, you have lost!
10. If you have guessed all the letters correctly with more than 0 lives, you have won! 

<a name="File-structure-of-the-project"></a>

# File structure of the project

<a name="License-information"></a>

# License information
MIT License

Copyright (c) [2024] [Pareena Shah]

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.


