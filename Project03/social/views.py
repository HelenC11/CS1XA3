from django.http import HttpResponse,HttpResponseNotFound
from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, PasswordChangeForm, UserChangeForm
from django.contrib.auth import authenticate, login, get_user, update_session_auth_hash
from django.contrib import messages
from datetime import datetime

from . import models

def messages_view(request):
    """Private Page Only an Authorized User Can View, renders messages page
       Displays all posts and friends, also allows user to make new posts and like posts
    Parameters
    ---------
      request: (HttpRequest) - should contain an authorized user
    Returns
    --------
      out: (HttpResponse) - if user is authenticated, will render private.djhtml
    """
    if request.user.is_authenticated:
        user_info = models.UserInfo.objects.get(user=request.user)
        friends=user_info.friends.all()

        # TODO Objective 9: query for posts (HINT only return posts needed to be displayed)
        posts = []
        posts = models.Post.objects.all()
        posts=posts[::-1]

        post_visits = request.session.get('post_visits', 0)
        allPosts=[]
        for post in posts:
            allPosts.append(post)



        listUpperBound = post_visits + 2
        postSize = len(allPosts)

        new_list = []
        if listUpperBound < postSize - 1:
            for i in range(listUpperBound):
                new_list.append(allPosts[i])
        else:
            new_list = allPosts

        # TODO Objective 10: check if user has like post, attach as a new attribute to each post

        context = { 'user_info':user_info,
                    'posts' : posts,
                    'friends':friends,
                    'new_list':new_list}

        return render(request,'messages.djhtml',context)

    request.session['failed'] = True
    return redirect('login:login_view')



def account_view(request):
    """Private Page Only an Authorized User Can View, allows user to update
       their account information (i.e UserInfo fields), including changing
       their password
    Parameters
    ---------
      request: (HttpRequest) should be either a GET or POST
    Returns
    --------
      out: (HttpResponse)
                 GET - if user is authenticated, will render account.djhtml
                 POST - handle form submissions for changing password, or User Info
                        (if handled in this view)
    """
    """if request.user.is_authenticated:
        form = None

        # TODO Objective 3: Create Forms and Handle POST to Update UserInfo / Password

        user_info = models.UserInfo.objects.get(user=request.user)
        context = { 'user_info' : user_info,
                    'form' : form }
        return render(request,'account.djhtml',context)
        request.session['failed'] = True
        return redirect('login:login_view')
        """

    if request.user.is_authenticated:
        form = None
        # TODO Objective 3: Create Forms and Handle POST to Update UserInfo / Password
        existingUserInfo = models.UserInfo.objects.get(user=request.user)
        print("existingUserInfo:----------",existingUserInfo.location)
        if request.method == 'POST':
            formName = request.POST.get('name')
            print("-------formName:" + formName);

            if (formName == 'pwdForm'):
                password = request.POST['password']
                if password is not None and password != "":
                    user = get_user(request)
                    user.set_password(password)
                    user.save()
                    return redirect('login:login_view')
            else:
                request.user.employment = request.POST['employment']
                request.user.location = request.POST['location']
                request.user.birthday = request.POST['birthday']
                request.user.interests = request.POST['interests']
                inter = models.Interest(label=request.POST['interests'])
                inter.save()
                request.user.save()

                if request.POST['employment'] != '':
                    existingUserInfo.employment = request.user.employment


                if request.POST['location'] != '':
                    existingUserInfo.location = request.user.location

                if request.POST['birthday'] != "":
                    existingUserInfo.birthday = request.user.birthday
                elif existingUserInfo.birthday==None:
                    # existingUserInfo.birthday = datetime.strptime(str(existingUserInfo.birthday), '%Y-%m-%d')
                    existingUserInfo.birthday = None

                if request.POST['interests'] != "" and request.POST['interests'] is not None:
                    inter = models.Interest(label=request.POST['interests'])
                    inter.save()
                    existingUserInfo.interests.add(inter)

                existingUserInfo.save()


        context = {'user_info': existingUserInfo,
                   'login_form': form}
        return render(request, 'account.djhtml', context)
        request.session['failed'] = True
        return redirect('login:login_view')



