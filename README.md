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

## Journal Questions
* How do you write programs that are maintainable, readable, and adaptable? Especially consider your work on the CRUD Python module from Project One, which you used to connect the dashboard widgets to the database in Project Two. What were the advantages of working in this way? How else could you use this CRUD Python module in the future?
  * Generally, when writing programs, in order to ensure that they are maintainable and readable, I try my best to format the code such that it is easy to read.  For instance, I make sure the indenting is correct, I try to put blank lines between different chunks of code, and will try my best to include comments as headers for these chunks of code.  I believe this also helps with keeping the code adaptable, as it makes it easier to find what needs to be changed/updated.  Prior to this project/course, I was aware of CRUD operations, but never really used them in code outside of very simple/direct operations.  For instance, if there was a CRUD method or operation in the code, it was often limited to a single variable, and another method had to be used for any other variable.  This course allowed me to see it in a more abstract and adaptable light, i.e. I was able to create and use CRUD operations that could be used to create/update/delete almost any attribute of the database dictionaries based on user input.  In the future, I can use this to hopefully create CRUD methods that are more universal. 
* How do you approach a problem as a computer scientist? Consider how you approached the database or dashboard requirements that Grazioso Salvare requested. How did your approach to this project differ from previous assignments in other courses? What techniques or strategies would you use in the future to create databases to meet other client requests?
  * When faced with a problem, my first step is to try to determine what the end goal is.  "What exactly needs to be implemented?"  From there, I will often break the project/to-do list into manageable sections, and work on them in whatever order I deem best.  I will also often consider past projects and see if I can utilize any experience from those to help with completing the current one.  However, for this database project, I had no past experience to reference, as this was my first time using MongoDB, and first time implementing HTML in an actual project.  For these reasons, I couldn't really reference previous projects for inspiration, and had to rely more on the textbook readings and outside research to assist me (although, as can be seen, I was still unable to fully complete the dashboard).  In the future, I think that my newfound experience with MongoDB will allow me to better understand database code, and I will be able to reference this project again should the need come up. 
* What do computer scientists do, and why does it matter? How would your work on this type of project help a company, like Grazioso Salvare, to do their work better?
  * A computer scientist does anything from designing algorithms to creating software to fulfill certain needs.  Essentially, all databse, program, CRM, or any other piece of software was designed by a computer scientist, or at the very least modified by one.  Without computer scientists, it would be impossible to work on computers, cloud computing would not exist, and we would still be storing all data through physical means.  As mentioned before, in addition to creating programs, computer scientists can also modify existing programs.  In this project, we modified an already existing dashboard to suit the needs of Grazioso Salvare.  Rather than sifting through an entire databse full of animals, we strived to implement filters that would allow for the database to be limited based on certain conditions.

## Contact
Your name: Aaron Campbell
