All right, aspiring SP8 Actuarial Specialist\! Let's build a robust understanding of diagnostics within the crucial domain of Generalised Linear Models (GLMs) for insurance pricing. This is a core competency, allowing us to scrutinise our models and ensure they are fit for purpose.

### **Diagnostics in Generalised Linear Models (GLMs) for Insurance Rating**

In the realm of Generalised Linear Models (GLMs) for insurance rating, diagnostics are indispensable tools that allow us to assess how well a model fits the data, identify areas for improvement, and ultimately ensure the reliability and interpretability of our rating plans. While GLMs offer significant advantages over univariate approaches, such as accounting for correlations and providing transparency in their output, these diagnostics help us validate our statistical assumptions and the appropriateness of the fitted model.

GLM software typically provides various statistics for each coefficient to help answer critical questions, such as whether a predictor genuinely affects the outcome or if its apparent effect is merely due to chance. These include standard error, p-value, and confidence intervals for individual coefficients, alongside broader measures of model fit like log-likelihood and deviance.

Let's delve into the specifics of these crucial diagnostic measures.

---

### **1\. Deviance: A Measure of Model Fit**

Deviance is a fundamental measure of how well a GLM fits the training data, highly useful for comparing candidate model specifications and assessing the predictive power of individual variables.

#### **1.1 Log-Likelihood and its Relation to Deviance**

The foundation of deviance lies in **log-likelihood**. For any given set of estimated coefficients, a GLM implies a probabilistic mean for each record. This, combined with the chosen distributional form and dispersion parameter, defines a full probability distribution for each observation. The **likelihood** is the product of the probabilities (or probability densities) that the GLM assigns to the actual outcomes that occurred across all records. Maximising this likelihood is the primary objective of GLM fitting software, as it finds the parameters that make the observed data most probable under the assumed model.

The **scaled deviance** for a GLM is formally defined as: *Scaled Deviance \= 2 × (log-likelihood of saturated model \- log-likelihood of evaluated model)*. The 'saturated model' is a theoretical model that perfectly fits every single data point, yielding the highest possible log-likelihood. Conversely, the 'null model' is the simplest model with no predictors, yielding the lowest possible log-likelihood. Your fitted GLM's log-likelihood (and thus its deviance) will fall somewhere between these two extremes.

The difference between the log-likelihood of the saturated model and your actual model reflects how much your model "missed" the perfect fit for each record. Summing these differences across all records and multiplying by two gives the scaled deviance.

Multiplying the scaled deviance by the estimated dispersion parameter ($\\phi$) yields the **unscaled deviance**. This unscaled deviance has the useful property of being independent of the dispersion parameter, making it suitable for comparing models that might have different estimates of dispersion.

Critically, the GLM fitting process inherently seeks to minimise deviance, which is mathematically equivalent to maximising the log-likelihood. Therefore, a smaller deviance value suggests a "better" model.

#### **1.2 Limitations of Log-Likelihood and Deviance Comparisons**

While powerful, direct comparisons of log-likelihood or deviance come with important caveats:

* **Identical Datasets:** Comparisons are only valid if the exact same datasets were used to fit both models. If adding a new variable to a model causes some records to be dropped due to missing values, the resulting measures of fit are no longer comparable because the models were fitted on different numbers of records.  
* **Identical Distributions:** For deviance comparisons, the assumed underlying distribution for the target variable must also be identical for both models. Changing the distribution would alter the "perfect" log-likelihood of the saturated model, invalidating the comparison.  
* **Parameter Count:** Adding predictors to a model will *always* reduce deviance, even if the predictors have no actual relationship with the target variable. This is because more parameters provide the model-fitting process with more "freedom" to fit the training data. This highlights that a reduction in deviance alone doesn't guarantee a better model; it could simply be overfitting noise.

---

### **2\. Comparing Candidate Models**

Given the limitations of simple deviance comparison, more sophisticated tests are needed to evaluate whether a model's improvement is statistically significant.

#### **2.1 The F-Test for Nested Models**

The F-test is specifically designed to compare **nested models**, where one model contains a subset of the variables of the other. Its purpose is to determine if the added predictors reduce deviance significantly more than what would be expected by chance alone.

The F-statistic is calculated as: $F \= \\frac{(D\_S \- D\_B) / (\\text{degrees of freedom of added parameters})}{\\hat{\\phi}\_B}$ Where:

* $D\_S$ is the unscaled deviance of the "small" model (fewer parameters).  
* $D\_B$ is the unscaled deviance of the "big" model (more parameters).  
* $\\hat{\\phi}\_B$ is the estimated dispersion parameter of the big model.  
* The "degrees of freedom of added parameters" is the number of new parameters introduced when moving from the small to the big model. For a categorical variable with 'm' levels, this typically adds (m-1) parameters.

The numerator represents the actual reduction in unscaled deviance achieved by adding the new parameters. The denominator, $\\hat{\\phi}\_B$ (multiplied by the number of added parameters), can be thought of as the expected reduction in unscaled deviance that would occur purely by chance for each new parameter added. By comparing this F-statistic against an F-distribution, we can assess the probability of observing such a deviance reduction if the added variables had no true predictive power. A sufficiently small p-value (e.g., less than 0.05) would lead us to reject the null hypothesis (that the added variables have no effect) and conclude they are significant.

