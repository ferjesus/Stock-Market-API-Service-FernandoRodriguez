# Stock-Market-API-Service-FernandoRodriguez

La api fue deployado en Heroku.
- Para autentificación se utiliza el siguiente endpoint: https://apifer.herokuapp.com/auth, se debe usar una Basic Auth. username: fer, Password: pwd. Debe retornar un token el cual debe ser usado para la siguiente operación.
- Market info: https://apifer.herokuapp.com/marketinfo. Enviar token en header como Bearer Token. Se debe enviar un body en json con los parámetros para realizar la consulta. Ejemplo: {"MARKET":"GOOGL", "FUNCTION":"TIME_SERIES_DAILY", "SIZE":"compact"}
- Se adjuntan capturas de pantalla de ejecucion.

Comentarios:
- Sobre la autentificación, no me quedo claro el requerimiento ya que normalmente si se requiere un registro se tendría que hacer usando oauth 2, para lo cual se tendría que implementar el API portal y poder registrar los API products, developers y consumidores.
- Por temas de tiempo se aplicó un método de autenticación muy básico para poder cumplir con el requerimiento.
- Queda la duda en el requerimiento si con la respuesta del API de alphavantage se tendría que realizar alguna transformación en el mensaje o algún agrupamiento. En este caso se está ejecutando un pass true, mostrando el mensaje tal como lo responde alphavantage.
