<?php
// Nombre y contraseña correctos (puedes cambiar estos valores)
$nombre_correcto = "juan";
$clave_correcta = "1234";

// Recoger datos del formulario
$nombre = $_POST['name'];
$edad = $_POST['age'];
$contraseña = $_POST['password'];

// Verificar si el nombre y la contraseña coinciden
if ($nombre === $nombre_correcto && $contraseña === $clave_correcta) {
    echo "Bienvenido, " . htmlspecialchars($nombre) . "<br>";
    echo "Edad: " . htmlspecialchars($edad);
} else {
    echo " Usuario o contraseña incorrecto.";
}
?>