def people_view(request):
    """Private Page Only an Authorized User Can View, renders people page
       Displays all users who are not friends of the current user and friend requests
    Parameters
    ---------
      request: (HttpRequest) - should contain an authorized user
    Returns
    --------
      out: (HttpResponse) - if user is authenticated, will render people.djhtml
    """
    if request.user.is_authenticated:
        # TODO Objective 4: create a list of all users who aren't friends to the current user (and limit size)

        all_users = models.UserInfo.objects.all()
        myuserInfo = models.UserInfo.objects.get(user=request.user)
        myFriends = myuserInfo.friends.all()

        all_people = []
        for personInfo in all_users.all():
            if personInfo not in myFriends:
                    all_people.append(personInfo)

        num_visits = request.session.get('num_visits', 0)

        listUpperBound = num_visits + 2
        peopleSize = len(all_people)

        new_list = []
        if listUpperBound < peopleSize - 1:
            for i in range(listUpperBound):
                new_list.append(all_people[i])
        else:
            new_list = all_people

        # TODO Objective 5: create a list of all friend requests to current user
        friend_list = models.FriendRequest.objects.filter(to_user=myuserInfo)
        given_list = models.FriendRequest.objects.filter(from_user=myuserInfo)

        sent_list=[]
        for stuff in given_list:
            sent_list.append(stuff.to_user)

        print(sent_list)

        friend_requests = []

        for friend in friend_list:
            friend_requests.append(friend.from_user)

        context = { 'user_info' : myuserInfo,
                    'all_people' : all_people,
                    'num_visits' : num_visits,
                    'new_list' : new_list,
                    'friend_requests' : friend_requests,
                    'sent_list' : sent_list}

        return render(request,'people.djhtml',context)

    request.session['failed'] = True
    return redirect('login:login_view')

def like_view(request):
    '''Handles POST Request recieved from clicking Like button in messages.djhtml,
       sent by messages.js, by updating the corrresponding entry in the Post Model
       by adding user to its likes field
    Parameters
	----------
	  request : (HttpRequest) - should contain json data with attribute postID,
                                a string of format post-n where n is an id in the
                                Post model

	Returns
	-------
   	  out : (HttpResponse) - queries the Post model for the corresponding postID, and
                             adds the current user to the likes attribute, then returns
                             an empty HttpResponse, 404 if any error occurs
    '''
    postIDReq = request.POST.get('postID')

    if postIDReq is not None:
        # remove 'post-' from postID and convert to int
        # TODO Objective 10: parse post id from postIDReq
        postID = postIDReq[5:]


        if request.user.is_authenticated:
            # TODO Objective 10: update Post model entry to add user to likes field
            if request.method=="POST":

                myuserInfo = models.UserInfo.objects.get(user=request.user)
                likedPost = models.Post.objects.filter(id=postID)[0]
                likedPost.likes.add(myuserInfo)

            return HttpResponse()
        else:
            return redirect('login:login_view')

    return HttpResponseNotFound('like_view called without postID in POST')

def post_submit_view(request):
    '''Handles POST Request recieved from submitting a post in messages.djhtml by adding an entry
       to the Post Model
    Parameters
	----------
	  request : (HttpRequest) - should contain json data with attribute postContent, a string of content

	Returns
	-------
   	  out : (HttpResponse) - after adding a new entry to the POST model, returns an empty HttpResponse,
                             or 404 if any error occurs
    '''

    postContent = request.POST.get('postContent')



    if postContent is not None:
        if request.user.is_authenticated:

            # TODO Objective 8: Add a new entry to the Post model
            if request.method == "POST":
                myuserInfo = models.UserInfo.objects.get(user=request.user)

                created = models.Post.objects.create(owner=myuserInfo , content=postContent)
                if created:
                    print("Post------", )
                else:
                    print("no")

            context={
                'postContent': postContent
            }
            # return status='success'
            return HttpResponse()
        else:
            return redirect('login:login_view')

    return HttpResponseNotFound('post_submit_view called without postContent in POST')

