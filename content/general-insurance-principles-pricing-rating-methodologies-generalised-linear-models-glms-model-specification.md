Alright team, let's break down the critical topic of Model Specification within the fascinating world of Generalised Linear Models, or GLMs, as it's a cornerstone for your SP8 exam on General Insurance Pricing. A well-specified model is not just a theoretical nicety; it's the very foundation of an accurate and robust rating plan.

### **1\. Introduction to Generalised Linear Models (GLMs) and Model Specification**

At its core, a Generalized Linear Model (GLM) serves as a powerful tool for actuaries to model the relationship between a variable whose outcome we aim to predict (the **target variable**, denoted *y*) and one or more **explanatory variables** or **predictors** (denoted *x1...xp*). In the context of property/casualty insurance ratemaking, this typically involves classifying risks and building effective rating plans from raw premium and loss data.

The process of **Model Specification** is paramount. It involves making crucial decisions about the structure and components of your GLM to ensure it accurately captures the underlying relationships within your insurance data. This isn't a one-and-done step; it's an iterative process, balancing both art and science, where preliminary models are built and refined based on analysis of the results. GLMs are widely accepted for classification ratemaking due to their transparency, allowing actuaries to understand and communicate how results were developed.

### **2\. The Fundamental Components of a GLM and Their Specification**

A GLM intrinsically assumes that the outcome of the target variable is driven by two key parts: a **systematic component** and a **random component**. The goal is to 'explain' as much variability as possible by shifting it from the random into the systematic component using your chosen predictors.

#### **2.1 The Random Component: The Exponential Family and Distribution Choice**

The **random component** defines the probability distribution that the target variable *y* is assumed to follow. This distribution *must* be a member of the **exponential family of distributions**, a class with properties particularly useful for fitting GLMs.

Key distributions within this family commonly used in general insurance pricing include:

* **Normal Distribution**: Often used in linear models, but GLMs generalise beyond its strict restrictions.  
* **Poisson Distribution**: The most common choice for modeling **claim frequency** (e.g., expected claim count per unit of exposure). While typically discrete, its GLM implementation can handle fractional values, useful when frequency is a ratio (e.g., claims per exposure). In such cases, the denominator of the frequency (e.g., exposure) is often set as the GLM's weight. The Poisson distribution assumes the variance is equal to the mean.  
* **Gamma Distribution**: Predominantly used for modeling **claim severity** (e.g., dollars of loss per claim). It's right-skewed, has a lower bound at zero, and its variance function (V(m) \= m^2) implies that claims with higher expected means also exhibit higher variance, a desirable characteristic for severity modeling.  
* **Binomial Distribution**: Used when the target variable is **dichotomous** (e.g., occurrence or non-occurrence of an event, such as policy renewal or fraud detection). The mean represents the probability of the event occurring.  
* **Tweedie Distribution**: A highly versatile distribution, often used for modeling **pure premium** (dollars of loss per exposure) or **loss ratio** (dollars of loss per dollar of premium). It’s a special extension of the exponential family. The Tweedie distribution has a point mass at zero, combining features of a Poisson claim number process and a gamma claim size distribution, and implicitly assumes that frequency and severity move in the same direction with a predictor.

The choice of distribution is critical and should aim to fit the data as closely as possible from the available options. The dispersion parameter ($\\phi$) of the chosen exponential family distribution is assumed constant for all records in a standard GLM.

#### **2.2 The Systematic Component: Linear Predictor, Predictors, and Link Function**

The **systematic component** defines how the model's prediction (the mean, *mi*) relates to the explanatory variables. This relationship is expressed as: $g(\\mu\_i) \= \\beta\_0 \+ \\beta\_1 x\_{1i} \+ \\ldots \+ \\beta\_p x\_{pi}$.

