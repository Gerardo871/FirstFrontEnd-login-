document.addEventListener('DOMContentLoaded', () => {
    console.log('¡Proyecto iniciado correctamente!');
});
document.getElementById('show-register').addEventListener('click', function() {
    document.getElementById('login_form').style.display = 'none';
    document.getElementById('register-form').style.display = 'block';
});

document.getElementById('show-login').addEventListener('click', function() {
    document.getElementById('register-form').style.display = 'none';
    document.getElementById('login_form').style.display = 'block';
});