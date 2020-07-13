# BugZapp

[![Build Status](https://travis-ci.org/geminerald/bugzapp.svg?branch=master)](https://travis-ci.org/geminerald/bugzapp)

An Online Bug tracker offering convenient ways to monitor and update statuses of bugs on your software. Fully customisable. 

Offering a trial for projects operated by me where users can submit bugs or feature requests for websites or games created by me. 

Alternatively users can buy the system for use on their own projects. The third optoin would be to select to purchase multiple copies of the system to use in a business setting.


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

- [Features](#features)
    - [Implemented](#developed-features)
    - [In Development](#features-in-development)
    - [To be Developed](#features-to-be-developed)

- [Technologies](#technologies)

- [Testing](#testing)

- [Bugs](#bugs)

- [Credits](#credits)


## UX

### Project Goals

The goal of this project is to provide a service to track issues with software, either individually or on a team. Users will be able to create accounts, log in, store details of their issues and update
the issues as required.

### User Goals

* Create bug reports and track them to resolution.
* Update bug reports.
* A visually appealing and straightforward design.
* A fully responsive service that operates the same across all devices.
* Have an overview of currently reported issues or historical data.

### Site Owner Goals

* Provide users with a service to track their software issues and generate revenue from paid version/ subscription.
* Generate revenue with advertising space targeted at software teams since this is the target audience.

### User Stories

* "I need a way to track issues for projects that I was working on. Notepad or sticky notes are just cluttered and often deleted or impossible to find" - John
* "I always think that you should let someone try a product before they buy it. It just makes it easier for everyone to get what they want" - Deborah
* "On a website you want to make sure that you only have the options you need - you don't want it cluttered up with hundreds of buttons you don't understand let alone use" - Victor

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
| ![#3700b3](https://placehold.it/15/3700b3/000000?text=+) | **"Trypan Blue"** | #3700B3 | Colour Info Here |
| ![#03dac6](https://placehold.it/15/03dac6/000000?text=+) | **"Turquoise"**  | #03DAC6 | Colour Info Here | 
| ![#bb86fc](https://placehold.it/15/bb86fc/000000?text=+) | **"Lavendar Floral"** | #BB86FC | Colour Info Here |
| ![#fdfffc](https://placehold.it/15/fdfffc/000000?text=+) | **"Baby Powder"** | #FDFFFC  | White |
| ![#efe9e7](https://placehold.it/15/efe9e7/000000?text=+) | **"Isabelline"** | #EFE9E7 | Off White |
| ![#121212](https://placehold.it/15/121212/000000?text=+) | **"Rich Black Fogra"** | #121212 | Black |
| ![#1e1e1e](https://placehold.it/15/1e1e1e/000000?text=+) | **"Eerie Black"** | #1E1E1E | Background Grey |
| ![#cf6679](https://placehold.it/15/cf6679/000000?text=+) | **"Cinnamon Satin"**  | #cf6679 | Error Red |
| ![#980707](https://placehold.it/15/980707/000000?text=+) | **"Dark Red"** |  #980707 | Required Red |
| ![#a1e44d](https://placehold.it/15/a1e44d/000000?text=+) | **"Inchworm"** | #a1e44d | Success Green |


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


### Root Styles

### Images

The images for this project were largely taken from [Pexels](https://www.pexels.com/) which has been a great resource for stock and background images. 

### Backgrounds

[Home Page Background](https://www.pexels.com/photo/illuminated-cityscape-against-blue-sky-at-night-316093/) courtesy of [Pixabay](https://www.pexels.com/@pixabay)

## Planning

### Wireframes

To view the wireframes for this project please go to the [Wireframes Folder](https://github.com/geminerald/bugzapp/tree/master/wireframes)

### Site Map

### Models

Bug Model

| Name | DB Name | Validation | Type |
| --- | --- | --- | --- |
| Title | title | max_length=70 | CharField |
| User | user | User, on_delete=models.CASCADE, null=True, blank=True | ForeignKey |
| Description | description | None | TextField |
| Type | type | max_length=7, choices=TYPE_CHOICES | CharField |
| Status | status | max_length=20, choices=STATUS_CHOICES, default="opened" | CharField |
| Creation Date | creation_date | auto_now_add=True | DateTimeField | 
| Score | score | default=0 | IntegerField |

Order Model

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

### Features in Development

- Ticket Model
- About Page

### Features to be Developed

- Organisation Model
- Profile Page
- Tags System
- Upvoting System
- Sort and Filter System
- Search Bugs System

## Technologies

### Core Technologies:

- HTML 5 
- CSS 
- JavaScript 
- Python 
- Git 

### Libraries/ Frameworks:

- CSS:
    - Bootstrap
    - Sass
- JavaScript:
    - Sweet Alerts
    - Stripe

- Python:
    - Django

- Git:
    - GitHub
    - Gitpod

### API/ External Resources:

- Gitpod
- Stripe

## Testing

**Automated testing** was implemented on this project from an early stage using **Travis**.

Travis ran automated testing on the code at each push and notified me via email of any issues.

In this way many errors were caught before they became embedded in the code and/or difficult to find.

**Manual Testing**



**User Testing**

**Code Validation**

Close attention was paid to formatting throughout this project. Formatting is vital when writing code as it allows other people (or the original writer at a later date) to quickly understand what the code is trying to achilve and be able to make alterations as needed. 

[Multiple articles](https://www.google.com/search?q=time+spent+reading+vs+writing+code&rlz=1C1CHBF_enIE796IE796&oq=time+spent+reading+c&aqs=chrome.1.69i57j0l2.5215j0j7&sourceid=chrome&ie=UTF-8) document that the time spent reading code is much higher than the time spent writing code and as such anything that can be done to improve this process, even to a small degree, is well worth doing. [One such article](https://www.informit.com/articles/article.aspx?p=1235624&seqNum=5#:~:text=Indeed%2C%20the%20ratio%20of%20time,is%20well%20over%2010%3A1.&text=Of%20course%20there's%20no%20way,makes%20it%20easier%20to%20write.) gives the approximate ratio of reading vs writing at over 10: 1.

It is also important to do this on an ongoing basis and not trying to refactor code to accommodate this at a later date since this essentially ensures that it will not be effective and is also not best practice for when working with others.

[GitPod](https://www.gitpod.io/) was the primary IDE used in the developement of this project and comes with a built in feature that allows errors and best practice opportunities to be shown in real time by means of underlining. This allowed me to keep the code clean and legible on an ongoing basis and be confident that I would be able to read and understand what I had written down at any point provided I ensured to address all the highlighted issues before comitting code. 

## Bugs

****

**Issue:** Navbar was not fixed to top on scroll. 

**Actions Taken:** Added position fixed to nav andd top 0

**Status:** Resolved

****
**Issue:** Login page failed to load due to allauth social tag.

**Actions Taken:** Reverted formatting changes to previous version

**Status:** Resolved

****
**Issue:** Admin Order Bug

**Actions Taken:** Tried removing full name and adding again and running migrations.

**Status:** Removed all migs and added again

****
**Issue:** Products quantity bug

**Actions Taken:** When quantity was rmoved from basic models the site couldn't add, set hidden qty in formatting

**Status:** Resolved
****

## Credits

Thanks to [Simen Daehlin](https://www.linkedin.com/in/simendaehlin?originalSubdomain=uk) - my mentor from Code Institute - for his feedback and constant belief and encouragement.

Thanks also to the [Code Institute](https://codeinstitute.net/) Tutors for their near endless patience and commitment.

Thanks to the hundreds of nameless people on [Stack Overflow](https://stackoverflow.com/) who answered my questions posted to google.

The Navbar elements were heavinly inspired by the [Dev Ed](https://github.com/developedbyed) [YouTube](https://www.youtube.com/channel/UClb90NQQcskPUGDIXsQEz5Q) channel. 
