




let myform = document.forms[0];

myform.addEventListener('submit',(e)=>{
  

    e.preventDefault();
let nameError = document.getElementsByClassName('name')[0];
let emailError = document.getElementsByClassName('email')[0];
let passwordError = document.getElementsByClassName('password')[0];



let name = document.getElementById('name');
let email = document.getElementById('email');
let password = document.getElementById('password');

  
console.log(name,email,password);

    if(name.value.trim() == '')
    {
        nameError.innerText = 'name should not be blank';
        nameError.style.display = 'block';
        return;
    }else if(name.length <= 2 )
    {
        nameError.innerText = 'name should be greater than 2 characters';
        nameError.style.display = 'block';
        return ;
    }else if (email.value.trim() == '')
    {
        emailError.innerText = 'email should not be blank';
        emailError.style.display = 'block';
        return ;
    }else if(email.length <= 12)
    {
        emailError.innerText = 'incorrect email';
        emailError.style.display = 'block';
        return ;
    }else if(password.value.length <= 5)
    {
        passwordError.innerText ='password should be greater than 5 characters';
        passwordError.style.display = 'block';
        return ;
    }else if(password.value.trim() == '')
    {
        passwordError.innerText = 'password cannot be blank';
        passwordError.style.display = 'block';
        return ;
    }else{
        myform.submit();
    }
})