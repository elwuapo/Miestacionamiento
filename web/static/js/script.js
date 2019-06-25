// ESTACIONAMIENTOS ALMACENADOS
var estacionamientos = 
  [
    // LAT = LATITUD, LNG = LONGITUD
    {lat:-33.4179935 ,lng: -70.6085788,},
    {lat:-33.4047827 ,lng: -70.6686312,},
  ];

// FUNCION QUE ME INICIA EL MAP DE GOOGLE MASPS
function iniciarMap(){

  var coordenada = {lat:-33.4179935 ,lng: -70.6085788,};

  var map = new google.maps.Map(document.getElementById('map'),{
    zoom: 10,
    center: coordenada
  });

  for (i = 0; i < estacionamientos.length; i++){
      var marker = new google.maps.Marker({
          position: estacionamientos[i],
          map: map
      });
  }
}

// FUNCION QUE ME AGREGARA UN ESTACIONAMIENTO

function agregarEstacionamiento(){

  var latitud = document.getElementById('latitud').value;
  var longitud = document.getElementById('longitud').value;
  
  num_latitud = parseFloat(latitud);
  num_longitud = parseFloat(longitud);

  // METODO QUE ME AGREGARA ESTE ELEMENTO AL FINAL DE MI ARREGLO 
  estacionamientos.push({lat: num_latitud, lng: num_longitud});
}

