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
  - [Commenting](#commenting)
  - [Social Links](#social-links)

## Navigation

All navigation links, including home icon, can be found in navbar or on small to medium screens in the burger drop-down menu.

| Feature | Action                             | Expected Result                 |
| :-----: | :---------------------------------:| :------------------------------:|
| **Home Link Icon** | While not on homepage, click icon. | Icon shrinks and expands. User is redirected back to homepage. |
| **"Courses" Link** | While not on homepage, click "Courses". | User is redirected back to course list page. |
| **"Login" Link** | While not authenticated, click "Login". | User is directed to Login form. |
| **"Registration" Link** | While not authenticated, click "Sign Up". | User is directed to Sign Up form. |
| **"Booking" Link** | While authenticated, click "Booking". | Renders list of courses with option to book three courses. |
| **"Profile" Link** | While authenticated, click "Profile". | User is directed to profile page to see the booked courses and total price. |
| **"Logout" Link** | While authenticated, click "Logout". | User is directed to page with Sign Out button. |

## CRUD

The full CRUD functionality is only available to authenticated users.

### Create

Write and submit a haiku via haiku submit form (authenticated users only).

| Feature | Action                             | Expected Result                 |
| :-----: | :---------------------------------:| :------------------------------:|
| **Title field** | Select field with placeholder "Enter a title" and start typing. | Placeholder disappears, title shows instead. Typing is disabled after 100 characters. |
| **Tag drop-down** | Click "Tag your haiku" drop-down menu and select tagname. | Shows all available tag options. Placeholder is not selectable. Selected options displays after closing drop-down. |
| **Content field** | Select field with placeholder "Write haiku here" and start typing. | Placeholder disappears, written text displays. |
| **Submit** | After completing haiku form, click submit button. | Alert message informs user of successful submission. User is re-directed to homepage with the newly submitted haiku showing top of the list. |
| **Incomplete form** | Failing to fill out all form fields, click submit button. | User remains on "Create" page and is prompted to complete missing fields. |

### Read

Read submitted haikus, including tanka extensions (available to all users).

| Feature | Action                             | Expected Result                 |
| :-----: | :---------------------------------:| :------------------------------:|
| **Haiku panel link** | On homepage, click on any haiku panel. | New view opens displaying haiku body, title, author and tagname. |
| **Tankas** | Scroll down below haiku body. | If available, tanka extensions render below haiku, listing body and author. If no tankas available, generic message dispalys. |

### Update

Option to edit existing haikus via haiku detail view (authenticated users only).

| Feature | Action                             | Expected Result                 |
| :-----: | :---------------------------------:| :------------------------------:|
| **User match** | On homepage, click haiku submitted by different user. | Haiku detail view does not show edit button to ensure users can only update their own haikus. |
| **Edit-Btn** | From haiku detail view, click edit button below haiku body. Button is only visible after loggin. | Renders haiku edit form with title and content field pre-populated by original post. |
| **Cancel** | Below edit form, click "Cancel". | User is redirected to homepage with no action taken. |
| **Submit** | Alter form input according to desired update. Click edit button below form. | Alert message informs user of successful update. User is re-directed to homepage with the newly edited haiku showing top of the list. |
| **Incomplete form** | Failing to fill out all form fields, click edit button. | User remains on edit form view and is prompted to complete missing fields. |

### Delete

Option to delete existing haikus via haiku detail view (authenticated users only).

| Feature | Action                             | Expected Result                 |
| :-----: | :---------------------------------:| :------------------------------:|
| **User match** | On homepage, click haiku submitted by different user. | Haiku detail view does not show delete button to ensure users can only delete their own haikus. |
| **Delete-Btn** | From haiku detail view, click delete button below haiku body. Button is only visible after loggin. | User is directed to delete page which prompts user to confirm delete action. |
| **Confirm Delete** | On delete page, click "Delete". | Alert message informs user of successful deletion. User is re-directed to homepage, selected haiku has been deleted. |
| **Cancel** | On delete page, click "Cancel". | User is re-directed to homepage with no delete action taken. |

## Sign Up

Account creation for unauthenticated users.

| Feature | Action                             | Expected Result                 |
| :-----: | :---------------------------------:| :------------------------------:|
| **Sign Up form** | Go to Sign Up page via nav link | Renders form input fields Username, Email (optional), Password, Password (confirm). |
| **Submit** | Fill in form fields accordingly. Click "Sign Up". | Self-closing message informs user of successfull account creation, including username. User is re-directed to homepage and navigation shows links for authenticated users. |
| **Incomplete form** | Failing to fill out all form fields, click "Sign Up". | User remains on Sign Up form view and is prompted to complete missing fields. |

## Login

Signing into existing account (authenticated users only).

| Feature | Action                             | Expected Result                 |
| :-----: | :---------------------------------:| :------------------------------:|
| **Login form** | Go to Login page via nav link | Renders form input fields Username, Password, Remember me (checkbox). |
| **Submit** | Fill in form fields accordingly. Click "Sign In". | Self-closing message informs user of successfull login, including username. User is re-directed to homepage and navigation shows links for authenticated users. |
| **Incomplete form** | Failing to fill out all form fields, click "Sign In". | User remains on Sign Up form view and is prompted to complete missing fields. |
| **Remember me** | When signing in, tick "Remember me". Logout and sign in again. | Login form is pre-populated with username and hidden password. |

## Logout

Allows user to sign out of existing account (authenticated users only).

| Feature | Action                             | Expected Result                 |
| :-----: | :---------------------------------:| :------------------------------:|
| **Logout form** | When authenticated, go to Logout page via nav link | User is directed to Logout page, asking user to confirm action. |
| **Sign Out** | On Logout page, click "Sign Out". | Self-closing message informs user of successfull logout. User is re-directed to homepage and navigation shows links for unauthenticated users. |

## Commenting

Option to add a tanka extension to own or other users' haikus (authenticated users only.)

| Feature | Action                             | Expected Result                 |
| :-----: | :---------------------------------:| :------------------------------:|
| **Submit tanka** | In haiku detail view, scroll down to tanka instructions and blank textfield input. Write tanka according to instructions. Click "Submit". | At the bottom of page, message informs user that submitted tanka awaits approval. Tanka will not be displayed until site admin has approved it. |
| **Tanka count** | Find tanka counter on haiku panel, both on homepage and in haiku details. | Number on counter matches all displayed tankas. This does not include tankas that are awaiting approval. |
| **View tankas** | After submitting tanka, wait for admin approval. | Once admin has approved submission, tanka (including author) can now be read below haiku detail view. |

## Social Links

Links to social media sites located in footer (available to all users).

| Feature | Action                             | Expected Result                 |
| :-----: | :---------------------------------:| :------------------------------:|
| **Link Icons in Footer** | Click on any of the social media icons | New tab opens with respective social media site |