## Función para el filtrado de noticias por tema
# Esta funcion toma una lista de oalabras y filtra las noticias que matchean con 4 o mas terminos y trae variables para el analisis de NLP

#1. Carga un modelo de procesamiento de lenguaje natural en español.
#2. Itera a través de los textos de noticias.
#3. Filtra las noticias con texto en blanco o muy cortas.
#4. Cuenta cuántas veces aparecen ciertos términos clave en cada noticia y filtra las noticias con pocas coincidencias.
#5. Utiliza SpaCy para analizar lingüísticamente el texto restante.
#6. Extrae información relevante como sustantivos, adjetivos, verbos, personas, organizaciones y lugares.
#7. Almacena esta información en un DataFrame.
#8. Finalmente, crea un DataFrame con los datos procesados para su posterior análisis.

import spacy
from datatable import dt, f
import pandas as pd

# Creo una funcion para procesar las noticias
def filtrar_noticias(lista_terminos, noticias_csv):
    nlp = spacy.load('es_core_news_md')
    # Carga el archivo CSV de noticias
    noticias = dt.fread(noticias_csv, header=True).to_pandas()

    # Contador
    i = 0
    textos = noticias['texto'].tolist()

    # Crea un dataframe vacio
    df = dt.Frame(id_noticia=[], diario=[], seccion=[], fecha=[], texto=[],
                  sustantivos=[], adjetivos=[], verbos=[],
                  personas=[], organizaciones=[], lugares=[], matcheos=[])

    total = str(len(textos))

    # Iteracion
    for texto in textos:
        print(str(i) + ' de ' + total)
        # oraciones = list(nlp(texto).sents)
        # for oracion in oraciones:
        
        # Filtro de noticias basado en la cantidad de coincidencias 
        if len(texto.strip()) == 0 or len(texto.strip()) < 10: #Comprueba si el texto esta en blanco o tiene menos de 10 caracteres
            i += 1
            continue

        conteo = 0 #conteo de terminos en el texto
        matcheos = [] #para almacenar los terminos que coinciden con la bolsa

        for termino in lista_terminos:
            conteo += int(termino in texto) # conteo de coincidencias
            if termino in texto:
                matcheos.append(termino)

        if conteo < 4 or conteo / len(texto) < 0.001: # Se queda con las noticias que tengan 4 o mas matches con la bolsa
            i += 1
            continue

        cuerpo = nlp(texto) # se procesa el texto con el modelo de NLP cargado arriba
        
        # Extraccion de informacion linguistica
        diario = noticias.loc[i, 'diario']
        seccion = noticias.loc[i, 'seccion']
        fecha = noticias.loc[i, 'fecha'][:10]
        titulo = noticias.loc[i, 'titulo']

        sustantivos = ','.join([t.lemma_.lower() + '-' + str(t.idx) for t in cuerpo if t.pos_ == 'NOUN'])
        adjetivos = ','.join([t.lemma_.lower() + '-' + str(t.idx) for t in cuerpo if t.pos_ == 'ADJ'])
        verbos = ','.join([t.lemma_.lower() + '-' + str(t.idx) for t in cuerpo if t.pos_ == 'VERB'])

        personas = ','.join([e.text + '-' + str(e.start_char) for e in cuerpo.ents if e.label_ == 'PER'])
        organizaciones = ','.join([e.text + '-' + str(e.start_char) for e in cuerpo.ents if e.label_ == 'ORG'])
        lugares = ','.join([e.text + '-' + str(e.start_char) for e in cuerpo.ents if e.label_ == 'LOC'])
        
        # fechas = ','.join([e.text for e in oracion.ents if e.label_ == 'DATE'])
        # geopoliticos = ','.join([e.text for e in oracion.ents if e.label_ == 'GPE'])
        # eventos = ','.join([e.text for e in oracion.ents if e.label_ == 'EVENT'])
    
    
        #crea el dataframe

        fila = dt.Frame({"id_noticia": [i], "diario": [diario], "seccion": [seccion], "fecha": [fecha],
                          "texto": [cuerpo.text.strip()],
                          "sustantivos": [sustantivos], "adjetivos": [adjetivos], "verbos": [verbos],
                          "personas": [personas], "organizaciones": [organizaciones], "lugares": [lugares],
                          "matcheos": [','.join(matcheos)]})

        df.rbind(fila)
        
        # contador de noticias para saber por donde va
        i += 1

    return df # Me devuelve el df