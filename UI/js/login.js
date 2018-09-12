let loginUrl = 'http://127.0.0.1:5000/api/v1/auth/login/';
const loginUser = () => {
    fetch(loginUrl, {
      method: 'POST',
      headers: {
        "Content-type": "application/json; charset=UTF-8"
      },
      body: JSON.stringify({
        username: document.getElementById('username').value,
        password: document.getElementById('password').value
      })
      })
    .then(response => response.json())
    .then(loginData => {
      console.log(loginData);
        if(loginData.message === "User successfully logged in"){
            window.location.href = "UI/Home.html";
            // let id = loginData.User.user_id;
            // sessionStorage.setItem("userId", id);
            // sessionStorage.setItem("token",loginData.token);
            console.log(loginData.message);
            console.log(loginData.token);
        }else{
            alert(loginData.message)
        }
    })
    .catch(function (error) {
      console.log('Request failed', error);
    });
  }