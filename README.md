
<h1 align=center> HEREDO </h1>


<p align=center>
This project is the website for Heredo family, my family's winery founded back in 2000s. </br>
We officially gave it a name last year and started branding this year. 
Heredo is all about wine culture and family heritage. 
</br>
Check it out to find more about our vineyards and buy yourself a bottle or more of good quality organic wine.

 </p>

<img  src="media/readme/mockup.png">


Live app link [here](https://heredo.herokuapp.com/)



## Table of contents
1. [Introduction](#Introduction)
2. [UX](#UX)
    1. [User Stories](###User Stories)
    3. [Strategy(##Strategy)
    4. [Scope](##Scope)
    5. [Structure](##Structure)
    6. [Skeleton](##Skeleton)
    7. [Surface](##Surface)
3. [Features]
    1. [Existing Features]
    2. [Features to Implement in the future]
4. [Issues and Bugs]
5. [Technologies Used]
     1. [Main Languages Used]
     2. [Additional Languages Used]
     3. [Frameworks, Libraries & Programs Used]
6. [Testing](#Testing)
     1. [Testing.md]
7. [Deployment](#Deployment)
8. [Credits]
     1. [Content]
     2. [static/Media]
     3. [Code]
9. [Acknowledgements](#Acknowledgements)



## UX




### User Stories

**Epic: Admin/Store Owner**

| ID  | Content                                                                                                                                                   |
| --- | --------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 1   | As a **store owner** I can log in so that I have full access to the store backend                                                                         |
| 2   | As a **store owner** I can add new product to the shop so that I can make sure the website is up to date                                                  |                                            |
| 3   | As a **store owner** I can edit/delete products so that I can make sure the website is up to date                                                         |                                                             | 4   | As a **store owner** I have created Facebook shop page to increase traffic on my website                                                                  |
| 10  | As a **store owner** I can read and respond to users questions sent by contact form                                                                       |

**Epic: Navigation**

| ID  | Content                                                                                                                      |
| --- | ---------------------------------------------------------------------------------------------------------------------------- |
| 12  | As a **user** I can see an interesting home page so that I can understand what shop sells                                    |
| 13  | As a **user** I can easily navigate through the site so that I can view desired content                                      |
| 14  | As a **user** I can easily find a navigation bar and footer so that I can see what content there is on the website           |
| 15  | Aa a **user** I can easily see the products list so that I can see what the store has to offer                               |
| 16  | As a **user** I can sort products by rating, price and category so that I can easily find what I'm looking for                   |
| 17  | As a **user** I can see the product details page so that I can see its name, rating, price, short description, year of harvest and ratings  |


**Epic: Purchase**
| ID | Content |
| --- | ----------- |
| 18 | As a **user** I can increase/decrease the quantity of the desired product.|
| 19 | As a **user** I can add a selected products into the shopping bag.|
| 20 | As a **user** I can see the shopping bag summary and total cost.|
| 21 | As a **user** I can remove items from shopping bag.|
| 22 | As a **user** I can put in my card details.|
| 23 | As a **user** I receive order confirmations on the email.|

**Epic: User Interaction**

| ID  | Content                                                                                                                                |
| --- | -------------------------------------------------------------------------------------------------------------------------------------- |
| 24 | As a **user** I get alerts about any changes I have made so that I have a clear understanding of what has been completed/updated/removed      |
| 25  | As a **user** I can connect to the social media sites so that I can follow them and keep up to date with their products and promotions |
| 26  | As a **user** I can contact the bookstore so that I can find out any information that I require                                        |
| 27 | As a **user** I can receive a contact confirmation email to let me know that my email has been sent                                    |



**Epic: Accounts**

| ID  | Content                                                                                                                  |
| --- | ------------------------------------------------------------------------------------------------------------------------ |
| 28  | As a **user** I can easily see if I'm logged-in or logged-out so that I can be sure what my status is                    |
| 29  | As a **user** I can log in/out off my account if I wish so that I can connect or disconnect from the website             |
| 30  | As a **user** I can register for an account so that I can use features for logged-in users                               |
| 31  | As a **user** I can receive a confirmation email when creating an account so that I know the registration was successful |
| 32  | As a **logged-in User** I can have my details saved so that I don't have to retype my address every time                 |

## 1. Strategy

 + **Project Goal**
  
  Create a project that allows its users to view, buy wine, create an account, view order history and have a simple, straightforward experience on Heredo winery's website.


## 2. Scope 

As a project owner, I would like to create :

* a simple, straightforward website with an intuitive UX experience.
* Clear and easy navigation for the user through each of Heredo's features.
* a visually appealing website on all devices.


[Back to top ⇧](#)

## 3. Structure

* The main Navbar  is fixed on top to facilitate Woofme users to navigate easily and pleasantly. 
* Layout is clear to allow Heredo users to navigate easily. 
* Login/Logout/Register options are present on the navbar to ensure that Woofme users can perform each of the actions easily.
* Enabling website admin to add/delete/edit product if logged in. 
* Home page with extra information about the winery and links to access the online store. 
* A secure and straightforward payment system to ensure the user has a pleasant experience when buying our wine.


[Back to top ⇧](#)

## 4. Skeleton

All wireframes are creating using Figma. 


[Back to top ⇧](#)

### 1. "All products" wireframe: 

<img width="500" src="media/readme/wireframes/all_products.png">



### 2. "Home-page" wireframe

<img width="500" src="media/readme/wireframes/home_page.jpg">


### 3. "Product detail" wireframe

<img width="500" src="media/readme/wireframes/product_detail.png">


### 4. "BAG" wireframe


<img width="500" src="media/readme/wireframes/BAG.png">


### 4. "Checkout" wireframe


<img width="500" src="media/readme/wireframes/Checkout.png">




### 6. "Allauth" wireframes

 + Login page:

<img width="500" src="media/readme/wireframes/3.png">

+ Register page:

<img width="500" src="media/readme/wireframes/4.png">

[Back to top ⇧](#)

## 5. Surface


* Colors


<img width="300" src="media/readme/color_palette.png">


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
* Shop section
* About section
* Vineyards section
* Contact section
* Gallery section
* Footer

2. Products Page

3. Product detail page

4. Admin Product management pages : 
* add product page
* edit product page
* delete product button

5. Bag Page

6. Empty Bag Page

7. Checkout success page. 

8. Profile page.

9. Allauth pages:
* Login
* Register

10. Header nav:
* Login button
* Bag button
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

+ Some pictures and images used in this project are from [Pexels](https://pexels.com) and some pictures are taken by me personally as this is my sister's winery.

### Work based on other code


[Back to top ⇧](#)

# Acknowledgements

[Back to top ⇧](#)
