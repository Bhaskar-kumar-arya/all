$(document).ready(function() {
    function getCookie(name) {
        let cookieValue = null;
        if (document.cookie && document.cookie !== '') {
            const cookies = document.cookie.split(';');
            for (let i = 0; i < cookies.length; i++) {
                const cookie = cookies[i].trim();
                // Does this cookie string begin with the name we want?
                if (cookie.substring(0, name.length + 1) === (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }
    const csrftoken = getCookie('csrftoken');

    $('#like-button').on('click', function() {
        const videoId = $(this).data('video-id');
        $.ajax({
            url: `/video/${videoId}/like/`,
            type: 'POST',
            data: {
                'action': 'like',
                'csrfmiddlewaretoken': csrftoken
            },
            success: function(response) {
                if (response.status === 'success') {
                    $('#likes-count').text(response.likes_count);
                    $('#dislikes-count').text(response.dislikes_count);
                    if (response.liked) {
                        $('#like-button').addClass('active');
                    } else {
                        $('#like-button').removeClass('active');
                    }
                    if (response.disliked) {
                        $('#dislike-button').addClass('active');
                    } else {
                        $('#dislike-button').removeClass('active');
                    }
                } else {
                    alert(response.message);
                }
            },
            error: function(xhr, status, error) {
                console.error("AJAX Error: ", status, error);
                alert("An error occurred. Please try again.");
            }
        });
    });

    $('#dislike-button').on('click', function() {
        const videoId = $(this).data('video-id');
        $.ajax({
            url: `/video/${videoId}/like/`,
            type: 'POST',
            data: {
                'action': 'dislike',
                'csrfmiddlewaretoken': csrftoken
            },
            success: function(response) {
                if (response.status === 'success') {
                    $('#likes-count').text(response.likes_count);
                    $('#dislikes-count').text(response.dislikes_count);
                    if (response.liked) {
                        $('#like-button').addClass('active');
                    } else {
                        $('#like-button').removeClass('active');
                    }
                    if (response.disliked) {
                        $('#dislike-button').addClass('active');
                    } else {
                        $('#dislike-button').removeClass('active');
                    }
                } else {
                    alert(response.message);
                }
            },
            error: function(xhr, status, error) {
                console.error("AJAX Error: ", status, error);
                alert("An error occurred. Please try again.");
            }
        });
    });
});