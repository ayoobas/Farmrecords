


const togglePassword = document.querySelector('#togglePassword');
const password = document.querySelector('#password');
togglePassword.addEventListener('click', (e) => {
    const type = password.getAttribute('type') === 'password' ? 'text': 'password';
    password.setAttribute('type', type);
    e.target.classList.toggle('bi-eye');
})

const ctogglePassword = document.querySelector('#ctogglePassword');
const cpassword = document.querySelector('#cpassword');
ctogglePassword.addEventListener('click', (e) => {
    const type = cpassword.getAttribute('type') === 'password' ? 'text': 'password';
    cpassword.setAttribute('type', type);
    e.target.classList.toggle('bi-eye');
})

// document.addEventListener("DOMContentLoaded", function () {
//   setTimeout(function() {
//     let alerts = document.querySelectorAll('.alert');
//     alerts.forEach(function(alert) {
//       alert.classList.remove('show'); 
//       setTimeout(() => {
//         if (alert) alert.remove();
//       }, 500);
//     });
//   }, 5000);
// });
 