* **Linear Predictor**: The right-hand side of this equation ($\\beta\_0 \+ \\beta\_1 x\_{1i} \+ \\ldots \+ \\beta\_p x\_{pi}$) is called the **linear predictor**. It is always a linear combination of the predictors and their coefficients.  
* **Link Function ($g(.)$)**: This is a user-specified transformation of the mean of the target variable that connects it to the linear predictor. It provides flexibility, as the mean doesn't have to be directly equal to the linear predictor.  
  * The **log link function** is almost always used in insurance risk models. It results in a **multiplicative structure** for the rating algorithm, which is often the most natural and desirable form for insurance pricing. Exponentiating the linear predictor in a log-link model yields the model prediction as a series of multiplicative factors.  
  * For **logistic regression** (binary target variables), a special **logit link function** is used. This is necessary because the linear predictor is unbounded, while the probability (mean of binomial) must be between 0 and 1\. The logit function maps probabilities from to \[-$\\infty$,+$\\infty$\]. Exponentiating the coefficients of a logistic model describes their effect on the *odds* of occurrence.  
* **Predictor Variables ($x\_1...x\_p$)**: These are policy terms or policyholder characteristics included in the rating plan. They are classified as either **continuous** or **categorical**.  
  * **Continuous Variables**: Input directly into the GLM, yielding a single coefficient. With a log link, each unit increase in the predictor results in a constant percentage change in the predicted value. For continuous variables in log-link models, it's often appropriate to **log them** (natural logarithm) before inclusion, as this allows the scale of the predictors to match the scale of the entity they are linearly predicting (the log of the mean outcome). This transforms the coefficient into a power transform of the original variable, which aligns with *a priori* expectations in insurance modeling.  
  * **Categorical Variables**: These take on distinct **levels** (e.g., "sedan," "SUV"). One level is designated as the **base level**. The GLM software internally creates **indicator (dummy) columns** for each non-base level, treating them as separate predictors, each receiving its own coefficient. This coefficient indicates the effect of being a member of that level *relative to the base level*. It's crucial to choose a base level with **populous data** to ensure the most accurate measures of significance. Sparser levels tend to have wider standard errors, indicating less confidence in their estimates.

#### **2.3 Weights and Offsets**

These are additional features that allow for more nuanced model specification:

* **Weights ($\\omega\_i$)**: Used when rows in the dataset represent aggregated data (e.g., averages of groups of similar risks, or pure premium per exposure). Weights inform the GLM about the relative importance or credibility of each observation, influencing the variance of the observed outcomes. For instance, a row representing the average of two claims should have half the variance of a single-claim row, which is achieved by setting the weight to the number of claims.  
  * In a claim frequency model, the number of exposures is typically used as the weight, as more exposures imply reduced variance in the average frequency.  
* **Offsets ($\\xi\_i$)**: A predictor variable whose coefficient is *constrained to be 1*. Offsets are added to the linear predictor scale. They are particularly useful when certain elements of the rating plan (e.g., territorial base loss costs, deductible factors) are derived *outside* the GLM and remain fixed. The GLM uses the offset to ensure that coefficients for other variables are optimal in the presence of these fixed elements.  
  * A common use is in **claim count models** where the target variable is number of claims; the (logged) number of exposures is included as an offset, reflecting the expectation that more exposures lead to more claims.  
  * Offsets can also be used to incorporate **restrictions** on certain rating factors (e.g., No Claims Discount scales) for commercial or legal reasons. The GLM then adjusts the relativities of other correlated factors to compensate for the fixed offset.

### **3\. Model Building Process and Form Selection**

The selection of the model form is an iterative journey of refinement. Key decisions about model specification include:

