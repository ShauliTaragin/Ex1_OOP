# Exercise 1 Object-Oriented Programming
Offline Algorithm, designing a smart elevator system.

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

The first 3 steps of our algorithm is  to design and plan all the exterior code. i.e utilizing every piece of information we can gather, and creating helper function and objects to insure we can create a clean and elegant algorithm.

Firstly are agenda is to use all the information available to us as one should in an offline oriented algorithm.The data we will exploit is  the number of elevators in the building, the Calls information such as (Call source, Call destination, Call time) and attributes of the elevators.

The next step we will take in designing our algorithm is implementing the following objects (Building, Elevator, Calls).

The last design step is to elaborate the objects we created. The calls class will help us read and write easily from a csv file. The elevator class will contain 2 synchronized lists. One of floors and a second list of time, representing when we will reach each floor in our floor list. This  in addition to all the properties of an elevator. These 2 lists represent at what time will the elevator reach the floor that it needs to stop at. (e.g time[i]=10 , floors[i]=135.25321. meaning will stop at floor 10 at time 135.25321)  

**Now for the algorithm itself:**

When reading each call(src, dst, time of call, building) we will iterate through all the elevators in our building. For each elevator we will create a copy elevator. Using a helper function(_add_call_ explained in the next paragraph) we will "simulate" adding the src and dst to their respected positions in the floors and time lists of our copy elevator. We will then calculate the time each person in the elevator was delayed by as an effect from the addition of the new call. After finishing iterating and checking the insertion in all the elevators the elevator that will delay the least amount of time will be the elevator we assign the call to.

_add_call_- In this auxiliary function we recieve a floor(either src or dst) and the time we estimate the elevator should reach that floor. if the length of the lists (floors and time) of the elevator are less then 2 we simply append the call to the end of the lists. Otherwise, we search in our time list when is the first time the time of the new call is greater than a call already in the list. if the floor of the new call is between the floors of the current location in the list, we add the call there. Otherwise ,  we continue to iterate over the time list. Finally if we reached the end of the list we add the call there. No matter where the call was added we update the times list as factored by the addition of the new call added.

Upon termination of this function are elevators lists are updated to represent at what time the elevator will be in which floor. 


---------

## Code Details


Unified Modeling Language (UML) :

<p align="center">
<img align="center" src="https://s8.gifyu.com/images/UML.png" />
</p>


Our class Building reading a json with containing a building with minimum floor and maximum floor, list  of elevators
we added a numbers of elevators function to help us in later.  Elevator class contains all information about each elevator speed close time doors etc.. 
Calls class is reading the csv and write output csv contain list of calls with all the calls in the csv, in additional we have set target function that re-write the (-1) value with the new elevator the algorithm choose for.
in the main class the heart of the project contain update time function that over of all the new calls that the algorithm decide to insert to the list, and the major function allocate elevator which the heart of the algorithm calculate the best elevator to give us with all parameters and calculated time between all elevators we got in the case.



---------
<!-- results -->
## Results

Our best Results:

|Building B1-B5|Call Case|Average Waiting Time|Number of incomplete calls|
|---------|---------|---------|---------|
|B1|a|15.12|10|
|B2|a|19.12|9|
|B3|a|18.12|8|
|B3|b|18.12|8|
|B3|c|18.12|8|
|B3|d|18.12|8|
|B4|a|17.12|7|
|B4|b|17.12|7|
|B4|c|17.12|7|
|B4|d|17.12|7|
|B5|a|16.12|6|
|B5|b|12.12|5|
|B5|c|16.12|6|
|B5|d|16.12|6|

Information: the first column is the cases with the B1,B2,B3,B4,B5, the second column is the call cases a,b,c,d the third column is the average waiting time of all calls the forth column is  the number of incomplete calls mains that the algorithm is missed a calls.

As you can see our results after analyzing the code, after going over all the results for the different cases we decided to present the best results for us
that results give us a boost in motivation for develop and improve the code to maximum performance with the minimum of issues or errors.



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
