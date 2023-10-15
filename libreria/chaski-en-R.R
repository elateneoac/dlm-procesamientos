################################## Importo librerias ##############################
library(tidyverse)
library(curl)
library(jsonlite)

################################## Usuario y contraseña #############################



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