* **Choosing the Target Variable**: This choice can be between separate frequency and severity models, or a single pure premium model. Data and time constraints often influence this (e.g., if frequency/severity data isn't available, pure premium might be necessary). The choice can also depend on policies with multiple coverages or perils.

* **Transforming the Target Variable**: Sometimes necessary to stabilise variance or improve fit (e.g., for loss ratio models, removing high-impact events).

* **Variable Selection**: Deciding which predictors to include in the model. A major criterion is **variable significance**, ensuring the indicated effect is from a true relationship, not noise.

  * **P-value**: A common statistic used to guide this, informing the probability of an estimated coefficient of that magnitude arising *if the true coefficient is zero*. A common rule of thumb is to reject the null hypothesis (that the coefficient is zero) if the p-value is 0.05 or lower, though actuaries should combine this with intuition and business knowledge, as a "magic number" doesn't exist.  
  * **Standard Error**: Indicates the certainty of the coefficient estimate. Wider standard errors suggest less confidence.  
  * **Confidence Interval**: A range of values for the coefficient that, if hypothesised, would not be rejected at a chosen p-value threshold.  
  * Automated variable selection algorithms can assist, but require careful use to avoid spurious effects.  
* **Transformation of Predictor Variables**: Non-linear relationships between predictors and the target variable often require transformation.

  * **Detecting Non-Linearity**: **Partial residual plots** are a useful graphical diagnostic. They plot the residual (actual value minus model prediction, adjusted to the linear predictor scale) against the portion of the linear predictor driven by the specific variable, revealing patterns not captured by the current linear fit.  
  * **Binning Continuous Predictors**: Converting a continuous variable into a new categorical variable by defining intervals. The model then estimates a coefficient for each interval.  
  * **Adding Polynomial Terms**: Including powers of the continuous predictor (e.g., age^2, age^3). This can capture curves but may lead to loss of interpretability and erratic behaviour at data edges.  
  * **Using Piecewise Linear Functions (Hinge Functions)**: Creating new variables that represent changes in slope at specific "break points." These are highly interpretable, as coefficients describe the change in slope at these points, and their significance can be tested using p-values.  
  * **Natural Cubic Splines**: Another method for handling non-linearity.  
* **Grouping Categorical Variables**: Combining levels of categorical variables, especially sparse ones, to improve stability and interpretability.

* **Interactions**: Modeling the combined effect of two or more variables that is "over and above their individual effects". An interaction means the effect of one predictor depends on the level of another. For a log link model, an interaction translates into a multiplicative factor on top of the main effects.

  * **Interacting Two Categorical Variables**: Achieved by adding new columns to the design matrix representing combinations of non-base levels.  
  * **Interacting a Categorical Variable with a Continuous Variable**: Involves adding a column that is the product of the indicator for the categorical level and the continuous variable.  
  * **Interacting Two Continuous Variables**: Also possible.  
  * The p-value for the interaction term helps determine if its inclusion significantly improves the model. Actuaries should check for interactions that align with business intuition or existing rating structures. Data mining techniques can also help identify candidates for interaction variables.

### **4\. Assessing Model Fit and Validation**

After specifying and fitting a model, assessing its fit and validating its predictive power is crucial. This is an iterative part of refinement, feeding back into specification decisions.

* **Measures of Model Fit**:  
  * **Log-Likelihood**: GLMs are fit by maximising the log-likelihood, which represents the probability of all historical outcomes occurring given the model's parameters.  
  * **Deviance**: Defined as 2 \* (log-likelihood of saturated model \- log-likelihood of current model). Minimising deviance is equivalent to maximising log-likelihood. The deviance provides a measure of how much the fitted values differ from the observations.  
  * **Limitations**: Log-likelihood and deviance comparisons are only valid if datasets are identical.  
* **Comparing Candidate Models**:  
  * **Nested Models and F-Test/Chi-squared Test**: When one model is a subset of another, adding predictors always reduces deviance. Statistical tests like the F-test (for unknown scale parameter) or Chi-squared test (for known scale parameter) compare the deviance reduction against the increase in degrees of freedom to determine if the larger model is a *significant* improvement.  
  * **Penalized Measures of Fit (for non-nested models)**:  
    * **AIC (Akaike Information Criterion)**: Penalizes for additional parameters.  
    * **BIC (Bayesian Information Criterion)**: Penalizes more heavily for additional parameters, especially with large datasets. AIC often produces more reasonable results in practice.  
* **Residual Analysis**: Visual inspection of residuals helps assess model fit.  
  * **Deviance Residuals**: Square is a record's contribution to unscaled deviance. Should appear normally distributed for continuous outcomes if model is good fit. Less useful for discrete distributions.  
  * **Working Residuals**: Used in the GLM fitting algorithm. Plotting binned working residuals against the linear predictor or exposures can reveal systematic under/over-prediction or heteroscedasticity, indicating shortcomings in model specification (e.g., missed non-linearity, need for weights).  
* **Model Stability**: Assessed by running models on different subsets of data (e.g., cross-validation, bootstrapping). A stable model produces similar results across subsets.  
* **Model Validation and Selection**: Performed on **hold-out data** (data not used in training) to prevent overfitting.  
  * **Actual vs. Predicted Plots**: Visually assess agreement between model predictions and actual outcomes.  
  * **Lift Measures**: Quantify how well a model differentiates risks. Examples include simple quantile plots, double lift charts, loss ratio charts, and the Gini index. A higher Gini index indicates a more predictive model.  
  * **Overfitting vs. Underfitting**: Overfitting occurs when a model fits the training data (including noise) too well, leading to poor predictions on unseen data. Underfitting means the model misses important statistical effects. The goal is to find a balance.

### **5\. Limitations of GLMs and Extensions for More Flexible Specification**

While robust, GLMs have inherent limitations that influence model specification choices and have led to more advanced techniques:

1. **Full Credibility to Data**: Standard GLMs assign full credibility to the data for every parameter, regardless of data sparsity. This can lead to volatile estimates for sparse cells.  
2. **Uncorrelated Random Outcomes**: GLMs assume the random component of outcomes is uncorrelated among records. This assumption can be violated by repeated policies from the same policyholder or geographically correlated events. Large correlations can distort results and over-optimistic significance measures.  
3. **Linear Function of Predictors**: Predictions are strictly based on a linear combination of predictors. While workarounds like polynomials and hinge functions exist, they must be manually specified.  
4. **Constant Dispersion Parameter ($\\phi$)**: The dispersion parameter of the exponential family is assumed to be constant across all records.

These limitations have led to the development of **variations on GLMs** that offer increased flexibility, robustness, and accuracy while often retaining interpretability. These variations offer more sophisticated specification options:

* **Generalized Linear Mixed Models (GLMMs)**: Address the full credibility and uncorrelated randomness limitations. GLMMs allow some coefficients (known as **random effects**) to be modeled as random variables, typically for categorical variables with many levels lacking credibility (e.g., territories). This induces a **shrinkage effect**, where estimates for sparse levels are pulled closer to the overall mean, analogous to Bühlmann-Straub credibility. They can also account for correlation among policy records from the same policyholder.  
* **GLMs with Dispersion Modeling (DGLMs)**: Address the constant dispersion limitation. DGLMs allow the dispersion parameter ($\\phi$) to vary by record, controlled by a separate linear combination of predictors (which may or may not be the same as those for the mean). This allows the model to give less weight to volatile business and more to stable data, improving signal over noise. They also provide more flexibility to model the full distribution, especially useful for Tweedie models where the dispersion parameter can reflect different frequency/severity effects.  
* **Generalized Additive Models (GAMs)**: Address the linearity limitation by handling non-linearity natively. In a GAM, the terms making up the linear predictor can be arbitrary "smooth functions" of the predictors, whose shapes are estimated by the software. While offering flexibility, their effects must be assessed graphically, as there are no simple coefficients.  
* **MARS Models (Multivariate Adaptive Regression Splines)**: Another GLM variant excellent at handling non-linearities and interactions automatically. They construct piecewise linear functions (hinge functions) for non-linear effects and can identify interactions. MARS can be used directly or as a tool to uncover non-linear transformations or interactions to then be replicated in a standard GLM.  
* **Elastic Net GLMs**: Address overfitting and instability due to many potential predictors or highly correlated predictors. They add a "penalty term" to the GLM's deviance minimisation, which pushes some coefficients towards zero (performing automatic variable selection) and others towards smaller values, exhibiting a shrinkage effect similar to credibility models.

In conclusion, specifying a GLM for insurance pricing requires careful consideration of the target variable, appropriate distribution, and thoughtful selection and transformation of predictor variables, as well as the strategic use of link functions, weights, and offsets. The iterative nature of model building, combined with robust diagnostic tools and an understanding of GLM limitations, guides actuaries in constructing models that are both statistically sound and practically useful for ratemaking.

