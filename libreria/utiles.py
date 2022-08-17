import os, csv, sys

def levantar_noticias():
    
    # aca los pasamos y los devolvemos
    archivos = [archivo for archivo in os.listdir ('./noticias') if archivo.endswith('.csv')]
    
    noticias = []

    for archivo in archivos:
        f = open('./noticias/' + archivo, 'rt')
        f.readline() # leo y descarto la primer fila que solo tiene la info de columnas.

        csv.field_size_limit(sys.maxsize) # config para que lea todo el contenido de la fila

        filas = csv.reader(f) # lo abro como un csv para poder iterarlo

        for diario, seccion, fecha, titulo, texto in filas:
            noticias.append( (diario, seccion, fecha, titulo, texto) )

    return noticias
