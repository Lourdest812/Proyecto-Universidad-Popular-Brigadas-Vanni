 //API
 async function getRandomUser(){
    const response = await fetch('https://randomuser.me/api');
    const data = await response.json();
    const user = data.results[0];
    console.log(user);
    displayUser(user);
  }

  function displayUser(user){
    const name = document.getElementById('name');
    const gender = document.getElementById('gender');
    const email = document.getElementById('email');
    const phone = document.getElementById('phone');
    const location = document.getElementById('location');
    const image = document.getElementById('image');

    name.innerText = `${user.name.title} ${user.name.first} ${user.name.last}`;
    gender.innerText=`${user.gender}`;
    email.innerText = `${user.email}`;
    phone.innerText = `${user.phone}`;
    
    location.innerText = `${user.location.country}`;
    image.setAttribute('src', `${user.picture.large}`);
  }

  getRandomUser();


  //GALERÍA DE IMAGENES EN SOBRE NOSOTROS
var imageThumbs = document.getElementById("image-thumbs");
var currentImage = document.getElementById("current-image");

for (var i = 1; i <= 5; i++) {
  var thumb = document.createElement("img");
  thumb.src = "img/image" + i + ".jpg";
  thumb.alt = "Image " + i;
  thumb.classList.add("thumb");
  imageThumbs.appendChild(thumb);
  thumb.addEventListener(
    "click", function() {
    currentImage.src = this.src;
    }
  );
}


//FORMULARIO DE CONTACTO

function habilitar(){
  campo1 = document.getElementById("campo1").value;
  campo2 = document.getElementById("campo2").value;
  campo3 = document.getElementById("campo3").value;
  val = 0;
  
  if(campo1 == ""){
      val++; 
  }
  if(campo2 == ""){
      val++; 
  }
  if(campo3 == ""){
      val++; 
  }
  
  if(val == 0){
      document.getElementById("enviar").disabled = false;
  }else{
      document.getElementById("enviar").disabled = true;
  }
   
  }
  
  document.getElementById("campo1").addEventListener("keyup", habilitar);
  document.getElementById("campo2").addEventListener("keyup", habilitar);
  document.getElementById("campo3").addEventListener("keyup", habilitar);

