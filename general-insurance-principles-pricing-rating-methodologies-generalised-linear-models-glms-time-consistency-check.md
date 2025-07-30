Alright, aspiring SP8 Actuarial Note Builders and Exam Coaches\! Let's dissect the concept of the **Time Consistency Check** within the broader framework of Generalized Linear Models (GLMs). This is a critical diagnostic in your toolkit, as it helps ensure that the rating factors you're developing from historical data remain robust and predictive for future policy periods.

### **Time Consistency Check in Generalised Linear Models (GLMs)**

In the rigorous world of General Insurance Pricing, GLMs are indispensable for building comprehensive rating plans, allowing us to simultaneously model the effects of multiple factors on outcomes like claim frequency or severity. A key strength of GLMs lies in their ability to account for moderate correlations among predictors, distinguishing each variable's unique contribution. However, the reliability of these models hinges on the stability of the underlying relationships over time, which is where the "time consistency check" becomes paramount.

#### **1\. What is the Time Consistency Check and Why is it Important?**

The **Time Consistency Check** is a diagnostic procedure designed to evaluate whether the estimated effects (parameters or relativities) of your rating factors in a GLM remain stable and consistent across different time periods within your historical dataset.

Its importance in pricing work cannot be overstated. When actuaries analyse data that is typically 2 to 7 years old to deploy rates for the upcoming year, it is crucial that the patterns identified in the past are still relevant and predictive for the future. If the effect of a rating factor is rapidly changing over time, a model averaged over several historical years might be inappropriate for future periods. A consistent factor, on the other hand, is likely to be a good predictor of future experience.

#### **2\. How to Perform a Time Consistency Check Using GLMs**

The primary method for performing a time consistency check within a GLM involves leveraging the concept of **interactions**.

* **2.1. Incorporating Interaction Terms:** To test the consistency of parameter estimates over time, you can fit a GLM that includes an **interaction of a single factor with a measure of time**, such as a calendar year. An interaction occurs when the effect of one variable depends on the level of another variable. In this context, we are testing whether the effect of your chosen rating factor varies depending on the year (or other specified time period) of the experience.

  * Behind the scenes, the model fitting software adds additional columns to the design matrix, representing the combinations of non-base levels for the interacting variables. The estimated coefficient for these new predictors indicates the added effect above the main effects.  
  * If this interaction term is insignificant, it suggests that the effect of the factor is the same across different time periods, indicating consistency.  
* **2.2. Statistical Significance Testing:** Just like any other variable or interaction term in a GLM, the statistical significance of the time interaction term can be assessed using various diagnostics:

  * **p-value:** A p-value is used to guide the decision to accept or reject the null hypothesis (that the true coefficient is zero). A sufficiently small p-value (e.g., 0.05 or lower, though actuaries must exercise judgment due to multiple tests) indicates that the time interaction term has a statistically significant effect, suggesting a lack of time consistency.  
  * **Deviance Tests (Chi-squared, F-statistic, AIC):** Deviance measures how much the fitted values differ from the observations. When comparing nested models (where one model is a subset of another, such as a model with main effects only vs. one including a time interaction), deviance tests can assess whether the additional variable(s) (the interaction terms) significantly improve the model's fit. A significant reduction in deviance when a time interaction is added suggests that the factor's effect indeed varies over time. The AIC (Akaike Information Criterion) and BIC (Bayesian Information Criterion) are penalized measures of fit that can compare non-nested models as well, though AIC tends to produce more reasonable results for large insurance datasets.  
* **2.3. Visual Inspection (Graphical Analysis):** Visualising the results is crucial for interpreting time consistency, as it can often reveal patterns that statistical tests alone might not fully capture.

  * You can plot the response variable (e.g., frequency or severity) against the factor of interest, with different lines on the graph representing different time periods (e.g., calendar years).  
  * **Example of a Time Consistency Problem:** One source provides an example from car theft frequency by vehicle age during a period of rapidly improving security measures. In such a scenario, the relativities for a given vehicle age might show a clear trend or divergence across different years, rather than varying randomly around an average. If this is the case, the model average selected might be inappropriate for future periods, and a more tailored projection (e.g., using the latest year's response with an ad-hoc adjustment for future development) might be needed.  
  * **Example of a Consistent Factor:** A more usual scenario involves the model fit line (representing the average effect) varying smoothly across the factor, with the time consistency responses (individual years) varying randomly around this average. For instance, vehicle age's effect on damage frequency might show less variation for lower car ages (higher exposure) and more variation for higher car ages (lower exposure), consistent with expectations. This indicates a stable relationship that is likely to be a good predictor of future experience.

#### **3\. Implications and Resolution of Time Inconsistency**

If a time consistency check reveals that a factor's effect is changing significantly over time (e.g., a statistically significant interaction with a time variable, or clear trends in the graphical analysis), it has several implications:

* **Inappropriate Projections:** The model's average relativities, derived from historical data, may not be suitable for future rating periods if the underlying relationship is dynamic.  
* **Need for Intervention:** Actuaries must apply judgment. If a trend emerges, it needs to be identified so that patterns can be projected appropriately for future periods. This might involve:  
  * **Excluding the variable:** If the instability is too high and cannot be reliably managed, the variable might be excluded from the model.  
  * **Dynamic Modelling:** For factors with evolving patterns (e.g., due to technological changes or market shifts), alternative modelling approaches might be considered. While the sources do not delve into specific dynamic GLMs for time consistency in detail, the overall concept points towards the need to reflect changing realities.  
  * **Ad-hoc Adjustments:** As seen in the car theft example, if the pattern is moving rapidly, the actuary might need to use the response for the latest year, translate it by the projection period, and apply an ad-hoc adjustment for anticipated future changes.

#### **4\. Broader Context within GLMs: Model Stability and Beyond**

The Time Consistency Check fits into the broader theme of **model stability** and **validation** within GLMs.

* **Model Stability:** A stable model should produce similar results when run on separate subsets of the initial modeling dataset, including subsets from different time periods. This concept is reinforced by other validation techniques like **cross-validation**, where the data is split into multiple folds (e.g., 10-fold cross-validation), and the model is trained on k-1 folds and tested on the remaining fold, with the process repeated for all folds. This provides multiple estimates of model performance, helping assess stability.  
* **Contrast with Aliasing:** It's important to distinguish time inconsistency from **aliasing**. Aliasing occurs when two or more predictor variables are *perfectly* correlated, meaning one can be perfectly linearly expressed by others. This results in no unique solution for coefficients and usually causes the GLM fitting software to automatically drop one of the aliased predictors. Near-perfect correlation can also cause instability, erratic coefficients, and convergence failure. While aliasing is a structural data problem leading to mathematical indeterminacy, time inconsistency relates to the *evolution* of relationships over time, impacting the model's predictive power for the future. Both, however, point to forms of model instability.  
* **Model Refinement:** The insights gained from a time consistency check directly feed into the model refinement process. If a factor shows time inconsistency, it prompts actuaries to consider whether the factor needs to be re-specified, transformed, or even excluded, to ensure a robust and market-ready classification plan.

In summary, as SP8 actuaries, your dedication to building accurate and reliable rating plans means rigorously scrutinizing not just the current fit of your GLMs, but also their **time consistency**. By systematically checking how factor effects evolve over time, using both statistical tests and careful graphical analysis, you can anticipate and mitigate potential issues, thereby ensuring your classification plans remain truly predictive and effective for the future. This proactive approach to data quality and model specification is fundamental to producing credible actuarial indications.

