Alright, aspiring pricing actuary\! Let's build out some robust notes on Generalised Linear Models (GLMs) within the vast landscape of rating methodologies, drawing directly from our core SP8 material. This is a critical area, not just for the exam, but for your future practice in general insurance pricing. Pay close attention, as we'll delve into both the theoretical underpinnings and the practical applications, much like we'd dissect a complex claims experience.

---

### **1\. Introduction to Generalised Linear Models (GLMs) in General Insurance Pricing**

To begin, let's establish what exactly a GLM is and why it has become such a ubiquitous tool in our actuarial toolkit for pricing.

#### **1.1 What are GLMs?**

A Generalised Linear Model (GLM) is a powerful statistical framework used to model the relationship between a target variable (the outcome we wish to predict) and one or more explanatory variables (predictors). It is essentially a flexible generalisation of ordinary least squares regression. For us, in property/casualty insurance ratemaking, the target variable, denoted as *y*, typically represents measures like claim frequency (claims per exposure), claim severity (dollars of loss per claim), pure premium (dollars of loss per exposure), or even loss ratio (dollars of loss per dollar of premium). For quantitative target variables, the GLM provides an estimate of the expected value of the outcome. For binary outcomes, such as policy renewal or fraud detection, a GLM can estimate the probability of the event occurring.

The explanatory variables, or predictors, denoted *x1...xp*, are typically policy terms or policyholder characteristics that influence risk, like vehicle type, driver age, marital status for personal auto, or construction type, building age, and amount of insurance (AOI) for homeowners insurance.

#### **1.2 History and Adoption in Insurance**

GLMs have been in use for over thirty years across various fields, but their widespread adoption in the general insurance marketplace, particularly for classification ratemaking, is a relatively recent phenomenon. They are now near-ubiquitous, especially in large-scale personal lines operations. The surge in their adoption around the late 20th and early 21st centuries was driven by several key factors:

* **Increased Computing Power:** What once required large mainframes can now be achieved rapidly on desktop PCs, allowing for the analysis of granular data.  
* **Improved Data Accessibility:** Insurers' data warehouse initiatives have significantly enhanced the granularity and accessibility of data for ratemaking.  
* **Competitive Pressure:** Early adopters gained a competitive advantage, pushing the rest of the industry to adopt these more sophisticated methods to avoid adverse selection and maintain profitability.

This monograph aims to bridge the gap by providing practicing actuaries with the tools needed to build market-ready classification plans using GLMs.

#### **1.3 Why GLMs are Preferred (Benefits over Univariate Methods)**

Compared to traditional univariate analyses, GLMs offer significant advantages in insurance pricing:

* **Multivariate Analysis:** A primary strength of GLMs is their ability to consider all rating variables simultaneously, automatically adjusting for exposure correlations between them. This is a major shortcoming of univariate methods, which examine each variable in isolation and can lead to distorted results due to correlations with other unconsidered factors. GLMs can sort out each variable's unique effect, preventing double-counting of information.  
* **Statistical Significance:** GLMs provide robust statistical diagnostics (e.g., standard error, p-value, confidence interval) for each coefficient, helping us determine if a predictor has a statistically significant effect on the outcome or if its apparent effect is due to chance.  
* **Model Structure Flexibility:** They allow us to tailor the model to the underlying distribution of the claims data (e.g., Poisson for frequency, Gamma for severity) by choosing an appropriate distribution from the exponential family and a specific link function (e.g., log link for multiplicative relationships). This enables us to model a wider range of data types than traditional linear models.  
* **Transparency and Interpretability:** While more sophisticated than univariate methods, GLMs are generally considered transparent. The output, particularly for a multiplicative GLM, consists of a series of multipliers, which aligns well with how the insurance industry structures rating algorithms and manuals. The coefficients describe the effect of predictor variables on the odds (with a logit link) or transform into multiplicative factors (with a log link), offering a natural interpretation.  
* **Predictive Power:** By capturing complex relationships, including interactions between variables, GLMs generally produce more accurate and robust premium rates, leading to better risk selection and improved profitability. They aim to remove unsystematic effects (noise) and capture only the systematic effects (signal).

#### **1.4 Target Audience for GLM Monograph**

This monograph is specifically aimed at credentialed or nearly credentialed actuaries working in property/casualty or general insurance. It assumes familiarity with actuarial terms and methods, including the material covered in earlier actuarial exams, Actuarial Standards of Practice, and ratemaking principles from texts like Werner and Modlin's *Basic Ratemaking*. While prior knowledge of the underlying mathematics of GLMs is beneficial, it's not strictly necessary, though familiarity with a programming language *is* required for implementation.

### **2\. Technical Foundations of GLMs**

Let's dissect the core machinery that powers a GLM, laying out the components systematically.

#### **2.1 The Components of the GLM**

A GLM posits that the outcome of the target variable is driven by both a systematic component and a random component. Our objective in modelling is to shift as much variability as possible from the random component into the systematic component, thereby explaining more of the outcome variation using our predictors.

##### **2.1.1 The Random Component: The Exponential Family**

In a GLM, the target variable *y* is modelled as a random variable following a distribution from the exponential family. This family is a set of distributions whose probability function or probability density function can be written in a specific canonical form. Key members of this family relevant to insurance include the Binomial, Poisson, Exponential, Gamma, Normal, Inverse Gaussian, and Tweedie distributions. The parameter *μ* (mu) is of special interest, representing the expected value (mean) of the outcome. The model's prediction is essentially the estimate of this *μ* parameter. GLMs leverage predictor variables to produce a unique, better estimate of *μ* for each risk, moving beyond a simple historical average.

##### **2.1.2 The Systematic Component: Linear Predictor and Link Function**

The GLM models the relationship between the model prediction (*μi*) and the predictors (*x*) through a systematic component, as follows: g(*μi*) \= *β0 \+ β1x1i \+ β2x2i \+ ... \+ βpxpi*

