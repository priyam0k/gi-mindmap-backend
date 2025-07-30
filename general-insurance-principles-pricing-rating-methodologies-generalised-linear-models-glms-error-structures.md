Alright SP8 candidates, let's dissect the concept of **Error Structures** within the overarching framework of Generalised Linear Models (GLMs). As your Specialist Actuarial Note Builder and Exam Coach, I'm here to ensure you grasp this fundamental aspect, which is critical for effective General Insurance Pricing.

### **Generalised Linear Models (GLMs): Understanding the Components**

Generalised Linear Models are powerful statistical tools used to model the relationship between a target variable (what we want to predict, denoted *y*) and one or more explanatory variables (predictors, denoted *x*1...*xp*). They are widely adopted in the personal lines insurance marketplace and increasingly for some commercial lines. A core strength of GLMs is their ability to handle various types of target variables, such as claim frequency, claim severity, pure premium, loss ratio, or the occurrence/non-occurrence of an event like policy renewal or fraud.

The flexibility and power of GLMs stem from explicit assumptions about two key components that drive the outcome of the target variable:

1. **The Systematic Component:** This refers to the portion of outcome variation explained by predictor values, forming a linear predictor.  
2. **The Random Component:** This is where **Error Structures** come into play. It assumes that the target variable *y* is a random variable belonging to a specific class of distributions called the **exponential family**. This fundamental assumption allows GLMs to accommodate a much wider variety of data types and relationships than traditional ordinary linear models.

### **The Random Component: Error Structures (The Exponential Family)**

The **Error Structure** in a GLM refers to the assumed probability distribution of the target variable, which must be a member of the exponential family of distributions. This family is a class of distributions with properties useful for fitting GLMs.

**Key Characteristics of the Exponential Family and their Implications for Error Structure:**

* **Mean and Variance Relationship:** A crucial aspect of the exponential family is that its distributions have a defined relationship between their mean (μ) and variance. Unlike ordinary linear models which assume constant variance (homoscedasticity), GLMs allow the magnitude of the variance of each measurement to be a function of its predicted value (mean). This means the variance function, V(μ), is a critical part of the chosen error structure. The general form of the variance is given as *var\[Yi\] \= φ \* V(μi) / ωi*, where V(μi) is the variance function, φ is a scale (dispersion) parameter, and ωi are weights.

**Common Distributions (Error Structures) in General Insurance Pricing:**

The sources highlight several members of the exponential family that are particularly relevant for general insurance applications:

1. **Poisson Distribution:**

   * **Application:** Most commonly used for modeling **claim frequency** (e.g., claims per exposure) and **claim counts**. It models the count of events occurring within a fixed time interval.  
   * **Properties:** Although typically a discrete distribution, its GLM implementation allows for fractional values, which is useful when frequency is calculated as a non-integral target variable (e.g., claim count divided by exposure).  
   * **Mean-Variance Relationship:** For a "true" Poisson distribution, the variance is equal to its mean (V(μ) \= μ).  
   * **Assumption:** It assumes that claims are independent. If there is correlation between claims, using a Poisson distribution may underestimate tail risk and the true number of claims.  
   * **Link Function:** Typically used with a **log link function**, which results in a multiplicative model structure for factors.  
   * **Offset:** When the target variable is claim counts, the log of exposure is commonly used as an offset.  
2. **Gamma Distribution:**

   * **Application:** A widely used distribution for modeling **claim severity** (e.g., dollars of loss per claim).  
   * **Properties:** It is right-skewed, with a sharp peak and a long tail to the right, and has a lower bound at zero, characteristics often exhibited by empirical claim severity distributions.  
   * **Mean-Variance Relationship:** The gamma variance function is V(μ) \= μ², meaning the assumed variance of severity for any claim is proportional to the square of its mean. This is a desirable characteristic, as claims with higher average severity are expected to exhibit higher variance in severity.  
   * **Link Function:** Typically used with a **log link function**, resulting in multiplicative effects on risk.  
3. **Tweedie Distribution:**

   * **Application:** Very useful in modeling insurance data, particularly for **pure premium** (dollars of loss per exposure) or **loss ratio**. This allows modeling both frequency and severity simultaneously.  
   * **Properties:** It is a special member of the exponential family with a variance function proportional to μ^p, where *p* is an additional parameter.  
   * **Mean-Variance Relationship:** For 1 \< *p* \< 2, the Tweedie distribution has a point mass at zero and corresponds to the compound distribution of a Poisson claim number process and a Gamma claim size distribution. It can behave like a Poisson distribution as *p* approaches 1, or like a Gamma distribution as *p* approaches 2\.  
   * **Robustness:** While assumptions about frequency and severity effects on variables might not always hold true (e.g., a variable increasing frequency but decreasing severity), Tweedie GLMs can be quite robust against such violations and still produce strong models.  
   * **Link Function:** Typically used with a **log link function**.  
