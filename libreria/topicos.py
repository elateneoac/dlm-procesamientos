import datetime, platform

def procesar(noticias, topicos, titulos=False, diarios=[], secciones=[], mapas={}, id = ''):
    contador = {}

    barra = '\\'
    if platform.system() == 'Linux':
        barra = '/'

    # itero cada una de las noticias (es decir, cada fila del csv)
    for diario, seccion, fecha, titulo, texto in noticias:

        # filtro los diarios y secciones que no queremos analizar
        if (len(diarios) and diario not in diarios) or (len(secciones) and seccion not in secciones):
            continue
        
        if 'diarios' in mapas:
            diario = mapas['diarios'][diario]

        if 'secciones' in mapas:
            seccion = mapas['secciones'][seccion]

        if titulos:
            texto = titulo

        # itero los topicos
        for topico in topicos:

            # armo clave de cada contador
            if 'grupo' in topico:
                clave = topico['etiqueta'] + ',' + fecha[:10] + "," + diario + ',' + seccion + ',' + topico['grupo']
            else:
                clave = topico['etiqueta'] + ',' + fecha[:10] + "," + diario + ',' + seccion + ','

            # itero los términos del tópico que estamos analizando
            for termino in topico['terminos']:

                # por fecha, diario y seccion
                if clave not in contador:
                    contador[clave] = 0

                contador[clave] += texto.lower().count(termino)

    # escribo csv final con las freqs de cada topico

    # si seteo id, entonces le agrego el guion al final:
    if id != '':
        id += '_'

    # me quedo con el timestamp
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d-%H%M%S")

    # por fecha, diario y seccion
    tabla = 'topico,fecha,diario,seccion,grupo,freq\n'

    for clave, freq in contador.items():
        tabla += clave + ',' + str(freq) + '\n'

    csv = open('.' + barra + 'resultados' + barra + id + 'topicos-fecha-diario-seccion_' + timestamp + '.csv', 'wt', encoding="utf-8")
    csv.write(tabla)
    csv.close()