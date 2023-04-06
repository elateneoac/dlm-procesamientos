import datetime, platform

import spacy
nlp = spacy.load('es_core_news_md')

def procesar(concepto, noticias, titulos=False, diarios=[], secciones=[], mapas={},top=50 ,id = ''):
    if type(concepto) is not list:
        concepto = [concepto]
    
    contador = {}

    i = 1
    total = str(len(noticias))
    for diario, seccion, fecha, titulo, texto in noticias:
        print(str(i) + ' de ' + total)
        if (len(diarios) and diario not in diarios) or (len(secciones) and seccion not in secciones):
            continue

        if 'diarios' in mapas:
            diario = mapas['diarios'][diario]

        if 'secciones' in mapas:
            seccion = mapas['secciones'][seccion]
            
        # terminos
        entrada = texto
        if titulos:
            entrada = titulo
        oraciones = list(nlp(entrada).sents)

        for oracion in oraciones:

            if len(oracion.text.strip()) is 0 or not any([t in oracion.text.strip().lower() for t in concepto]):
                continue

            for t in oracion:
                termino = t.lemma_.lower()
                if any([t in termino for t in concepto]) or t.pos_ not in ['NOUN', 'ADJ', 'VERB'] or len(termino) < 3 or termino.startswith('http'):
                    continue
                
                if t.pos_ is 'NOUN':
                    k = termino + ',' + fecha[:10] + ',' + diario + ',' + seccion + ',' + 'sustantivo'
                if t.pos_ is 'ADJ':
                    k = termino + ',' + fecha[:10] + ',' + diario + ',' + seccion + ',' + 'adjetivo'
                if t.pos_ is 'VERB':
                    k = termino + ',' + fecha[:10] + ',' + diario + ',' + seccion + ',' + 'verbo'

                if k not in contador:
                    contador[k] = 0
                contador[k] += 1
            
            for e in oracion.ents:
                if any([t in e.text.lower() for t in concepto]) or ',' in e.text or len(e.text) > 20:
                    continue

                k = e.text + ',' + fecha[:10] + ',' + diario + ',' + seccion + ',' + 'entidad'
                if k not in contador:
                    contador[k] = 0
                contador[k] += 1

        i += 1 

    aux = sorted(contador.items(), key=lambda i : i[1], reverse=True)[:top]
    
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d-%H%M%S")

    # por fecha, diario y seccion
    tabla = 'termino,fecha,diario,seccion,tipo,freq\n'

    for clave, freq in aux:
        tabla += clave + ',' + str(freq) + '\n'

    barra = '\\'
    if platform.system() == 'Linux':
        barra = '/'

    csv = open('.' + barra + 'resultados' + barra + id + 'cercanos-fecha-diario-seccion_' + timestamp + '.csv', 'wt', encoding="utf-8")
    csv.write(tabla)
    csv.close()



