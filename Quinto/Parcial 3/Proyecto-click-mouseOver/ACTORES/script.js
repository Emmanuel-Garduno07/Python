const actores = {
    actor1: {
      nombre: "Robert Downey Jr.",
      descripcion: `
        <p>Robert Downey Jr. es un actor y productor estadounidense, conocido principalmente por su papel como Iron Man en el Universo Cinematográfico de Marvel (MCU).</p>
        <p>Ha sido galardonado con varios premios, incluyendo un Globo de Oro, y es considerado uno de los actores más carismáticos de Hollywood.</p>`,
      imagen: "act1.jpg"
    },
    actor2: {
      nombre: "Scarlett Johansson",
      descripcion: `
        <p>Scarlett Johansson es una actriz y cantante estadounidense, famosa por su papel de Natasha Romanoff (Viuda Negra) en el MCU.</p>
        <p>Ha trabajado en una amplia variedad de géneros cinematográficos, desde acción hasta drama, y es una de las actrices más influyentes de su generación.</p>`,
      imagen: "act2.jpg"
    },
    actor3: {
      nombre: "Chris Hemsworth",
      descripcion: `
        <p>Chris Hemsworth es un actor australiano, conocido mundialmente por su papel de Thor en el MCU.</p>
        <p>Hemsworth ha sido parte de numerosas películas de gran éxito y es considerado uno de los actores más destacados de la industria cinematográfica actual.</p>`,
      imagen: "act3.jpg"
    },
    actor4: {
      nombre: "Chris Evans",
      descripcion: `
        <p>Chris Evans es un actor y director estadounidense, conocido por interpretar a Steve Rogers/Captain America en el MCU.</p>
        <p>Ha sido aclamado por su capacidad para interpretar papeles de héroe y ha tenido una carrera exitosa en la televisión y el cine.</p>`,
      imagen: "act4.jpg"
    }
  };
  
  function mostrarActor(actor) {
    const datosActor = actores[actor];
  
    // Cambiar contenido textual
    document.getElementById("nombreActor").textContent = datosActor.nombre;
    document.getElementById("descripcionActor").innerHTML = datosActor.descripcion; // Usar innerHTML para permitir HTML
  
    // Mostrar imagen
    const imagen = document.getElementById("imagenActor");
    imagen.src = datosActor.imagen;
    imagen.alt = datosActor.nombre;
    imagen.style.display = "block";
  }
  