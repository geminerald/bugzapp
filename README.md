# BugZapp

[![Build Status](https://travis-ci.org/geminerald/bugzapp.svg?branch=master)](https://travis-ci.org/geminerald/bugzapp)

An Online Bug tracker offering convenient ways to monitor and update statuses of bugs on your software. Fully customisable. 

Offering a trial for projects operated by me where users can submit bugs or feature requests for websites or games created by me. 

Alternatively users can buy the system for use on their own projects. The third option would be to select to purchase multiple copies of the system to use in a business setting.

Free version only allows creation of tickets for sites or games which I own (for testing, user feedback etc.) Were this project to be developed commercially it would create an organisation model which would only load bugs associated with a specific organisation or user. 

Click [here](https://bugzapp.herokuapp.com/) to view the deployed project.

## Contents:

- [UX](#user-experience)
    - [Project Goals](#project-goals)
    - [User Goals](#user-goals)
    - [Site Owner Goals](#site-owner-goals)
    - [User Stories](#user-stories)
    - [User Requirements and Expectations](#user-requirements-and-expectations)

- [Design](#design)
    - [Fonts](#fonts)
    - [Icons](#icons)
    - [Colours](#colours)
    - [Styling](#root-styles)
    - [Images](#images)
    - [Backgrounds](#backgrounds)

- [Planning](#planning)
    - [Wireframes](#wireframes)
    - [Site Map](#site-map)
    - [Informational Architecture](#informational-architecture)

- [Features](#features)
    - [Implemented](#developed-features)
    - [In Development](#features-in-development)
    - [To be Developed](#features-to-be-developed)

- [Technologies](#technologies)
    - [Languages](#languages)
    - [Libraries](#libraries)
    - [Tools](#tools)

- [Testing](#testing)
    - [Automated Testing](#automated-testing)
    - [Manual Testing](#manual-testing)
    - [User Testing](#user-testing)
    - [Code Validation](#code-validation)
    - [Testing Against User Stories](#testing-against-user-stories)

- [Bugs](#bugs)

- [Deployment](#deployment)
    - [Running Locally](#running-this-project-locally)
    - [Deploying to Heroku](#deploying-bugzapp-to-heroku)

- [Credits](#credits)


## UX

### Project Goals

The goal of this project is to provide a service to track issues with software, either individually or on a team. Users will be able to create accounts, log in, store details of their issues and update
the issues as required.

### User Goals

* Create bug reports and track them to resolution.
* A visually appealing and straightforward design.
* A fully responsive service that operates the same across all devices.
* Have an overview of currently reported issues.

### Site Owner Goals

* Provide users with a service to track their software issues and generate revenue from paid version/ subscription.
* Generate revenue with advertising space targeted at software teams since this is the target audience.

### User Stories


| As a | I want to | So that I can |
| --- | --- | --- |
| User | Create Bug Reports |  let the relevant people know of issues |
| User | Have a fully responsive service |  access tickets across all devices |
| User | Be able to try the service before I buy it |  be confident in  my purchase |
| User | Create an account and have the website repond accordingly |  access secure areas of the website |
| User | Purchase the software securely  | use the system myself without risking my personal data |
| Site Owner | Receive bug reports and feature requests | improve my work |
| Site Owner | Generate revenue by selling this software | afford to work more on my own projects |
| Site Owner | Learn Django | create websites quickly and effectively |


### User Requirements and Expectations

These days internet shopping is more common than ever - yet as people become more familiar with it they also become more cautious and savvy with their purchases.
Therefore providing the best UX, proper authentication and using secure payment gateways (in this case Stripe) is necessary to offer the best solution.

#### User Requirements

* Interact with a visually appealling and intuitive website.
* Navigate with ease on any device.
* Quickly grap the basic function and controls of the website and service.
* Choose the version you wish to use (Free, Trial or Paid) and purchase it quickly and easily.
* Create new bug reports and add them to the database.
* Update bugs with a few clicks.
* Can reach out to the developer as required.


#### User Expectations

* Safe storage of any details provided.
* No payment information stored - once the transaction is completed the business has no need to store the user's payment information.
* Service can be used across any device with no drop in functionality.
* Easy and intuitive navigation.

## Design

As this is targeted at the technology sector the colour scheme is based on a 'Dark Mode' colour palate since this is common and preferred in this sector and is also prevelant in the imagery of
technology. The colour scheme was taken from [coolers.co](https://coolors.co/1e1e1e-3700b3-03dac6-bb86fc-fdfffc) and is currently as follows:

### Colours

The colour scheme was based on a "Dark Mode" theme - this is extremely popular with developers and IT professionals and so was chosen to reflect the target audience.

Most people report that dark mode themese are easier on the eyes for people who have to spend extended periods looking at a screen. The classic dark mode colours are a dark background, white fonts and bright accent colours for contrast.

#### Colour Samples Table

Below is a table showing a sample of the colours chosen for this theme, the name of the colour according to [coolers](https://coolors.co/), the Hex ref and a description of the colour, what it is used for and why it was chosen.

| Placeholder | Name | Hex | Description |
| --- | --- | --- | --- |
| ![#3700b3](https://placehold.it/15/3700b3/000000?text=+) | **"Trypan Blue"** | #3700B3 | Selected as a colour that would stand out while keeping in the dark theme. |
| ![#03dac6](https://placehold.it/15/03dac6/000000?text=+) | **"Turquoise"**  | #03DAC6 | Selected as a similar colour but to stand out more for accent. |
| ![#bb86fc](https://placehold.it/15/bb86fc/000000?text=+) | **"Lavendar Floral"** | #BB86FC | A tertiary colour which would give contrast while not drawing attention |
| ![#fdfffc](https://placehold.it/15/fdfffc/000000?text=+) | **"Baby Powder"** | #FDFFFC  | The main white colour, used as a bright white |
| ![#efe9e7](https://placehold.it/15/efe9e7/000000?text=+) | **"Isabelline"** | #EFE9E7 | The softer off-white colour |
| ![#121212](https://placehold.it/15/121212/000000?text=+) | **"Rich Black Fogra"** | #121212 | Used where a harsh black colour was required for contrast. |
| ![#1e1e1e](https://placehold.it/15/1e1e1e/000000?text=+) | **"Eerie Black"** | #1E1E1E | Used as a standard background colour throughout the site |
| ![#cf6679](https://placehold.it/15/cf6679/000000?text=+) | **"Cinnamon Satin"**  | #cf6679 | Used as a ref flag, designed to stand out more than required red |
| ![#980707](https://placehold.it/15/980707/000000?text=+) | **"Dark Red"** |  #980707 | Used as a softer colour to highlight issues |
| ![#a1e44d](https://placehold.it/15/a1e44d/000000?text=+) | **"Inchworm"** | #a1e44d | Used for a success colour and also for hyperlinks |


#### Colour Code

This is the css code used for the various colours used in this project. 

```css

:root {
    --primary-colour: #3700B3; 
    --secondary-colour:#03dac6;
    --tertiary-colour:#bb86fc;
    --white-colour:#fdfffc;
    --off-white-colour:#efe9e7;
    --background-grey:#1e1e1e;
    --black-colour:#121212;
    --required-colour:#980707;
    --error-colour:#cf6679;
    --success-colour:#a1e44d;

}

```

### Fonts

The **Archivo** font was chosen for this project as it was **clear** and **concise** with a variety of different font weights available. It is **similar to Helvetica** which is well known throughout the technology field as a popular choice for website design.

### Icons

The icons for this project came from [Font Awesome](https://fontawesome.com/6?next=%2F) as they are universally highly regarded as having a great selection of icons for development.

### Images

The images for this project were largely taken from [Pexels](https://www.pexels.com/) which has been a great resource for stock and background images. 

### Backgrounds

[Home Page Background](https://www.pexels.com/photo/illuminated-cityscape-against-blue-sky-at-night-316093/) courtesy of [Pixabay](https://www.pexels.com/@pixabay)

## Planning

### Wireframes

To view the wireframes for this project please go to the [Wireframes Folder](https://github.com/geminerald/bugzapp/tree/master/wireframes)

### Site Map

![alt text](https://raw.githubusercontent.com/geminerald/bugzapp/master/wireframes/Sitemap.JPG "Sitemap")

### Informational Architecture

#### Bug Model

| Name | DB Name | Validation | Type |
| --- | --- | --- | --- |
| Title | title | max_length=70 | CharField |
| User | user | User, on_delete=models.CASCADE, null=True, blank=True | ForeignKey |
| Description | description | None | TextField |
| Type | type | max_length=7, choices=TYPE_CHOICES | CharField |
| Status | status | max_length=20, choices=STATUS_CHOICES, default="opened" | CharField |
| Creation Date | creation_date | auto_now_add=True | DateTimeField | 
| Score | score | default=0 | IntegerField |

#### Order Model

| Name | DB Name | Validation | Type |
| --- | --- | --- | --- |
| Order Number | order_number | max_length=32, null=False, editable=False | CharField |
| Full Name | full_name | max_length=50, null=False, blank=False | CharField |
| Email Address | email | max_length=254, null=False, blank=False | EmailField |
| Phone Number | phone_number | max_length=20, null=False, blank=False | CharField |
| Street Address 1 | street_address1 | max_length=80, null=False, blank=False | CharField |
| Street Address 2 | street_address2 | max_length=80, null=True, blank=True | CharField |
| Town or City | town_or_city | max_length=40, null=False, blank=False | CharField |
| County | county | max_length=50, null=False, blank=False | CharField |
| Postcode | postcode | max_length=20, null=True, blank=True | CharField |
| Order Date | date | auto_now_add=True | DateTimeField |
| Order Total | order_total | max_digits=10, decimal_places=2, null=False, default=0 | DecimalField |


## Features

### Developed Features

- Home Page
- Authentication System
- Checkout System
- Cart System
- Cart Page
- Payment System
- Checkout & Payment Page
- User Model
- Ticket Model
- About Page
- Search Bugs System

### Features in Development

- Sort and Filter System

### Features to be Developed in Future

- Organisation Model
- Profile Page
- Tags System
- Upvoting System

## Technologies

### Languages

- HTML
- CSS 
- JavaScript 
- Python 
- Git 

### Libraries

- Bootstrap
- jQuery
- Django

### Tools

- Gitpod
- Stripe
- Whitenoise
- Django Crispy Forms
- GitHub
- GitPod

<br>

## Testing

<br>

### **Automated testing** 

Automated Testing was implemented on this project from an early stage using [**Travis**](https://travis-ci.org/). Travis allows the results of their testing to be shown in realtime in a readme file - it is available near the top of this readme and also here: 

[![Build Status](https://travis-ci.org/geminerald/bugzapp.svg?branch=master)](https://travis-ci.org/geminerald/bugzapp)

Travis ran automated testing on the code at each push and notified me via email of any issues.

In this way many errors were caught before they became embedded in the code and/or difficult to find. This also allowed errors to be more easily identified due to the frequency of the Travis tests and the log of the tests run by Travis. 

<br>

### **Manual Testing**

Manual testing was undertaken throughout development to ensure that all features were functioning and also that new features were not interfering with previously implemented ones. The following is an example of manual testing undertaken by the devleoper throughout development.


****

**System to Test:** Navigation

**Actions Taken:** Firstly layout was important, ensuring that the navbar was consistent throughout the project by including it in the base template helped ensure there was less chance of an error. Apart from this it was ensured that all links went to the correct place by clicking on them.

**Result:** All links functioned as expected throughout and were corrected in the cases where there had been an error.

**Conclusion** Navigation works as designed and is modular enough to allow for future updates if needed.

****

**System to Test:** Order Cycle

**Actions Taken:** Go to checkout, select product, proceed to checkout with fake details. 

**Result:** Order placed when correct info entered and appropriate messaging appeared for invalid info.

**Conclusion** Orders placing as required and good user feedback provided. 

****

**System to Test:** Create Tickets

**Actions Taken:** Navigate to Add Ticket page (via main navbar available on all pages). Required fields entered.

**Result:** Tickets adding to db and showing correctly in tickets page.

**Conclusion** System functional.

****
**System to Test:** View Tickets

**Actions Taken:** Navigate to view tickets page. Tickets showing correctly in this page with clear layout of all available information and can view more details on individual tickets. 

**Result:** Viewing tickets works as expected.

**Conclusion** System working as designed. 

****

**System to Test:** Search Tickets

**Actions Taken:** Searched for tickets using title and keyword. System handles appropriately including messaging if no applicable tickets. 

**Result:** Information was displayed correctly and good feedback provided to users. 

**Conclusion** Tickets can be searched as expected.

****

**System to Test:** Checkout

**Actions Taken:** Entered credit card info from the Stripe website both correctly and incorrectly to ensure that validation was working as it should.

**Result:** Card info was accepted and validated correctly. Correct Error info shown.

**Conclusion** Checkout system is functional.

****


**System to Test:** Negative Order Value

**Actions Taken:** Selected to purchase a negative quantity of a product. This threw an error so changed quantity to a select to stop this.

**Result:** Users can no longer select a negative value for quantity. 

**Conclusion** The bug is fixed.

****

<br>


###  **User Testing**

The project was demonstrated to multiple users throughout development. The users in question were primarily my family and friends. I am fortunate in this regard as in this group there are people who would be within the target audience including professional developers and technology professionals and also complete novices who are unfamiliar with the industry.

The users who tested the project who were not in the target audience helped ensure that it was kept simple and straightforward and that there was sufficient explanation for elements. This helps ensure that if launching this project it would not have any issues with new users. 

The other users who would be more tech savvy also helped ensure that it would be intuitive for people within the industry and that it had the key features that mattered to them. I would like to particularly thank [Deborah Boyewa](https://www.linkedin.com/in/deborah-b-6474b7158/), [Shane Quinn](https://www.linkedin.com/in/shanequinn/) and [Steven Verjans](https://www.linkedin.com/in/stevenverjans/) for their assistance in this matter. 


****

**System to Test:** Layout

**User Feedback:** Users were asked to sign up and navigate around the website to specific places. No assistance was provided to them to ensure that any issues were discovered and noted. 

**Actions Taken:** Extra links were added which lead to the same place, for example there are multiple links to the "Sign Up" page to ensure that whichever way people found out that they wanted to they were able to sign up for an account.

**Result:** It is now very intuitive and simple to sign up for an account and navigate around the site by means of large buttons, icons on buttons and clear messaging.

**Conclusion** Success but more user feedback is always needed to strive to constantly improve. 

****

<br>

### **Code Validation**

Close attention was paid to formatting throughout this project. Formatting is vital when writing code as it allows other people (or the original writer at a later date) to quickly understand what the code is trying to achilve and be able to make alterations as needed. 

[Multiple articles](https://www.google.com/search?q=time+spent+reading+vs+writing+code&rlz=1C1CHBF_enIE796IE796&oq=time+spent+reading+c&aqs=chrome.1.69i57j0l2.5215j0j7&sourceid=chrome&ie=UTF-8) document that the time spent reading code is much higher than the time spent writing code and as such anything that can be done to improve this process, even to a small degree, is well worth doing. [One such article](https://www.informit.com/articles/article.aspx?p=1235624&seqNum=5#:~:text=Indeed%2C%20the%20ratio%20of%20time,is%20well%20over%2010%3A1.&text=Of%20course%20there's%20no%20way,makes%20it%20easier%20to%20write.) gives the approximate ratio of reading vs writing at over 10: 1.

It is also important to do this on an ongoing basis and not trying to refactor code to accommodate this at a later date since this essentially ensures that it will not be effective and is also not best practice for when working with others.

[GitPod](https://www.gitpod.io/) was the primary IDE used in the developement of this project and comes with a built in feature that allows errors and best practice opportunities to be shown in real time by means of underlining. This allowed me to keep the code clean and legible on an ongoing basis and be confident that I would be able to read and understand what I had written down at any point provided I ensured to address all the highlighted issues before comitting code. 

****
****

### Testing Against User Stories

| As a | I want to | So that I can | Test Run | Verdict |
| --- | --- | --- | --- | --- | 
| User |Create Bug Reports |  let the relevant people know of issues | Clicking Add Ticket to create a new bug report | Test Passes |
| User |Have a fully responsive service |  access tickets across all devices | Using Dev tools to ensure functionality accross tablet and mobile devices | Test Passes |
| User | Be able to try the service before I buy it |  be confident in  my purchase | Users can set up accounts and access base functionality | Test Passes |
| User | Create an account  |  access secure areas of the website | Trying to access checkout or ticket system while not logged in redirects to login page | Test passes |
| User | Purchase the software securely  | use the system myself without risking my personal data | Checkouts can be completed securely using Stripe which also handles security | Test Passes |
|  |  |  |  | |
| Site Owner | Receive bug reports and feature requests | improve my work | Tickets can be created and are shown in the Tickets page | Test Passes |
| Site Owner | Generate revenue by selling this software| afford to work more on my own projects | functionality is there - would just need to be updated on Stripe | Test Passes
| Site Owner | Learn Django | create websites quickly and effectively | I am able to create and run django projects and apps | Passing and ongoing |

## Bugs

****

**Issue:** Navbar was not fixed to top on scroll. 

**Actions Taken:** Added position fixed to nav and top 0

**Status:** Resolved

****
**Issue:** Login page failed to load due to allauth social tag.

**Actions Taken:** Reverted formatting changes to previous version

**Status:** Resolved

****
**Issue:** Admin Order Bug

**Actions Taken:** Tried removing full name and adding again and running migrations.

**Status:** Removed all migrations and added again

****
**Issue:** Products quantity bug

**Actions Taken:** When quantity was rmoved from basic models the site couldn't add, set hidden qty in formatting

**Status:** Resolved


****

**Issue:** No message displayed if no Q entered on tickets page. 

**Actions Taken:** Added logic to test for empty field and display appropriate messaging.

**Status:** Resolved

****
**Issue:** Notes will not save to a ticket due to validation errors. . 

**Actions Taken:** Views fields are being edited and form fields are being adjusted to try to get system working. Updated ticket object to resolve.

**Status:** Resolved
****
**Issue:** Selecting a negative quantity on checkout caused site to crash. 

**Actions Taken:** Changed quantity to a select element

**Status:** Resolved

****

## Deployment


### Running this project locally

To run BugZapp please follow the steps below!

Before starting make sure you have the following:

* An IDE (interactive development environment) such as [Visual Studio Code](https://code.visualstudio.com/) or [GitPod](https://www.gitpod.io/) (both are free)
* You <strong>MUST</strong> have the following installed on your machine if using Visual Studio:
* * <a href="https://pip.pypa.io/en/stable/installing/">PIP</a>
* * <a href="https://www.python.org/">Python3</a>
* * <a href="https://git-scm.com/">Git</a>
* You will also <strong>need to</strong> create an account with [Stripe](https://stripe.com/) in order to run this project.


#### Instructions

WARNING: You may need to follow a different guide based on the OS you are using, more info is avaiable [here](https://python.readthedocs.io/en/latest/library/venv.html)


* 1: <strong>Clone</strong> The BugZapp repository from [here](https://github.com/geminerald/bugzapp) or by entering the following into the command line:
```bash
git clone https://github.com/geminerald/bugzapp
```
* 2: <strong>Navigate</strong> to this folder in your terminal.
* 3: <strong>Enter</strong> the following command into your terminal.
```bash
python3 -m .venv venv
```
* 4: <strong>Initialize</strong> the environment by using the following command.
```bash
.venv\bin\activate
```

* 5: <strong>Install</strong> the requirements and dependancies from the requirements.txt file
```bash
pip3 -r requirements.txt
```

* 6: Within your IDE now <strong>create</strong> a file where you can store your secret information for the app, either using an env.py file or Visual Studio's settings.json.

* 7: <strong>Enter</strong> the following command into the terminal to migrate models into database.
```bash
python3 manage.py migrate
```

* 8: Then you need to <strong>Create</strong> a 'superuser' for the project using the terminal, enter the following command.
```bash
python3 manage.py createsuperuser
```

* 9: The app can now be ran locally using the following command.
```bash
python3 manage.py runserver
```

Congratulations, BugZapp is now running locally.

### Deploying BugzApp to Heroku

* 1: <strong>Create</strong> a requirements.txt file using the following command.
```bash
pip3 freeze > requirements.txt
```

* 2: <strong>Create</strong> a procfile with the following command.
```bash
echo web: python3 app.py > Procfile
```
* 3: Push these newly created files to your repository.
* 4: Create a new app for this project on the Heroku Dashboard.
* 5: Select your deployment method by clicking on the deployment method button and select GitHub.
* 6: On the dashboard, set the following config variables:

**Key**|**Value**
:-----:|:-----:
DATABASE\_URL|<your\_database\_url>
SECRET\_KEY|<your\_secret\_key>
SENDGRID\_API\_KEY|<your\_sendgrid\_api\_key>
STRIPE\_PUBLISHABLE|<your\_stripe\_publishable\_key>
STRIPE\_SECRET|<your\_stripe\_secret\_key>

* 7: <strong>Click</strong> the deploy button on the heroku Dashboard.
* 8: Wait for the build to finish and click the view project link once it has!

Congratulations, BugzApp is now hosted on Heroku and is live!

## Credits

Thanks to [Simen Daehlin](https://www.linkedin.com/in/simendaehlin?originalSubdomain=uk) - my mentor from Code Institute - for his feedback and constant belief and encouragement.

Thanks also to the [Code Institute](https://codeinstitute.net/) Tutors for their near endless patience and commitment.

Thanks to the hundreds of nameless people on [Stack Overflow](https://stackoverflow.com/) who answered my questions posted to google.

The Navbar elements were inspired by the [Dev Ed](https://github.com/developedbyed) [YouTube](https://www.youtube.com/channel/UClb90NQQcskPUGDIXsQEz5Q) channel. 