Here, *g(.)* is the **link function**, a user-specified transformation of *μi*. The right-hand side, *β0 \+ β1x1i \+ ... \+ βpxpi*, is known as the **linear predictor**. When calculated, it yields the transformed prediction *g(μi)*. To get the actual model prediction (*μi*), the inverse of the link function is applied to the linear predictor. The link function provides flexibility, allowing a transformed value of the mean to be linearly related to the predictors, rather than requiring the mean itself to be directly linear.

###### **2.1.2.1 Log Link Function**

The **log link function** is particularly common and natural for insurance risk models because it produces a multiplicative rating structure. When a log link is specified, the additive terms of the linear predictor transform into a series of multiplicative factors when deriving the model prediction. For example, if the linear predictor is *β0 \+ β1x1i \+ β2x2i*, then *μi* becomes *e^(β0) \* e^(β1x1i) \* e^(β2x2i)*. This means that the impact of each predictor is a multiplicative factor on the base premium, which aligns well with how many insurance rating algorithms are structured.

#### **2.2 Exponential Family Variance**

A key characteristic of exponential family distributions is that their variance is a function of their mean. Specifically, the variance of the *i*\-th observation, *Var\[Yi\]*, can be expressed as *φ \* V(μi) / ωi*, where *V(μi)* is the variance function, *φ* is the scale parameter, and *ωi* are the weights assigned to each observation. The variance function, *V(μi)*, is derived from the properties of the exponential family and is a function of the mean parameter *μi*.

#### **2.3 Variable Significance (Statistical Diagnostics)**

When fitting a GLM, we want to know if the estimated coefficient for a predictor is "reasonably close" to the true coefficient, and more importantly, if the predictor actually has *any* effect on the outcome (i.e., if its "true" coefficient is non-zero). GLM software provides several statistical diagnostics to help answer these questions:

##### **2.3.1 Standard Error**

The standard error is a measure of the variability or uncertainty of the estimated coefficient. A smaller standard error indicates greater confidence in the estimate. Roughly, two standard errors from the parameter estimates correspond to a 95% confidence interval.

##### **2.3.2 p-value**

The p-value helps us test the null hypothesis that the true value of the variable's coefficient is zero (meaning the variable has no effect). A sufficiently small p-value allows us to reject the null hypothesis, accepting that the variable has a non-zero effect. A common rule of thumb is to reject the null hypothesis if the p-value is 0.05 or lower, though this threshold might be too high in insurance modelling projects where many variables are tested, potentially leading to spurious effects.

##### **2.3.3 Confidence Interval**

The confidence interval is a range of values within which the true coefficient is likely to fall, given a chosen confidence level (e.g., 95%). It represents a "reasonable range of estimates" for the coefficient. If the confidence interval for a coefficient includes zero, it suggests that the variable might not be statistically significant, as a zero effect cannot be ruled out.

#### **2.4 Types of Predictor Variables**

Predictor variables in a GLM are classified as either continuous or categorical, each receiving distinct treatment.

##### **2.4.1 Treatment of Continuous Variables**

Continuous variables are numeric and represent measurements on a continuous scale (e.g., age, amount of insurance, population density). They are typically input into the GLM as-is, and the GLM outputs a single coefficient for them. This results in a direct linear relationship with the linear predictor: for each unit increase in the predictor, the linear predictor changes by the coefficient's value. If a log link is used, this translates to the predicted value increasing or decreasing by a constant *percentage* for each unit increase in the predictor.

###### **2.4.1.1 Logging Continuous Variables**

When using a log link, it is often appropriate to take the natural logarithm of continuous predictors before including them in the model. This aligns the scale of the predictors with the scale of the entity being linearly predicted (the log of the mean of the outcome). Logging a continuous predictor in a log link model causes the resulting coefficient to act as a power transform of the original variable, meaning the predicted value is proportional to the original variable raised to the power of its coefficient.

##### **2.4.2 Treatment of Categorical Variables**

Categorical variables take on one of two or more distinct values, assigning each risk to a category (e.g., vehicle primary use, vehicle type, territory). The distinct values are called **levels**. The treatment is more involved:

* **Base Level:** One level is designated as the **base level**.  
* **Indicator Columns:** The GLM software replaces the categorical variable with a series of binary **indicator columns** (0 or 1\) in the **design matrix**, one for each non-base level.  
* **Coefficients:** Each indicator column is treated as a separate predictor and receives its own coefficient. The coefficient for each non-base level indicates its effect *relative to the base level*. For a risk belonging to the base level, all related coefficients drop out of the linear predictor.

For instance, if "sedan" is the base level for vehicle type, a positive coefficient for "SUV" indicates that SUVs have a higher claim frequency than sedans. Conversely, a negative coefficient for "van" indicates lower claim frequency than sedans.

###### **2.4.2.1 Importance of Base Level**

The choice of the base level significantly impacts the significance statistics (e.g., p-values, confidence intervals). Selecting a base level with sufficient data volume is crucial for accurate measures of significance, as sparser levels tend to have wider standard errors due to less data supporting their estimates.

#### **2.5 Weights**

Datasets for GLMs often include rows representing aggregated outcomes (e.g., average loss amount for several claims with identical characteristics) rather than individual records. To properly account for the varying information volume, **weights** are used. For example, in a severity dataset, setting the weight to the number of claims allows the GLM to reflect that a row representing two claims should have half the variance of a single-claim row. Weights are typically defined as the exposure or credibility of the data. In a frequency model, where the target is claims per exposure, the number of exposures is usually set as the weight, as additional exposure reduces expected variance due to greater stability in the average frequency.

#### **2.6 Offsets**

