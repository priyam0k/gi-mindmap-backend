As a Specialist Actuarial Note Builder and Exam Coach for SP8, I can confirm that the Frequency/Severity approach is a fundamental and extensively discussed methodology within General Insurance Pricing. It is explicitly identified as a key pricing approach in the syllabus and is crucial for calculating the pure risk premium.

Let's delve into what the sources say about the "Description" of the Frequency/Severity approach within the larger context of rating methodologies.

### **1\. Description of the Frequency/Severity Approach**

The Frequency/Severity approach is a specific technique used under the "cost plus" approach to calculate the **pure risk premium**. The pure risk premium represents the expected cost of claims for a given period, without any allowance for expenses, profit, or other loadings.

At a high level, this method involves:

* **Estimating the expected number of claims (Frequency)** per unit of exposure.  
* **Estimating the expected average cost of claims (Severity)**.  
* **Multiplying these two components** to determine the risk premium.

This approach is considered fundamental because it mirrors the underlying claims generation process in the real world: claims occur (frequency), and each claim has an ultimate value (severity).

### **2\. Context within Rating Methodologies**

The Frequency/Severity approach is a core component of the "cost plus" pricing method, where the price is set based on a statistically driven analysis of expected costs. After the pure risk premium is determined using this method, various loadings for expenses, profit, reinsurance costs, and contingencies (with investment income often as a deduction) are applied to arrive at the final office premium.

**Comparison with Burning Cost Approach**: The sources highlight key differences and advantages of the Frequency/Severity approach over the Burning Cost approach:

* **Underlying Process Reflection**: The Frequency/Severity approach explicitly models the occurrence and cost of claims, directly reflecting the actual process, unlike the Burning Cost method which largely ignores the number of claims and focuses on total aggregate claims.  
* **Data Insight and Trends**: By separately analysing frequency and severity, this method offers deeper insights into loss experience drivers. It allows for the identification of distinct trends in claim frequency and severity that might be obscured in an aggregate (Burning Cost) analysis. For instance, an increasing frequency might be offset by a decreasing severity, leading to a seemingly stable overall trend in a burning cost calculation. Changes in claims handling procedures can also be highlighted by analysing changes in severity.  
* **Complexity of Structures**: The Frequency/Severity method is particularly useful for complex insurance structures involving excesses, deductibles, or limits, as it allows for the separate assessment and combination of these components.  
* **Data Requirements**: It is more data-intensive, requiring detailed information on claim numbers and individual claim amounts, not just aggregate sums.  
* **Complexity and Expertise**: This approach is generally more complex and time-consuming, often requiring sophisticated statistical techniques and simulation, thus demanding a higher level of actuarial expertise compared to the simpler Burning Cost method. Consequently, it is more commonly used in commercial lines, especially for liability classes where single risks can generate numerous claims.

### **3\. Data Requirements and Adjustments**

To apply the Frequency/Severity approach effectively, high-quality and sufficient data are paramount.

**Data Items Required**:

* **Policy data**: Needed to calculate exposure and identify risk characteristics. Exposure is the basic unit for measuring a policy's loss exposure and serves as the premium basis. A good exposure base should be proportional to expected loss, practical, and consistent over time. Examples include employee count for employers' liability or vehicle years for motor insurance.  
* **Claims data**: Essential for estimating the ultimate cost of claims, including claim reference, loss date, description, and amount. Data by type of peril is particularly useful for costing policy options and adjusting for unusual events.  
* **Consistency**: Individual loss information must be consistent with exposure information, especially after adjustments for corporate activities like acquisitions or disposals.  
* **Volume and Period**: Five years of historical loss and exposure data is often a minimum for liability classes, with more being desirable to ensure credibility and allow for fitting distributions.  
* **Gross of Reinsurance and Ground-up**: Data should ideally be *gross of reinsurance* and from the *ground up* (i.e., the whole loss without deductions for excesses or deductibles), as reinsurance costs are handled separately later.

**Adjustments to Historical Data**: Historical data needs several adjustments to be relevant for future pricing periods:

* **Trending**: Adjusting historical frequencies and severities to reflect expected future changes. Separate trends are applied to frequency and severity components:

  * **Frequency Trends**: Drivers include changes in accident frequency, propensity to make claims, social/economic environment, legislation, and risk structure (e.g., changes in policy conditions or underwriting).  
  * **Severity Trends**: Drivers include economic inflation, changes in court awards, legislation, and the structure of the risk. Severity trending is usually applied at the ground-up individual loss level.  
  * **Application**: Trends can be applied using indices that reflect periods of high/low trend or discontinuities (e.g., due to legal changes), or as a constant annual rate. Linear and exponential regression models are common for measuring trend, with exponential models generally preferred as they avoid projecting negative values for frequency or severity. Actuarial judgment is crucial for selecting appropriate trends.  
  * **Large Losses**: Catastrophic losses and other large individual losses are often treated separately to avoid distorting frequency and severity patterns, typically relying on catastrophe models rather than historical averages. Trends can also be a function of loss size. The "leveraged effect of limits on severity trend" is an important consideration, where a uniform trend in total limits losses can dampen or amplify trends for basic limits or excess layers.  
