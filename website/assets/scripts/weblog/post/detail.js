const like_count = document.getElementById("like-count");
const like_button = document.getElementById("like-button");
const csrf_token = like_button.getAttribute("data-csrf-token");
const data = {
        headers: {
            "X-CSRFToken": csrf_token,
            "Content-Type": "application/json",
    },
};


const get_like_status = () => {
    data["method"] = "GET";
    fetch(`like/`, data)
        .then(response => response.json())
        .then(data => {
            if (data.liked) {
                like_button.textContent = "Unlike";
            } else {
                like_button.textContent = "Like";
            }
            like_count.textContent = data.likes;
            return data.liked;
        }
    );
};
  

const like = () => {
    data["method"] = "POST";
    fetch(`like/`, data)
        .then(response => response.json())
        .then(data => {
            if (get_like_status()) {
                like_button.textContent = "Unlike";
            } else {
                like_button.textContent = "Like";
            };
        }
    );
};

get_like_status()
