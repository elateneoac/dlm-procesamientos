################################## Importo librerias ##############################
library(tidyverse)
library(curl)
library(jsonlite)

################################## Usuario y contraseña #############################

usuario ="joaquin.lovizio@gmail.com"
token = "09876"

# Armo funcion
query_noticias <- function(desde, hasta, medios, secciones, todos, alguno, ninguno, textual) {
  h <- new_handle()
  handle_setheaders(h, usuario = usuario, token = token)
  
  # Construimos la URL con base a los parámetros de mas abajo
  url <- paste0("https://chaski.com.ar/noticias/",
                desde, "/",
                hasta, "/",
                paste(medios, collapse = "-"),
                "/",
                paste(secciones, collapse = "-"))
  
  # Si son NULL no los incorpota y trae todos
  if (!is.null(todos)) {
    url <- paste0(url, "?todos=", URLencode(todos))
  }
  if (!is.null(alguno)) {
    url <- paste0(url, "&alguno=", URLencode(alguno))
  }
  if (!is.null(ninguno)) {
    url <- paste0(url, "&ninguno=", URLencode(ninguno))
  }
  if (!is.null(textual)) {
    url <- paste0(url, "&textual=", URLencode(textual))
  }
  
  destfile <- "datos.json"
  base <- curl_download(url, destfile = destfile, handle = h)
  
  json <- fromJSON(destfile)
  data <- as.data.frame(json$noticia)
  return(data)
}

################################## Traigo noticias #############################################
# Parametros de la consulta 
## Obligatorios
desde <- '20231007' # noticias DESDE esta fecha (se puede especificar horario: 20231005-10:30:00)
hasta <- '20231015'# noticias HASTA esta fecha (se puede especificar horario: 20231007-21:30:00)
medios <- c('clarin', 'lanacion', 'infobae', 'paginadoce', 'perfil', 'eldestape') # Diarios a filtrar

## Opcionales
#En caso de no querer filtrar por algo de lo siguiente se debe incorporar el NULL 

secciones <- NULL #c('politica', 'economia', 'sociedad', 'espectaculos') 
todos <- NULL  #noticias que contengan TODOS estos términos
alguno <- NULL # noticias que contengan ALGUNO de estos términos
ninguno <- NULL # noticias que contengan NINGUNO de estos términos
textual <- NULL  #noticias que contengan EXACTAMENTE estos términos

# Corremos la función
notis <- query_noticias(desde, hasta, medios, secciones, todos, alguno, ninguno, textual)

### Guardo en un csv

write.csv(notis,paste("noticias/notis",desde,hasta,".csv",sep = "-"), row.names = FALSE)
