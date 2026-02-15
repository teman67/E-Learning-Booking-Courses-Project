# E-Learning Booking Courses

Welcome to our E-Learning Booking Courses platform, where knowledge meets convenience! Our user-friendly website is your gateway to a world of online learning opportunities tailored to fit your schedule and learning preferences. Explore a diverse range of courses and enhance your skills from the comfort of your own space.

![Home Screen](/readme/responsive.jpg)

#### [View E-Learning Booking Courses live website on Heroku](https://e-learning-platform-9ab8292ca70f.herokuapp.com/)
#### [View E-Learning Booking Courses live website on Onrender](https://e-learning-booking-courses-project.onrender.com)
- - -

## Table of Contents

### [User Experience](#user-experience-ux)

* [Project Goals](#project-goals)
* [Agile Methodology](#agile-methodology)
* [First time user](#first-time-user)
* [Registered user](#registered-user)
* [Admin user](#admin-user)

### [Design](#design-1)

* [Course Images and Texts](#Course-Images-and-Texts)
* [Wireframes](#wireframes)
* [Data Model](#data-models)
* [Database Scheme](#database-scheme)

### [Security Features](#Security-Features)

* [User Authentication](#User-Authentication)
* [CSRF Protection](#CSRF-Protection)


### [Technologies Used](#technologies-used-1)

* [Languages Used](#languages-used)
* [Databases Used](#databases-used)
* [Frameworks Used](#frameworks-used)
* [Programs Used](#programs-used)

### [Deployment and Local developement](#deployment-and-local-developement-1)

* [Local Developement](#local-developement)
* [ElephantSQL Database](#elephantsql-database)
* [Cloudinary](#cloudinary)
* [Heroku Deployment](#heroku-deployment)

### [Testing](#Testing)

* [Manual Testing](#Manual-Testing)
* [Automated Testing](#Automated-Testing)

### [References](#References)

* [Content](#content)
* [Acknowledgments](#acknowledgments)

---

## User Experience (UX)

Embark on a journey of effortless learning and skill development with our E-Learning Booking Courses platform. Immerse yourself in a user-friendly interface designed to make your educational experience seamless and captivating. Navigate through our diverse course catalog effortlessly, with intuitive features and visually engaging content. Our platform goes beyond the ordinary, providing personalized course recommendations based on your interests and goals. Access comprehensive information about each course, and rest easy with responsive support available at every step of your learning journey.

### Project Goals

The goal of the E-Learning Booking Courses project is to create an immersive and user-friendly online platform that allows visitors to explore,and book online courses. The project aims to prioritize user satisfaction through an intuitive and accessible platform, fostering seamless interaction and engagement.

### Agile Methodology

Agile Methodology was used to help prioritize and organize tasks, writting the user stories and using Project Boards on [Github](https://github.com/users/teman67/projects/5). Template was created to help write User Stories and define Epics

* Epics were written containing possible user stories and based on that the website was made.
* User stories were created by looking at epics and through iterations the project was advancing.
* Project Board is set to public.
* Project Board was used to track progression of the task through the Todo, In progress and Done columns
* Labels were added to sort the issues based on the importance.

### User Stories

#### Epics

* Initial Deployment
* Home Page
* User Registration
* Website Admin and Bookings
* Maintain consistent design with responsiveness in mind

#### User Stories

1. Initial Deployment

* Create new Heroku application
* Link Github repository to the Heroku app

2. Home Page

* Create a navigation bar
* Create a footer

3. User Registration

* Sign Up page
* User registration, log in, log out
* Display users name

4. Website Admin and Bookings

* Alert messages
* Crud functionality
* Course Lists
* Admin panel
* Limitation of Bookings for each user
* Course Description
* Total Price

5. Commenting

* User can leave comment for each courses
* Crud functionality
* Alert messages

6. Maintain consistent design with responsiveness in mind

* Maintain consistent design
* Test responsiveness


### First time user

* Simple and intuitive website navigation for easy exploration and discovery.
* Informative content providing an overview of courses.
* User-friendly forms with clear validation messages to ensure accurate input.
* Easy Registration process.
* Read Comments

### Registered User

* Seamless login process with a secure and personalized user account.
* Browsing available courses.
* Booking.
* Access to a personalized profile displaying booking history.
* Ability to easily modify or cancel existing bookings for flexibility and convenience.
* Leaving Comments.

### Admin user

* Secure and separate login portal for admin users with appropriate access control.
* Access to an admin dashboard for managing booking, course lists, and comments.
* Ability to add, edit, or delete courses, booking, and comments.
* Ability to delete user accounts, providing the necessary control for managing user data and accounts.

## Design

The E-Learning Booking Courses website boasts an inviting and visually pleasing design. Develop an intuitive and user-friendly interface for seamless navigation and interaction. Prioritize accessibility, ensuring a positive experience for users with diverse needs. Establish mechanisms for gathering user feedback to enhance course content and platform functionality. Social media links are presented in the contact section, and the footer complements the overall design.

### Course Images and Texts

All course images and texts were token from random online courses of [Udemy](https://www.udemy.com/).

### Logo

Logo was downloaded from goolge image [Google](https://www.google.com/).


### Wireframes

[Home Page](/readme/Home_page.jpg)

[Home Page after logged in](/readme/Home_page_login.jpg)

[Course List Page](/readme/Course_list.jpg)

[Login Page](/readme/login.jpg)

[Logout Page](/readme/logout.jpg)

[Registration Page](/readme/registration.jpg)

[Course Info Page](/readme/course_info.jpg)

[Booking Page](/readme/Booking_page.jpg)

[Edit Booking Page](/readme/Edit.jpg)

[Delete Booking Page](/readme/Delete.jpg)

[Profile Page](/readme/Profile.jpg)

[Search Page](/readme/search.jpg)

### Data Models

1. AllAuth User Model
    * Django Allauth, the User model is the default user model provided by the Django authentication system
    * The User entity has a one-to-many relationship with the Booking and Comment entities. This means that a User can have multiple Bookings and Comments, but each Booking and Comment is associated with only one User.

---

2. Course Model
    * Admin can add multiply courses in Course model. So users can see the courses and the relevent information on course list page.
    * Only Admin can change the data in the backend.
    * User can see the course information and image based on the chosen course.
    * Information provided is price, image,and description.
    * Course model has many to many relationship with Booking model. Therefore, each course offered on the platform can be booked by multiple users. This reflects the idea that a course can have numerous participants or bookings. Conversely, each booking made by a user can be associated with multiple courses. This means that a user can enroll in or book multiple courses.
    * Course model has one to many relationship with Comment model. it means that each instance of the "Course" model can have multiple associated instances of the "Comment" model. However, each instance of the "Comment" model is associated with only one specific instance of the "Course" model.
    * Each course can be booked by maximum 5 users.

---

3. Booking Model
    * A User can have multiple Bookings, but each Booking is associated with only one User. This is represented by the foreign key relationship between User and Booking.
    * Each user can book maximum 3 courses.
    * User cannot book a same course several times.
     
---

4. Userprofile Model
    * A User has one profile page with one to one relationship with User model.
    * All booked courses are shown to user.
    * Total price is calculated in the backend that is then displayed to user to show the total price of the booking.
    * Full CRUD functionality is available to the user.
     
---

5. Comment Model
    * Each user can comment on multiple courses, but each Comment is associated with only one User. This is represented by the foreign key relationship between User and Comment.
    * Full CRUD functionality is available to the user.

### Database Scheme

Entity Relationship Diagram (ERD)

![DataScheme](/Erd/erd_1.png)

* The ERD image was created using [Graphviz](https://graphviz.org/), 'django_extensions' app and pydot package. I followed the following steps to create the ERD image:
  - pip3 install graphviz
  - pip3 install django-extensions
  - Go to settings.py > add 'django_extensions', to INSTALLED_APPS
  - Add the following code
    GRAPH_MODELS ={
    'all_applications': True,
    'graph_models': True,
     }
    to settings.py
  - pip3 install pyparsing pydot
  - python3 manage.py graph_models -a > erd.dot && python3 manage.py graph_models --pydot -a -g -o erd.png

* This relationship diagram represents how different models are conneted to each other

## CRUD

CRUD functionality was implemented in both booking courses and commenting where:

- Create: An authenticated user can create a booking or leaving a comment.

- Read: A user can read the course information and comments .

- Update: An authenticated user can edit and update their own booked courses or comments.

- Delete: An authenticated user can delete their own booked courses or comments.

## Security Features

### User Authentication

* Django Allauth is a popular authentication and authorization library for Django, which provides a set of features for managing user authentication, registration, and account management.

### CSRF Protection

* Django provides built-in protection against Cross-Site Request Forgery (CSRF) attacks. CSRF tokens are generated for each user session, and they are required to submit forms or perform state-changing actions. When a user logs out, the session and associated CSRF token are invalidated, making it difficult for an attacker to forge a valid request using a copied URL.


### Custom error pages

* 404 Error Page, provides user with a button the redirect to home page.

## Technologies Used

### Languages Used

* [HTML5](https://en.wikipedia.org/wiki/HTML5)
* [CSS3](https://en.wikipedia.org/wiki/CSS)
* [JavaScript](https://en.wikipedia.org/wiki/JavaScript)
* [Python](https://en.wikipedia.org/wiki/Python_(programming_language))

### Databases Used

* [ElephantSQL](https://www.elephantsql.com/) - Postgres database
* [Cloudinary](https://cloudinary.com/) - Online static file storage

### Frameworks Used

* [Django](https://www.djangoproject.com/) - Python framework
* [Bootstrap 5.3.2](https://getbootstrap.com/docs/5.3/getting-started/introduction/) - CSS framework

### Programs Used

* [Github](https://github.com/) - Storing the code online
* [Gitpod](https://www.gitpod.io/) - To write the code.
* [Heroku](https://www.heroku.com/) - Used as the cloud-based platform to deploy the site.
* [Google Fonts](https://fonts.google.com/) - Import main font the website.
* [Git](https://git-scm.com/) - Version control
* [Favicon Generator](https://realfavicongenerator.net/) - Used to create a favicon
* [JSHint](https://jshint.com/) - Used to validate JavaScript
* [W3C Markup Validation Service](https://validator.w3.org/) - Used to validate HTML
* [CSS Validation Service](https://jigsaw.w3.org/css-validator/) - Used to validate CSS
* [CI Python Linter](https://pep8ci.herokuapp.com/#) - Used to validate Python

## Deployment and Local Developement

Live deployment can be found on this [View E-Learning Booking Courses live website here](https://book-courses-cbaeecdf3d3f.herokuapp.com/)

### Local Developement

#### How to Fork

1. Log in(or Sign Up) to Github
2. Go to repository for this project [Project_4](https://github.com/teman67/Project_4)
3. Click the fork button in the top right corner

#### How to Clone

1. Log in(or Sign Up) to Github
2. Go to repository for this project [Project_4](https://github.com/teman67/Project_4)
3. Click on the code button, select whether you would like to clone with HTTPS, SSH or GitHub CLI and copy the link shown.
4. Open the terminal in your code editor and change the current working directory to the location you want to use for the cloned directory.
5. Type the following command in the terminal (after the git clone you will need to paste the link you copied in step 3 above)
6. Set up a virtual environment (this step is not required if you are using the Code Institute Template in GitPod as this will already be set up for you).
7. Install the packages from the requirements.txt file - run Command pip3 install -r requirements.txt

### ElephantSQL Database

[ElephantSQL](https://www.elephantsql.com/) is using as PostgreSQL Database as follow:

1. Click Create New Instance to start a new database.
2. Provide a name (this is commonly the name of the project: tribe).
3. Select the Tiny Turtle (Free) plan.
4. You can leave the Tags blank.
5. Select the Region and Data Center closest to you.
6. Once created, click on the new database name, where you can view the database URL and Password.

### Cloudinary

[Cloudinary](https://cloudinary.com/) is used as a cloud to store images:

1. For Primary interest, you can choose Programmable Media for image and video API.
2. Optional: edit your assigned cloud name to something more memorable.
3. On your Cloudinary Dashboard, you can copy your API Environment Variable.
4. Be sure to remove the CLOUDINARY_URL= as part of the API value; this is the key.

### Heroku Deployment

* Log into [Heroku](https://www.heroku.com/) account or create an account.
* Click the "New" button at the top right corner and select "Create New App".
* Enter a unique application name
* Select your region
* Click "Create App"

#### Prepare enviroment and settings.py

* In your GitPod workspace, create an env.py file in the main directory.
* Add the DATABASE_URL value and your chosen SECRET_KEY value to the env.py file.
* Update the settings.py file to import the env.py file and add the SECRETKEY and DATABASE_URL file paths.
* Comment out the default database configuration.
* Save all files and make migrations.
* Add the Cloudinary URL to env.py
* Add the Cloudinary libraries to the list of installed apps.
* Add the STATIC files settings - the url, storage path, directory path, root path, media url and default file storage path.
* Link the file to the templates directory in Heroku.
* Change the templates directory to TEMPLATES_DIR
* Add Heroku to the ALLOWED_HOSTS list the format ['app_name.heroku.com', 'localhost']

#### Add the following Config Vars in Heroku

* SECRET_KEY - This can be any Django random secret key
* CLOUDINARY_URL - Insert your own Cloudinary API key
* PORT = 8000
* DATABASE_URL - Insert your own ElephantSQL database URL here

#### Heroku needs two additional files to deploy properly

* requirements.txt
* Procfile

#### Deploy

1. Make sure DEBUG = False in the settings.py
2. Go to the deploy tab on Heroku and connect to GitHub, then to the required repository.
3. Scroll to the bottom of the deploy page and either click Enable Automatic Deploys for automatic deploys or Deploy Branch to deploy manually. Manually deployed branches will need re-deploying each time the GitHub repository is updated.
4. Click 'Open App' to view the deployed live site.

Site is now live

## Testing

### Manual Testing

Please see  [TESTING.md](/readme/testing.md) for all the detailed testing performed.

### Automated Testing

I use TestCase from django.test to test my models.py, views.py, and forms.py. A summery of the testings is shown bellow where 74% part of my codes was tested using django test model. The report was generated by coverage as follow:
- pip3 install coverage
- coverage run --source=courses manage.py test

![Coverage report](/readme/Coverage_report.jpg)

The test files can be found in [courses folder](https://github.com/teman67/Project_4/tree/main/courses) named: "test_models.py test_forms.py test_views.py".

- To run these tests I changed the DATABASES in settings.py to local databases instead of external databases, otherwise the tests could not run due to permission problem.
- Totally 17 tests ran where I got the following output:  "..........E...F.." which shows 15 tests ran successfully.

## Fixed bugs

- Error Bad Request (400)
  * I got Bad request error (400) when I deployed on heroku. After checking different options I figured it out that this error came when I set DEBUG=False in settings.py. Finally the issue was solved when I changed '/css/style.css' to 'css/style.css' (removing / from path of style.css).

- When a user try to edit or delete booking of other users by copying the edit/delete URLs and pasting in web browser an error appears 
  * To solve the issue I added "if not request.user.is_authenticated: return redirect('home')" to both edit and delete class in views.py. Therefore, a user will redirect to the home page if he/she trys to edit/delete booking of others.

## Unfixed bugs

- In the login page there is link "Forgot your password?" which comes from nowhere! I could not figure it out the source of this link in my login template and I just changed the code so users redirect to a customized page shown "Under Constraction" when they click on "Forgot your password?" link.

## References

### Content

* All of the course images, prices, and descriptions were taken from [Udemy](www.udemy.com)
* Logo of the webpage was downloaden from google image.
* The template for manual testing [TESTING.md](/readme/testing.md) was taken from (https://github.com/Kathrin-ddggxh/woohoo-haiku/blob/main/TESTING.md#liking).

### Acknowledgments

* I would like to thank my mentor for support and feedback throughout this project, Mitko Bachvarov.
* I would also like to extend my appreciation to the Slack community for their continuous engagement and willingness to share knowledge. The collaborative environment provided a platform for learning, troubleshooting, and gaining inspiration from fellow developers.
