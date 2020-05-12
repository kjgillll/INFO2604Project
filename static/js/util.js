const server = "https://pacific-earth-73565.herokuapp.com/";

function toast(message){
  M.toast({html: message});
}

async function sendRequest(url, method, data){
  try{
    //retrieve token from localStorage
    let token = window.localStorage.getItem('access_token');

    let options = {//options passed to fetch function
        method: method,
        headers: { 
          'Content-Type' : 'application/json',
          'Authorization' : `JWT ${token}`//send token in request
        }
    };

    if(data)//data will be given for PUT & POST requests
      options.body = JSON.stringify(data);//convert data to JSON string

    let response = await fetch(url, options);
      
    let result = await response.json();//Get json data from response
    return result;//return the result

  }catch(error){
    return error;//catch and log any errors
  }
}