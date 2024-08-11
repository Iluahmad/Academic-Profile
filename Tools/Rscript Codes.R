
# Data Wrangling in R

This is a very useful tidyverse tool for Data manipulation and cleaning, it's executable using the Dplyr Package in R. 
Load the necessary packages for executing functions
library(tidyverse)
library(dplyr)
library(ggplot2)
The Dplyr package consist of different verbs, such as Filter, select, Mutate, etc

## Subset by row with filter()

?filter
diamonds_sm<- filter(diamonds, cut == "Ideal")
diamonds_sm1<- filter(diamonds, price > 10000)
diamonds_sm2<- filter(diamonds, cut == "Ideal", 
+                       price > 10000)
diamonds_sm3<- filter(diamonds, cut == "Ideal" |
+                       price > 10000)
## Subset by column with select()

?select
diamonds_sm4<- select(diamonds,cut,color)
diamonds_sm5<- select(diamonds,1:4)
diamonds_sm6<- select(diamonds,starts_with("c"))
diamonds_sm8<- select(diamonds,
+                       price, everything())
diamonds_sm9<- select(diamonds, -carat)

## using the Pipe operator
diamonds_sm10 <- diamonds %>% select(-carat)

## reorder row with arrange()
diamonds_sm10 <- diamonds %>% select(-carat)
diamonds_arr <- diamonds %>% arrange(color, carat)
diamonds_arr <- diamonds %>% arrange(desc(carat))

# add or modify columns with mutate()
 diamonds_new <- diamonds %>% mutate(mass_g= 0.2*carat) 
 glimpse(diamonds_new)
 diamonds_new1 <- diamonds %>% mutate(mass_g= 0.2*carat, price_per_carat= price/carat) 
 


# Other Verbs -------------------------------------------------------------
?slice_max
?bind_rows
?left_join

 # grouped summaries with group_by() and summarise()
 

