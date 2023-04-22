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

mapas = {
    'diarios' : {
      'clarin' : 'Clarín',
      'lanacion' : 'La Nación',
      'infobae' : 'Infobae',
      'eldestape' : 'El Destape',
      'todonoticias' : 'TN',
      'ambito' : 'Ámbito',
      'paginadoce' : 'Página 12',
      'perfil' : 'Perfil',
      'casarosada' : 'Casa Rosada',
      'diariodeleuco' : 'Diario de Lueco'
    }
}

notis = noticias.levantar()
topicos.procesar(
    noticias=notis,
    topicos=lista_topicos, 
    mapas=mapas,
    id='cfk_vs_larreta'
)