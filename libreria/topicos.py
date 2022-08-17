import datetime

def procesar(noticias, topicos, etiqueta = ''):
    contador_fecha = {}
    contador_fecha_diario = {}
    contador_fecha_diario_seccion = {}

    # itero cada una de las noticias (es decir, cada fila del csv)
    for diario, seccion, fecha, titulo, texto in noticias:
        
        # itero los topicos
        for topico in topicos:

            # armo clave de cada contador
            etiqueta = topico['etiqueta']
            topico_fecha = etiqueta + ',' + fecha[:10]
            topico_fecha_diario = topico_fecha + "," + diario
            topico_fecha_diario_seccion = topico_fecha_diario + ',' + seccion

            # itero los términos del tópico que estamos analizando
            for termino in topico['terminos']:

                # por fecha
                if topico_fecha not in contador_fecha:
                    contador_fecha[topico_fecha] = 0

                contador_fecha[topico_fecha] += texto.lower().count(termino)

                # por fecha y diario
                if topico_fecha_diario not in contador_fecha_diario:
                    contador_fecha_diario[topico_fecha_diario] = 0
                    
                contador_fecha_diario[topico_fecha_diario] += texto.lower().count(termino)

                # por fecha, diario y seccion
                if topico_fecha_diario_seccion not in contador_fecha_diario_seccion:
                    contador_fecha_diario_seccion[topico_fecha_diario_seccion] = 0

                contador_fecha_diario_seccion[topico_fecha_diario_seccion] += texto.lower().count(termino)

    # escribo los csv finales con las freqs de cada topico

    # si seteo etiqueta, entonces le agrego el guion al final:
    if etiqueta != '':
        etiqueta += '_'

    # me quedo con el timestamp
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d-%H:%M:%S")

    # por fecha
    tabla_fecha = 'topico,fecha,freq\n'

    for topico_fecha, freq in contador_fecha.items():
        tabla_fecha += topico_fecha + ',' + str(freq) + '\n'

    csv = open('../resultados/' + etiqueta + 'topicos-fecha_' + timestamp + '.csv', 'wt')
    csv.write(tabla_fecha)
    csv.close()

    # por fecha y diario
    tabla_fecha_diario = 'topico,fecha,diario,freq\n'

    for topico_fecha_diario, freq in contador_fecha_diario.items():
        tabla_fecha_diario += topico_fecha_diario + ',' + str(freq) + '\n'

    csv = open('../resultados/' + etiqueta + 'topicos-fecha-diario_' + timestamp + '.csv', 'wt')
    csv.write(tabla_fecha_diario)
    csv.close()

    # por fecha, diario y seccion
    tabla_fecha_diario_seccion = 'topico,fecha,diario,seccion,freq\n'

    for topico_fecha_diario_seccion, freq in contador_fecha_diario_seccion.items():
        tabla_fecha_diario_seccion += topico_fecha_diario_seccion + ',' + str(freq) + '\n'

    csv = open('../resultados/' + etiqueta + 'topicos-fecha-diario-seccion_' + timestamp + '.csv', 'wt')
    csv.write(tabla_fecha_diario_seccion)
    csv.close()