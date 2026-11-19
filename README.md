Fibonacci con Python (unittest)

Se he separado la práctica en dos módulos independientes siguiendo las instrucciones.

fibo.py:  Mediante una función que recibe un parámetro n, y utiliza un bucle while para sumar los dos últimos valores y añadir el siguiente con append(). 

fibotest.py:  unittest.

test_fibonacci_9_elementos: Verifica que al solicitar 9 elementos, la lista devuelta coincide exactamente con los 9 primeros valores de la serie (terminando en 21).

test_fibonacci_11_elementos: Amplía la comprobación para 11 elementos, hasta el valor 55.

test_fibonacci_caso_cero: La entrada de 0 devuelve una lista vacía sin arrojar excepciones.

El script se ejecuta directamente desde la terminal mediante el intérprete de comandos de Python para verificar de forma automatizada el éxito de todas las aserciones (assertEqual).
