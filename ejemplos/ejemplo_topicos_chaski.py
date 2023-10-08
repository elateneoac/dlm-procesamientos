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
    'desde':'20231005',
    'hasta':'20231007', # para buscar por horario: '20231007-21:30:00'
    # 'medios' : ['clarin-lanacion'],
    # 'secciones' : ['politica-economia'],
    # 'todos':['milei','massa'],
    # 'alguno':['bullrich'],
    # 'ninguno':['larreta'],
    # 'textual':'frase textual a buscar en titulos o textos',
    # 'en_titulo':True, # busco en titulos
    # 'en_texto':True, # busco en textos
}
notis = c.noticias(query)

topicos.procesar(
    noticias=notis,
    topicos=lista_topicos,
    mapas=mapas
)