* **Developing Losses to Ultimate**: Claims data must be developed to their likely ultimate settlement levels, accounting for reported but unsettled claims (outstanding reported claims) and incurred but not yet reported (IBNR) claims.

  * **Individual Loss Development**: For the Frequency/Severity approach, it is critical to develop *each individual loss* to its ultimate level, unlike aggregate methods. This precision is especially important for policies with deductibles or limits to accurately estimate retained or covered portions of losses.  
  * **Methods**: Standard reserving techniques like the chain ladder or Bornhuetter-Ferguson methods can be used to calculate ultimate overall claim amounts. Stochastic development methods may also be employed to account for variation. IBNR for claim counts is also developed to ultimate, considering reporting delays.  
  * **Homogeneity**: Loss development analysis should be undertaken on homogeneous claims (e.g., by line of business, coverage, geography) with extraordinary losses removed and material benefit changes adjusted for.

### **4\. Fitting Distributions and Simulation**

After historical data has been adjusted for trending and development, frequency and severity distributions are typically fitted to this adjusted loss data.

* **Choice of Distributions**: Common choices for claim numbers (frequency) include Poisson or Negative Binomial distributions. For claim amounts (severity), Log-normal, Weibull, Pareto, or Gamma distributions are frequently used.  
* **Parameter Estimation**: Parameters for these chosen distributions are estimated from the data. Methods for assessing parameter uncertainty include bootstrapping, asymptotic approximations for maximum likelihood estimates, and Bayesian methods. It is crucial to check for acceptable goodness of fit.  
* **Simulation Techniques**: While exact formulas for aggregate loss distributions can sometimes be derived, simulation (e.g., Monte Carlo) is commonly used, especially for complex product structures (e.g., aggregate deductibles, non-ranking deductibles, or various policy limits). This allows for assessing the expected loss cost and the distribution of other components impacted by the policy structure. Simulation methods are still widely used where data is imperfect.

### **5\. Practical Considerations and Applications**

The Frequency/Severity approach is particularly prevalent in commercial lines, especially for liability insurance and large commercial risks, due to the volume of claims these can generate for a single risk. It is also frequently applied in pricing excess of loss reinsurance contracts, especially where direct data at higher layers is sparse.

Actuarial judgment is continuously exercised throughout the process, from selecting appropriate trends and development patterns to choosing distributions and evaluating the reasonableness of the final results. The method's ability to model the underlying process and provide detailed insights makes it a powerful tool, particularly for understanding the impact of policy conditions like deductibles and limits.

### **6\. Link to GLMs and Multivariate Modelling**

The principles of the Frequency/Severity approach are deeply intertwined with Generalised Linear Models (GLMs) and multivariate analysis, which are standard tools for classification ratemaking.

* **Addressing Univariate Shortcomings**: Univariate (one-way) analyses, which examine each rating variable in isolation, suffer from the primary shortcoming of not accurately accounting for the effect of other rating variables or exposure correlations. This can lead to distortions and "double-counting" effects.  
* **Multivariate Benefits**: GLMs and other multivariate methods overcome these limitations by considering all rating variables simultaneously and automatically adjusting for exposure correlations.  
  * **Frequency and Severity Models**: It is very common when using GLMs to model claim frequency and claim severity separately. A log link function is typically used, leading to a multiplicative rating structure, which is common in the insurance industry. GLM analysis is typically performed on loss cost data or, preferably, frequency and severity separately.  
  * **Model Diagnostics**: Multivariate methods provide statistical diagnostics (e.g., standard errors, deviance tests, R-squared) that aid in understanding the certainty of results and the appropriateness of the model fitted.  
  * **Interactions**: They can also incorporate interactions between rating variables, where the effect of one variable changes depending on the level of another.  
* **Initial Analyses**: Before running a multivariate model, actuaries typically perform initial analyses like one-way tables, two-way tables, correlation analyses, and distribution analyses. These steps help in understanding the data and identifying potential issues.  
* **Credibility**: When performing multivariate classification analysis using statistical techniques like GLMs, statistical diagnostics are used to gauge the meaningfulness of the results, rather than traditional credibility weighting with univariate estimates.

In essence, the Frequency/Severity approach provides the conceptual framework (separating drivers of claim counts and costs), while GLMs and multivariate models offer powerful statistical tools to implement this framework comprehensively, accounting for complex interdependencies in modern pricing.

