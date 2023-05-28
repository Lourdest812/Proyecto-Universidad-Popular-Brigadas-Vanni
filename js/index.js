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

