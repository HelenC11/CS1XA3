# CS 1XA3 Project03 - <chenh214>

## Usage
Install conda environment with conda activate djangoenv

**Run locally with:**
python manage.py runserver localhost:8000

**Run on mac1xa3.ca with:**
python manage.py runserver localhost:10019
python manage.py collectstatic

Log in with TestUser, password 1234


## Objective 01
**Description:** Allows the user to sign up a new account (username and password)
- this feature is displayed in signup.djhtml which is rendered by Signup_view
- makes a POST request for Username and Password, creates a User and UserInfo for the new user
- redirects the user to messages page once an account is created

**Exceptions:** all Usernames must be unique so if a already made username is used, an exception may occur


## Objective 02
**Description:** Displays the users interests, birthday, location, employment 
- template in social_base.djhtml, rendered in the left column for messages.djhtml, people.djhtml and account.djhtml 


## Objective 03
**Description:** Allows user to change interest, birthday, location, employment and password
- Displayed in account.djhtml, rendered by account_view 
- if password is changed, it redirects the user to the login page
- POST request for content to be changed
**Exceptions:** If birthday is not entered in proper format (YYYY-MM-DD) or a nonexistent date is entered an error will occur

## Objective 04
**Description:** Displays a list of people who are not friends with the user
- Displayed in people.djhtml, rendered by people_view
- it makes a POST Request from people.js which is handled by more_ppl_view
- session controls number of people displayed by more button, is reset once the user logs out


## Objective 05
**Description:** List of all the friend requests the user has.
- friend_request_view handles POST Request received from clicking Friend Request button in people.djhtml sent by people.js, by adding an entry to the FriendRequest Models
- Displayed in people.djhtml, rendered by people_view


## Objective 06 
**Description:** Allows the user to reject/accept friend requests
- Displayed in people.djhtml, rendered by accept_decline_view, script in people.js
- accept_decline_view handles POST Request received from accepting or declining a friend request in people.djhtml,
 sent by people.js
- deletes corresponding FriendRequest entry and adds to users friends relation if accepted


## Objective 07
**Description:** Displays a list of the users friends
- Displayed in messages.djhtml (right column)


## Objective 08
**Description:** Allows the user to create a post
- Displayed in people.djhtml, rendered by people_view
- creates Post object for user
- messages.js scripts moreResponse and submitMore used to handle post request
- post_submit_view handles POST Request received from submitting a post in messages.djhtml by adding an entry to the Post Model


## Objective 09
**Description:** Displays a list of posts by everyone from most recent post to oldest
- Displayed in messages.djhtml, rendered by messages_view
- session controls number of post seen, reset once user logs out  
- more_post_view handles POST Request requesting to increase the amount of Post's displayed in messages.djhtml


## Objective 10
**Description:** Allows the user to like a post and displays number of likes a post has
- Displayed in messages.djhtml, rendered by message_view
- like_view handles POST Request received from clicking Like button in messages.djhtml, sent by messages.js
- updates the corresponding entry in the Post Model by adding user to its likes field


## Objective 11
**Description:** Sample social media with test users. Username in front and password in brackets

- TestUser (1234)
- TestUser2 (1234)
- Jane Doe (1234)
- TurtleLover23 (1111) 
- 2KidsInATrenchcoat (2222)
- DefinitelyNotARobot (3333)
- Coronavirus (4444)
- Miss Goody 2 Shoes (5555)
-Dragon (6666)
- Cat (7777)


*Note: TurtleLover23 has a space behind his name*

