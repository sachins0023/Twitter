var show_tweets = document.getElementById("show-tweets-button");
show_tweets.addEventListener("click", getRequest);

let tweetsRequest;

function getRequest() {
    tweetsRequest = new XMLHttpRequest();
    if (!tweetsRequest) {
        alert("Could not make request!");
        return false;
    }
    tweetsRequest.onreadystatechange = sendResponse;
    tweetsRequest.open('GET', 'http://127.0.0.1:8000/tweet/');
    tweetsRequest.send();
}

function sendResponse() {
    if (tweetsRequest.readyState === XMLHttpRequest.DONE) {
        if (tweetsRequest.status === 200) {
            let bodyWrapper = document.getElementById("tweet-ui");
            bodyWrapper.innerHTML = '';
            let tweets = JSON.parse(tweetsRequest.responseText);
            for (var i = 0; i < tweets.length; i++) {
                let tweet = tweets[i];
                bodyWrapper.insertAdjacentHTML('beforeend', "<div uiclass='ui-tweet'>\
                <div class='ui-tweet-top'>\
                <div class='ui-tweet-user-img'></div>\
                <div class='ui-tweet-user-details'>\
                <div class='ui-tweet-user-name'>" + tweet.user_name + "</div>\
                <div class='ui-tweet-tweet-time'>" + tweet.date_time_updated + "</div>\
                </div>\
                </div>\
                <div class='ui-tweet-bottom'>" + tweet.text + "</div>\
                </div>")
            }
        } else {
            alert("Error occured!");
        }
    }
}