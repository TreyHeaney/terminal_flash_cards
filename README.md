# Flash Cards
A flash card program written in python for the terminal featuring persistent saves and save management, a remote save API written in node.js, and algorithmic card sequencing.

# Prerequisites
The following things must be installed before local setup.
- Python3
- Git
- Node.js

# Installation
While the front end runs almost completely out of the box, the server requires a small amount of setup.

1. Clone the git repository
```
$ git clone https://github.com/TreyHeaney/terminal_flash_cards.git
```

2. Change directories to the `terminal_flash_cards/server` subdirectory.
```
$ cd terminal_flash_cards/server
```
3. Install node.js dependencies.
```
$ npm install
```

# Usage
1. Start the server.
```
$ cd terminal_flash_cards/server
$ node server.js
```
2. Start the client.
```
$ cd terminal_flash_cards
$ python main.py
```
