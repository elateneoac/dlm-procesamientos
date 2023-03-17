from libreria import noticias, cercanos

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
      'perfil' : 'Perfil'
    }
}

cfk = ['cfk', 'cristina fernández', 'cristina fernández de kirchner']
notis = noticias.levantar(diarios=['clarin'], secciones=['politica'])

cercanos.procesar(
   concepto=cfk,
   noticias=notis,
   top=50,
   mapas=mapas
)