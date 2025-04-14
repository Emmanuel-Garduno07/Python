const frutas = {
    amarillo: {
      nombre: "Plátano",
      descripcion: `
        <p>La banana, conocida también como banano, plátano, guineo maduro, guineo, cambur, gualele o mínimo, es un fruto comestible de varios tipos de grandes plantas herbáceas del género Musa (de origen indomalayo). A estas plantas de gran porte que tienen aspecto de arbolillo se las denomina plataneras, bananeros, bananeras, plátanos o bananos.</p>
        <p>El plátano es una de las frutas más consumidas en el mundo. Tiene un alto contenido en potasio y fibra, lo que lo convierte en una excelente opción para la salud cardiovascular y digestiva.</p>
        <p>Es una fuente rápida de energía, ideal para deportistas y personas que realizan actividades físicas. Además, su sabor dulce lo convierte en un tentempié delicioso y nutritivo.</p>`,
      imagen: "platano.jpeg"
    },
    verde: {
      nombre: "Manzana Verde",
      descripcion: `
        <p>El kiwi es refrescante, ácido y muy saludable.</p>
        <p>Las manzanas verdes, como la variedad Granny Smith, son conocidas por su sabor ácido y su textura crujiente. Son una excelente fuente de vitaminas, especialmente vitamina C, y tienen un alto contenido de fibra.</p>
        <p>Además, las manzanas verdes son bajas en calorías, lo que las convierte en una opción perfecta para aquellos que buscan mantener una dieta equilibrada y saludable.</p>`,
      imagen: "manzana.jpeg"
    },
    naranja: {
      nombre: "Naranja",
      descripcion: `
        <p>La naranja es una fruta cítrica de forma esférica, con pulpa jugosa y sabor agridulce. Su color varía entre el anaranjado y el amarillo, aunque a veces también es verde.</p>
        <p>Es una fuente rica de vitamina C, lo que ayuda a fortalecer el sistema inmunológico y a mejorar la salud de la piel. Las naranjas también contienen antioxidantes, que son beneficiosos para la salud general.</p>
        <p>Al ser refrescantes y jugosas, las naranjas son una excelente opción para el desayuno o como un snack saludable durante el día.</p>`,
      imagen: "naranja.jpeg"
    },
    morado: {
      nombre: "Uva morada",
      descripcion: `
        <p>Las uvas moradas son frutos jugosos y carnosos de color morado, con una piel delgada y resistente. Son ricas en vitaminas y minerales, y tienen propiedades antioxidantes y antiinflamatorias.</p>
        <p>Estas uvas son especialmente populares por sus beneficios para la salud cardiovascular. El consumo de uvas moradas puede ayudar a reducir la presión arterial y mejorar la circulación sanguínea.</p>
        <p>Además, las uvas moradas contienen resveratrol, un compuesto que se ha asociado con la mejora de la longevidad y la prevención de enfermedades crónicas.</p>`,
      imagen: "uva.jpg"
    }
  };
  
  function mostrarFruta(color) {
    const fruta = frutas[color];
  
    // Cambiar contenido textual
    document.getElementById("nombreFruta").textContent = fruta.nombre;
    document.getElementById("descripcionFruta").innerHTML = fruta.descripcion; // Usar innerHTML para permitir HTML
  
    // Mostrar imagen
    const imagen = document.getElementById("imagenFruta");
    imagen.src = fruta.imagen;
    imagen.alt = fruta.nombre;
    imagen.style.display = "block";
  }
  