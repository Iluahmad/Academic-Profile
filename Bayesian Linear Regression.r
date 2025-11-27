library(brms)
set.seed(42)
n <- 100  # Number of observations

# Generate synthetic macroeconomic data
M <- rnorm(n, mean = 100, sd = 10)    # Money Supply
pi <- rnorm(n, mean = 5, sd = 1)      # Inflation Rate (%)
r <- rnorm(n, mean = 3, sd = 0.5)     # Interest Rate (%)
y <- 2 + 0.5 * M - 0.8 * pi - 0.2 * r + rnorm(n, mean = 0, sd = 2)  # GDP Growth

# Create DataFrame
macro_data <- data.frame(y, M, pi, r)
library(brms)

# Define Bayesian regression model
bayes_macro_model <- brm(y ~ M + pi + r, data = macro_data, family = gaussian(),
                         prior = c(prior(normal(0, 10), class = "b"),   # Priors for beta coefficients
                                   prior(normal(0, 10), class = "Intercept")),
                         chains = 4, iter = 2000, warmup = 500, seed = 42)

# Model Summary
summary(bayes_macro_model)
prior_summary(bayes_macro_model)
plot(bayes_macro_model)
stanplot(bayes_macro_model)


# New data for prediction
new_macro_data <- data.frame(M = c(105, 95), pi = c(6, 4), r = c(3.5, 2.8))

# Predict GDP growth with uncertainty
preds <- posterior_predict(bayes_macro_model, newdata = new_macro_data)
pred_mean <- colMeans(preds)
pred_sd <- apply(preds, 2, sd)

# Print Predictions
data.frame(new_macro_data, GDP_Growth_Estimate = pred_mean, Uncertainty = pred_sd)

library(ggplot2)

# Create prediction intervals
pred_data <- data.frame(M = macro_data$M, y = macro_data$y, 
                        y_pred = fitted(bayes_macro_model)[, "Estimate"],
                        y_lower = fitted(bayes_macro_model)[, "Q2.5"],
                        y_upper = fitted(bayes_macro_model)[, "Q97.5"])

# Plot actual vs predicted
ggplot(pred_data, aes(x = M, y = y)) +
  geom_point(color = "blue") +
  geom_line(aes(y = y_pred), color = "red") +
  geom_ribbon(aes(ymin = y_lower, ymax = y_upper), fill = "red", alpha = 0.2) +
  ggtitle("Bayesian Linear Regression: Macro Model Predictions") +
  theme_minimal()

