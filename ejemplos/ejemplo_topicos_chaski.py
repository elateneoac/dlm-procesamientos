from libreria.chaski import Chaski
from libreria import topicos

lista_topicos = [
   {
      'etiqueta' : 'dólar',
      'terminos' : ['dólar blue', 'dólar informal']
   }
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
      'diariodeleuco' : 'Diario de Leuco',
      'casarosada' : 'Casa Rosada',
    }
}

usuario='mail de mercagopago'
token='token que llegó por mail'

c = Chaski(usuario, token)

query = {
    'desde':'20231003', # noticias DESDE esta fecha (se puede especificar horario: 20231005-10:30:00)
    'hasta':'20231010', # noticias HASTA esta fecha (se puede especificar horario: 20231007-21:30:00)
    # 'medios' : ['clarin-lanacion'], # diarios a filtrar
    # 'secciones' : ['politica-economia'], # secciones a filtrar
    # 'todos':['milei','massa'], # noticias que contengan TODOS estos términos
    # 'alguno':['bullrich'], # noticias que contengan ALGUNO estos términos
    # 'ninguno':['larreta'], # noticias que NO contengan NINGUNO de estos términos
    # 'textual':'frase textual a buscar en titulos o textos', # noticias que contengan EXACTAMENTE ESTA FRASE
    # 'en_titulo':True, # busco en titulos
    # 'en_texto':True, # busco en textos
}
notis = c.noticias(query)

topicos.procesar(
    noticias=notis,
    topicos=lista_topicos,
    mapas=mapas
)