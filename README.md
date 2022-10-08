
<h1 align=center> HEREDO </h1>


<p align=center>

 </p>

<img  src="media/readme/mockup.png">


Live app link [here](https://heredo.herokuapp.com/)



## Table of contents
1. [Introduction](#Introduction)
2. [UX](#UX)
    1. [Ideal User Demographic]
    2. [User Stories](###User Stories)
    3. [Development Planes]
    4. [Design]
3. [Features]
    1. [Design Features]
    2. [Existing Features]
    3. [Features to Implement in the future]
4. [Issues and Bugs]
5. [Technologies Used]
     1. [Main Languages Used]
     2. [Additional Languages Used]
     3. [Frameworks, Libraries & Programs Used]
6. [Testing](#Testing)
     1. [Testing.md]
7. [Deployment](#Deployment)
     1. [Deploying on Heroku]
     2. [Forking the Repository]
     3. [Creating a Clone]
8. [Credits]
     1. [Content]
     2. [static/Media]
     3. [Code]
9. [Acknowledgements]



## UX




### User Stories



<details>
<summary> As a user, I would like to be able to:  </summary>

1. Login/Register to the platform.
2. View all products. 
3. Filter products by wine type, gifts, mistery box.
4. Sort products by category, rating and price. 
5. View a detailed page of each product.
6. Add to cart a desired product.
7. Delete or update quantity of the product in cart. 
8. Checkout safely.
9. Receive order confirmation.


</details>

<details>
<summary>
 As a logged user, I would like to be able to:
</summary>

1. View order history.
2. Update personal details. 

 
</details>


<details>
<summary>
 As an admin, I would like to be able to:
</summary>

1. Add a new product.
2. Delete/Update product.

 
</details>

## 1. Strategy

 + **Project Goal**
  


## 2. Scope 

As a project owner, I would like to create :

An online shop and website for the Heredo winery. The goal is to enable its users to get to know more information about the winery, be able to contact the owners, research their products and even buy wine or other products from them. 



[Back to top ⇧](#)

## 3. Structure


[Back to top ⇧](#)

## 4. Skeleton


[Back to top ⇧](#)

### 1.  wireframe

<img width="500" src="media/readme/wireframes/1.png">



### 2.  wireframe

<img width="500" src="media/readme/wireframes/2.png">


### 3. e wireframe

<img width="500" src="media/readme/wireframes/6.png">


### 4. wireframe


<img width="500" src="media/readme/wireframes/5.png">


### 5.  wireframes

 + Login page:

<img width="500" src="media/readme/wireframes/3.png">

+ Register page:

<img width="500" src="media/readme/wireframes/4.png">

[Back to top ⇧](#)

## 5. Surface


* Colors


<img width="300" src="media/readme/color_palette.jpg">


* Font selection


<img width="500" src="media/readme/fonts.png">

[Back to top ⇧](#)

## Functional Scope 
**Heredo Flowchart**

<img width="500" src="media/readme/flowchart.jpeg">

**Agile Methodology**


<img width="500" src="media/readme/agile.png">


<details>
<summary>All sprints are described here.</summary>

Test cases were linked with every User story presented above, and can be found in TESTING.md(TESTING.md) - Automated testing section. 

* Sprint 1

  + Base template
  + Setup Allauth



* Sprint 2
  + Setup Home App

  

* Sprint 3
  + Setup Products app
  + Setup Bag app


* Sprint 4
  + Setup Checkout app
  + Setup Profile app
  + Toasts


* Sprint 5

  + Setup Admin profiles: add/update/delete product
  + Setup Real Time Email
  + Heroku Deployment 

* Sprint 6

  + Create final tests + TESTING file
  + README file

</details>

[Back to top ⇧](#)

## Features

1. Home Page

2. Products Page

3. Product detail page

4. Admin Product management pages : 
* add product page
* edit product page
* delete product button

[Back to top ⇧](#)

## Future Features

I would like to implement the following features: 


[Back to top ⇧](#)


## Languages Used



## Frameworks, Libraries & Programs Used


[Back to top ⇧](#)

## Testing and Code validation 
All code validation and test details can be found [here](TESTING.md).

## Project Bugs and Solutions:

| Bugs              | Solutions |
| ---               | --------- |
| When deploying, the website CSS and database were failing on Heroku. | Debug Update and transfer all data to Postgres. A model did not have a slug as per old migrations.

[Back to top ⇧](#)

## Deployment 

This App is deployed using Heroku.

<details>
<summary>Deployment steps </summary>
 
 1. Ensure all apps are listed on requirements.txt. 
 
Command:  ` pip3 freeze > requirements.txt`. 
 
2. Setting up your Heroku
 
  2.1 Login to Heroku and enter your details: 
  command: ` Heroku login -i` 

    
  2.2 Get your app name from Heroku.
    command: `Heroku apps`
    

  2.3 Set the Heroku remote. 
    command: `Heroku git: remote -a woofmeapp`
    

  2.4 Add, commit, and push to GitHub
    command: `git add. && git commit -m "Deploy to Heroku via CLI"`

  2.5 Push to both GitHub and Heroku
    `command: git push origin main`
    `command: git push Heroku main`
       
</details>

[Back to top ⇧](#)

# Credits

## Media

+ All pictures and images used in this project are from [Pexels](https://pexels.com).

### Work based on other code


[Back to top ⇧](#)

# Acknowledgements

[Back to top ⇧](#)
