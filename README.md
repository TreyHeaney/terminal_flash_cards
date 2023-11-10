# Flash Cards
A flash card program written in python for the terminal featuring persistent 
saves and save management, a remote save API written in node.js, and algorithmic 
card sequencing.

# Prerequisites
The following things must be installed before local setup.
- Python3
- Git
- Node.js

# Installation
1. Clone the git repository
```
$ git clone https://github.com/TreyHeaney/terminal_flash_cards.git
```
2. Install front-end dependencies (package manager agnostic)
```
$ cd terminal_flash_cards
$ pip install -r requirements.txt 
```
3. Install server dependencies
```
$ cd server
$ npm install
```


# Usage
1. Start the server.
Change directory to terminal_flash_cards/server
```
$ node server.js
```
2. Start the client.
Chance directory to terminal_flash_cards/
```
$ python main.py
```
Now you're at the main menu. You can open the card groups you have, manage your
save, edit your settings, sign in/sign up to the remote save hosting service. 
Each save is a collection of card groups and each card group is a collection of 
cards. 

# Card Scores and Card Draw Dynamics
Every card has a hidden "score" that abstracts your mastery of that card. 
Answering *correctly increases* the score, *decreasing the liklihood* it will be 
displayed, and answering *incorrectly viceversa*. If you answer a card 
correctly, subsequent correct answers will cause a larger increase in it's 
score. The longer the time since the last correct answer the larger the increase 
in score.

Whenever a card is incorrectly answered a "strong draw" is triggered. A strong
draw inverts card draw liklihoods, helping to associate information you've
learned with information you're still memorizing.

# Save transfering
At the moment I don't have a server for storing saves so transfering them
between environments involves a flash drive, file transfer server or ssh. To do 
this you can either overrite the default save.json (located in 
terminal_flash_cards/static) or point to a save by using a custom save 
(main menu -> manage saves (b) -> custom save (2)). 
