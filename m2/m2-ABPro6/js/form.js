/*
// FORMA 3

function verifica(name, email, pais) {
    
  let name = name.value;
  let email = email.value;
  let pais = pais.value;
  
  while (true) {
      
      if (name == "") {
          alert("El campo nombre no puede estar vacio");
          let name = False;
      }
      
      if (email == "") {
          alert("El campo email no puede estar vacio");
          let email = False;
      }

      if (pais == "") {
          alert("El campo pais no puede estar vacio");
          let pais = False;
      }

      if (name&&email&&pais) {
          console.log("Todo correcto");
          break;
      } else {
          console.log("Todo incorrecto");
      }
          }
  }
}


verifica('javier', 'javito@email.com', 'chile');


function sendMail() {

  let name = document.getElementById('name').value;
  let email = document.getElementById('email').value;
  let subject = document.getElementById('subject').value;
  let country = document.getElementById('country').value;

  verifica(name, email, subject, country);

}



*/

// FORMA 1

// function sendMail() {

  // let name = document.getElementById('name').value;
  // let email = document.getElementById('email').value;
  // let subject = document.getElementById('subject').value;
  // let country = document.getElementById('country').value;

  // if (name == ''){
  //   alert('nombre está vacio')
  // }else if(email == ''){
  //   alert('email está vacio')
  // }else if(subject == ''){
  //   alert('tema está vacio')
  // }else if(country == 'ninguno'){
  //   alert('país está vacio')
  // }else{
  //   alert('FORMULARIO ENVIADO');
  // }

// }











// FORMA 2
let alerta_name = document.getElementById('alerta_name');



function sendMail() {

  let name = document.getElementById('name').value;
  let email = document.getElementById('email').value;
  let subject = document.getElementById('subject').value;
  let country = document.getElementById('country').value;

  let alerta_name = document.getElementById('alerta_name');
  let alerta_area = document.getElementById('alerta_area');
  let alerta_email = document.getElementById('alerta_email');
  let alerta_select = document.getElementById('alerta_select');

  if (name == ''){
    alert('nombre está vacio')
   // document.getElementById('name').classList.add('error');
    alerta_name.innerHTML = '<p class="text-danger bg-white">nombre está vacío</p>';// return false;
  }
  if(email == ''){
    alert('email está vacio')
    alerta_email.innerHTML = '<p class="text-danger bg-white">email está vacio</p>'
  }
  if(subject == ''){
    alert('tema está vacio')
    alerta_area.innerHTML = '<p class="text-danger bg-white">el asunto está vacio</p>';
  }
  if(country == 'ninguno'){
    alert('país está vacio')
    alerta_select.innerHTML = '<p class="text-danger bg-white">país está vacio</p>';
  }

  if(
    name != '' &&
    email != ''  &&
    subject != '' &&
    country != 'ninguno') {
   alert('FORMULARIO ENVIADO');
  }
 }


























  
