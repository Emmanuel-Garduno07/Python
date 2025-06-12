<?php
move_uploaded_file($_FILES["archivo"]["tmp_name"], 'archivo/' . $_FILES["archivo"]["name"]);
echo "Archivo Subido";
?>