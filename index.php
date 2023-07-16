<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Sistema de registro</title>
    <!-- estilo de la carpeta login -->
    <link rel="stylesheet" href="./login/estilo.css">
    <!-- estilos de bootstrap -->
    <link rel="stylesheet" href="./plugin/bootstrap/dist/css/bootstrap.min.css">
</head>
<body>
    <div class="loginbox">
        <img src="login/img/2.jpeg" alt="" class="avatar">
        
        <h4 class="text text-center">INICIO DE SESION</h1>
      
        <form action="" method="post">
            <p>Usuario </p>
                <input type="text"placeholder="Ingrese su Usuario" name="usuario"> 
                <p>Contraseña</p>
                    <input type="password"placeholder="Ingrese su Contraseña" name="password"> 
                    <input type="submit" value="ingresar" name="btningresar">
        </form>
        <?php
        include('model/conexion.php');
        include('controller/controlador_login.php');
        ?>
    </div>

</body>
</html>