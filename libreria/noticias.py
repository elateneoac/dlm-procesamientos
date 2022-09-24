import os, csv, sys, platform

def levantar(diarios=[], secciones=[], palabras_en_titulo=[], palabras_en_texto=[]):
    
    barra = '\\'
    if platform.system() == 'Linux':
        barra = '/'

    # aca los pasamos y los devolvemos
    archivos = [archivo for archivo in os.listdir ('.' + barra + 'noticias') if archivo.endswith('.csv')]
    
    noticias = []

    for archivo in archivos:
        f = open('.' + barra + 'noticias' + barra + archivo, 'rt', encoding="utf-8")
        f.readline() # leo y descarto la primer fila que solo tiene la info de columnas.

        # csv.field_size_limit(sys.maxsize) # config para que lea todo el contenido de la fila
        csv.field_size_limit(1310720000) # config para que lea todo el contenido de la fila

        filas = csv.reader(f) # lo abro como un csv para poder iterarlo

        for diario, seccion, fecha, titulo, texto in filas:
            # filtro los diarios y secciones que no queremos analizar
            filtro_diario = len(diarios) and diario not in diarios
            filtro_seccion = len(secciones) and seccion not in secciones
            filtro_texto = len(palabras_en_texto) and not any(palabra in texto for palabra in palabras_en_texto)
            filtro_titulo = len(palabras_en_titulo) and not any(palabra in titulo for palabra in palabras_en_titulo)
            
            if filtro_diario or filtro_seccion or filtro_texto or filtro_titulo:
                continue

            noticias.append( (diario, seccion, fecha, titulo, texto) )

    return noticias
