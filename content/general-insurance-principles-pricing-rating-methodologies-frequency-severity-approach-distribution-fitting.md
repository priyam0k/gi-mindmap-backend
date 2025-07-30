Alright team, let's consolidate our understanding of **Distribution Fitting** within the essential **Frequency/Severity Approach** for general insurance pricing. This is a core topic for your SP8 exam, so pay close attention to the details and their practical implications.

### **The Frequency/Severity Approach: A Foundation for Pricing**

The **frequency/severity approach** is a fundamental technique used in general insurance pricing, particularly for commercial risks, that mirrors the underlying claims generation process. Unlike the simpler burning cost approach, which aggregates total claims, the frequency/severity method separates the analysis into two distinct components:

1. **Frequency**: The expected number of claims.  
2. **Severity**: The average cost of each claim.

The pure risk premium is then calculated by combining these two elements.

**Why is this approach so valuable?**

* **Deep Insight**: By analyzing frequency and severity separately, actuaries gain a much deeper understanding of the underlying drivers of loss costs. This allows us to spot trends that might be obscured in an aggregate analysis; for instance, a decreasing frequency could be offsetting an increasing severity, leading to a misleading flat overall trend.  
* **Complex Structures**: It is particularly effective for pricing policies with complex features like excesses, deductibles, or limits, as the impact of these features can be precisely modeled on the claim size distribution.  
* **Clarity for Underwriters**: This approach aligns well with how claims actually occur – individual events with associated costs – making it intuitive and understandable for underwriters.

However, this increased insight comes with increased demands: it requires more detailed and higher-quality data, and the analytical process can be more time-consuming and complex, often necessitating advanced techniques like simulation.

### **The Data Journey: From Raw to Ready for Fitting**

Before we even think about fitting distributions, the data needs significant preparation. The frequency/severity approach has robust data requirements, focusing on both quantity and quality.

1. **Data Collection and Consistency**:

   * We need detailed historical loss and exposure information for as many years as possible, with five years often cited as a minimum for liability classes.  
   * Individual loss information must be consistent with the exposure data; for example, adjustments for corporate acquisitions or disposals should be applied consistently to both.  
   * The data should be "gross of reinsurance and from the ground up," meaning the full loss amount before any reinsurance recoveries or application of policy limits.  
2. **Trending Historical Data**:

   * **Purpose**: Historical data must be adjusted (**trended**) to reflect expected conditions in the future policy period when the new rates will be in effect. This ensures relevance for prospective pricing.  
   * **Separate Trends**: Crucially, frequency and severity are trended *separately*.  
     * **Frequency Trend Drivers**: Changes in accident frequency, propensity to claim (social/economic environment), legislation, or the structure of the risk (e.g., changes in policy conditions, underwriting).  
     * **Severity Trend Drivers**: Economic inflation, changes in court awards and legislation, economic conditions, and changes to the risk structure.  
   * **Application**: Severity trending is typically applied at the *ground-up individual loss level*, while frequency trending is applied to *claim frequencies for each historical policy year*. The combined impact of these adjustments is often summarized using index figures.  
   * **Special Considerations**: Catastrophic losses are usually excluded from standard loss trend analysis and treated separately, often leveraging output from catastrophe modeling systems. Unusually large individual losses may also be removed or adjusted, or severity trends based on basic limits data may be used to reduce instability.  
3. **Developing Losses to Ultimate**:

   * **Purpose**: Raw claims data are immature; they need to be projected to their estimated ultimate values. This accounts for reported but not fully settled claims (outstanding reported claims) and incurred but not yet reported (IBNR) claims.  
   * **Individual Loss Development**: For the frequency/severity approach, it is vital to develop *each individual loss* to its likely ultimate level, rather than just the aggregate loss amount for a cohort. This is particularly important when dealing with deductibles and limits.  
   * **Methods**: Standard reserving techniques like the chain ladder or Bornhuetter-Ferguson methods can be used to develop ultimate claims. Stochastic methods can also be employed to account for variation in individual ultimate loss amounts.  
   * **IBNR Calculation**: Methods for calculating IBNR explicitly include simple ratio methods, delay tables (or run-off analyses), and projection methods based on historical development.

### **Distribution Fitting: The Heart of the Analysis**

Once losses have been meticulously trended and developed to their ultimate levels, the next critical step is to fit statistical distributions to this refined data. This is where the mathematical foundation meets practical application.

**1\. Choice of Distributions:** The selection of an appropriate distribution is paramount, as it directly impacts the accuracy of the risk premium estimation. Actuaries typically select distributions that reflect the empirical characteristics of the data.

