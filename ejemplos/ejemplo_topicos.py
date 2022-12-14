# procesamiento 'cfk-vs-larreta'

from libreria import noticias, topicos

lista_topicos = [
   {
      'etiqueta' : 'cfk',
      'terminos' : ['cristina fernández', 'cristina kirchner', 'cristina fernández de kirchner']
   },
   {
      'etiqueta' : 'larreta',
      'terminos' : ['horacio rodríguez larreta', 'horacio larreta', 'jefe de gobierno']
   },
]

notis = noticias.levantar()
topicos.procesar(notis, lista_topicos, 'cfk_vs_larreta')