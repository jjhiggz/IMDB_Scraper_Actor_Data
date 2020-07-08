# IMDB Scraper
> Input an actor URL, return a Nested Data Structure of information about that actor, including all the movies they've been in

## Intro
My first programming project (back in January 2020) was building this silly little Bill Murray CLI movie rating app using Ruby with my classmate and good friend Todd Carlson. 

> Here you can see that although the app wasn't that great, our classmates still got a kick out of it https://www.youtube.com/watch?v=i6CNisYx1Uw&feature=youtu.be

In order to turn this app from something useless into something usefull, there was one crucial element missing. The app needed to actually contain data on all of the Bill Murray movies that exist. The problem is that Bill Murray stars in like 72 movies or something insane, and as a programmer it felt wrong to manually input all of those movies. So I decided to build a scraper that would allow you to do this, not only for Bill Murray, but for any actor/actress on IMDB. 

## Tech
For now this application runs through a pipenv virtual shell and uses the requests, beautiful soup, lxml, and ipython libraries. 

- requests
    This is used to get the html from a website as a raw text file

- beautiful soup (bs4)
    This is python's most common library for parsing the html text file

- lxml
    This is the parser that I chose to pass into beautiful soup. Apparently it  runs more efficiently than bs4's built in httparser.

- pipenv
    This python module is used to set up a Python virtual environment. first you run this command to set up your dependenccies
    ```
    pipenv install
    ```
    Then run this command to enter your virtual pipenv environment
    ```
    pipenv shell
    ```
## Using the App

After you have your environment set up all you need to do is change the variable 'input' to be the IMDB URL of the actor/actress you wish to collect data on. 

Then run the following command to run the script 
```
python IMDB_scraper.py
```

This will take 30 sec to 15 minutes to run depending on which actor/actress you choose. The more movies they were in the longer this will take. After it runs, you will be caught in the embed() debugger tool that comes wiwth the 'ipython' library. 

While in this debugger playground the data structure is called actor_data. You can feel free to search through it or play around. You can print that from the terminal, or write code to export that data structure into your application. 

## Greatest Challenge
The greatest challenge that I encountered while building this application was working with Python's package manager and virtual environments. Let me explain what I learned in case you run into similar issues. 

- ### Mac has python 2.7 installed, and you can't delete or change that
    Don't go down a rabbit hole trying to change your mac to default to from python 2.7 to python 3. Apparently there is some ancient architectural software on many macs that is written in python2 so if you actually did manage to achieve this you could mess up your computer. 

    instead just use python3 when you want to use python 3, if you want to use pip, use pip3 when you want to install  a python3 package using pip.
    
- ### pipenv vs virtualenv
    pip is Python's package manager and it always likes to install packages globally to a project. So how do we deal with versioning issues? The answer is that we have to create a virtual environment to trick pip (so to speak) into installing into that virtual environment's root rather than the r0ot on your computer. 
    
    Virtualenv is a means of doing that turns a directory into a virtual machine. It does this by installing a bunch of files that turn that directory into a virtual machine.

    pipenv instead works by installing a pipfile, which acts to track the dependencies of your project. Then you turn your terminal into a virtual machine by running the pipenv command. I found this means alot more elegant as it made shareabilty of the project better. 
    
## Future Improvements

At some point I'd really like to implemnent the following feateres on this project

- database integration
    This project would be a lot more useful if it stored data that users looked up. Especially given the long run time for the algorithm. Soon I would like to set this project up to have a backend endpoint allowing users to use this app as a legitimate alternative to IMDB for small non-profit projects. 
- Frontend Interface
    At some point it might be nice to allow users to interact with the database in a more friendly format. Although admittedly it might not be the best use of time to invest into a website based off of a data-scraper when unfortunately at any moment IMDB could change their algorithms and render this scraper entirely useless.

## Summary

I had a blast building this project. I learned a whole lot about python's virtual environment and package manager , and also figured out how easy and powerful building a web scraper could be!. 