* **For Claim Frequency:**

  * **Poisson Distribution**: This is a common choice, particularly when the number of claims may be well-modeled by a Poisson process, implying that successive claims are independent of each other. It helps ensure that model frequencies remain positive.  
  * **Negative Binomial Distribution**: Often preferred over Poisson in practice because it allows for **dependencies between claims** and can account for "over-dispersion," where the variance of the claim count exceeds its mean. This is a more realistic assumption for many insurance portfolios.  
* **For Claim Severity:**

  * **Lognormal, Weibull, Pareto, Generalised Pareto, Gamma Distributions**: These are frequently used, especially as claim amount distributions are often positively skewed (meaning smaller losses are more frequent, but large losses, though rare, can be very impactful).  
  * **Tail Heaviness**: It's crucial to select a curve with the appropriate "degree of tail heaviness," particularly for classes of insurance with very skewed claim amount distributions, to accurately capture the risk of large, infrequent claims. For instance, a Pareto distribution is often suitable for very large losses due to its relatively long, thick tail.  
  * **Combining Severity Distributions**: For comprehensive accuracy, actuaries may fit different severity distributions to different parts of the overall loss range. For example:  
    * **Small attritional losses**: Lognormal distribution.  
    * **Medium-sized losses (up to a large loss threshold)**: Gamma or skewed Weibull distribution.  
    * **Very large losses**: Pareto distribution.  
    * **Catastrophe losses**: Simulated using distributional assumptions from catastrophe models. This approach acknowledges the different underlying incident types (e.g., slips, falls, vehicle accidents) that contribute to the overall claim severity.

**2\. The Fitting Process:** Once distributions are chosen, parameters must be estimated.

* **Methods of Estimation**: Common methods include **Maximum Likelihood Estimation (MLE)**, **Method of Least Squares**, and **Method of Moments**. These methods aim to find the parameters that best describe the observed data.  
* **Software**: Proprietary software packages greatly assist in fitting a wide variety of distributions, though in-house routines can also be developed.  
* **Parameter Uncertainty**: It's vital to be aware of the "estimation error" or "parameter error" around the fitted parameters due to using a finite sample of data. This uncertainty can be assessed using techniques like **bootstrapping**, **asymptotic approximations for maximum likelihood estimates**, or **Bayesian methods**. Bootstrapping, a simulation technique, involves repeatedly sampling from the observed data to create pseudo-datasets and refitting the model to obtain a distribution of parameters.

**3\. Testing Goodness of Fit:** After fitting, rigorous testing is necessary to ensure the chosen distribution adequately represents the data.

* **Visual Checks**: Plotting the density functions of observations against the fitted distribution allows for a quick visual assessment of fit.  
* **Statistical Tests**: More robust assessments come from statistical goodness-of-fit tests:  
  * **Anderson-Darling (A-D) Statistic**: Measures the distance between the empirical and theoretical cumulative distribution functions, placing *more weight on differences in the tails* of the distribution. It is often more powerful than K-S for testing normality.  
  * **Kolmogorov-Smirnov (K-S) Statistic**: Also measures the distance but is *more sensitive to deviations around the center* of the distribution.  
* **Theoretical and Practical Sense**: Beyond statistical fit, it's good practice to ensure the selected distribution makes theoretical and practical sense for the specific type of claims being modeled. For example, if a model "fans out" on a residual plot, it indicates that the chosen distributional assumptions (e.g., variance proportional to mean) are incorrect.

### **Simulation: Bridging the Gap**

While exact formulas for aggregate loss distributions can sometimes be derived, they often become unmanageably complex for realistic product structures or combinations of frequency and severity distributions. This is where **stochastic simulation**, particularly Monte Carlo methods, becomes an invaluable tool.

* **Approximating Aggregate Distributions**: Simulation allows us to obtain predictive distributions of reserves and aggregate loss distributions even when analytical methods are impractical.  
* **Process**: It typically involves:  
  1. Simulating claim numbers from a chosen frequency distribution (e.g., Poisson or negative binomial).  
  2. For each simulated claim, generating a claim amount from the chosen severity distribution (e.g., lognormal, Pareto, Gamma).  
  3. Aggregating these simulated claims to arrive at an estimated total loss for a given period.  
  4. Repeating this process thousands of times to build a distribution of possible outcomes.  
* **Assessing Complexities**: Simulation models are powerful for assessing the impact of policy features like deductibles (per occurrence, aggregate, etc.) and limits on the expected loss to the insurer, as well as the distribution of other components.  
* **Error Management**: While simulation introduces its own "simulation error" due to the finite number of runs, this can be reduced by performing more simulations or using techniques like Latin Hypercube sampling.

In essence, distribution fitting and its subsequent application through simulation are critical for translating historical, adjusted claims data into actionable predictions for future pricing. This meticulous process ensures that the fundamental insurance equation remains balanced, allowing for competitive and sustainable rates.

