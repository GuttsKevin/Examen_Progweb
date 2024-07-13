function serSocio(variable) {
    Swal.fire({
        position: 'top-end',
        icon: 'success',
        title: `Felicitaciones, ya eres socio! ${variable}`,
        showConfirmButton: false,
        timer: 1500
    });
}

document.addEventListener('DOMContentLoaded', function () {
    const botonUnirse = document.getElementById('botonUnirse');
    const formularioCorreo = document.getElementById('formularioCorreo');
    const botonCerrar = document.getElementById('botonCerrar');
    const formularioSuscripcion = document.getElementById('formularioSuscripcion');

    botonUnirse.addEventListener('click', function () {
        formularioCorreo.style.display = 'block';
    });

    botonCerrar.addEventListener('click', function () {
        formularioCorreo.style.display = 'none';
    });

    formularioSuscripcion.addEventListener('submit', function (event) {
        event.preventDefault();

        const entradaCorreo = document.getElementById('entradaCorreo').value;
        
        Swal.fire({
            position: 'top-end',
            icon: 'success',
            title: 'Tu información ha sido enviada',
            showConfirmButton: false,
            timer: 1500
        }).then(() => {
            formularioCorreo.style.display = 'none';
            serSocio('Información de suscripción');
        });
    });
});

AOS.init({
    duration: 1200, 
});

function verMas(id) {
    $.ajax({
      url: `/api/libros/${id}/`,  // Endpoint para obtener detalles del libro
      method: "GET",
      success: function (data) {
        // Rellena el modal con la información del libro
        $("#libroNombre").text(data.nombre);
        $("#libroAutor").text(data.autor);
        $("#libroAnio").text(data.anio);
        $("#libroPrecio").text(data.precio);
        // Muestra el modal
        $("#detalleLibroModal").modal('show');
      },
      error: function (xhr, status, error) {
        console.error("Error al obtener los detalles del libro: ", error);
      }
    });
  }