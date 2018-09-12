let signupUrl = 'http://127.0.0.1:5000/api/v1/auth/signup/';
function registerUser(){
    fetch(signupUrl, {
      method: 'POST',
      body: JSON.stringify({
        username: document.getElementById('username').value,
        email: document.getElementById('email').value,
        password: document.getElementById('password').value
      }),
      headers: {
        'Content-type': 'application/json'
      }
      })
      .then(response => response.json())
      .then(registerData => {
        console.log(registerData);
        if(registerData.message === "User created successfully"){
          // window.location.replace("./login.html");
          console.log(registerData);
          // sessionStorage.setItem("username", registerData.username);
        }else{
            alert(registerData.message);
            console.log(registerData.message);
        }
    })
    .catch(function (error) {
      console.log('Request failed', error);
    });
  }