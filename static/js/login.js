async function login(event){
  event.preventDefault();

  const form = event.target;

  let fields = form.elements;
  
  let data = {
    username: fields['username'].value,
    password: fields['password'].value,
  }

  form.reset();

  let result = await sendRequest(`${server}/auth`, 'POST', data);

  if('error' in result){
    toast("Login Failed: "+result['description']);
  }else{
    toast("Logged Successful");
    window.localStorage.setItem('access_token', result['access_token']);//save token
    window.location.href= 'index.html';
  }

}

document.forms['loginForm'].addEventListener('submit', login);