# Testing Instructions

## Table of Contents

- [Testing Instructions](#testing-instructions)
  - [Table of Contents](#table-of-contents)
  - [Navigation](#navigation)
  - [CRUD](#crud)
    - [Create](#create)
    - [Read](#read)
    - [Update](#update)
    - [Delete](#delete)
  - [Sign Up](#sign-up)
  - [Login](#login)
  - [Logout](#logout)
  - [Social Links](#social-links)

## Navigation

All navigation links, including home icon, can be found in navbar or on small to medium screens in the burger drop-down menu.

| Feature | Action                             | Expected Result                 |
| :-----: | :---------------------------------:| :------------------------------:|
| **"Home" Link** | click "Home". | User is redirected back to homepage. |
| **Logo** | click on logo image. | User is redirected back to homepage. |
| **"Courses" Link** | click "Courses". | User is redirected back to course list page. |
| **"Search" Link** | Type for example "python" and press search button. | User is redirected to search results page and show the relevant search for "python". |
| **"Login" Link** | While not authenticated, click "Login". | User is directed to Login form. |
| **"Registration" Link** | While not authenticated, click "Sign Up". | User is directed to Sign Up form. |
| **"Booking" Link** | While authenticated, click "Booking". | Renders list of courses with option to book three courses. |
| **"Profile" Link** | While authenticated, click "Profile". | User is directed to profile page to see the booked courses and total price. |
| **"Logout" Link** | While authenticated, click "Logout". | User is directed to page with Sign Out button. |

## CRUD

The full CRUD functionality is only available to authenticated users.

### Create

Book courses and leaving comments (authenticated users only).

| Feature | Action                             | Expected Result                 |
| :-----: | :---------------------------------:| :------------------------------:|
| **"Learn more & Booking" button** | While on Courses page, click "Learn more & Booking". | User is redirected to course description page. |
| **"Course Description" page** | While authenticated, click "Book this Course". | User is redirected to booking page. |
| **"Course Description" page** | While authenticated, leaving comment. | The comment will show on the page. |
| **"Booking" page** | While authenticated, select courses and enter first and last name, then press "Submit Booking". | The booking successfully message shows and the courses are booked. |
| **Select more than three courses** | While authenticated, on booking page, try to select 4 or more courses. | Getting an error message: "You can select up to 3 courses." |
| **Try to book a course which already fully booked** | While authenticated, on booking page, try to book a course which is fully booked. | Getting an error message: "The name of the fully booked courses + already fully booked". |

### Read

Read course information, number of bookings for each course, available for booking, and comments (available to all users).

| Feature | Action                             | Expected Result                 |
| :-----: | :---------------------------------:| :------------------------------:|
| **Course List** | On courses page, click on learn more & booking button. | The title, description, and price of the course show to user. |
| **Hover on Images** | Hover on each Images on courses page. | Display a text that shows the course is available for booking or fully booked. |
| **Comments** | Go to course description for each courses. | Display the comments of other users with CRUD functionality for authenticated users. |

### Update

Option to edit existing booked courses and posted comments (authenticated users only).

| Feature | Action                             | Expected Result                 |
| :-----: | :---------------------------------:| :------------------------------:|
| **Edit Bookings** | On profile page, click on edit button. | Users redirect to Edit Booking page. |
| **Save Changes-Btn** | Edit the booked courses and press save changes button | Redirect to profile page with getting a message that courses updated and see the update list of the courses. |
| **Try to book a course which is already booked by the user** | While authenticated, on Edit booking page, try to book a course which is booked by the user. | Getting an error message: "You have already booked one or more of the selected courses". |
| **Try to book 4 or more courses** | While authenticated, on Edit booking page, try to book a course/courses while the user booked 3 courses. | Getting an error message: "You are trying to book more than 3 courses!". |
| **Edit comments** | On course description page, click on edit button for own comments. | User is redirected to Edit Comment page. |
| **Save Changes-Btn on Edit Comment page** | Update the text and press save changes button. | Redirect to course description page with updated comment. |

### Delete

Option to delete existing booked courses and posted comments (authenticated users only).

| Feature | Action                             | Expected Result                 |
| :-----: | :---------------------------------:| :------------------------------:|
| **Edit Bookings** | On profile page, click on delete button. | Users redirect to Delete Booking page. |
| **Delete-Btn** | Confirm the deletion of the courses | Redirect to profile page with getting a message that courses deleted and see no booked courses. |
| **Delete comments** | On course description page, click on delete button for own comments. | Confirm deleting of the comment. |
| **OK-Btn** | Press OK to confirm deleting. | Redirect to course description page with no comment. |

## Sign Up

Account creation for unauthenticated users.

| Feature | Action                             | Expected Result                 |
| :-----: | :---------------------------------:| :------------------------------:|
| **Sign Up form** | Go to Registration page via nav link | Renders form input fields Username, Email, Password, Password (confirm). |
| **Sign UP** | Fill in form fields accordingly. Click "Sign Up". | Self-closing message informs user of successfull account creation, including username. User is re-directed to homepage and navigation shows links for authenticated users. |
| **Incomplete form** | Failing to fill out all form fields, click "Sign Up". | User remains on Sign Up form view and is prompted to complete missing fields. |

## Login

Signing into existing account (authenticated users only).

| Feature | Action                             | Expected Result                 |
| :-----: | :---------------------------------:| :------------------------------:|
| **Login form** | Go to Login page via nav link | Renders form input fields Username, Password, Remember me (checkbox). |
| **Sign In** | Fill in form fields accordingly. Click "Sign In". | Self-closing message informs user of successfull login, including username. User is re-directed to homepage and navigation shows links for authenticated users. |
| **Incomplete form** | Failing to fill out all form fields, click "Sign In". | User remains on Sign Up form view and is prompted to complete missing fields. |
| **Remember me** | When signing in, tick "Remember me". Logout and sign in again. | Login form is pre-populated with username and hidden password. |

## Logout

Allows user to sign out of existing account (authenticated users only).

| Feature | Action                             | Expected Result                 |
| :-----: | :---------------------------------:| :------------------------------:|
| **Logout form** | When authenticated, go to Logout page via nav link | User is directed to Logout page, asking user to confirm action. |
| **Sign Out** | On Logout page, click "Sign Out". | User is re-directed to homepage and navigation shows links for unauthenticated users. |

## Social Links

Links to social media sites located in footer (available to all users).

| Feature | Action                             | Expected Result                 |
| :-----: | :---------------------------------:| :------------------------------:|
| **Link Icons in Footer** | Click on any of the social media icons | New tab opens with respective social media site |