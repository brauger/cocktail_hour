
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

##### When successfully in the program environment, use the following code in the command-line to demonstrate your ability to run the Python script:

```
python cocktail_hour.py
```