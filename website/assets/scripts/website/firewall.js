function get_ip() {
    const xhr = new XMLHttpRequest();
    xhr.open('GET', 'https://api.ipify.org?format=json', false);
    xhr.send();
    if (xhr.status === 200) {
        const response = JSON.parse(xhr.responseText);
        return response.ip;
    }
    return null;
}

function get_info(ip) {
    const url = `https://api.iplocation.net/?ip=${ip}`;
    const xhr = new XMLHttpRequest();
    xhr.open("GET", url, false);
    xhr.send();
    
    if (xhr.status === 200) {
        const data = JSON.parse(xhr.responseText);
        return [data.country_code2, data.country_name];
    } else {
        return "Unable to retrieve country information.";
    }
}

function ro(ip) {
    document.getElementById("go").classList.toggle("display-none");
    document.getElementById("c").style.opacity = "100";
    document.getElementById("info").innerHTML = "Your country is Iran!!!\nIp: " + ip;
}
ip = ip()
country_info = get_info(ip)
black_list = ["IR"]
alert("I'm ok")
for (country of black_list) {
    if (country == country_info[0]) {
        document.innerHTML = `<h1>Banned IP</h1><br><h2>Ip: ${ip}</h2><br><h2>Country: ${country_info[1]}</h2>`
        break
    } else {
        document.getElementById("c").style.color = "#0c0"
        document.getElementById("go").classList.toggle("display-none");
        document.getElementById("c").style.opacity = "100";
        document.getElementById("t").innerHTML = "Welcome";
        document.getElementById("info").innerHTML = "Your country is " + ban_list[index] + "! (IP: " + ip + ")";
    }
}