# Bayesian VARS
## Data Preparation
as.matrix(Energy_Data)
EDA=as.matrix(Energy_Data)
time_series <- ts(EDA, start = c(2010, 1), frequency = 12)
EDF <- subset(time_series, select = -c(Year, Month))
EDF <- ts(EDF, start = c(2010, 1), frequency = 12)
# plot data
plot.ts(EDF[,c(1,2,3)],main = "", col = "#F500BD",lwd = 4, cex.axis = 2, cex.lab = 2)
# plot data
plot.ts(EDF,main = "TimeSeries Plot", col = "#F500BD",lwd = 4, cex.axis = 2, cex.lab = 2)

# Main Model
library(bsvars)
spec = specify_bsvar$new(EDF)
burn = estimate(spec, S = 1000)
post = estimate(burn, S = 10000)
irfs = compute_impulse_responses(post , horizon = 12)
fevd = compute_variance_decompositions(post, horizon = 12)
hds  = compute_historical_decompositions(post)
ss   = compute_structural_shocks(post)
csds = compute_conditional_sd(post)
sddr = verify_identification(post)
fvs  = compute_fitted_values(post)
fore = forecast(post, horizon = 12)
plot(irfs)
summary(irfs)

