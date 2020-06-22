# BugZapp

[![Build Status](https://travis-ci.org/geminerald/bugzapp.svg?branch=master)](https://travis-ci.org/geminerald/bugzapp)

An Online Bug tracker offering convenient ways to monitor and update statuses of bugs on your software. Fully customisable. 

Offering a free version for individuals who want to use it on personal projects or for study or a competitively priced paid version for companies with a 2 week free trial offer.


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
    - [Flowcharts](#flowcharts)
    - [Databse Schema](#database-schema)

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
technology. The colour scheme was taken from coolers.co and is currently as follows (TBC):

### Fonts

The **Archivo** font was chosen for this project as it was **clear** and **concise** with a variety of different font weights available. It is **similar to Helvetica** which is well known throughout the technology field as a popular choice for website design.

### Icons

The icons for this project came from [Font Awesome](https://fontawesome.com/6?next=%2F) as they are universally highly regarded as having a great selection of icons for development.

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


### Root Styles

### Images

The images for this project were largely taken from [Pexels](https://www.pexels.com/) which has been a great resource for stock and background images. 

### Backgrounds

[Home Page Background](https://www.pexels.com/photo/illuminated-cityscape-against-blue-sky-at-night-316093/) courtesy of [Pixabay](https://www.pexels.com/@pixabay)

## Planning

### Wireframes

To view the wireframes for this project please go to the [Wireframes Folder](https://github.com/geminerald/bugzapp/tree/master/wireframes)

### Site Map

### Flowcharts

### Database Schema

### Models

User Model

Bug Model

Organisation Model

## Features

### Developed Features

- Home Page
- Authentication System

### Features in Development

- Ticket Model
- About Page
- User Model
- Checkout System
- Cart Page
- Cart System
- Checkout & Payment Page
- Payment System

### Features to be Developed

- Organisation Model
- Profile Page

## Technologies

### Core Technologies:

- HTML
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

## Bugs

## Credits