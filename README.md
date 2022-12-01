# Indian States Guessing Game
### _A fun graphical interactive game to teach you about all the Indian States_

## Screenshots
![Screenshot (496)](https://user-images.githubusercontent.com/65783653/205167332-9023c321-6f22-40c4-8e2f-287354248faa.png)
![Screenshot (497)](https://user-images.githubusercontent.com/65783653/205167305-273e84fd-2103-46f9-9ad1-8e05d1d72021.png)
![Screenshot (499)](https://user-images.githubusercontent.com/65783653/205168234-40cb00b7-541d-4ba3-9353-62e443cce0c4.png)

## Features

- Easy to use and fun to play
- Add or remove states 
- Score tracking
- Location of each state is displayed correctly on the map
- States which a player is not able to guess are stored inside **Incomplete_states.csv** 

## Requirements

The game needs following python modules to work stack to work properly:
- [Python 3.7+] - Game logic
- [Tkinter] - To display popup messages
- [Turtle] - To display the map and render the game
- [Pandas] - To read and store data from csv file


## Installation

### Make sure you have Python 3.7 or later version installed on your system 
Clone the repository and then execute the following commands.

```sh
cd Indian-States-Guessing-Game
pip install pandas
```

The Tkinter and the Turtle library are built-in with every Python installation so we don't need to install it separately

## Run
Run the game using following command

```sh
python main.py
```

## Customization
In case you want to want to add additional features such as (including union territory) or  want to use different map you can do so by modifying ``data.py`` and ``states.txt`` files from **Game Building files** folder and ``map.gif`` from the root folder.


[//]: # (These are reference links used in the body of this note and get stripped out when the markdown processor does its job. There is no need to format nicely because it shouldn't be seen. Thanks SO - http://stackoverflow.com/questions/4823468/store-comments-in-markdown-syntax)

   [Python 3.7+]: <https://www.python.org/>
   [Tkinter]: <https://docs.python.org/3/library/tkinter.html>
   [Turtle]: <https://docs.python.org/3/library/turtle.html>
   [Pandas]: <https://pandas.pydata.org/docs/index.html>
