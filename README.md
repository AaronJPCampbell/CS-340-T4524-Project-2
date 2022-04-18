# CS-340-T4524-Project-2
## About the Project
This project provides a dashboard through which a user can access a database of animals in an animal shelter, and filter the results based on predetermined filter options (in this case radio options).

## Motivation
This project sets the framework for creating a dashboard to access a MongoDB database, and display/filter the results as desired.  MongoDB is a great choice for a project such as this because it can be run either locally or in a cloud based environment.  That means the database can be accessed from multiple different systems, which can each be running a variation of this dashboard. 

The current database being used is an animal shelter database which lists all animals and their sex, age, location, and all other pertinent information.  Grazioso Salvare requested a dashboard which would allow the user to view the database, and filter the results based on certain attributes.  This would allow the user to identify dogs that are good candidates for search-and-rescue training.

## Getting Started
In order to get started, you must first import your data (the AAC spreadsheet which contains data for animals in an animal shelter) into MongoDB, and download the provided Python files, as well as the Dashboard program.  The program is currently set to access MongoDB through the ‘aacuser’ user account, so this might have to be edited to suit your own needs.

## Installation
In addition to the provided files, the following programs/tools will also be required:
* MongoDB
  * The database program we will be using
  * https://www.mongodb.com/docs/manual/administration/install-on-linux/
* Jupyter Notebook
  * Allows for composition and testing of code and script files
  * https://jupyter.org/install
* The latest version of Python
  * https://opensource.com/article/20/4/install-python-linux

## Creating the Dashboard and Challenges
As mentioned above, this program is designed to provide a dashboard to access a database.  I took the code provided by SNHU, and some of the code from the previous project submission, and that gave me a dashboard with a working map.  However, at this point, there were no images or filter options available.  Adding the image was fairly simple, and, after doing some research, I settled on adding in radio options for filters, as they seemed to be fairly straightforward.  This is where I ran into an early challenge: I found that I was able to implement them, but they didn’t actually do anything.  I realized there were a few typos, mostly due to how many parentheses/brackets were necessary for the filter code.  There were also a few instances where I neglected to put in the correct variables, and placeholder variables were listed instead.  Still, after correcting these mistakes, the radio options did not have any effect on the displayed data.  As a result, the code I provided, as of right now, is not fully functional.  The framework is there, and it is able to display the dashboard and image as intended, but I was unable to get it to apply filters as desired (the console does provide an error message, but I honestly wasn’t sure what it meant, and looking it up provided little insight).  Another issue is I was unable to display the graph as intended, and I believe this is tied to the error with the filter code.

## Roadmap
As mentioned above, the current code does not support all of the desired functionality.  Any future development would focus on correcting the current bugs/errors and making sure all desired functionality is implemented.

## Contact
Your name: Aaron Campbell
