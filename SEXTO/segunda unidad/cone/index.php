<?php
$servidor = "localhost";
$usuario = "root";
$clave = "";
$basedatos = "sistema";

$conexion = new MySQLi($servidor, $usuario, $clave, $basedatos);

if ($conexion) {
    echo "conexión exitosa";
}

$conexion->close();
?>