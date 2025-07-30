As a Specialist Actuarial Note Builder and Exam Coach for SP8, I can confirm that the Frequency/Severity approach is a cornerstone of General Insurance Pricing methodologies. It's explicitly listed in your SP8 syllabus as a core pricing method, often alongside the Burning Cost approach, and forms a critical foundation for more advanced techniques like Generalised Linear Models (GLMs) and multivariate modelling.

Let’s dissect the Frequency/Severity Approach in detail, placing it within the broader context of rating methodologies:

### **1\. Definition and Core Concept**

The Frequency/Severity approach is a method used to calculate the **pure risk premium** – the amount of premium required to cover only the expected cost of claims. It achieves this by:

* **Estimating the expected number of claims (Frequency)** per unit of exposure.  
* **Estimating the expected average cost of claims (Severity)**.  
* **Multiplying these two components** to arrive at the risk premium for a specific period.

This approach is considered fundamental because it mirrors the underlying claims process: losses are generated (frequency), and each loss has an ultimate value (severity).

### **2\. Context within Rating Methodologies**

The Frequency/Severity approach falls under the 'cost plus' approach to pricing, where the price is set based on a statistically driven analysis of expected costs. After deriving the risk premium using this method, various loadings are applied to cover other items like expenses (including commission), reinsurance costs, profit, and contingencies, with investment income often serving as a deduction, to arrive at the final 'office premium'.

This methodology is particularly useful for rating complex insurance structures, such as those involving excesses, deductibles, or limits, as it allows for the separate assessment and combination of these components.

### **3\. Comparison with the Burning Cost Approach**

While both are common methods for deriving the risk premium, the Frequency/Severity approach offers distinct advantages over the Burning Cost approach:

* **Underlying Process Reflection**: The Frequency/Severity approach explicitly models the occurrence and cost of claims, which directly reflects the real-world process of how claims arise and are valued. In contrast, the Burning Cost approach largely ignores the number of claims, focusing only on the total aggregate claims expressed as an annual rate per unit of exposure.  
* **Data Insight and Trends**: By separately analysing frequency and severity, this method provides deeper insights into the drivers of loss experience. It enables the identification of distinct trends in claim frequency and severity, which might otherwise be masked if only aggregate claims (as in Burning Cost) were considered. For example, an increasing frequency trend might be offset by a decreasing severity trend, leading to no discernible overall trend in a burning cost analysis.  
* **Data Requirements**: The Frequency/Severity approach is more data-intensive than the Burning Cost method, requiring detailed information on claim numbers and individual claim amounts, not just aggregate sums. This can be a disadvantage if data is sparse or of poor quality.  
* **Complexity and Expertise**: Due to its detailed nature, the Frequency/Severity approach is generally more complex and time-consuming to perform, often requiring sophisticated statistical techniques and simulation. This typically means it requires a higher level of actuarial expertise compared to the simpler Burning Cost method.

### **4\. Data Requirements and Adjustments**

The quality and quantity of data are paramount for the Frequency/Severity approach. Key data items include:

* **Policy data**: To calculate exposure and identify risk characteristics.  
* **Claims data**: To estimate the ultimate cost of claims, including loss date, description, and amount. Data by type of peril is particularly useful for costing policy options and making adjustments for unusual events.  
* **Consistency**: Individual loss information must be consistent with exposure information, especially after adjustments for corporate activities like acquisitions or disposals.  
* **Volume and Period**: Typically, five years of historical loss and exposure information is considered a minimum for liability classes, with more being desirable to ensure credibility.  
* **Gross of Reinsurance**: Data should generally be *gross of reinsurance* and from the *ground up* (i.e., the whole loss without deductions for excesses or deductibles), as reinsurance costs are accounted for separately later in the premium calculation process.

Once collected, historical data needs several adjustments to make it relevant for future pricing periods:

* **Trending**: This involves adjusting historical frequencies and severities to reflect expected future changes. Separate trends are applied to frequency and severity components.

  * **Frequency Trends**: Drivers include changes in accident frequency, propensity to make claims, social/economic environment, legislation, and risk structure.  
  * **Severity Trends**: Drivers include economic inflation, changes in court awards, legislation, and the structure of the risk. Severity trending is usually applied at the ground-up individual loss level.  
  * **Application**: Trends can be applied using indices that reflect periods of high/low trend or discontinuities (e.g., due to legal changes), or as a constant annual rate. Actuarial judgment is crucial to determine if the trend is reasonable and likely to continue.  
  * **Large Losses**: Catastrophic losses and other large individual losses are often treated separately from attritional claims to avoid distorting frequency and severity patterns, typically relying on catastrophe models rather than historical averages.  