def more_post_view(request):
    '''Handles POST Request requesting to increase the amount of Post's displayed in messages.djhtml
    Parameters
	----------
	  request : (HttpRequest) - should be an empty POST

	Returns
	-------
   	  out : (HttpResponse) - should return an empty HttpResponse after updating hte num_posts sessions variable
    '''
    if request.user.is_authenticated:
        # update the # of posts dispalyed
        myuserInfo = models.UserInfo.objects.get(user=request.user)
        # TODO Objective 9: update how many posts are displayed/returned by messages_view
        post_visits = request.session.get('post_visits', 0)
        request.session['post_visits'] = post_visits + 1

        context = {'post_visits': post_visits}

        # return status='success'


        return HttpResponse()

    return redirect('login:login_view')


def more_ppl_view(request):
    '''Handles POST Request requesting to increase the amount of People displayed in people.djhtml
    Parameters
	----------
	  request : (HttpRequest) - should be an empty POST

	Returns
	-------
   	  out : (HttpResponse) - should return an empty HttpResponse after updating the num ppl sessions variable
    '''
    if request.user.is_authenticated:
        # update the # of people dispalyed

        num_visits = request.session.get('num_visits', 0)
        request.session['num_visits'] = num_visits + 1

        context = {'num_visits': num_visits}

        # TODO Objective 4: increment session variable for keeping track of num ppl displayed
        # return status='success'
        return HttpResponse()

    return redirect('login:login_view')

def friend_request_view(request):
    '''Handles POST Request recieved from clicking Friend Request button in people.djhtml,
       sent by people.js, by adding an entry to the FriendRequest Model
    Parameters
	----------
	  request : (HttpRequest) - should contain json data with attribute frID,
                                a string of format fr-name where name is a valid username

	Returns
	-------
   	  out : (HttpResponse) - adds an etnry to the FriendRequest Model, then returns
                             an empty HttpResponse, 404 if POST data doesn't contain frID
    '''
    frID = request.POST.get('frID')

    if frID is not None:
        # remove 'fr-' from frID
        username = frID[3:]

        if request.user.is_authenticated:
            # TODO Objective 5: add new entry to FriendRequest
            friend = models.User.objects.filter(username=username)[:1].get()
            print("-------key--" , friend.username)

            if request.method == "POST":
                from_user = models.UserInfo.objects.get(user=request.user)
                to_user= models.UserInfo.objects.get(user_id=friend.id)

                created = models.FriendRequest.objects.get_or_create(from_user=from_user, to_user=to_user)

                if created is False:
                    print("already created")
                else:
                    print("friend request created")

            # return status='success'
            return HttpResponse()
        else:
            return redirect('login:login_view')

    return HttpResponseNotFound('friend_request_view called without frID in POST')

def accept_decline_view(request):
    '''Handles POST Request recieved from accepting or declining a friend request in people.djhtml,
       sent by people.js, deletes corresponding FriendRequest entry and adds to users friends relation
       if accepted
    Parameters
	----------
	  request : (HttpRequest) - should contain json data with attribute decision,
                                a string of format A-name or D-name where name is
                                a valid username (the user who sent the request)

	Returns
	-------
   	  out : (HttpResponse) - deletes entry to FriendRequest table, appends friends in UserInfo Models,
                             then returns an empty HttpResponse, 404 if POST data doesn't contain decision
    '''
    data = request.POST.get('decision')

    if data is not None:
        # TODO Objective 6: parse decision from data
        username = data[2:]
        choice=data[:1]

        if request.user.is_authenticated:

            person = models.User.objects.filter(username=username)[:1].get()
            print("------------" , person.username)
            personInfo = models.UserInfo.objects.get(user=person)
            myuserInfo = models.UserInfo.objects.get(user=request.user)

            # TODO Objective 6: delete FriendRequest entry and update friends in both Users


            if choice == 'A':

                myuserInfo.friends.add(personInfo)
                myuserInfo.save()

                personInfo.friends.add(myuserInfo)
                personInfo.save()


                exist_requests = models.FriendRequest.objects.filter(to_user=myuserInfo, from_user=personInfo)

                exist_requests.delete()
            else:

                exist_requests = models.FriendRequest.objects.filter(to_user=myuserInfo, from_user=personInfo)
                exist_requests.delete()

            # return status='success'
            return HttpResponse()
        else:
            return redirect('login:login_view')

    return HttpResponseNotFound('accept-decline-view called without decision in POST')
