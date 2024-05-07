# Simon says

This is a fully deployed game of "Simon says", play against your Friends and everyone who got the url.
Your task is to name the colors in the right order exactly as Simon says. With each round it will be one color more you need to name.
An example would be:
<ol> 
    <li>Round: red 
    </li>
    <li>Round: red, yellow 
    </li>
    <li>Round: red, yellow, yellow 
    </li>
    <li>Round: red, yellow, yellow, blue 
    </li>
    <li>Round: red, yellow, yellow, blue, green.
    </li>
</ol>
This continues indefinitely until you name a wrong order of colors. Your maximum of Rounds will be sent to the Highscore sheet.
Try to beat your own highscore or try to beat the one of your friends. With three different difficulties and every difficulty has its own rankings.

## Table of content
<ol>
    <li>
    Features</li>
        <ol>
            <li>
            Menu</li>
            <li>
            Introduction</li>
            <li>
            Colorama</li>
            <li>
            Three different difficulties</li>
            <li>
            Highscores</li>
            <li>
            Tracking the rankings</li>
            <li>
            Replay immediately</li>
        </ol>
    <li>
    Testing</li>
        <ol>
        <li>
        Problems and Bugs encountered
        </li>
    <li>
    Deployment</li>
    <li>
    Sources</li>
</ol>

## Features

The game offers you various Features which will be available on the deployed version of the game, which are listed below.

### Menu
The game allows you to navigate through a quick and simple Menu to get where you want to.
<img src="" alt=""/>

### Introduction
The Game offers an quick Introduction on what to do and what the goal of the game is.
<img src="" alt=""/>

### Colorama
The game offers colorized Fonts for the colors which you need to name in order to continue with your run. This was able via the Colorama library.
<img src="" alt=""/>

### Three different difficulties
The game allows you to play on three different difficulties. Each shortens the time you have to memorize the new color in your sequence.
You can play on "easy" difficulty. Which gives you 1 second of time.
You can play on "medium" difficulty. Which gives you 1 second of time.
If you want the ultimate challenge, you can play on "hard" difficulty. This only gives you 0.3 seconds of time.

### Highscores
The game will track how many rounds you beat succesfully and rank them accordingly. Every difficulty has its own rankings.

### Track your ranking.
If you want to know who was better you or your friend. You can always check the Highscores in the Terminal.

### Replay immediately
If you lose, you can start a new Round immediately without the program exiting.
<img src="" alt="" /> 

## Testing

I tested the program throughout various phases of its development.

In order to keep this clean and because some of the features are implemented with a very short timelimit, I decided to record one full testing of every function of the program in a Video. The url will be provided here"Videolink".

### Problems and Bugs encountered

The Major problem I encountered during the development was to ensure the colors are randomized during the complete sequence.
This was solved through the "random.choice" command and the "sequence.append" command.
In order to show the right color in the terminal the "f" statement in my print statement ensured exactly that. I got helped for that through "https://stackoverflow.com/" 

Another Problem encountered was the right use of the Colorama library. Which got recommended by my Mentor for this project.
Especially the different options for the different difficulties. Which I managed to create with the help of a Friend of mine who works as a Software developer.


The Function to clear the screen I used the AI Chatgpt, because I spent a lot of time trying and searching, without getting the result I liked. 

### Validation

The Code was tested for Validation and Readability with "https://pep8ci.herokuapp.com/"
No Major issues were detected. Mostly the issue of having more than 79 characters in one line. Which I didn't change because it broke the program multiple times.
<img src="" alt="" />



## Deployment

The site was deployed using Code Institute's mock terminal for Heroku. The steps to deploy are as follows:
<ul>
    <li>
    Make sure every "input" method has a new line.</li>
    <li>
    Update the requirements.txt</li>
    <li>
    Log in or Create a Heroku Account</li>
    <li>
    Fork or clone this repository</li>
    <li>
    Create a new Heroku app</li>
    <li>
    Set the buildbacks to Python and NodeJS in that order</li>
    <li>
    Link the Heroku app to the repository</li>
    <li>
    Click on Deploy</li>