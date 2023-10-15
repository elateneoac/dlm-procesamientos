library(tidyverse)
library(tidytext)
library(stringi)

# Traigo la funcion de la libreria
source('libreria/chaski-en-R.R')

################################## Traigo noticias #############################################

usuario ="joaquin.lovizio@gmail.com"
token = "09876"


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
