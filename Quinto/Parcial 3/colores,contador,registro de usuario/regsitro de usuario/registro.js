function registrarUsuario() {
    const nombre = prompt("Ingresa tu nombre:");
    const correo = prompt("Ingresa tu correo:");
    const edad = prompt("Ingresa tu edad:");
  
    if (nombre && correo && edad) {
      const mensaje = `
        <p>Nombre: ${nombre}</p>
        <p>Correo: ${correo}</p>
        <p>Edad: ${edad}</p>
      `;
      document.getElementById("datosUsuario").innerHTML = mensaje;
      alert("¡Registro exitoso!");
    } else {
      alert("Por favor, completa todos los campos.");
    }
  }
  