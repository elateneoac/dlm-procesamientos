library(tidyverse)
library(tidytext)
library(stringi)
library(janitor)

#seteo directorio donde voy a trabajar
setwd(getwd())


source('libreria/chaski-en-R.R')

################################## Traigo noticias #############################################

usuario ="joaquin.lovizio@gmail.com"
token = "09876"


# Parametros de la consulta 
## Obligatorios

# Noticias de la ultima semana 
desde <- format(Sys.Date()-8 , "%Y%m%d") 
hasta <- format(Sys.Date()-1 , "%Y%m%d") 

## Opcionales
#En caso de no querer filtrar por algo de lo siguiente se debe incorporar el NULL 
medios <- NULL
secciones <- NULL #c('politica', 'economia', 'sociedad', 'espectaculos') 
todos <- NULL  #noticias que contengan TODOS estos términos
alguno <- NULL # noticias que contengan ALGUNO de estos términos
ninguno <- NULL # noticias que contengan NINGUNO de estos términos
textual <- NULL  #noticias que contengan EXACTAMENTE estos términos

# Corremos la función
base <- query_noticias(desde, hasta, medios, secciones, todos, alguno, ninguno, textual)
rm(medios,secciones,todos,alguno,ninguno,textual,desde,hasta)

################################# Armo df para nube ###########################################

# defino candidato
candidato<-"grindetti"

#limpio textos de noticias y filtro las que mencionan al candidato
noticias<-base%>%
  clean_names() %>% #pasa las variables a minuscula
  mutate(
    texto= str_to_lower(texto),
    texto= stri_trans_general(texto, "Latin - ASCII"),
    texto= str_replace_all(texto,"www\\S*", ""), #saco urls con REGEX
    texto= str_replace_all(texto,"https\\S*", ""), #saco urls con REGEX
    texto= str_replace_all(texto, "[[:punct:]]", " "),
    texto= str_replace_all(texto, "[[:digit:]]+", " "))%>%
  filter(str_detect(texto, candidato))

#creo un filtro de palabras que no quiero que salgan en el conteo
filtro_palabras<-c(stri_trans_general(stopwords::stopwords("es"), "Latin-ASCII"), 
                   "patricia", "bullrich", "javier", "milei", "sergio", "massa", "myriam", "bregman", "schiaretti",
                   "anos", "dos",'grindetti')

#hago el conteo de palabras
palabras<-noticias%>%
  unnest_tokens(input = texto, output = word)%>%
  filter(!word %in% filtro_palabras)%>%
  group_by(word)%>%
  summarise(cantidad = n())%>%
  arrange(desc(cantidad))%>%
  slice(1:150)

write.table(palabras, file = paste0("./resultados/", candidato, "_nubedepalabras_", Sys.Date(),".csv"), quote = F, row.names = F, sep = ";")

