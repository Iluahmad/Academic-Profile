# Exploring Social Media Usage

################################################################################
library(ggplot2)
library(cowplot)
library(gridExtra)
Yearly = ggplot(Social_Media_Users, aes(x =Year , y =`Social Media User`)) +

library(readxl)
library(readxl)
################################################################################
## Loading the Data
Social_Media_Users <- read_excel("C:/Users/Ahmad Ilu/Downloads/Social Media Users.xlsx", 
 +     sheet = "Sheet1") 
View(Social_Media_Users)
attach(Social_Media_Users)
################################################################################
# Ploting the Data
################################################################################
## No Of Social Media Users
Yearly = ggplot(Social_Media_Users, aes(x =Year , y =`Social Media User`)) +  geom_bar(stat = "identity", fill="steelblue") +  ggtitle("No Of Social Media Users")+ theme(plot.title = element_text(hjust = 0.5)) + scale_alpha()
Yearly
ggdraw(Yearly) + draw_image("C:/Users/Ahmad Ilu/Desktop/PC/Lenovo 2023/ACCER 2020/RESEARCH COLLECTION/Rstudio/Rmarkdown Practice/BEAMER/Finmetrics.png",  x = 0.0021, y = 0.3, scale = .2)
Yearly = ggplot(Social_Media_Users, aes(x =Country , y =`Average time spent on social media per day`)) +
## Average time spent on social media per day
Time = ggplot(Social_Media_Users, aes(x =Country , y =`Average time spent on social media per day`)) + geom_bar(stat = "identity", fill="steelblue") +  ggtitle("Average time spent on social media per day")+ theme(plot.title = element_text(hjust = 0.5)) + scale_alpha()
Time
ggdraw(Time) + draw_image("C:/Users/Ahmad Ilu/Desktop/PC/Lenovo 2023/ACCER 2020/RESEARCH COLLECTION/Rstudio/Rmarkdown Practice/BEAMER/Finmetrics.png",  x = 0.1, y = 0.3, scale = .2)
Time2 = ggdraw(Time) + draw_image("C:/Users/Ahmad Ilu/Desktop/PC/Lenovo 2023/ACCER 2020/RESEARCH COLLECTION/Rstudio/Rmarkdown Practice/BEAMER/Finmetrics.png",  x = 0.1, y = 0.3, scale = .2)
Time2
## Twitter Age Demographics 2022 (%)
Age= ggplot(Social_Media_Users, aes(x =`Age Bracket ` , y =`Percentage of Users `,fill= `Age Bracket `)) + geom_bar(stat = "identity", position = "dodge")  +  ggtitle("Twitter Age Demographics 2022 (%)")+ theme(plot.title = element_text(hjust = 0.5)) + scale_alpha()
Age
Age2 = ggdraw(Age) + draw_image("C:/Users/Ahmad Ilu/Desktop/PC/Lenovo 2023/ACCER 2020/RESEARCH COLLECTION/Rstudio/Rmarkdown Practice/BEAMER/Finmetrics.png",  x = 0.25, y = 0.3, scale = .2)
Age2
## Pie Chart
Gender = ggplot(Social_Media_Users, aes(x="", y=`Percentage of Users (%)`, fill=`Gender `)) + geom_bar(stat="identity", width=1) + coord_polar("y", start=0) + geom_text(aes(label = paste0(`Percentage of Users (%)`, "%")), position = position_stack(vjust=0.5)) +  ggtitle("Twitter Gender Demographics 2022 (%)") + theme_void() + labs(x = NULL, y = NULL, fill = NULL)
Gender
Gender2= ggdraw(Gender) + draw_image("C:/Users/Ahmad Ilu/Desktop/PC/Lenovo 2023/ACCER 2020/RESEARCH COLLECTION/Rstudio/Rmarkdown Practice/BEAMER/Finmetrics.png",  x = 0.23, y = 0.3, scale = .21)
Gender2
## Grid Arrange
grid.arrange(Gender2,Age2,Year2,Time2)