#### **2.2 Penalised Measures of Fit (AIC and BIC)**

For **non-nested models** (where neither model is a subset of the other), or when a more general comparison is desired, penalised measures of fit are employed. These measures address the problem of overfitting by adding a penalty for model complexity, thus discouraging models with too many parameters that might only fit noise in the training data.

* **Akaike Information Criterion (AIC):** $AIC \= \-2 \\times \\text{log-likelihood} \+ 2 \\times p$ Where 'p' is the number of parameters in the model. A smaller AIC indicates a "better" model. The penalty term ($2 \\times p$) increases AIC for each added parameter, balancing model fit against complexity. The first term is effectively related to scaled deviance (without the constant saturated model term), so AIC can also be considered a penalised measure of deviance.  
* **Bayesian Information Criterion (BIC):** $BIC \= \-2 \\times \\text{log-likelihood} \+ p \\times \\text{log}(n)$ Where 'n' is the number of data points the model is fitted on. For typical large insurance datasets, the penalty imposed by BIC is often much larger than AIC's, which can lead to the exclusion of genuinely predictive variables. In practical terms, AIC tends to yield more reasonable results.

---

### **3\. Residual Analysis: Unveiling Model Shortcomings**

Residuals are vital for assessing how well the specified model fits the data. For any given record, a residual measures the deviation of the individual data point from its predicted value. This deviation is assumed to represent the random component of the model – the portion of the outcome not explained by the predictors. By analysing these residuals, we can determine if our model effectively captures this randomness and if there are any systematic patterns that suggest uncaptured predictive power.

#### **3.1 Deviance Residuals**

The **deviance residual** for any given record is defined such that its square is that record's contribution to the unscaled deviance. It takes the same sign as (actual \- predicted). Intuitively, deviance residuals are "adjusted" for the shape of the assumed GLM distribution.

For a well-fit model, deviance residuals should ideally have two properties:

1. **No Predictable Pattern:** They should appear randomly distributed. If a pattern is observed, it indicates that the model is leaving predictive power on the table, implying that the model can be improved.  
2. **Normally Distributed with Constant Variance (Homoscedasticity):** Raw residuals are not expected to be normally distributed (unless the normal distribution was chosen), and their variance depends on the predicted mean. However, deviance residuals are adjusted, so they *are* expected to be normal and homoscedastic. Significant deviations from normality or homoscedasticity may signal that the selected distribution for the GLM is incorrect.

**Graphical Assessment of Deviance Residuals:**

* **Histogram:** A histogram of deviance residuals, with a superimposed normal curve, helps visually assess their normality. Deviations (e.g., skewness) suggest that the chosen GLM distribution might not adequately capture the data's characteristics.  
* **Q-Q Plot (Quantile-Quantile Plot):** This plot compares the empirical quantiles of the deviance residuals against the theoretical quantiles of a normal distribution. If the residuals are normal, the points should fall along a straight line. Deviations from this line, especially at the tails, indicate departures from normality (e.g., greater skewness than assumed). For example, if a gamma distribution (less skewed) was used but the data is more skewed, an inverse Gaussian distribution might be more appropriate, as evidenced by better-fitting Q-Q plots.

**Limitations for Discrete Distributions:** Deviance residuals are less useful for discrete distributions (like Poisson or Negative Binomial) or distributions with a point mass (like Tweedie). This is because they do not adjust for discreteness, causing residuals to cluster. In such cases, **randomised quantile residuals** (which add random "jitter") or **binned working residuals** (discussed next) may be more appropriate. For highly aggregated discrete data, where the target variable takes many distinct values, deviance residuals become more useful as the data effectively smooths towards a continuous distribution.

#### **3.2 Working Residuals**

**Working residuals** are quantities used internally by the Iteratively Reweighted Least Squares (IRLS) algorithm during the GLM fitting process. They offer an additional powerful tool for assessing model fit, particularly when visual inspection of raw residuals is challenging due to large datasets or skewed outcomes.

**Binned Working Residuals:** To make working residuals practically useful for large datasets, they are aggregated into bins, usually with a roughly equal sum of **working weights**. Working weights adjust for the inherent mean/variance relationship of the chosen distribution and link function. The **binned working residual** for each bin is the weighted average of the individual working residuals within that bin.

**Graphical Assessment of Binned Working Residuals (Scatterplots):** These plots are excellent for detecting predictable patterns or "fanning out" (heteroscedasticity), which indicate shortcomings in the model specification.

