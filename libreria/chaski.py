import datetime, requests, time

class Chaski:
    def __init__(self, usuario, token):
        self.credenciales = {
            'token' : token,
            'usuario' : usuario
        }
        self.url = 'https://chaski.com.ar/noticias/'

    def noticias(self, query, path=''):
        """
        Recupero noticias que matcheen con la 'query'.
        """
        endpoint = self.__armarendpoint__(query)
        r = requests.get(endpoint, headers=self.credenciales,)
        rta = r.json()
        if 'error' in rta:
            print(rta)
            return []

        notis = []
        for n in rta['noticias']:
            notis.append( (n['Medio'], n['Seccion'], n['Fecha'], n['Titulo'], n['Texto']) )

        if len(path):

            tabla = 'diario,seccion,fecha,titulo,texto\n'
            for n in rta['noticias']:
                tabla += '{},{},{},"{}","{}"\n'.format(n['Medio'], n['Seccion'], n['Fecha'], n['Titulo'].replace('"',''), n['Texto'].replace('"',''))

            csv = open(path, 'wt', encoding="utf-8")
            csv.write(tabla)
            csv.close()

        time.sleep(1.5)

        return notis

    def prepros(self, query):
        """
        Recupero preprocesamientos de noticias que matcheen con la 'query'.
        """
        endpoint = self.__armarendpoint__(query, 'prepro')
        r = requests.get(endpoint, headers=self.credenciales)
        rta = r.json()
        if 'error' in rta:
            print(rta)
            return []

        prepros = []
        for p in rta['prepros']:
            prepros.append( (p['Medio'], p['Seccion'], p['Fecha'], p['Mapa']) )

        time.sleep(1.5)

        return prepros

    def contar(self, query):
        """
        Cuento la cantida de noticias que matcheen con la 'query'.
        """
        endpoint = self.__armarendpoint__(query, 'contar')
        r = requests.get(endpoint, headers=self.credenciales)
        rta = r.json()
        if 'error' in rta:
            print(rta)
            return []

        time.sleep(1.5)

        return rta['cantidad']

    def __armarendpoint__(self, query, accion=''):
        if 'desde' not in query:
            raise Exception('Tiene que estar definida la fecha "desde" cuando hacer la consulta.')

        endpoint = self.url + query['desde'] + '/'

        if 'hasta' not in query:
            query['hasta'] = datetime.date.strftime(datetime.date.today(), "YYYYMMDD")
            
        endpoint += query['hasta']

        if 'medios' in query and len(query['medios']):
            endpoint += '/' + '-'.join(query['medios'])

        if 'secciones' in query and len(query['secciones']):
            if 'medios' not in query or len(query['medios']) == 0:
                endpoint += '/'
            endpoint += '/' + '-'.join(query['secciones'])

        endpoint += '/' + accion
        
        filtro = []
        if 'todos' in query and len(query['todos']):
            filtro.append('todos=' + ','.join(query['todos']))

        if 'alguno' in query and len(query['alguno']):
            filtro.append('alguno=' + ','.join(query['alguno']))
            
        if 'ninguno' in query and len(query['ninguno']):
            filtro.append('ninguno=' + ','.join(query['ninguno']))

        if 'textual' in query and len(query['textual']):
            filtro.append('textual=' + ','.join(query['textual']))

        if len(filtro):
                en = []

                if 'en_titulo' in query and query['en_titulo']:
                    en.append('titulo')

                if 'en_texto' in query and query['en_texto']:
                    en.append('en_texto')
                
                if len(en):
                    filtro.append('en=' + ','.join(en))
                
                endpoint += '?' + '&'.join(filtro)

        return endpoint



    