In insurance rating, sometimes certain rating plan elements are kept fixed (e.g., base loss costs by region, deductible factors) and are not to be estimated by the GLM. An **offset** is a mechanism that allows the GLM to account for these "fixed" variables in the rating plan, ensuring that the estimated coefficients for other variables are optimally determined in their presence. Formally, an offset is a predictor whose coefficient is constrained to be 1\. It is an added term to the linear predictor.

For a log-link model, if you wish to offset for a pre-determined territorial base loss cost and a deductible factor, you would add the natural logarithm of these values to the offset variable. It's crucial to understand the distinction between weights and offsets: an offset adjusts the mean, while a weight adjusts the variance. For instance, in a claim count model, additional exposures increase the *expected* number of claims (requiring an offset), while in a claim frequency model, additional exposures increase stability (reducing variance) but don't change the expected *mean* frequency, thus requiring a weight but no offset.

#### **2.7 An Inventory of Distributions for Insurance Rating**

The choice of distribution from the exponential family is critical and depends on the nature of the target variable.

##### **2.7.1 Distributions for Severity: Gamma and Inverse Gaussian**

When modelling claim or occurrence severity (loss amount per claim), the **Gamma distribution** is the most widely used and natural fit. It is right-skewed, with a sharp peak and a long tail to the right, and has a lower bound at zero, characteristics commonly exhibited by empirical claim severity distributions. The Gamma variance function is *V(μ) \= μ^2*, meaning variance is proportional to the square of its mean. The **Inverse Gaussian distribution** is another option.

##### **2.7.2 Distributions for Frequency: Poisson and Negative Binomial**

For modelling claim frequency (expected claim count per unit of exposure), the **Poisson distribution** is most commonly used. Although typically discrete, its GLM implementation allows for fractional values, useful when modelling frequency (claim count divided by exposure). The **Negative Binomial distribution** is another available choice. For frequency models, the number of exposures is typically used as the GLM weight.

##### **2.7.3 A Distribution for Pure Premium: the Tweedie Distribution**

The **Tweedie distribution** is a powerful distribution suitable for modelling pure premium, which often combines frequency (counts) and severity (amounts) and frequently has a mass at zero (representing policies with no claims). It is a special extension of the exponential family. It's commonly used when total loss amount is the target variable. Although it assumes a relationship between mean and variance that might not always hold true (e.g., a variable increasing frequency but decreasing severity), Tweedie GLMs are generally robust.

##### **2.7.4 Logistic Regression for Binary Outcomes (Logit Link)**

When the target variable is binary (e.g., occurrence or non-occurrence of an event, such as policy renewal or fraud detection), **logistic regression** is used. The most common link function for this purpose is the **logit link function**, defined as *g(μ) \= ln(μ / (1-μ))*. The inverse of the logit function is the logistic function, which translates the linear predictor's value into a probability of occurrence. Exponentiating the coefficients in a logistic GLM provides the effect of predictor variables on the *odds* of occurrence, offering a natural interpretation.

#### **2.8 Correlation Among Predictors, Multicollinearity and Aliasing**

Predictors in a GLM often exhibit correlation. GLMs are adept at handling moderate correlations, making them superior to univariate analyses for sorting out each variable's unique effect and avoiding double-counting of information. However, very large correlation between predictors can cause issues:

* **Multicollinearity:** When two or more predictors are highly correlated, the GLM struggles to precisely apportion the response effect, leading to erratic coefficients and large standard errors. This can result in an unstable model.  
* **Aliasing:** This occurs when predictors are perfectly correlated. **Intrinsic aliasing** arises from inherent dependencies in covariate definitions and is handled by modelling software. **Extrinsic aliasing** occurs when two or more factors have perfectly correlated levels. "Near" aliasing is when correlation is almost, but not quite, perfect.

##### **2.8.1 Handling High Correlation**

To mitigate issues from high correlation, techniques like **dimensionality-reduction** (e.g., principal components analysis (PCA) or factor analysis) can be used. These methods create new, less correlated variables from groups of predictors, which are more useful in a GLM. Factor analysis can also help reduce the number of parameter estimates or condense levels within a variable.

#### **2.9 Limitations of GLMs**

Despite their power, GLMs have inherent limitations to be mindful of:

##### **2.9.1 GLMs Assign Full Credibility to the Data**

GLMs assume that the data is fully credible for every parameter being estimated. This means the model fits coefficients to best match the training data, without explicit consideration for the thinness or volume of data underlying each estimate. For categorical variables with sparse data in certain levels, this can lead to unstable or unreliable estimates, as the model will simply take the raw indication from the limited data without applying credibility. While traditional actuarial credibility procedures would modify such indications (e.g., blending with a statewide average), a standard GLM does not inherently do this.

##### **2.9.2 GLMs Assume the Randomness of Outcomes is Uncorrelated**

A fundamental assumption of GLMs is that the random component of the target variable's outcome is uncorrelated among records in the training set. While GLMs *do* capture correlations between outcomes driven by predictors, they assume independence for the portion of the outcome not explained by the model. This assumption can be violated if latent variables or uncaptured factors lead to groups of records with similar outcomes (e.g., multiple renewals of the same policy, policyholders in the same area affected by a storm). Large instances of such correlated outcomes can cause the GLM to overemphasise those events, picking up "too much random noise" and leading to sub-optimal predictions and overly optimistic statistical significance measures.

### **3\. The GLM Model-Building Process**

Building a GLM for insurance rating is a structured process that goes beyond just fitting the model. It encompasses several stages, from initial data understanding to final model validation and implementation.

#### **3.1 Overall Process Overview**

While each project has unique objectives, a predictive modelling project using GLMs should generally include the following components:

