# Procesamiento de noticias para ***dlm***

Repo para **estandarizar** el procesamiento de noticias, **evitar errores** y **agilizar** el *proceso de producción*.

___

## Receta a seguir

*Básicamente*, la idea es seguir los siguientes pasos:

 1. **Bajar csvs** con noticias a procesar y guardarlos en '*noticias*'
 2. **Armar script** en la carpeta base del repo (misma altura que las carpetas) que levante las noticias y prepare y corra algún modelo de la '*libreria*'.
 3. **Correr script**
 4. **Chequear resultados** generados en la carpeta '*resultados*'.

___

#### **Rol de cada carpeta**

- '*libreria*': contiene todos los *modelos* que podemos procesar con las **noticias**. Y también contiene funciones *útiles* (que no son modelos).
- '*noticias*': contiene todos los *archivos que tengan noticias* a procesar. Por ejemplo: los *dias* que bajemos del drive. El contenido de esta carpeta está vacio, cada unx tiene que llenarlo con las noticias que vaya a procesar.
- '*resultados*': contiene los resultados de procesamiento. Una vez que corramos un modelo de la libreria, el resultado va a guardarse en esta carpeta. La sintaxis de los resultados generados son: "**\<nombre\>**\_**\<modelo\>**\_**\<fecha\>**.csv". Por ejemplo: el día *17/08/2022 a las 19:10:30* corremos el modelo '*topicos*' y le ponemos nombre '*naranja*', el archivo resultado de salida va a ser: "**naranja**\_**topicos**\_**202200817-191030**.csv".
- '*ejemplos*': contiene ejemplos de cómo correr cada modelo + 1 ejemplo de archivo con noticias (*ejemplo_noticias.csv*, tiene 100 noticias)

 ### **Ejemplos**

La carpeta '*ejemplos*' contiene scripts de ejemplo para usar los modelos, y un ejemplo de archivo con noticia (*ejemplo_noticias.csv*). Se pueden copiar y pegar en la base del repo (al mismo nivel que las carpetas) y correr directamente

### **Cómo correr los scripts?**

Desde vs code, los scripts se pueden correr:

1. parados en el scripts, apretar '**f5**' para debugear, o **'ctrl' + 'f5'** para correr sin debugear.
2. click derecho en el script a correr -> "*Run Python File in Terminal*"
3. desde la terminal, nos paramos en la carpeta base del proyecto `cd dlm-procesamientos` y ejecutamos `python <archivo_py_con_script_a_ejecutar>`.

