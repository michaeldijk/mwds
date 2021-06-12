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
| 1 | As a visitor, I want to find information about a certain topic | - Ability to search posts for a specific word, and to read more about it | - Ability to view the posters profile to know more about them |
| 2 | As a visitor, I want to share my knowledge with the community | - Ability to create an account, and to post a story | - Ability to update my profile, with information about myself, and my knowlegde |
| 3 | As a visitor, I want to be able to contact the site's owner | - Ability to contact site's owner | - Contact form easily findeable |
| 4 | As a visitor, I want the site to be intuitive, and easy to navigate | - Well guided design, and menu | - Intuitive navigation from top to bottom |

#### Structure Plane
##### Front-end
The website exists out of several pages, that interlink together. Several pages are only accessible for admin user, and, some pages are only accessible after a user has logged on to the site.

![image](https://github.com/michaeldijk/mwds/blob/main/readme_files/structure_files/navigation.png)

- **Home** &#40;`stories.html`&#41;<br> the main page of the site, leading to all other pages. The page has all stories summarized with short view on full text, and if user is not logged on, they will need to login in order to read further. Furthermore, if a new user reaches the page, it welcomes them to either sign-up or register, and has several links to terms and conditions, contact, and languages page

- **Single Story** &#40;`single_story.html`&#41;<br> This page, is visible, and available once users login to the site, and they are then able to read full stories, from the stories (index) page.

- **Stories Search** &#40;`stories_search.html`&#41;<br> This page is visible, if users are logged in to the site, and once they have searched for criteria on the stories (index) page.

- **register** &#40;`register.html`&#41;<br> This page is visible for everyone, if not logged in, allowing users to register, and this page also links to a reset password page (contact), and login page.

- **profile** &#40;`profile.html`&#41;<br> This page is visible, once user logs in to the site, they are then able to view their profile, and from this page, they can then edit stories, edit profile.

- **profile public** &#40;`profile_public.html`&#41;<br> This page is visible for all logged in users, once they click on username of the user that posted a story, they will see this page.

- **profile edit** &#40;`profile_edit.html`&#41;<br> This page is only visible to the user that logged in, and allows them to edit the profile.

- **new story** &#40;`new_story.html`&#41;<br> This page is visible to all logged in users, to allow to post new stories.

- **login** &#40;`login.html`&#41;<br> This page, is visible to all not logged in users.

- **edit story** &#40;`edit_story.html`&#41;<br> This page is visible to users logged in, from their profile page.


There are several pages, only available to the admin user:
- **manage languages** &#40;`manage_languages.html`&#41;<br> This page, is visible only to the administator, to manage languages, and add languages.

- **manage stories** &#40;`manage_stories.html`&#41;<br> This page, is visible, only to the administrator, where it's possible to edit and delete stories.

- **manage users** &#40;`manage_users.html`&#41;<br> This page is also only visible to admin user, allowing to delete users, and delete all user stories at once.

There are two more pages, only available for admin user, that is available through manage languages and manage stories.
- **edit language** &#40;`edit_language.html`&#41;<br> This page is only available through manage languages, and allows admin user to adjust language name.

- **edit story** &#40;`edit_story.html`&#41;<br> This page is only available through manage stories, and allows admin user to adjust story posted.

##### Back-end
Users need an account to create new stories.
Admin user needs to be able to add new languages.
Users need to able to adjust their stories.

Therefore, we decided on three collections, interlinking to each other.

Stories uses users, for username, and stories itself for the data it populates for the stories view.
Profile uses users about me and avatar fields.
Admin user requires all collections, to adjust these details through the admin portal.

![image](https://github.com/michaeldijk/mwds/blob/main/readme_files/structure_files/db_structure.png)