4. **Binomial Distribution:**

   * **Application:** Used for **binary (dichotomous) target variables**, where the outcome is an occurrence or non-occurrence of an event (e.g., policy renewal, fraud detection, claim occurrence).  
   * **Mean:** The mean of the binomial distribution represents the probability that the event will occur.  
   * **Link Function:** Requires a **special type of link function**, such as the **logit link function**. This is because the linear predictor is unbounded (-∞ to \+∞), but the mean of a binomial distribution (a probability) must be bounded between 0 and 1\. The logit link maps the-ranged probability to an unbounded scale, and its inverse (the logistic function) translates the unbounded linear predictor back into a probability between 0 and 1\. Other available links for this purpose include the probit link and complementary log-log link.  
5. **Normal Distribution:**

   * **Application:** While GLMs generalize linear models, the normal distribution is part of the exponential family and is implicitly assumed as the error structure in **ordinary linear regression**.  
   * **Mean-Variance Relationship:** In this context, the error term is assumed to be normally distributed with a mean of zero and constant variance.  
   * **Link Function:** The **identity link function** is implicitly used, meaning the mean of the target variable is directly equal to the linear predictor.  
6. **Inverse Gaussian Distribution:**

   * **Application:** Also mentioned as a commonly used distribution for modeling **severity of claims**.

### **Selecting the Appropriate Error Structure (Distribution)**

The selection and specification of the distribution (error structure) is a crucial and iterative part of the model building process. The sources highlight the importance of choosing a distribution that aligns with the nature of the target variable:

* **Target Variable Type:** For quantitative target variables (frequency, severity, pure premium, loss ratio), the GLM produces an estimate of the expected value of the outcome. For occurrence/non-occurrence target variables, it estimates the probability of the event. The choice of distribution must align with this (e.g., Poisson for counts, Gamma for continuous positive amounts, Binomial for probabilities).  
* **Data Characteristics:** The chosen distribution should reflect the empirical characteristics of the data, such as skewness and bounds (e.g., Gamma for right-skewed, positive severity data).  
* **Practical Considerations:** The ultimate goal is to build a market-ready classification plan. The desirability of a multiplicative rating plan often leads to the widespread use of the log link, which in turn influences the most natural model choice for insurance risk, often aligning with Poisson, Gamma, or Tweedie distributions.

**Assessing the Appropriateness of the Chosen Error Structure:**

Once a model is built, it's vital to check if the chosen error structure (and link function) is appropriate for the data.

* **Residual Analysis:** This is a key technique for assessing model fit and checking the appropriateness of the error structure.  
  * **Deviance Residuals:** The square of the deviance residual for any record is its contribution to the unscaled deviance. These residuals should ideally be small, have a mean of zero, and show no predictable pattern for a well-fit model. They can be used to assess the appropriateness of a distribution, especially for continuous distributions like Inverse Gaussian where their histogram should match a normal curve and the Q-Q plot approximates a straight line. However, for discrete distributions (like Poisson or Tweedie), deviance residuals may not follow a normal distribution, as they don't adjust for discreteness, making them less useful for assessing the appropriateness of such distributions.  
  * **Working Residuals:** These are quantities used by the Iteratively Reweighted Least Squares (IRLS) algorithm during the fitting process. They are useful for visually inspecting residuals, particularly for large, skewed datasets where individual residuals might be hard to interpret. Binned working residuals, when plotted over the linear predictor or a predictor variable, should form an uninformative cloud with no apparent pattern, indicating no structural flaws. If patterns like "miscalibrations" or "fanning out" (indicating non-constant variance) are observed, it suggests the model specification (including the error structure) may be flawed.  
  * **Properties of Good Residuals:** For a good model, residuals should be symmetrical about the x-axis, have an average residual of zero, and be fairly constant across the width of the fitted values (homoscedasticity).

### **Limitations of GLMs and Extensions Addressing Error Structure**

The "standard" GLM, while powerful, has certain inherent limitations regarding its assumptions about the error structure:

1. **Constant Dispersion Parameter (φ):** In a standard GLM, the dispersion parameter (φ) of the exponential family must be held constant for all records.

   * **Solution:** **GLMs with Dispersion Modeling (DGLMs)**, also called Double-Generalized Linear Models, address this by allowing each record to have a unique φ, controlled by a linear combination of predictors. This enables the model to give less weight to historical outcomes of volatile business and more weight to stable business, potentially leading to better predictions of the mean.  
2. **Uncorrelated Random Outcomes:** GLMs assume that the random component of the outcome of the target variable is uncorrelated among the records in the training set. While the model aims to capture systematic correlations (e.g., similar outcomes for similar drivers), it assumes the unexplained "noise" is independent.

   * **Solution:** **Generalized Linear Mixed Models (GLMMs)** can account for such correlations in the data, for instance, by including policy ID as a random effect for multi-year policy data.

In essence, the choice and validation of the **Error Structure** (the assumed distribution from the exponential family) are pivotal in GLM specification. It directly impacts how the model captures the underlying randomness of the insurance data and, consequently, the accuracy and interpretability of the resulting rating plan.

