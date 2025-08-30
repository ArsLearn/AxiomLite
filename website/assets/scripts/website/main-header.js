const get_width = () => {
    document.getElementById("test").innerHTML = window.innerWidth
};

setInterval(get_width, 10)