* **Plotting Residuals over the Linear Predictor:** This helps reveal "miscalibrations" – areas of the prediction space where the model systematically under- or over-predicts. A well-fit model would show an uninformative cloud of points around zero. A systematic pattern (e.g., residuals consistently below or above the zero line in certain regions) suggests a missed non-linear effect or other model flaw.  
* **Plotting Residuals over the Value of a Predictor Variable:** This is akin to partial residual plots (Section 5.4.1 of source) and is crucial for identifying non-linear relationships that the model may not have adequately captured (e.g., if a continuous variable like age has a parabolic effect on claims but was only included linearly). A "fixed" plot would show residuals randomly scattered around zero.  
* **Plotting Residuals over the Weight Variable:** This type of plot helps assess the appropriateness of the model's weight variable (e.g., exposures). If the variance of residuals changes with the weight, it suggests the model's implicit assumption about the mean-variance relationship is not being adequately met, or that weights are needed where none were applied. For example, higher exposure usually implies lower average frequency variance; if this isn't captured, residuals might "fan out". A well-specified weight would result in a homoscedastic cloud of residuals.

---

### **4\. Leverage and Cook's Distance: Identifying Influential Observations**

These diagnostics help identify individual data points that exert disproportionate influence on the model's parameter estimates, which is crucial for assessing model stability.

#### **4.1 Leverage**

**Leverage** ($h\_{ii}$) measures how much influence an individual observed value has on its own fitted value. High leverage points are observations with unusual predictor variable values that pull the regression line towards themselves.

#### **4.2 Cook's Distance**

**Cook's distance** is a widely used measure to estimate the influence of a data point on the overall model results. It combines information about the residual and the leverage for each observation.

The formula for Cook's distance for the $i$-th data point is: $D\_i \= \\frac{P\_i^2}{p} \\times \\frac{h\_{ii}}{(1-h\_{ii})^2}$ Where:

* $P\_i$ is the Pearson residual for the $i$-th data point.  
* $p$ is the number of parameters in the model.  
* $h\_{ii}$ is the leverage of the $i$-th data point (diagonal element of the hat matrix).

A common rule of thumb is that data points with a Cook's distance of **1 or more** are considered to merit closer examination, as they may be "influential records" that disproportionately pull the model's coefficients. These influential records often correspond to highly weighted outliers.

#### **4.3 Practical Implications of Leverage and Cook's Distance**

Identifying and investigating records with high Cook's distance is critical for model stability. For example, an unusually large loss in a small class could drastically skew the estimated risk for that class. Removing such a loss might swing the class's indicated risk wildly, revealing an unstable model.

Based on investigations into high Cook's distance points, actuaries might decide to:

* **Cap the amounts** of large losses at a certain threshold to reduce their undue influence.  
* **Remove the observations** altogether, though if done, it's essential to ensure these removed observations are accounted for later to avoid understating claim frequencies or amounts in the final rating plan.

Assessing the impact of influential records provides a straightforward way to gauge model stability. If rerunning the model without some of the most influential records significantly changes parameter estimates, it indicates instability. This further underscores why credibility-like estimation methods, such as Generalized Linear Mixed Models (GLMMs) or Elastic Net GLMs (discussed in Chapter 10 of source), are valuable as they can implicitly address thin data by "shrinking" estimates towards a mean.

---

### **5\. Broader Context and Actuarial Judgment**

These diagnostics are not isolated tools but integral parts of the iterative model-building and refinement process.

* **Variable Selection and Transformation:** Diagnostics guide decisions on which predictors to include, how to group categorical variables, and how to transform continuous variables to capture non-linear effects. Partial residual plots, for instance, are explicitly used to detect non-linearity in continuous predictors, informing choices like binning, adding polynomial terms, or using piecewise linear functions (hinge functions).  
* **Addressing Multicollinearity:** Deviance and standard errors can behave erratically when predictors are highly correlated (multicollinearity). Diagnostics help detect instability caused by such issues, guiding decisions to remove highly correlated variables or use techniques like Principal Components Analysis (PCA). Variance Inflation Factor (VIF), output by most software, quantifies this increase in standard error due to collinearity, with values over 10 often considered high. Perfect correlation (aliasing) can cause model failure, and diagnostics like examining two-way tables can help identify and resolve near-aliasing.  
* **Overfitting and Underfitting:** The careful use of diagnostics, particularly on holdout data (data not used in training), is crucial to prevent overfitting. An overfitted model performs well on training data (including noise) but poorly on unseen data. Conversely, underfitting means the model misses important systematic effects. Diagnostics, along with out-of-sample testing techniques like lift charts, Gini index, and ROC curves (for logistic regression), help strike the right balance between model complexity and predictive power.  
* **Transparency and Communication:** A significant benefit of GLMs compared to some "black box" machine learning models is their transparency. The diagnostics discussed here contribute directly to this transparency, allowing actuaries to explain model behaviour, certainty of results, and underlying assumptions to non-technical stakeholders (e.g., management, underwriters, regulators). It is critical to communicate how results were developed and to translate them into something actionable.

Ultimately, while statistical tests and diagnostics provide invaluable quantitative evidence, **actuarial judgment, business intuition, and domain knowledge** remain paramount. There is no "magic number" p-value or fixed diagnostic threshold below which a variable is automatically deemed significant or a model perfect. Instead, these diagnostics are pieces of information that, combined with an actuary's understanding of the business and data, guide the iterative process of building a robust and market-ready classification plan.

