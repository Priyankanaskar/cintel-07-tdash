## PyShiny Basic Dashboard (Penguins)

# Introduction

This Project Is baseed on Python Application with Shiny Layout Application

**Author**
This Project is created by Priyanka Naskar Under Guidence OF **Dr.Case**.

 **Date** 
4/17/2024

## PyShiny Express: Palmer Penguins Dashboard 

**Repository: pyshiny-penguins-dashboard-express** 

**Live App: Penguins Dashboard (Express)**

Run and publish interactive apps using PyShiny Express and GitHub Pages.

This is a teaching version of the app written for clarity and understanding. To contribute, please fork the repository and submit a pull request.

# Data Description
This app uses the Palmer Penguins dataset which includes three penguin species observed on three islands in the Palmer Archipelago, Antarctica. The data has been made available by Dr. Kristen Gorman and the Palmer Station, Antarctica LTER, a member of the Long Term Ecological Research Network.

*Column names for the penguins dataset include:*

* .species: penguin species (Chinstrap, Adelie, or Gentoo)
* .island: island name (Dream, Torgersen, or Biscoe) in the Palmer Archipelago
* .bill_length_mm: length of the bill in millimeters
* .bill_depth_mm: depth of the bill in millimeters
* .flipper_length_mm: length of the flipper in millimeters
* .body_mass_g: body mass in grams
* .sex: MALE or FEMALE

**See: https://allisonhorst.github.io/palmerpenguins/**

* Data Cleaning and Transformation

The data includes some missing values. We generally clean the data by removing rows with missing values and possibly transform the data to use columns that are more easily read (or use labels on charts and tables).

* Source:

From https://shiny.posit.co/py/docs/user-interfaces.html. This version has been modified slightly for hosting with GitHub Pages.

## Tools

- Python
- Shiny for Python
- VS Code + Python Extension
- Git
- GitHub

## Try in the Browser

Go to PyShiny Templates at <https://shiny.posit.co/py/templates/>.
Go to Dashboards / Basic Dashboard.

- <https://shiny.posit.co/py/templates/dashboard/>

## Reference App with Detailed Instructions

For more detailed instructions, see <https://github.com/denisecase/pyshiny-penguins-dashboard-express>.
That project README.md has more detailed instructions, including reminders for Mac and Linux. 

## Get the Code

Fork this project into your own GitHub account.
Clone **your** GitHub repo down to your local machine.
IMPORTANT: Use your GitHub **username** in place of denisecase.
[GitHub CLI](https://cli.github.com/) may work better on some machines.

```shell
git clone https://github.com/Priyankanaskar/cintel-07-tdash
```
## Publish the App with GitHub Pages (one-time setup)

The first time you set up an app, you'll need to navigate to the repository on GitHub and configure the settings to publish the app with GitHub Pages. After configuring the repository once, each time you push changes to the main branch, the app will automatically update.


1. Go to the repository on GitHub and navigate to the Settings tab.
2. Scroll down and click the Pages section.
3. Select branch main as the source for the site.
4. Change from the root folder to the docs folder to publish from.
5. Click Save and wait for the site to build.
6. Edit the "About" section of the repository to include a link to the live app.

## Run Locally - Initial Start

After cloning your project down to your Documents folder, open the project folder for editing in VS Code.

Create a local project virtual environment named .venv, activate it, and install the requirements.

When VS Code asks to use it for the workspace, select Yes.
If you miss the window, after installing, select from the VS Code menu, View / Command Palette, and type "Python: Select Interpreter" and select the .venv folder.

Open a terminal (VS Code menu "View" / "Terminal") in the root project folder and run these commands (for Windows - the activate command is slightly different Linux/Mac).

```shell
py -m venv .venv
.venv\Scripts\Activate
py -m pip install --upgrade pip setuptools
py -m pip install --upgrade -r requirements.txt
```

Open a terminal (VS Code menu "View" / "Terminal") in the root project folder and run these commands.

```shell
shiny run --reload --launch-browser app/app.py
```

Open a browser to local host ("http://[::1]:8008/") and test the app.

## Run Locally - Subsequent Starts

Open a terminal (VS Code menu "View" / "Terminal") in the root project folder and run these commands.

```shell
.venv\Scripts\Activate
shiny run --reload --launch-browser app/app.py
```

While the app is running, the terminal is fully engaged and cannot be used for other commands. 
To kill the terminal, click the trashcan icon in the VS Code terminal window. 

## After Changes, Export to Docs Folder

Export to docs folder and test GitHub Pages locally.

Open a new terminal (VS Code menu "Terminal" / "New Terminal") in the root project folder and run these commands. 
Remember to activate the environment first. 

```shell
.venv\Scripts\Activate
shiny static-assets remove
shinylive export app docs
py -m http.server --directory docs --bind localhost 8008
```

Open a browser to ("http://[::1]:8008/") and test the Pages app.

## Push Changes back to GitHub

Open a terminal (VS Code menu "Terminal" / "New Terminal") in the root project folder and run these commands.

```shell
git add .
git commit -m "Useful commit message"
git push -u origin main
```

## Enable GitHub Pages

Go to your GitHub repo settings and enable GitHub Pages for the docs folder.

## Resources

Example csv data from penguins.csv. Used for review only. In the app, we import the data from the palmerpenguins package.

* Palmer Penguins published in:

Horst AM, Hill AP, Gorman KB (2020). palmerpenguins: Palmer Archipelago (Antarctica) penguin data. R package version 0.1.0. https://allisonhorst.github.io/palmerpenguins/. doi: 10.5281/zenodo.3960218.
Data originally published in:

Gorman KB, Williams TD, Fraser WR (2014). Ecological sexual dimorphism and environmental variability within a community of Antarctic penguins (genus Pygoscelis). PLoS ONE 9(3):e90081. https://doi.org/10.1371/journal.pone.0090081
The Shiny development team. Shiny for Python [Computer software]. https://github.com/posit-dev/py-shiny

## Contributing

**Special Thanks to Dr.Case for guidence and controbution on this project.**