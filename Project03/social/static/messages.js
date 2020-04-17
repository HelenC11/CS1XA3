/* ********************************************************************************************
   | Handle Submitting Posts - called by $('#post-button').click(submitPost)
   ********************************************************************************************
   */

function submitPostResponse(data,status) {
    if (status == 'success') {
        // reload page to display new Post
        location.reload();
    }
    else {
        alert('failed to request more posts' + status);
    }
}

function submitPost(event) {
  // TODO Objective 8: send contents of post-text via AJAX Post to post_submit_view (reload page upon success)

    // globally defined in messages.djhtml using i{% url 'social:more_post_view' %}

    let postText = event.target.querySelector('[contenteditable]');

    let json_data = { 'postContent' : postText };

    let url_path =  post_submit_url;

    // AJAX post
    $.post(url_path,
           json_data,
           submitPostResponse);
}



/* ********************************************************************************************
   | Handle Liking Posts - called by $('.like-button').click(submitLike)
   ********************************************************************************************
   */

function likeResponse(data,status) {
    if (status == 'success') {
        // reload page to update like count
        location.reload();
    }
    else {
        alert('failed to create like ' + status);
    }
}
function submitLike(event) {
    // TODO Objective 10: send post-n id via AJAX POST to like_view (reload page upon success)
    let likes = event.target.id;
    let json_data = { 'postID' : likes };
    // globally defined in messages.djhtml using i{% url 'social:like_view' %}
    let url_path = like_post_url;

    // AJAX post
    $.post(url_path,
           json_data,
           likeResponse);
}

/* ********************************************************************************************
   | Handle Requesting More Posts - called by $('#more-button').click(submitMore)
   ********************************************************************************************
   */
function moreResponse(data,status) {
    if (status == 'success') {
        // reload page to display new Post
        location.reload();
    }
    else {
        alert('failed to request more posts' + status);
    }
}

function submitMore(event) {
    // submit empty data
    let json_data = { };
    // globally defined in messages.djhtml using i{% url 'social:more_post_view' %}
    let url_path = more_post_url;

    // AJAX post
    $.post(url_path,
           json_data,
           moreResponse);
}

/* ********************************************************************************************
   | Document Ready (Only Execute After Document Has Been Loaded)
   ********************************************************************************************
   */
$(document).ready(function() {
    // handle post submission
    $('#post-button').click(submitPost);
    // handle likes
    $('.like-button').click(submitLike);
    // handle more posts
    $('#more-button').click(submitMore);
});
