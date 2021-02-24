
### Comandos ###
Nota: Necesarios 'pip' y 'virtualenv': 

    Instalar dependencias: make install

    Correr tests: make tests

    Correr aplicacion: make run

    Todos a la vez: make all


Alternativamente:
> pip install -r requirements.txt

Recomendado usar un entorno virtual
> source venv/bin/activate

Test:
> python manage.py test

Ejecutar:
> python manage.py run
 
 
Es necesario hacer las migraciones iniciales en la base de datos.
> python manage.py db init
> python manage.py db migrate
> python manage.py db upgrade


### Documentación  ###
    Documentación  de swagger en localhost:
    http://127.0.0.1:5000/

### Restx en lugar de RestPlus
https://github.com/noirbizarre/flask-restplus/pull/778
No hay mucha diferencia.
