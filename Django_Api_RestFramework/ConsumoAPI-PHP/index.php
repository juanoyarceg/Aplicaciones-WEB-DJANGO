<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Vistas Catalogo</title>

    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css">
    <script src="https://cdnjs.cloudflare.com/ajax/libs/jquery/3.4.1/jquery.js"></script>

    <script>
        $(document).ready(function () {
            Listar();
        });

        function Limpiar() {
            $("#pk").val('');
            $("#nombre").val('');
            $("#detalle").val('');
            $("#precio").val('');
            $("#pcrear").show();
            $("#peditar").hide();
        }

        function Listar() {
            Limpiar();
            var str = '';
            $.ajax({
                url: 'http://127.0.0.1:8000/catalogo/',
                type: 'get',
                success: function (datos) {
                    $.each(datos, function (i, item) {
                        str += '<tr>';
                        str += '<td>' + item.nombre + '</td>';
                        str += '<td>' + item.detalle + '</td>';
                        str += '<td>' + item.precio + '</td>';
                        str += '<td><input class="btn btn-warning" type="button" value="E" onclick="Editar(' + item.pk + ')"></td>';
                        str += '<td><input class="btn btn-danger" type="button" value="X" onclick="Borrar(' + item.pk + ')"></td>';
                        str += '</tr>';
                    });
                    $("#listar").html(str);
                }
            });
        }

        function Crear() {
            var nom = $("#nombre").val();
            var det = $("#detalle").val();
            var pre = $("#precio").val();
            $.ajax({
                url: 'http://127.0.0.1:8000/catalogo/',
                data: {
                    nombre: nom,
                    detalle: det,
                    precio: pre
                },
                type: 'post',
                success: function (datos) {
                    Listar();
                }
            });
        }

        function Editar(pk) {
            $("#pcrear").hide();
            $("#peditar").show();
            $.ajax({
                url: 'http://127.0.0.1:8000/catalogo/' + pk + '/',
                type: 'get',
                success: function (datos) {
                    $("#pk").val(datos.pk);
                    $("#nombre").val(datos.nombre);
                    $("#detalle").val(datos.detalle);
                    $("#precio").val(datos.precio);
                }
            });
        }

        function Update() {
            var pk = $("#pk").val();
            var nom = $("#nombre").val();
            var det = $("#detalle").val();
            var pre = $("#precio").val();
            $.ajax({
                url: 'http://127.0.0.1:8000/catalogo/' + pk + '/',
                data: {
                    pk: pk,
                    nombre: nom,
                    detalle: det,
                    precio: pre
                },
                type: 'put',
                success: function (datos) {
                    Listar();
                }
            });
        }

        function Borrar(pk) {
            $.ajax({
                url: 'http://127.0.0.1:8000/catalogo/' + pk + '/',
                type: 'delete',
                success: function (datos) {
                    Listar();
                }
            });
        }
    </script>
</head>

<body>
    <div class="container">
        <h2>Consumo de API Rest-Django</h2>
        <div class="row">
            <div class="col-md-4">
                <form action="" method="post">
                    <p>
                        <label for="pk">PK</label>
                        <input readonly class="form-control" type="text" name="pk" id="pk">
                    </p>
                    <p>
                        <label for="nombre">Nombre</label>
                        <input class="form-control" type="text" name="nombre" id="nombre">
                    </p>
                    <p>
                        <label for="nombre">Detalle</label>
                        <input class="form-control" type="text" name="detalle" id="detalle">
                    </p>
                    <p>
                        <label for="nombre">precio</label>
                        <input class="form-control" type="number" name="precio" id="precio">
                    </p>
                    <p id="pcrear">
                        <input class="btn btn-primary" type="button" value="Crear" onclick="Crear()">
                    </p>
                    <p id="peditar">
                        <input class="btn btn-primary" type="button" value="Update" onclick="Update()">
                    </p>
                </form>
            </div>
            <div class="col-md-1"></div>
            <div class="col-md-7">
                <table class="table table-bordered table-striped">
                    <thead>
                        <tr class="table-info">
                            <td>Nombre</td>
                            <td>Detalle</td>
                            <td>Precio</td>
                            <td></td>
                            <td></td>
                        </tr>
                    </thead>
                    <tbody id="listar"></tbody>
                </table>
            </div>
        </div>
    </div>
</body>

</html>