* **Developing Losses to Ultimate**: Claims data must be developed to their likely ultimate settlement levels, accounting for claims that are reported but not fully settled (outstanding reported claims) and those that have occurred but not yet reported (IBNR).

  * **Individual Loss Development**: For the Frequency/Severity approach, it's critical to develop *each individual loss* to its ultimate level, rather than just aggregate loss amounts.  
  * **Methods**: Standard reserving techniques like the chain ladder or Bornhuetter-Ferguson methods can be used, though stochastic development methods may also be employed to account for variation.  
  * **Importance for Deductibles/Limits**: Accurate development of individual losses is especially important for policies with deductibles or limits, to precisely estimate the portions of losses retained by the insured or covered by specific layers.

### **5\. Fitting Distributions and Simulation**

After historical data has been trended and developed, frequency and severity distributions are typically fitted to this adjusted loss data.

* **Choice of Distributions**: Common choices include:  
  * **Frequency**: Poisson or Negative Binomial distributions. A log link function is often used to yield a multiplicative model structure.  
  * **Severity**: Log-normal, Weibull, Pareto, or Gamma distributions. A log link function is also common for severity models, assuming a multiplicative effect of factors.  
* **Parameter Estimation**: Parameters for these chosen distributions are estimated from the data. Methods for assessing parameter uncertainty include bootstrapping, asymptotic approximations for maximum likelihood estimates, and Bayesian methods.  
* **Goodness of Fit**: It's crucial to check that the chosen distributions provide an acceptable goodness of fit to the observed data.  
* **Simulation Techniques**: While exact formulas for aggregate loss distributions can sometimes be derived, simulation (e.g., Monte Carlo) is commonly used, especially for complex product structures (e.g., aggregate deductibles, non-ranking deductibles, or various policy limits). This allows for assessing the expected loss cost and the distribution of other components impacted by the structure.

### **6\. Practical Considerations and Applications**

The Frequency/Severity approach is predominantly used in commercial lines, particularly for liability insurance and large commercial risks, where single risks can generate a large number of claims. It's also frequently applied in pricing excess of loss reinsurance contracts, especially where direct data at higher layers is sparse, despite the lack of data often posing a challenge.

Actuarial judgment plays a continuous role, from selecting appropriate trends and development patterns to choosing distributions and evaluating the reasonableness of the final results. The method's ability to model the underlying process and provide detailed insights makes it a powerful tool, particularly for understanding the impact of policy conditions like deductibles and limits.

### **7\. Link to GLMs and Multivariate Modelling**

The principles of the Frequency/Severity approach are deeply intertwined with Generalised Linear Models (GLMs) and multivariate analysis, which are standard tools for classification ratemaking.

* **Addressing Univariate Shortcomings**: Univariate (one-way) analyses, which examine each rating variable in isolation, suffer from the primary shortcoming of not accurately accounting for the effect of other rating variables or exposure correlations. This can lead to distortions and "double-counting" effects.  
* **Multivariate Benefits**: GLMs and other multivariate methods overcome these limitations by considering all rating variables simultaneously and automatically adjusting for exposure correlations.  
  * **Frequency and Severity Models**: It is very common when using GLMs to model claim frequency and claim severity separately. A log link function is typically used, leading to a multiplicative rating structure, which is familiar to the insurance industry.  
  * **Model Diagnostics**: Multivariate methods provide statistical diagnostics (e.g., standard errors, deviance tests) that aid in understanding the certainty of results and the appropriateness of the model.  
  * **Interactions**: They can also incorporate interactions between rating variables, where the effect of one variable changes depending on the level of another.  
* **Initial Analyses**: Before running a multivariate model, actuaries typically perform initial analyses like one-way tables (for preliminary indication of factor effect), two-way tables (to understand correlations between factor pairs), correlation analyses, and distribution analyses. These steps help in familiarising with the data and identifying potential issues.

In essence, the Frequency/Severity approach provides the conceptual framework (separating drivers of claim counts and costs), while GLMs and multivariate models offer the powerful statistical tools to implement this framework comprehensively, accounting for complex interdependencies in modern pricing.

