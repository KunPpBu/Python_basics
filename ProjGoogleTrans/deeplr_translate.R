library(dplyr)
install.packages("deeplr")
library("deeplr")

#12636ffa-c0c0-7b5d-0102-e560a6c68617:fx

translate2("I like to translate texts.", target_lang = "DE", auth_key = "12636ffa-c0c0-7b5d-0102-e560a6c68617:fx")


EBLANGUAGES <- read_excel("EBLANGUAGES Strings-13-Sept.xlsx")
EBLANGUAGES<- data.frame(EBLANGUAGES)
str(EBLANGUAGES)

EBLANGUAGES %>%
  mutate_if(is.character, ~gsub('[^ -~]', '', .))

trans <- translate2(EBLANGUAGES, target_lang = "ES", auth_key = "12636ffa-c0c0-7b5d-0102-e560a6c68617:fx")

trans <- matrix(NA,dim(EBLANGUAGES)[1],dim(EBLANGUAGES)[2])
for (i in 1:dim(EBLANGUAGES)[1]){
  trans[i,] <- translate2(EBLANGUAGES[i,], target_lang = "ES", auth_key = "12636ffa-c0c0-7b5d-0102-e560a6c68617:fx")
}