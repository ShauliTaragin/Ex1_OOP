# Exercise 1 Object-Oriented Programming
Offline Algorithm

<!-- TABLE OF CONTENTS -->
<details open="open">
  <summary>Content</summary>
  <ol>
    <li><a href="#about-the-project">About The Project</a></li>
    <li><a href="#the-algorithm">The Algorithm</a></li>
    <li><a href="#code-details">Code Details</a></li>
    <li><a href="#results">Results</a></li>
    <li><a href="#languages-and-tools">Languages and Tools</a></li>
    <li><a href="#acknowledgements">Acknowledgements</a></li>
    <li><a href="#contact">Contact</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

Exercise 1 Object-Oriented Programming

This Exercise is a focus for learning python when it is actually a sequel to exercise 0 (performed in java). As usual, it is recommended to start planning the exercise (without a code) and only after we have a basic plan should we move on to the implementation phase of the code.
Similar to exercise 0, this exercise also opens an algorithm for a system of elevators and the amount of high-rise building.
In this exercise the challenge will be to deal with the offline version of the problem - meaning all the readings are given to us in advance, and we just need to stroke each reading in general (so that the rule of waiting for elevators is kept to a minimum). In fact the current exercise is mostly practical in the challenge of assigning a "call" to the elevator, but to accomplish this properly you will also need to understand and simulate the movement of the fillings.


"Good code is Its Own Best Documentation 📃"

---------

## The Algorithm

Our offline algorithm for elevators is designed as follows:

For the first time we use all the information available to us in an offline algorithm such as the number of elevators in the building, the Calls information such as (Call source, Call destination, Call times), We will implement the departments (Building, Elevator, Calls) for each elevator we will create 2 lists, one contains all the floors from the calls that are placed, the other contains all the times that the elevator runs its route to the destination call, we will go through all the elevators. For each elevator we will copy the calls that exist in it into a copy of a list of the same elevator. And we will check for each elevator- given the insertion of the source and destination call into the list in their correct location how long it will take for the elevator to make all its calls.
We will use the helper function that updates us on the total time it will take for the elevator to make all its calls (go through all the organs list "copy"). The elevator that will be assigned to the call is the elevator that will complete all its calls, including the new call that was completed in the shortest time.
After locating the optimal elevator we are called to the auxiliary function again only this time we will put in the original list of that elevator the new call in its correct location. And we'll bring back the same elevator.

---------

## Code Details


Unified Modeling Language (UML) :

![https://github.com/GalKoaz](https://s8.gifyu.com/images/UML.png)

here will be details about the classes with the functions deep information.


---------
<!-- results -->
## Results

Our best Results:

|Building B1-B5|Call Case|Average Waiting Time|Number on incomplete calls|
|---------|---------|---------|---------|
|B1|a|15.12|10|
|B2|b|19.12|9|
|B3|c|18.12|8|
|B4|d|17.12|7|
|B5|a|16.12|6|
|B4|b|12.12|5|

explanation about the Results why this exercise improve our skills and more ...

---------


## Languages and Tools

  <div align="center">
  
 <code><img height="40" width="40" src="https://upload.wikimedia.org/wikipedia/commons/thumb/c/c3/Python-logo-notext.svg/1200px-Python-logo-notext.svg.png"></code> 
 <code><img height="40" height="40" src="https://jupyter.org/assets/main-logo.svg"/></code>
 <code><img height="40" width="80" src="https://pandas.pydata.org/static/img/pandas_white.svg"/></code>
 <code><img height="40" width="70" src="https://upload.wikimedia.org/wikipedia/commons/d/d5/UML_logo.svg"/></code>
 <code><img height="40" width="40" src="https://upload.wikimedia.org/wikipedia/commons/thumb/1/1d/PyCharm_Icon.svg/1024px-PyCharm_Icon.svg.png"/></code>
 <code><img height="40" height="40" src="https://raw.githubusercontent.com/github/explore/80688e429a7d4ef2fca1e82350fe8e3517d3494d/topics/git/git.png"></code>
 <code><img height="40" height="40" src="https://raw.githubusercontent.com/github/explore/80688e429a7d4ef2fca1e82350fe8e3517d3494d/topics/terminal/terminal.png"></code>
  </div>


<!-- ACKNOWLEDGEMENTS -->
## Acknowledgements
* [Python](https://www.python.org/)
* [UML](https://en.wikipedia.org/wiki/Unified_Modeling_Language)
* [Git](https://git-scm.com/)
* [Jupyter](https://jupyter.org/)
* [Pandas](https://pandas.pydata.org/)
* [Git-scm](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)


<!-- CONTACT -->
## Contact

 Gal - [here](https://github.com/GalKoaz/)
 
 Shauli - [here](https://github.com/ShauliTaragin/)

Project Link: [here](https://github.com/ShauliTaragin/Ex1_OOP)
