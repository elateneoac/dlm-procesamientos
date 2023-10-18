library(tidyverse)
library(tidytext)
library(stringi)

#seteo directorio donde voy a trabajar
setwd(getwd())

#defino los csv
archivos <- list.files(path = "./noticias", pattern = "csv")

#creo un df vac?o
base<-data.frame()

#levanto todas las noticias en un solo df
for (i in archivos) {
  
  df<-read.csv(paste0("./noticias/", i), encoding = "UTF-8")
  
  base<-rbind(base, df)
}

# defino candidato
candidato<-"bregman"

#limpio textos de noticias y filtro las que mencionan al candidato
noticias<-base%>%
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
                   "anos", "dos")

#hago el conteo de palabras
palabras<-noticias%>%
  unnest_tokens(input = texto, output = word)%>%
  filter(!word %in% filtro_palabras)%>%
  group_by(word)%>%
  summarise(cantidad = n())%>%
  arrange(desc(cantidad))%>%
  slice(1:150)

write.table(palabras, file = paste0("./resultados/", candidato, "_nubedepalabras_", Sys.Date(),".csv"), quote = F, row.names = F, sep = ";")