1. **Collecting and Preparing Data:** Ensuring data quality and suitability.  
2. **Conducting Exploratory Data Analysis (EDA):** Understanding data characteristics and relationships.  
3. **Specifying Model Form:** Defining the target, predictors, distribution, and link function.  
4. **Evaluating Model Output:** Assessing fit, significance, and areas for improvement.  
5. **Model Refinement:** Iteratively improving the model based on evaluation.  
6. **Validating the Model:** Testing performance on unseen data.  
7. **Translating the Model into a Product:** Implementing the model (e.g., as a rating plan).

#### **3.2 Data Preparation**

High-quality data is the underpinning of sound ratemaking. Data collection and preparation are crucial steps, involving:

* **Matching Databases:** Ensuring claims and policy records can be uniquely matched.  
* **Handling Missing/Erroneous Values:** Replacing problematic values with means/modes and adding error flags, or imputing values using other predictors.  
* **Excluding/Adjusting Outliers:** Deciding whether to remove or adjust influential outliers to prevent undue influence on parameter estimates.  
* **Loss Development:** Developing losses to ultimate for lines of business not at full maturity, matching development factors to the type of entity modelled (severity vs. pure premium/loss ratio).

#### **3.3 Exploratory Data Analysis (EDA)**

Before constructing models, conducting EDA is essential to understand the data's nature and relationships between variables. Helpful EDA plots include:

* Plotting each predictor against the target variable to identify relationships and inform variable transformations.  
* Plotting continuous predictors against each other to assess correlation.  
* Reviewing one-way and two-way analyses (exposure, claims, frequency, severity, loss ratio) to check data distributions, identify sparse levels, understand likely factor effects, and validate data against other sources. This is crucial even with multivariate methods.  
* Distribution analyses, particularly for claim sizes, can highlight anomalies and ensure best estimates are used for pricing.

#### **3.4 Specifying Model Form**

This involves making key decisions about the model structure, including:

* Choosing the target variable (e.g., frequency/severity vs. pure premium).  
* Selecting the appropriate distribution from the exponential family.  
* Deciding which explanatory variables to include.  
* Determining if transformations should be applied to the target or predictors.  
* Choosing the link function (e.g., log link for multiplicative effects).

#### **3.5 Model Refinement**

This iterative process involves evaluating preliminary results and making adjustments to improve model fit. It includes:

* Assessing overall model fit using measures like log-likelihood and deviance.  
* Analysing the significance of each predictor, removing or transforming variables as needed.  
* Comparing candidate models using statistical tests.  
* Performing residual analysis to check model assumptions and identify areas for improvement.

#### **3.6 Model Validation and Selection**

Model validation is a critical step that should not be overlooked. It involves rigorously testing the model's performance on unseen data to ensure its predictive power and robustness. This is covered in detail in a later section.

#### **3.7 Translating the Model into a Product**

The ultimate goal of most modelling projects is to implement the final model as a product, often a rating plan. This involves considerations such as timing of database updates and ensuring unique keys for data matching. The model output needs to be translated into a usable format, often a series of multipliers for rating algorithms, which are customary in the insurance industry.

### **4\. Selection of Model Form**

Once preliminary data analysis is complete, the focus shifts to formally defining the model's structure.

#### **4.1 Choosing the Target Variable**

The target variable is the outcome you aim to predict.

* **Frequency/Severity versus Pure Premium:** While pure premium (loss per exposure) can be modelled directly, it's often preferable to model claim frequency (claims per exposure) and claim severity (loss per claim) separately. This allows for a deeper understanding of how factors affect different components of loss and for separate trending of frequency and severity. The results can then be combined, typically by multiplying the frequency and severity multipliers for multiplicative models.  
* **Policies with Multiple Coverages and Perils:** For policies covering multiple perils or coverages, separate models for each can provide more accurate risk assessment.  
* **Transforming the Target Variable:** Sometimes, transforming the target variable (e.g., using a log transform for severity or pure premium) can help meet the linearity assumptions of the GLM after applying the link function.

#### **4.2 Choosing the Distribution**

The choice of distribution from the exponential family is crucial and must reflect the characteristics of the target variable. We've already covered the common distributions for severity (Gamma, Inverse Gaussian), frequency (Poisson, Negative Binomial), pure premium (Tweedie), and binary outcomes (Binomial with logit link) in detail. The goal is to find the distribution that best fits the data from the available options, even if no distribution perfectly fits.

#### **4.3 Variable Selection**

For projects aiming to update existing rating factors, variable selection might not be an issue as variables are pre-determined. However, for more complex projects, especially those incorporating external data, there can be hundreds or thousands of potential predictors. Automated variable selection algorithms can assist, though they require careful use to avoid introducing spurious effects.

#### **4.4 Transformation of Variables (Handling Non-Linearity)**

GLMs assume a linear relationship between the transformed mean of the target variable and the predictors. When continuous predictors exhibit non-linear effects, several workarounds can be employed:

##### **4.4.1 Detecting Non-Linearity with Partial Residual Plots**

Partial residual plots are a valuable tool for detecting non-linearity. They plot the partial residuals (actual values with all model components except the one being examined subtracted out) against the model's estimate for that variable. This helps visualise if the current linear fit adequately captures the relationship.

##### **4.4.2 Binning Continuous Predictors**

One approach is to convert a continuous variable into a new categorical variable by creating intervals (bins) over its range. The model then estimates a separate coefficient for each interval, treating it as a categorical variable. While this allows for flexible shapes, it doesn't guarantee continuity in the estimates between bins, and volatility in sparse bins can lead to inconsistent patterns.

##### **4.4.3 Adding Polynomial Terms**

Non-linearity can also be accommodated by adding polynomial terms (e.g., squared or cubed terms) of the continuous predictor to the model. This creates a smooth, curvilinear relationship. A downside is reduced interpretability, as discerning the curve's shape requires graphing the function, and higher-order polynomials can behave erratically at the edges of the data.

##### **4.4.4 Using Piecewise Linear Functions (Hinge Functions)**

