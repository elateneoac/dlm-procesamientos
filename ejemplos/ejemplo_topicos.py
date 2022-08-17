# procesamiento 'cfk-vs-larreta'

from libreria import topicos, utiles

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

noticias = utiles.levantar_noticias()
topicos.procesar(noticias, lista_topicos, 'cfk_vs_larreta')