# loading Relevant Packages
library(urca)
library(vars)
library(mFilter)
library(tseries)
library(TSstudio)
library(forecast)
library(tidyverse)
library(readxl)
# loading Data
Energy_Data <- read_excel("C:/Users/Ahmad Ilu/Desktop/PC/Lenovo 2023/ACCER 2020/RESEARCH COLLECTION/Latex Practice/Energy Conference/Energy Data.xlsx",sheet = "Sheet1")
View(Energy_Data)
head(Energy_Data)

# Creating the three Time Series Objectives
S <- ts(Energy_Data$`Exchange Rate`, start = c(2010,1,1), frequency = 12)
pi <- ts(Energy_Data$`Inflation Rate`, start = c(2010,1,1), frequency = 12)
PMS <- ts(Energy_Data$PMS, start = c(2010,1,1), frequency = 12)

# Time Series Plots
ts_plot(S, title = "Avearge Monthly Exchange Rate", Xtitle = "Time", Ytitle = "Exchange Rate")
ts_plot(pi, title = "Inflation Rate", Xtitle = "Time", Ytitle = "Inflation Rate")
ts_plot(PMS, title = "Average PMS Price per Litre", Xtitle = "Time", Ytitle = "PMS")

# Setting the Restrictions
amat <- diag(3)
amat[2,1] <- NA
amat[3,1] <- NA
amat[3,2] <- NA
amat

# Buidling the Model
sv <- cbind(S, pi, PMS)
colnames(sv) <- cbind("Exchange Rate", "Inflation Rate", "PMS")
view(sv)
# Lag Select Criteria
lagselect <- VARselect(sv, lag.max = 8, type = "both")
lagselect$selection
lagselect$criteria
# Model
Model1 <- VAR(sv, p = 7, season = NULL, exog = NULL, type = "const")
Model1
SVARMod1 <- SVAR(Model1, Amat = amat, Bmat = NULL, hessian = TRUE, estmethod = c("scoring", "direct"))
SVARMod1
# Impulse Response Functions
SVARog1 <- irf(SVARMod1, impulse = "Exchange.Rate", response = "Exchange.Rate", n.head = 20)
SVARog1
plot(SVARog1)
forecast<-predict(Model1,n.ahead = 4)
fanchart(forecast,names ="Exchange.Rate")

SVARog2 <- irf(SVARMod1, impulse = "Exchange.Rate", response = "Inflation.Rate", n.head = 20)
SVARog2
plot(SVARog2)

SVARog3 <- irf(SVARMod1, impulse = "Exchange.Rate", response = "PMS", n.head = 20)
SVARog3
plot(SVARog3)

SVARog <- irf(SVARMod1, impulse = "Exchange.Rate", response = c("Exchange.Rate", "Inflation.Rate", "PMS"), n.head = 20, boot = TRUE)
SVARog
plot(SVARog)
SVAR555 <- irf(SVARMod1, impulse = "e", response = c("Exchange.Rate", "Inflation.Rate", "PMS"), boot =TRUE)

# Variance Decomposition
VD <- fevd(SVARMod1, n.ahead = 10)
plot(vD)
#Granger Causality
granger1<- causality(Model1,cause = "Exchange.Rate")
granger1

svar.a <- SVAR(Model1, estmethod = "direct", Amat = amat)
SVAR222 <- irf(svar.a, impulse = "Exchange.Rate", response = c("Exchange.Rate", "Inflation.Rate", "PMS"), boot = FALSE)