This involves defining linear segments for different ranges of the continuous variable, allowing the slope of the relationship to change at specified "knots" or "cut points". A common form is the hinge function, *h(x-c) \= max(x-c, 0\)*. This provides flexibility while maintaining some interpretability.

##### **4.4.5 Natural Cubic Splines**

Splines are a more advanced way to model smooth non-linear relationships, allowing for flexible curves by fitting piecewise polynomial functions that are smooth at their connection points (knots).

#### **4.5 Grouping Categorical Variables**

When a categorical variable has a very large number of levels, or many levels with sparse data, it may be necessary to group these levels into a smaller, more manageable number of homogeneous categories. This can be done prior to modelling, or GLMs can be improved by smoothing parameter values via grouping or fitting curves. Grouping ensures sufficient data in each level for credible estimates and helps the maximum likelihood algorithm converge. Approaches include spatial smoothing for geographic factors (e.g., postcodes) or vehicle classification techniques.

#### **4.6 Interactions**

Interactions occur when the effect of one predictor on the target variable depends on the level of another predictor. GLMs can explicitly include interaction terms, allowing us to test if combining variables significantly improves the model beyond their individual effects.

##### **4.6.1 Interacting Two Categorical Variables**

For two categorical variables, interaction terms are added by creating additional columns in the design matrix, representing combinations of non-base levels. The coefficient for each interaction term indicates the *added effect* (above the main effects) of a risk having that specific combination of levels. Statistical significance (e.g., low p-value) of these interaction terms helps determine if the combined effect is meaningful. If an interaction term for a specific combination is not significant, those levels might be combined for that interaction.

##### **4.6.2 Interacting a Categorical Variable with a Continuous Variable**

This type of interaction explores if the relationship (slope) of a continuous variable changes across different levels of a categorical variable. For example, if a log(AOI) variable interacts with a "sprinklered" categorical variable, the GLM software adds a column that is the product of the indicator for "sprinklered:Yes" and log(AOI). This allows the "AOI curve" (the effect of AOI on the target) to differ for sprinklered vs. non-sprinklered properties. The main effect for the continuous variable then represents its effect for the base level of the categorical variable.

##### **4.6.3 Interacting Two Continuous Variables**

Interactions can also exist between two continuous variables. This allows the effect of one continuous variable to depend on the value of another, potentially creating complex response surfaces. As with other interactions, the p-value for the interaction term helps assess its significance.

### **5\. Model Refinement**

Model refinement is an iterative process where we assess how well our model fits the data and identify avenues for improvement.

#### **5.1 Some Measures of Model Fit**

GLM software provides statistical measures to gauge model fit, particularly useful for comparing candidate models.

##### **5.1.1 Log-Likelihood**

For any given set of coefficients, a GLM defines a probability distribution for each record, allowing us to calculate the probability (or probability density) that the model assigns to the observed actual outcome. The product of these probabilities across all records is the **likelihood**. The **log-likelihood** is the natural logarithm of this value, and GLM fitting procedures aim to maximize it. A higher log-likelihood indicates a better fit. The log-likelihood of a model falls between that of a null model (lowest possible) and a saturated model (highest possible).

##### **5.1.2 Deviance**

**Scaled deviance** is a key measure of model fit, defined as twice the difference between the log-likelihood of the saturated model and the log-likelihood of the model being evaluated. The saturated model perfectly fits the data, thus having a deviance of zero. The null model represents the inherent total deviance in the data. A lower deviance for your model indicates a better fit. The square of the **deviance residual** for any given record is its contribution to the unscaled deviance.

##### **5.1.3 Limitations on the Use of Log-Likelihood and Deviance**

When comparing models using log-likelihood or deviance, the comparison is only valid if the datasets used to fit both models are *exactly identical*. Differences in the number of records will distort the comparison, as total log-likelihood is a sum across records.

#### **5.2 Comparing Candidate Models**

As model building is iterative, we need statistical tests to compare successive model runs and guide decisions on predictor inclusion, transformations, and groupings. Adding predictors *always* reduces deviance, as more parameters allow for a better fit to the training data, even if the predictors lack predictive power.

##### **5.2.1 Nested Models and the F-Test**

For **nested models** (where one model is a subset of the other, e.g., adding a new predictor to an existing model), the F-test (or Chi-squared statistic for certain distributions) can be used to assess whether the additional predictors significantly improve the model fit. The F-statistic compares the reduction in deviance (from adding variables) relative to the residual deviance, accounting for the degrees of freedom. A sufficiently small p-value for the F-test indicates that the added variables are statistically significant.

##### **5.2.2 Penalized Measures of Fit (AIC, BIC)**

When models are not nested, or to provide a penalty for model complexity, penalized measures of fit are useful.

* **Akaike Information Criterion (AIC):** Defined as *\-2 × log-likelihood \+ 2p*, where *p* is the number of parameters.  
* **Bayesian Information Criterion (BIC):** Defined as *\-2 × log-likelihood \+ p log(n)*, where *n* is the number of data points. Both measures penalize models for having more parameters, encouraging parsimony (simplicity). Generally, a lower AIC or BIC indicates a better model. In practice, AIC often yields more reasonable results for insurance models, as BIC's heavier penalty for additional parameters on large datasets can sometimes lead to the exclusion of predictive variables.

#### **5.3 Residual Analysis**

Visual inspection of residuals – measures of the deviations of individual data points from their predicted values – is a useful and important way to assess model fit. Residuals represent the random component of the model, so their patterns reveal how well the model captures randomness.

##### **5.3.1 Deviance Residuals**

The deviance residual for a record measures its contribution to the unscaled deviance, taking the same sign as the actual minus predicted value. For continuous distributions like Gamma, deviance residuals in a well-fitted model should approximate a normal distribution, appearing as a homoscedastic cloud when plotted against the linear predictor. However, for discrete distributions (e.g., Poisson, Negative Binomial) or those with point masses (e.g., Tweedie at zero), deviance residuals may not follow a normal distribution, making them less useful for assessing distributional appropriateness.

