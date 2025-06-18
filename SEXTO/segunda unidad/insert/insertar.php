<?php
$host = "localhost";
$user = "root";
$password = "";
$database = "sistema";

// Obtener el nombre desde el formulario
$nombre = $_POST['nombre'];

// Crear la conexión
$conexion = new mysqli($host, $user, $password, $database);

// Verificar la conexión
if ($conexion->connect_error) {
    die("Conexión fallida: " . $conexion->connect_error);
}

// Preparar la consulta para insertar en la tabla login
$insertar = $conexion->prepare("INSERT INTO login (nombre) VALUES (?)");

if ($insertar) {
    $insertar->bind_param("s", $nombre);

    if ($insertar->execute()) {
        echo "Nombre guardado correctamente";
    } else {
        echo "Error al guardar el nombre: " . $insertar->error;
    }

    $insertar->close();
} else {
    echo "Error en la preparación: " . $conexion->error;
}

$conexion->close();
?>