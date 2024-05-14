# API Funcionamiento

## Introducción

Para entender como recorre la api puedes usar la guia de usuario [aquí](https://exoplanetarchive.ipac.caltech.edu/docs/program_interfaces.html#data).

Entender que podemos encontrar en la web con sola la url de la api y declarando la tabla que necesitamos, es con conocimiento de base de datos y de la estructura de la web.

tenemos que tener nuestra url base que es: https://exoplanetarchive.ipac.caltech.edu/cgi-bin/nstedAPI/nph-nstedAPI?table=exoplanets

y saber que tablas podemos usar, en este caso usaremos la tabla de cumulative.

## Cumulative

podemos acceder a mas informacion con otros parametros de SQL

como parametros a la url que podemos agregar son:

```python
where=koi_disposition like 'CANDIDATE' and koi_period>300 and koi_prad<2
```

La url completa seria:
https://exoplanetarchive.ipac.caltech.edu/cgi-bin/nstedAPI/nph-nstedAPI?table=cumulative&where=koi_disposition like 'CANDIDATE' and koi_period>300 and koi_prad<2

Se nota que añadimos SQL a la url, esto es para filtrar la informacion que queremos obtener.
y de esa forma seran nuestras consultas ala API.

El ejemplo de uso que tenemos para entender esta en nuestro archivo user_guide de python.

Para ejecutarlo debes crear tu entorno virtual:

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

y luego ejecutar el archivo:

```bash
python3 user_guide.py
```

y veras como se ejecuta el codigo y te muestra la informacion que obtiene de la API en Chrome.

## Guardar la informacion en un archivo

Para guardar la informacion en un archivo podemos usar wget, curl o python.

Desde bash podemos usar wget o curl:

```bash
wget -O exoplanets.csv "https://exoplanetarchive.ipac.caltech.edu/cgi-bin/nstedAPI/nph-nstedAPI?table=cumulative&where=koi_disposition like 'CANDIDATE' and koi_period>300 and koi_prad<2"
```

o con curl:

```bash
curl "https://exoplanetarchive.ipac.caltech.edu/cgi-bin/nstedAPI/nph-nstedAPI?table=cumulative&where=koi_disposition like 'CANDIDATE' and koi_period>300 and koi_prad<2" > exoplanets.csv
```
