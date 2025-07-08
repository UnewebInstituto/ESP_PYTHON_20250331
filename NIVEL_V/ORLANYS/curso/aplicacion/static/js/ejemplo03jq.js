$('#btnCalcular').click(function(){
  // Declaración de variables 
  var a, b, c, x1, x2, subR, mensaje;
  // Inicialización de variables
  a = 0; b = 0; c = 0; x1 = 0; x2 = 0, subR = 0;
  mensaje = '';
  // Tomar valores del documento html
  a = $('#a').val();
  b = $('#b').val();
  c = $('#c').val();
  // Convertir de texto a numero
  a = parseFloat(a);
  b = parseFloat(b);
  c = parseFloat(c);
  // Evaluación de los datos
  if (a == 0){
      mensaje = '<div class=\'alert alert-danger\'><strong>Error: </strong>El valor de a debe ser diferente de cero.</div>';
  }else{
      subR = Math.pow(b,2) - 4 * a * c;
      if ( subR < 0 ){
          mensaje = '<div class=\'alert alert-warning\'><strong>Atención: </strong>El resultado de la expresión sub radical no puede ser negativo.</div>';
      }else{
          x1 = (-b - Math.sqrt(subR))/(2 * a);
          x2 = (-b + Math.sqrt(subR))/(2 * a);
          mensaje = '<div class=\'alert alert-success\'><strong>Resultado: </strong><br>x1: ' + x1 +' <br> x2: ' + x2 + '</div>';
      }
  }
  // Presentar los resultados
  $('#resultado').html(mensaje);
});

$('#btnLimpiar').click(function(){
  $('#a').val('');
  $('#b').val('');
  $('#c').val('');
  $('#resultado').html('');
});