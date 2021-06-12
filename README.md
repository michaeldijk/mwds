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
	* [Scope Plane](https://github.com/michaeldijk/mwds#scope-plane)
	* [Structure Plane](https://github.com/michaeldijk/mwds#structure-plane)
	* [Skeleton Plane](https://github.com/michaeldijk/mwds#skeleton-plane)
    * [Surface Plane](https://github.com/michaeldijk/mwds#surface-plane)
* [Features](https://github.com/michaeldijk/mwds#features)
	* [Home](https://github.com/michaeldijk/mwds#home)
    * [Log In](https://github.com/michaeldijk/mwds#login)
    * [Register](https://github.com/michaeldijk/mwds#register)
    * [Profile](https://github.com/michaeldijk/mwds#profile)
    * [New Story](https://github.com/michaeldijk/mwds#new-story)
* [Features for admin user](https://github.com/michaeldijk/mwds#features-for-admin-user)
    * [Manage Languages](https://github.com/michaeldijk/mwds#manage-languages)
    * [Manage Users](https://github.com/michaeldijk/mwds#manage-users)
    * [Manage Stories](https://github.com/michaeldijk/mwds#manage-stories)
* [Other features](https://github.com/michaeldijk/mwds#other-features)
    * [404](https://github.com/michaeldijk/mwds#404-page)
    * [Search](https://github.com/michaeldijk/mwds#search-page)
    * [Features left to implement](https://github.com/michaeldijk/mwds#features-left-to-implement)
* [Technologies Used](https://github.com/michaeldijk/mwds#technologies-used)
* [Testing](https://github.com/michaeldijk/mwds#testing)
    * [User Story Testing](https://github.com/michaeldijk/mwds#user-story-testing)
    * [Manual testing across devices / browsers](https://github.com/michaeldijk/mwds#manual-testing-across-devices--browsers)
    * [HTML](https://github.com/michaeldijk/mwds#html-testing)
    * [CSS](https://github.com/michaeldijk/mwds#css-testing)
    * [JavaScript](https://github.com/michaeldijk/mwds#javascript-testing)
    * [Python](https://github.com/michaeldijk/mwds#python-testing)
* [Version Control & deployment](https://github.com/michaeldijk/mwds#version-control--deployment)
* [Project barriers & Solutions](https://github.com/michaeldijk/mwds#project-barriers--solutions)
* [Credits](https://github.com/michaeldijk/mwds#credits)
    * [Code](https://github.com/michaeldijk/mwds#code)
    * [Media](https://github.com/michaeldijk/mwds#media)
    * [Content](https://github.com/michaeldijk/mwds#content)
* [Acknowledgements](https://github.com/michaeldijk/mwds#acknowledgements)

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

#### Skeleton Plane
The site is designed with mobile-first approach. And as we're using mostly bootstraps features, we didn't need to adjust much in terms of resizing for mobile.

- [Wireframes: &#40;`index`&#41;](https://github.com/michaeldijk/mwds/blob/main/readme_files/wireframes_files/homepage.png)
- [Wireframes: &#40;`admin edit users`&#41;](https://github.com/michaeldijk/mwds/blob/main/readme_files/wireframes_files/admin_edit_users.png)
- [Wireframes: &#40;`admin manage categories`&#41;](https://github.com/michaeldijk/mwds/blob/main/readme_files/wireframes_files/admin_manage_categories.png)
- [Wireframes: &#40;`admin manage stories`&#41;](https://github.com/michaeldijk/mwds/blob/main/readme_files/wireframes_files/admin_manage_stories.png)
- [Wireframes: &#40;`login page`&#41;](https://github.com/michaeldijk/mwds/blob/main/readme_files/wireframes_files/login_page.png)
- [Wireframes: &#40;`menus`&#41;](https://github.com/michaeldijk/mwds/blob/main/readme_files/wireframes_files/menus.png)
- [Wireframes: &#40;`story page`&#41;](https://github.com/michaeldijk/mwds/blob/main/readme_files/wireframes_files/story_page.png)
- [Wireframes: &#40;`user new story`&#41;](https://github.com/michaeldijk/mwds/blob/main/readme_files/wireframes_files/user_new_story.png)
- [Wireframes: &#40;`user profile`&#41;](https://github.com/michaeldijk/mwds/blob/main/readme_files/wireframes_files/user_profile.png)

#### Surface Plane
As I am colour-blind, I have some issues with matching colours, nonetheless, we went with several shades of colours, that matched each other, and colours that match my "feelings".

![image](https://github.com/michaeldijk/mwds/blob/main/readme_files/surface_files/colours.png)
![image](https://github.com/michaeldijk/mwds/blob/main/readme_files/surface_files/colours1.png)

I used [Color Hunt](https://colorhunt.co/palette/195877) for helping me choose the correct colours, and making sure that they matched.
I used [Contrast Checker](https://contrastchecker.com/) for making sure, that the colours matched ranging from small to large, and with foreground and background colours.

### Features
The site incorporates many different features, and uses clever ways of having users login to the site, in order to make full use of the site itself.<br>
I have stories, open in a new page, as once the stories are filling up, I wanted to have a similar effect as what [Quora](https://quora.com/) does, where you have an infinite scroll on the main page, and stories load and load more, when you scroll down, and once you close the newly opened page, you return to the page you left off at.<br>

#### Home
* shows a welcome banner (card) on top, when users are not logged in, this banner allows users to directly click to register account, or, login, also, this allows users to read more about the site, terms and conditions, contact site owner, and, see what languages are covered.
* the stories are posted here, and, small snippet is visible for users, if they click read more, they have to login if not logged in, or, register
* the stories are displayed with pagination, but uses clever way of "infinite scrolling", from [infinite-scroll.com](https://infinite-scroll.com/), to allow seamless viewing experience, if they reach the end of the page, inifinte scroll loads a new page immediate thereafter, making the experience for the user smooth, without them knowing this is taking place.
* you can also click on the profile (username) of the poster, and this brings you to the user's public profile (if you are logged in, if you are not, it brings you to the login page)

#### Login
* The login page, does it's job well, it allows users to login to the site
* It also allows users to request a reset password, by clicking on the link
* and, it allows users to register an account, if not registered yet, by clicking on the link

#### Register
* Register allows users to register to the site
* It also brings users, if they have an account, to the login page, if they click the link
* It also brings users to reset password, if they've forgotten the password.

* Register checks on several fields: username, email address, password. If the username is already taken, it will prompt so, if password does not conform the required settings, it will also report this back to user.
* Usernames like "admin", "root", "superuser", "adminaccount", "Administrator", "administrator", are not allowed, and it will return users to register page again.

#### Profile
* Profile page allows users to edit their "profile", by default it sets it to a value of "Edit profile, if you want to enter a small bio".
* The proile page also allows users to set an avatar. By default it sets it to a silouette
* The profile page, also has a link, to post a new story, if they want to go from here, as this page will the opened up, when user logs in

#### New Story
* This is the page, where users post a new story, it has three fields: Language discussed, story title, story itself.
* The story itself, is a WYSIWYG editor, and allows users to enter info, like they do using word

### Features for admin user
The following features, are only available for the admin user

#### Manage Languages
* This page, allows admin user, to manage languages, and edit the language if a type-o has been made
* Admin user can also add directly a new language from this page
* When clicking on delete, it prompts user before deletion

#### Manage Users
* This page, allows admin user, to manage users, and delete stories of a user in bulk
* when deleting the user profile, it prompts before deletion takes place
* When deleting bulk stories, it prompts before deletion takes place

#### Manage Stories
* This page, allows admin user, to manage stories, and delete stories of a all users individually
* This page also allows admin user, to edit a processed story, if for instance it needs to be sensorred

### Other features
Some of the other features added to the site

#### 404 page
* There is a custom 404 page, in line with coding, and coders, it uses a doge meme image
* The 404 page, then has a link, to "Go Home"

#### search page
* Search is only visible to logged in users, and only accessible to logged in users

#### Features left to implement
* Comment system, to allow users to comment on other stories
* Tag system, to allow users to add tags of a certain category(ies)
* Create an upvote system, when some stories are downvoted to much, remove them from the site

### Technologies used
* [HTML5](https://en.wikipedia.org/wiki/HTML) for markup
* [CSS3](https://en.wikipedia.org/wiki/CSS) for styling
* [Bootstrap 5](https://getbootstrap.com) as HTML framework
* [JQuery](https://jquery.com/) Javascript (JQuery) for some interaction
* [Python3](https://www.python.org/) As backend language
* [Flask](https://flask.palletsprojects.com/en/2.0.x/) Flask (Micro web framework written in Python)
* [MongoDB](https://www.mongodb.com) MongoDB Atlas as database
* [Google Fonts](https://fonts.google.com/) for font useage
* [Font Awesome](https://fontawesome.com/) for the icons
* [Git](https://git-scm.com/) for local version control
* [GitHub](https://www.github.com) for online version control
* [Heroku](https://heroku.com/) Heroku for deploying the finished site

### Testing
#### User Story Testing
I created a separate markdown file, for user story testing, please click following link:
* [User Stories](https://github.com/michaeldijk/mwds/blob/main/readme_files/user_story_files/USER_STORIES.md)

#### Manual testing across devices / browsers
I tested the site with different devices and browsers, see my notes below for each test:
* Mobile: I discovered that while testing it on an iPhone, the overlay for stories, was distorted, so I adjusted this with a change in the CSS
![image](https://github.com/michaeldijk/mwds/blob/main/readme_files/manual_testing/iphone_testing.jpg)
* Opened the site on different browsers: Chrome, Safari, Opera, Edge, to make sure all the functions where working and visuals where displaying correctly.
* Opened the site on several different browsers, to confirm useability across those, and there where no issues present:
    * Chrome
    * Opera
    * Safari
    * Brave
    * Edge
    * Vivaldi

#### HTML testing
##### Code validator
When I completed all my HTML code, I carried out several validation tests, by using [W3C Markup Validation Service](https://validator.w3.org/), which is a worldwide recognized validator created by the WWC, that allows checking HTML and XHTML code, to check if markup was documented correctly, and correct any errors along the way.

#### css testing
##### Code validator
When I completed the site, I carried out validation tests, using [W3C CSS Validation Service](https://jigsaw.w3.org/css-validator/), and adjusted my code thereafter accordingly, to fix any errors that was present.

#### Javascript testing
##### Code validator
When I completed the site, I carried out validation tests, using [JSHint](https://jshint.com/), for JS, there was no errors present.

#### Python testing
##### Code validator
When I completed the site, I carried out validation tests, using [PEP8 online](http://pep8online.com/), there where some lines exceeding the character limit, which I fixed.<br>
There where also some additional errors, due to lines to long, but these are errors present due to commenting in the code, and breaking them, would not show the comments in the appropriate way.
![image](https://github.com/michaeldijk/mwds/blob/main/readme_files/manual_testing/pep8.png)

Furthermore, each section that I wrote, was tested extensively, by first allowing the route, to open a page, and slowly building the routes up from there. Making sure that any get and post requests, accurately handled the responses.

#### Defensive design
* All pages where users are not allowed to go to, or, when they need to be logged in, return back with values of the error
* All admin pages, can only and only with the "admin" credential opened
* When users login, or, when a form is not correctly processed, it reports an error


### Version Control & deployment
This website, and application was developed using VS-Code, version control was locally maintained with Git, and online with GitHub.<br>
While developing the site, I incorporated the use of several brances, to work on features, and only implementing these to the main branch, if the feature was complete.<br>
While using branches, initially, I made a small mistake by mixing them up, but I quickly adapted and adjusted using this, and I really enjoy developing this way, as this allows clear separation between features.<br>

#### Deployment
Deployment was achieved by:
1. Pushing code from my IDE to GitHub, via Git, with Git terminal in VS-Code
2. Creating an app on Heroku, and then therafter deploying it from Heroku
3. In Heroku "Deploy Tab" deployment was setup so that any new update to GitHub, would automatically populate to Heroku, and thereafter update the app itself.
    1. Sometimes, I would change branch, to test if something worked across the board, from local to remote
4. The completed deployment can be found on [Visit the site on Heroku - MWDS](http://mwds.herokuapp.com/)

#### Cloning the repository
1. Select the repository from GitHub [GitHub Repo Link](https://github.com/michaeldijk/mwds)
2. Click on "Clone or download" from the Code button in just slightly below top right
3. Click on the clipboard icon, to copy the GIT url
4. Open your IDE, and open the terminal window, navigating to the correct location where you want the cloned repo being saved to
5. Paste the GIT url, and follow your IDE instructions to clone further and work on it locally

### Project barriers & Solutions
* Initially I had a lot of problems with Imposter syndrome, feeling like I couldn't do it, but once I made a start, things started flowing by itself
* Currently, my partner is affected with COVID, and this made studying quite hard, this combined with work requirements, but I am really proud of what I have achieved
* Most of my answers to any questions I had, or have, where found on [Stack Overflow](https://stackoverflow.com)
* Currently, I am using [Summernote WYSIWYG Editor](https://summernote.org/), and unfortunately, field validation does not work on this, I wanted to implement some JS for validation, but was a bit constraint with time. Further besides this field, all other fields are validated before submittion

### Credits
The following, are credits, to any code that I may have used, or any help that I have received. I am very proud of what I have build and accomplished, and I hope to expand only further from here onwards

#### Code
* Form fields, and how to use WTForms [Moguel Grinberg, Flask Mega Tutorial](https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-iii-web-forms)
* WTForms, Noneof, and how to use apply it [Stack Overflow](https://stackoverflow.com/questions/58464698/anyof-validation-in-flask)
* How to use Excerpts [Stack Overflow](https://stackoverflow.com/questions/26030590/how-do-i-provide-a-blog-excerpt-without-having-to-show-html-code-using-jinja2-te)
* Ed Bradley, from Slack, helped me with applying a filter for avatar image on stories view [Ed Bradley](https://github.com/Edb83)
* Found help, for the About section, where an update, if no value added, errored the form, how to solve this, with using default values [Stack Overflow](https://stackoverflow.com/questions/21831216/get-none-from-a-fields-data-in-instead-of-an-empty-string)
* Found a solution to using $set, as I wasn't sure how to implement set, but this helped a lot [Stack Overflow](https://stackoverflow.com/questions/29837370/pymongo-update-one-syntax-error) & [MongoDB](https://docs.mongodb.com/manual/reference/operator/update/set/)
* Found a solution to using pagination, and showing correct values from [Stack Overflow](https://stackoverflow.com/questions/54053873/implementation-of-pagination-using-flask-paginate-pymongo)
* Found solution for infinite scroll, with the help of :last-child-selector [jQuery](https://api.jquery.com/last-child-selector/)
* Found a solution, how to add a class to Jinja templates [Stack Overflow](https://stackoverflow.com/questions/61714589/add-css-classes-to-jinja-template-for-form)
* Found help, for using the contact form, and implementing email sending [EnvatoTuts+](https://code.tutsplus.com/tutorials/intro-to-flask-adding-a-contact-page--net-28982)
* Found help, for pass values to dropdown [Stack Overflow](https://stackoverflow.com/questions/51027440/how-do-i-set-a-value-for-a-hidden-field-in-a-flask-form-using-wtf-quick-form)
* Found solution, to remove file upload from Summernote WYSIWYG [Stack Overflow](https://stackoverflow.com/questions/33615669/disable-image-upload-in-summernote/33659947)

#### Media
* Found doge meme picture on [PNG Arts](https://www.pngarts.com/explore/216324)
* Found about image on [Pixabay](https://pixabay.com/photos/confused-hands-up-unsure-perplexed-2681507/)
* Found country flags image on [Pixabay](https://pixabay.com/vectors/flags-russia-usa-germany-china-1722052/)

#### Content
* Found HTML history from [Washington EDU](https://www.washington.edu/accesscomputing/webd2/student/unit1/module3/html_history.html)
* Found CSS history from [Wikipedia](https://en.wikipedia.org/wiki/CSS)
* Found Priorities, from [Level Up](https://levelup.gitconnected.com/the-funny-side-of-a-programmers-life-44cab153edf9)
* Found if it works, from [Level Up](https://levelup.gitconnected.com/the-funny-side-of-a-programmers-life-44cab153edf9)

### Acknowledgements
I have to first and foremost, acknowledge myself for persistence and perseverence.<br>
All Code Institute Tutors, and mentors, who are always avaialble online<br>
Slack community<br>
Coffee, lots and lots of coffee