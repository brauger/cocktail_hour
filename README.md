
# Welcome to Cocktail Hour!

# Purpose

##### If you like to explore new cocktails and even make them for yourself at home or for friends, this is the app for you! You can receive randomized cocktail recipes by running Cocktail Hour.

# Installation

##### In order to search and find your cocktail recipe, you will need to clone the repository to your local computer.

1. Navigate to the code dropdown menu on the repository in GitHub
2. Select "Open with GitHub Desktop"
3. Clone to an easy to find location like your local desktop

##### From the command-line, navigate to the local repository by using code like the following:

```
cd ~/Desktop/cocktail_hour
```

##### If you don't remember where you saved the repo locally, use the "Show in Finder" option when you open the file in GitHub Desktop.

# Setting Up Your Environment

##### Create and activate an Anaconda environment for the program using the following code:

```
conda create -n cocktail-env python=3.8 # (first time only)
conda activate cocktail-env
```

##### If you are uncertain if Anaconda is installed, use the following in your command-line:

```
conda --version
```

##### If it is not found, **[install Anaconda](https://www.anaconda.com/products/distribution)** before proceeding with setting up your environment.

##### Then, within an active virtual environment, install package dependencies:

```
pip install -r requirements.txt
```

# Running Cocktail Hour

##### When successfully in the program environment, use the following code in the command-line to demonstrate your ability to run the Python script:

```
python cocktail_hour.py
```
# Program Tips



##### Once you have run the program, a window (see example below) will pop up prompting you to enter your name. Enter your name, select "Display" and then "Exit" to proceed with the program.

![Image](https://imgur.com/Ios4Q64)

# Testing

##### When you want to run and a test and make sure the program is running correctly, run the following on your computer's command line:

```
pytest
```