##### **5.3.2 Working Residuals**

Working residuals are quantities used internally by the Iteratively Reweighted Least Squares (IRLS) algorithm during GLM fitting. Analysing them provides an additional tool to assess fit. They are often aggregated into bins, with the binned working residual being the weighted average of individual residuals within the bin. Plotting binned working residuals against the linear predictor or individual predictors can reveal miscalibrations (systematic under- or over-prediction) or heteroscedasticity (non-constant variance). For example, a "fanning out" pattern in residuals when plotted against exposure might indicate that weights were not appropriately applied to account for varying stability across records.

#### **5.4 Assessing Model Stability**

Model stability refers to whether small changes in the input data lead to large changes in the model's results.

* **Influential Records (Cook's Distance):** Cook's distance is a common measure of a record's influence on GLM results. Higher Cook's distance indicates greater influence. Rerunning the model without highly influential records can reveal instability if parameter estimates change significantly.  
* **Cross-Validation:** This technique, also used for out-of-sample performance testing, assesses stability by running the model on different subsets of the data (folds). Similar parameter estimates across different folds indicate a stable model.  
* **Bootstrapping:** By repeatedly sampling with replacement from the original dataset and refitting the model, bootstrapping provides empirical statistics (mean, variance, confidence intervals) for parameter estimates, giving a sense of their stability. Many actuaries prefer bootstrapped confidence intervals over those provided by standard GLM software.

### **6\. Model Validation and Selection**

Once a model is refined, it must be rigorously validated to confirm its predictive accuracy and readiness for deployment.

#### **6.1 Assessing Fit with Plots of Actual vs. Predicted**

Plots of actual versus predicted values provide a straightforward visual assessment of model fit. For a good model, actual and predicted values should align closely. It is critical to create these plots on *holdout data* (data not used in training) to avoid misleadingly good results from overfitting.

#### **6.2 Measuring Lift**

**Model lift** is a relative concept, comparing the ability of one model to differentiate risks compared to another (e.g., a proposed model vs. an existing rating plan). Lift should always be measured on holdout data to prevent overfitting.

##### **6.2.1 Simple Quantile Plots**

These plots visually represent a model's ability to differentiate risks. The dataset is sorted by predicted loss cost and bucketed into quantiles (e.g., deciles). The actual loss costs for each quantile are then plotted. A good model will exhibit:

* **Accuracy:** Actual loss costs align closely with predicted loss costs within each quantile.  
* **Monotonicity:** Loss costs increase consistently across quantiles from best to worst risks.  
* **Vertical Distance (Spread):** A larger spread between the best and worst quantiles indicates greater differentiation ability.

##### **6.2.2 Double Lift Charts**

Double lift charts compare two competing models or a proposed model against a current rating plan. The data is sorted based on the ratio of the proposed model's prediction to the current plan's prediction. This allows visual assessment of how much better the proposed model predicts actual pure premium across different risk segments compared to the current plan.

##### **6.2.3 Loss Ratio Charts**

Similar to quantile plots, loss ratio charts group data by predicted loss ratio and display the actual loss ratios for each group, providing insight into the model's predictive accuracy across the risk spectrum.

##### **6.2.4 The Gini Index**

The Gini index is a statistical measure of a model's ability to differentiate between best and worst risks, often visualised using a **Lorenz curve**. The data is sorted by predicted loss cost, and then the cumulative percentage of exposures is plotted against the cumulative percentage of losses. The Gini index is twice the area between the Lorenz curve and the line of equality (a 45-degree line representing a model that perfectly predicts no differentiation). A higher Gini index (ranging from 0 to 1\) indicates a more predictive model. It quantifies the rating plan's ability to differentiate risk, which can lead to increased profitability assuming pricing and underwriting flexibility.

#### **6.3 Validation of Logistic Regression Models**

For logistic regression models (which predict probabilities of event occurrence), many standard validation diagnostics apply.

* **Quantile Plots:** Records can be bucketed by predicted probability, and actual occurrence proportions can be graphed against average predicted probabilities.  
* **Lorenz Curve and Gini Index:** These can be created by sorting records by predicted probability and plotting cumulative risks against cumulative occurrences, providing a measure of discrimination.  
* **Receiver Operating Characteristic (ROC) Curves:** ROC curves plot the true positive rate against the false positive rate for various discrimination thresholds. They assess a model's diagnostic ability and help select an optimal threshold for converting probabilities into binary outcomes.  
* **Confusion Matrix:** A 2x2 table that displays the counts of true positives, true negatives, false positives, and false negatives for a given discrimination threshold, useful for understanding classification performance.

### **7\. Other Topics and Extensions Related to GLMs**

The monograph delves into additional considerations and advanced variations of GLMs that address their limitations.

#### **7.1 Model Documentation**

Documenting your model is paramount for transparency, reproducibility, and stakeholder management. Documentation should include everything needed to reproduce the model from source data to output, all assumptions and justifications, data issues and resolutions, reliance on external models, model performance and shortcomings, and compliance with actuarial standards (e.g., ASOP 41).

#### **7.2 Why You Probably Shouldn’t Model Coverage Options with GLMs (Selection Effects)**

While it's tempting to include coverage options (like deductibles or limits) as predictors in a GLM, it often produces counterintuitive results (e.g., higher premiums for less coverage). This is largely due to **selection effects**: policyholders choosing higher deductibles might already be lower risks or more financially responsible. The GLM might pick up this increased risk for certain options, which is predictive for existing policies but not suitable for pricing future policies. Therefore, it is recommended to estimate factors for coverage options using traditional actuarial loss elimination techniques (e.g., increased limits factors, deductible factors) *outside* the GLM and then include them in the GLM as an offset.

#### **7.3 Territory Modeling (as Offset)**

Territories pose a challenge for GLMs due to their high dimensionality (hundreds or thousands of levels) and strong correlation with other variables. While spatial smoothing techniques are better suited for territory modelling, the GLM should still account for territory effects. This is achieved by including territory as an offset in the GLM, populating policy records with their indicated territory loss cost from a standalone territory model. This ensures the classification plan variables are fitted *after* accounting for territorial effects, preventing them from acting as proxies for territory.

#### **7.4 Ensembling**

**Ensemble models** combine information from two or more individual models to produce a prediction that often outperforms any single model. A simple yet powerful ensembling method is to take the straight average of model predictions. For log-link GLMs, taking the geometric average of predictions preserves the multiplicative structure. The "ensemble effect" (where more models generally lead to better performance) is a notable exception to the parsimony principle. For the ensemble effect to work optimally, model errors should be as uncorrelated as possible, ideally achieved by having models built by multiple independent teams.

#### **7.5 Variations on the Generalized Linear Model (Addressing Limitations)**

Several extensions to GLMs have been developed to address their inherent limitations, offering increased flexibility, robustness, and accuracy while largely preserving interpretability.

##### **7.5.1 Generalized Linear Mixed Models (GLMMs)**

Standard GLMs assume coefficients are fixed values and give full credibility to data, even for thin segments. **GLMMs** relax this by allowing some coefficients (called **random effects**) to be modelled as random variables themselves. This is particularly useful for categorical variables with many levels that lack sufficient credibility for direct estimation. GLMMs balance fitting the data closely with pulling sparse estimates closer to a group mean (a phenomenon known as **shrinkage**). This is analogous to **Bühlmann-Straub credibility**, where the GLMM effectively blends full-credibility estimates with a grand mean, with weighting determined by data volume and estimated variances. GLMMs also provide a way to account for correlation among random outcomes, such as in multi-year datasets with multiple policy renewals.

##### **7.5.2 GLMs with Dispersion Modeling (DGLMs)**

A standard GLM assumes the dispersion parameter (*φ*) of the exponential family is constant across all records. **DGLMs** (Double-Generalized Linear Models) extend this by allowing *each record to have a unique φ*, also modelled as a linear combination of predictors (which may or may not be the same as those for the mean *μ*). This allows the model to give less weight to volatile business and more weight to stable business, thereby improving predictions of the mean by accounting for varying volatility across different classes of business.

##### **7.5.3 Generalized Additive Models (GAMs)**

While GLMs require manual specification of non-linear transformations (polynomials, binning), **GAMs** handle non-linearity natively. In a GAM, the linear predictor is a sum of arbitrary smooth functions of the predictors, whose shapes are estimated by the software. This provides great flexibility to capture complex, non-linear relationships. Although GAMs offer no direct numerical coefficient interpretation, predictor effects can be assessed graphically.

##### **7.5.4 MARS Models**

**MARS** (Multivariate Adaptive Regression Splines) is another GLM variant excellent at handling non-linearities and interactions automatically. MARS uses piecewise linear functions (hinge functions) to approximate non-linear relationships and can automatically select relevant variables and interactions. It produces highly interpretable models by presenting basis functions and coefficients, making the non-linear effects relatively clear.

##### **7.5.5 Elastic Net GLMs (Regularization)**

Traditional GLMs fit parameters to best fit the training data, which can lead to overfitting and poor performance on unseen data if too many predictors are included. **Elastic Net GLMs** address this by adding a "penalty term" to the function being minimized (deviance). This penalty is an increasing function of the magnitude of the coefficients, encouraging smaller coefficients and even forcing some less-important predictors' coefficients to zero, effectively performing automatic variable selection. Elastic Nets combine properties of lasso (absolute value penalty, can force coefficients to zero) and ridge (squared coefficients penalty, shrinks coefficients) regression.

### **8\. GLMs in the Broader Ratemaking Context**

Finally, let's contextualise GLMs within the larger framework of general insurance ratemaking methodologies.

#### **8.1 Classification Ratemaking and the Evolution to Multivariate Methods**

Classification ratemaking involves subdividing the insured population into homogeneous groups using rating variables to determine appropriate rate differentials. Historically, actuaries used **univariate (one-way) methods**, which examine the loss experience of each rating variable in isolation.

##### **8.1.1 Shortcomings of Univariate Methods**

Univariate approaches have significant shortcomings:

* **Failure to Account for Other Variables:** They do not accurately consider the effect of other rating variables or exposure correlations between them. This leads to distortions, especially when variables are correlated (e.g., young drivers predominantly using lower car groups, making lower car groups appear riskier than they are).  
* **Inclusion of Noise:** Univariate methods include both systematic effects (signal) and unsystematic effects (noise) in their results.  
* **Lack of Diagnostics:** They do not provide statistical diagnostics about the certainty or appropriateness of the results.  
* **Difficulty with Interactions:** Incorporating interactions requires expanding to two-way or three-way tables, which becomes computationally impractical with many variables.

##### **8.1.2 Iteratively Standardized One-Way Approaches (Minimum Bias)**

Methods like **minimum bias procedures** arose to address some univariate shortcomings. These involve iterating univariate analyses, adjusting for exposure weights and previous variables' indications. While not technically multivariate, many minimum bias procedures correspond directly to GLMs, and sufficient iterations can lead to convergence with GLM results.

##### **8.1.3 Drivers for Adoption of Multivariate Methods**

The widespread adoption of statistical techniques like GLMs was a result of:

* Rapid increases in **computing power**.  
* Insurers instituting **data warehouse initiatives** leading to more granular and accessible data.  
* **Competitive pressure**, as early adopters gained a significant advantage.

#### **8.2 Benefits of Multivariate Methods (including GLMs)**

The move to multivariate methods, particularly GLMs, was driven by their superior capabilities:

* **Adjust for Exposure Correlations:** They simultaneously consider all rating variables, automatically accounting for correlations.  
* **Allow for Nature of Random Process:** They attempt to remove noise and capture only systematic effects, reflecting the random process of insurance more accurately.  
* **Provide Diagnostics:** They produce statistical diagnostics that provide information about the certainty of results and the appropriateness of the model.  
* **Allow Interaction Variables:** They can explicitly incorporate interactions, which are crucial refinements that improve predictive value.  
* **Considered Transparent:** Compared to other complex multivariate models (e.g., neural networks), GLMs are considered transparent, with easily interpretable output (e.g., multiplicative factors). This allows actuaries to follow and communicate how results were developed.

#### **8.3 GLMs as the Standard for Classification Ratemaking**

GLMs have quickly become the standard for classification ratemaking in many countries and lines of business.

##### **8.3.1 Mathematical Foundation (from Linear Models)**

GLMs are a generalized version of linear models (LMs), which express a response variable as the sum of its mean and a random error term, with the mean being a linear combination of predictors. GLMs "loosen the restrictions" of LMs by removing the assumptions of normality and constant variance for the error term. They also introduce the link function, which allows the relationship between the expected response and the linear predictor to be non-additive (e.g., multiplicative with a log link). The parameters of a GLM are typically estimated using the maximum likelihood approach.

##### **8.3.2 Applications: Personal Lines and Small Commercial Risks**

GLMs are widely applied to the rating of personal lines business (e.g., motor, household) and, to a lesser extent, small commercial risks. This is due to the high volume of homogenous data available in these lines, which aligns well with the strengths of GLMs in statistical modelling.

#### **8.4 Integration with Other Techniques**

GLMs are often used in conjunction with other data analysis and modelling techniques.

##### **8.4.1 Data Mining: Factor Analysis, Cluster Analysis, CART, MARS, Neural Networks**

While GLMs are a core technique, various data mining methods can augment GLM analysis. These techniques may not directly produce rate differentials but enhance the underlying classification analysis in several ways:

* **Variable Reduction:** Whittle down a long list of potential explanatory variables to a more manageable set for GLMs (e.g., Factor Analysis/PCA).  
* **Categorization/Dimension Reduction:** Provide guidance on how to categorize discrete variables or condense multi-level discrete variables into homogeneous levels (e.g., Cluster Analysis, CART).  
* **Interaction Identification:** Identify candidates for interaction variables by detecting patterns of interdependency between variables.  
* **Complementary Models:** Results from complex models like Neural Networks can highlight areas for improvement in a GLM (e.g., a missing interaction). MARS models also offer natural non-linearity handling and automatic variable/interaction selection.

##### **8.4.2 External Data Sources**

The adoption of GLMs and data mining has influenced classification ratemaking by encouraging the incorporation of external data sources to enhance predictive power. This includes data on geo-demographics, geo-physical variables, and other third-party information.

#### **8.5 Practical Considerations for Actuaries using GLMs**

While commercial software packages simplify the technical implementation of GLMs, the actuary's role remains crucial. Focus areas include:

* Understanding the data and its limitations.  
* Selecting appropriate assumptions for GLMs (e.g., link function, error structure, grouping of factors).  
* Assessing the reasonableness and consistency of model results, especially when compared to intuition or prior knowledge.  
* Managing stakeholders and communicating complex model outputs effectively.  
* Ensuring the model's output can be translated into a practical rating algorithm, considering IT support and system constraints.  
* Being aware of and accounting for potential distortions like selection effects (e.g., for deductible factors), often best handled by traditional methods and integrated via offsets.  
* Considering the competitive market and potential deviations from theoretical rates for business reasons (e.g., NCD scales).

#### **8.6 GLM Output and Diagnostics**

GLMs provide detailed output, including:

* **Parameter coefficients:** Estimates for the intercept and each predictor variable.  
* **Statistical diagnostics:** Standard errors, p-values, and confidence intervals for coefficients to assess significance.  
* **Graphical output:** Visualisations of factor relativities with confidence intervals to show significance and data volume.  
* **Model fit measures:** Log-likelihood and deviance.  
* **Residual plots:** Deviance and working residuals plots to assess model fit, identify non-linearities, and check for homoscedasticity.  
* **Model stability checks:** Cook's distance to identify influential records, and cross-validation/bootstrapping to check consistency across data subsets.  
* **Validation plots:** Actual vs. predicted plots, lift curves, gains curves, and Gini index to test out-of-sample predictiveness.

#### **8.7 Credibility and GLMs**

While standard GLMs do not inherently apply credibility adjustments (they assign full credibility to data), extensions like Generalized Linear Mixed Models (GLMMs) effectively introduce credibility-like estimation methods. GLMMs induce shrinkage, blending sparse estimates towards a group mean, much like Bühlmann-Straub credibility. Traditional credibility methods are typically not credibility-weighted with GLM results; instead, GLM diagnostics inform the modeler's final selections.

#### **8.8 GLMs and Other Pricing Approaches (Burning Cost, Frequency/Severity)**

GLMs are key tools in the broader "cost plus" approach to pricing, where premiums are based on statistically driven analyses of expected claim costs loaded for expenses and profit. They are particularly used within the **frequency/severity approach** by modelling claim frequency and severity separately and then combining them. This contrasts with the **burning cost approach**, which uses historical aggregate claims (total claims per unit of exposure) and largely ignores claim counts. While GLMs can be used to rate premiums for both, the frequency/severity approach is often preferred when data allows, due to the detailed understanding it provides of factor effects.

This comprehensive overview should give you a solid foundation for understanding GLMs in the context of general insurance pricing methodologies. Keep reviewing these points and connect them to practical scenarios to solidify your knowledge for the SP8 exam\!

