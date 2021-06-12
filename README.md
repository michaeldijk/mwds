![image](https://github.com/michaeldijk/mwds/blob/main/readme_files/mwds_image.png?raw=true)

# MWDS - My WebDev Story
## Milestone #3 study project

[Visit the site on Heroku - MWDS](http://mwds.herokuapp.com/)

This site is created as Milestone #3 project for Code Institute, showcasing my progress in becoming a confident front/backend (full stack) developer.
MWDS is, a site / community, where others can leave their story, in web development. And, this story is then shared among the community of other users, that use the site.
It is also a place where users can just share snippets, of certain things, or, code. Or, just post general information to others.

## Table of contents
* [Who is the website for?](https://github.com/michaeldijk/mwds#who-is-the-website-for)
* [Who is the owner?](https://github.com/michaeldijk/mwds#who-is-the-owner)
* [UX Planes](https://github.com/michaeldijk/mwds#ux-planes)
	* [Strategy Plane](https://github.com/michaeldijk/mwds#strategy-plane)
	* [Scope Plane](#)
	* [Structure Plane](#)
	* [Skeleton Plane](#)
    * [Surface Plane](#)
* [Features](#)
	* [Home](#)
    * [Log In](#)
    * [Register](#)
    * [Profile](#)
    * [New Story](#)
    * [Manage Languages](#)
    * [Manage Users](#)
    * [Manage Stories](#)
    * [404](#)
    * [Features left to implement](#)
* [Technologies Used](#)
* [Testing](#)
    * [User Story Testing](#)
    * [Manual testing across devices / browsers](#)
    * [HTML](#)
    * [Lighthouse testing](#)
    * [CSS](#)
    * [JavaScript](#)
    * [Unsolved issues](#)
* [Version Control](#)
* [Project barriers & Solutions](#)
    * [Project barriers & Solutions - General](#)
* [Deployment](#)
* [How to run this project locally](#)
* [Credits](#)
    * [Code](#)
    * [Content](#)
    * [Media](#)
* [Acknowledgements](#)

---

### Who is the website for?
The audience is geared towards developers, creators, coders, and anyone who feel like sharing stories, coding techniques, and handy knowhows.

### Who is the Owner?
Michael Dijk, is the site's owner and developer.

Michael's aim with this site was first and foremost, to show the ability to create a site with CRUD functionality. And secondly, to create a community where users can share their stories, and align with other people of same interest.
The idea was brought to live, as Michael, enjoys using the site Quora, and some of it's features are designed and created as an hommage to this site.

Michael's goals where:
* Showcasing the skills to build a front/backend project.
* Showcasing the use of MongoDB
* Showcasing the use of Flask
* Building full CRUD functionality
* Creating a place for an online community

### UX Planes
The following parts, describe the different planes and how I incorporated them into my project

#### Strategy Plane
The audience is geared towards developers, creators, coders, and anyone who feel like sharing stories, coding techniques, and handy knowhows. 
We're making a site for people to share their story, and be able to read other stories, search by tags, and or the story itself.
The site allows users to share excitement regarding coding, to the world, and the community MWDS is.
For users, they can expect an audience reading their content, their solutions to problems, and, being able to be part of a “community” of like-minded people.

| #  | Opportunity/Problem |  Importance | Viability/Feasibility |
| ------------- | ------------- | ------------- | ------------- |
| 1  | Create an online community for users, to sign up, login and share their stories   | 5  | 5  |
| 2  | Create a voting system to vote on stories  | 3  | 3  |
| 3  | Create a comment system, for users to allow comments on stories  | 5  | 3  |
| 4  | Allow tagging of “tags”, for languages covered  | 5  | 2  |
| 5  | Allow users to create an enticing profile, with details about themselves  | 5  | 3  |
| 6  | Create a database, and app with Mongo + Flask  | 5  | 5  |
| 7  | Create a login system with Mongo + Flask  | 5  | 5  |

![image](https://github.com/michaeldijk/mwds/blob/main/readme_files/other_files/viabilityFeasibility.png)

##### What can/could be covered?
I had the following schedule in mind, to cover features:
1. Create an online community for users, to sign up, login and share their stories
6. Create a database, and app with Mongo + Flask
7. Create a login system with Mongo + Flask

Then once, the above three options are covered, we will focus on the following two:
3. Create a comment system, for users to allow comments on stories
5. Allow users to create an enticing profile, with details about themselves

And, once these features are implemented, we will focus on the last sprint:
4. Allow tagging of “tags”, for languages covered
2. Create a voting system to vote on stories

Due to circumstances with my partner, and contracting COVID, I was not able to push forward for a while, due to time constraints, but nonetheless, I covered most parts, bar the following:
* Create a comment system, for users to allow comments on stories
* Allow tagging of “tags”, for languages covered
* Create a voting system to vote on stories

The main features of the site are working, and, the functionality that I wanted to go for, which was incorporating full CRUD functions, are in place.
I will continue to work on this, as a side project, as I am very fond of the outcome so far.

Currently, the site brings value to the table, to allow users sharing stories. Not directly like a social media platform, but more like a platform geared towards a particular set of users, and these users are (web) developers, who feel like sharing their story, solution, or other things that are useful to be shared within the “community” of developers. With that in mind, I do hope this can grow to something bigger than just a study / exam project.

#### Scope Plane
In terms of features, as described in the Strategy plane, I have been able to cover most aspects of the site, and functionality is in place.

The site had to bring a specific function in mind to the user, and be easy to navigate, to work on, on both mobile and desktop devices, it also needed to allow users to connect with others, which is present. The only real missing point at the moment, is the comment section, but this will be incorporated soon.

##### User Stories/scopes
| #  | Scenario |  Requirements |
| ------------- | ------------- | ------------- |
| 1 | Story | - Reqs | - Reqs |
| 2 | Story | - Reqs | - Reqs |
| 3 | Story | - Reqs | - Reqs |
| 4 | Story | - Reqs | - Reqs |
| 5 | Story | - Reqs | - Reqs |
| 6 | Story | - Reqs | - Reqs |