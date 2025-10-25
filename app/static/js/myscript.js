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

//To hide and show plant_number and cocopeat
  const step1 = document.getElementById("step1");
  const step2 = document.getElementById("step2");
  const nextBtn = document.getElementById("nextBtn");
  const backBtn = document.getElementById("backBtn");
  const progressBar = document.getElementById("progress-bar");

  nextBtn.addEventListener("click", () => {
    step1.classList.add("d-none");
    step2.classList.remove("d-none");
    progressBar.style.width = "100%";
    progressBar.innerText = "Step 2 of 2";
  });

  backBtn.addEventListener("click", () => {
    step2.classList.add("d-none");
    step1.classList.remove("d-none");
    progressBar.style.width = "50%";
    progressBar.innerText = "Step 1 of 2";
  });

  //Hide and show nursery and permanent stage
  document.addEventListener('DOMContentLoaded', function() {
  const stageSelect = document.getElementById('id_plant_stage');
  const plantNumberDiv = document.getElementById('div_id_plant_number');
  const plantAgeDiv = document.getElementById('div_id_plant_age');
  const cocopeatNameDiv = document.getElementById('div_id_cocopeat_name');
  const cocopeatWeightDiv = document.getElementById('div_id_cocopeat_weight');

  // Function to toggle visibility
  function toggleFields() {
    const stageValue = stageSelect.value;

    if (stageValue === '1') { // Nursery selected
      plantNumberDiv.style.display = 'none';
      plantAgeDiv.style.display = 'none';
      cocopeatNameDiv.style.display = 'block';
      cocopeatWeightDiv.style.display = 'block';
    } else {
      plantNumberDiv.style.display = 'block';
      plantAgeDiv.style.display = 'block';
      cocopeatNameDiv.style.display = 'none';
      cocopeatWeightDiv.style.display = 'none';
    }
  }

  // Run on page load
  toggleFields();

  // Run when dropdown changes
  stageSelect.addEventListener('change', toggleFields);
});
