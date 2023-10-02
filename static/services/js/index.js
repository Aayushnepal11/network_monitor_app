const loginButton = document.getElementById('openLoginForm');

loginButton.addEventListener('click',function(){
    const loginModal = document.getElementById('loginModal');
    loginModal.style.display='flex';
    loginModal.style.flexDirection='column'; 
}); 



document.getElementById('loginForm').addEventListener('submit', function(e){
    e.preventDefault();


    setTimeout(function(){
        alert("Login Successfully");
        document.getElementById('loginModal').style.display='none';
    }, 1000);

});
