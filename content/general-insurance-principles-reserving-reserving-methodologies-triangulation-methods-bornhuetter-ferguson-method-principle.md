## **📗 Chapter: Reserving Methods (Specifically, Bornhuetter-Ferguson)**

### **4.0 Introduction to the Bornhuetter-Ferguson (BF) Method: The Core Principle**

The Bornhuetter-Ferguson (BF) method is a sophisticated approach to estimating general insurance reserves that transcends the simplicity of basic projection techniques. Its core principle lies in its nature as a **credibility estimate**. This means it intelligently combines two distinct, yet complementary, sources of information to produce a more stable and reliable estimate of ultimate claims:

1. **Experience-based Projection (from data to date)**: This component leverages the actual claims experience observed for a specific cohort (e.g., accident year or underwriting year). It uses a development pattern, often akin to those derived from the chain ladder method, to project the known claims into the future. This element provides a data-driven view of how claims are emerging and settling based on historical trends.

2. **A Priori (Prior) Expectation (from external or initial assumptions)**: This is an independent estimate of the ultimate claims for the cohort, typically derived from an expected loss ratio. This *a priori* component incorporates pre-existing knowledge, initial pricing assumptions, underwriter's opinion, or external benchmarks (e.g., market data). It represents an informed "belief" about the ultimate cost, independent of the current, possibly immature, claims development.

**The Fundamental Philosophy: Balancing Act and Stability**

The genius of the BF method's principle is its ability to avoid over-reliance on immature or sparse claims data for projection alone. For recent cohorts or long-tailed lines of business, early claims data can be highly volatile. A pure projection method (like the basic chain ladder) applied to such data could produce wildly distorted ultimate estimates if the initial experience is unusually high or low.

The BF method addresses this by systematically "backing off" the latest experience to the *a priori* estimate for the undeveloped portion of claims. This process effectively tempers the influence of potentially erratic early development, leading to a more stable and less volatile reserve estimate. It assumes that while actual claims will emerge over time, the ultimate cost for the undeveloped portion is better informed by a broader, prior expectation, especially when observed data is not yet fully credible. This "backing off" is the essence of its credibility weighting, ensuring that a significant portion of the ultimate liability is based on the initial expectation rather than solely on immature observations.

### **4.1 Application of the BF Principle: Step-by-Step**

The principle is put into practice through a clear, sequential application to determine the estimated ultimate claim amount for a given origin period (e.g., accident year):

1. **Determine an Initial Expected Ultimate Claim Amount (LR)**: This is your *a priori* estimate. It's often set using an expected loss ratio, which might come from the previous year's best estimates, adjusted for factors like anticipated claims inflation, changes in premium rates, or expectations regarding large claims.  
2. **Estimate the Proportion of Claims Currently Incurred or Paid (p)**: This is determined from the observed data and represents the proportion of the ultimate claims for that cohort that have already materialised and been accounted for (either paid or case-estimated).  
3. **Derive the Proportion of Claims Yet to Be Incurred or Paid (1-p)**: This is simply the complement of 'p', representing the undeveloped or outstanding portion of the ultimate claims.  
4. **Calculate the Value of Undeveloped/Unpaid Claims**: Multiply the Initial Expected Ultimate Claim Amount (LR) by the proportion of claims yet to be incurred or paid (1-p). This component effectively estimates the Incurred But Not Reported (IBNR) claims or future payments for claims that have already occurred but are not fully settled.  
5. **Calculate the Final Expected Ultimate Claims**: Sum the currently incurred or paid claims (C) with the estimated undeveloped/unpaid claims from Step 4\.  
   * **Formula**: Ultimate Claims \= Current Incurred/Paid (C) \+ LR × (1-p)

The BF method is versatile and can be applied using either **paid claims data** or **incurred claims data**, provided that the relevant historical data and development patterns are available. Furthermore, it's not limited to just ultimate claim amounts; it can also be adapted to estimate ultimate loss ratios, ultimate claim numbers, or even ultimate premiums.

### **4.2 Advantages and Appropriate Use Cases**

The unique principle of the BF method offers several advantages, making it particularly suitable for specific reserving scenarios:

#### **Advantages**

* **Robustness for Immature Data**: Its primary strength is providing more stable and reliable reserve estimates when claims data for a particular cohort is still very immature or sparse. This prevents extreme projections that might arise from limited, volatile early experience if relying solely on a chain ladder method.  
* **Avoids Zero Ultimate Estimates**: Unlike pure projection methods (e.g., chain ladder) that might produce a zero ultimate if no claims have been incurred to date for a new cohort, BF can provide a sensible non-zero ultimate based on the *a priori* estimate.  
* **Structured Credibility Blending**: It offers a transparent and actuarially sound way to combine empirical data with expert judgment or external benchmarks, formalising a credibility approach to reserve estimation.

#### **Appropriate Use Cases**

The BF method is especially effective in the following situations:

* **Early Development Stages**: For cohorts that are very recent and have limited claims development, such as newly written business or the most recent accident years in a long-tailed portfolio.  
* **Long-Tailed Business**: Useful for classes of business with protracted claims development patterns (e.g., liability excess of loss reinsurance), where maturity takes a significant amount of time.  
* **Volatile or Sparse Data**: Applicable to lines of business with small premium volumes or inherently volatile claims activity, where a purely data-driven projection might be unreliable.  
* **Blending Experience with Exposure**: When actuarial judgment suggests that a blend of observed experience and an independent, exposure-based estimate is the most appropriate approach to reflect the underlying risk.  
* **Unusual Experience**: Can serve as a useful alternative for years with unusually heavy or light claims experience that are not yet fully developed, helping to prevent over- or underestimation of IBNR.

### **4.3 Limitations and Practical Considerations**

Despite its strengths, the application of the BF principle is not without its challenges:

#### **Weaknesses**

* **Sensitivity to Prior Estimate**: The most significant limitation is the potential difficulty in accurately determining the *a priori* estimate (e.g., the initial expected loss ratio). The final reserve figure, particularly in the early stages of a cohort's development, can be highly sensitive to this subjective prior estimate.  
* **Negative Development**: If the incremental claims data exhibits a "negative tail" (e.g., significant claim recoveries or reserve reductions), the assumed percentage developed (1-p) might become unsuitable as a credibility weight. In such cases, applying BF to paid (rather than incurred) development might be a more appropriate adjustment.

#### **Practical Considerations and Relationship with Other Methods**

* **Complementary Use**: In practice, actuaries frequently employ a combination of projection methods. It's common to apply both the BF method and a chain ladder projection. For more mature cohorts with extensive claims data, projection-based methods are often given more weight, while BF receives greater weight for less developed periods.  
* **Inflation Allowance**: While some traditional statistical methods implicitly assume that future inflation will mirror past trends, the BF method, by using an independent ultimate loss ratio assumption, can explicitly incorporate anticipated future inflation (e.g., from an inflation-adjusted chain ladder approach). When setting assumptions for BF projections, such as initial loss ratios, it's crucial that these are rigorously supported by the results from earlier years or relevant benchmarks, adjusted for any changes in rates or terms and conditions.  
* **Consistency in Financial Reporting**: For external financial reporting, such as in Bornhuetter-Ferguson reserving, consistency is key. If the *a priori* loss ratio used is based on premiums gross of commission, then the premium input into the BF calculation should also be gross of commission, and vice versa.

### **V. Broader Actuarial Context: Credibility and Stochastic Reserving**

The principle of the Bornhuetter-Ferguson method extends into broader actuarial concepts, showcasing its versatility and theoretical underpinnings:

#### **A. Connection to Credibility Theory**

The BF method is a direct application of **credibility theory**. Credibility theory provides a framework for optimally blending observed experience with external or prior information, especially when the observed experience is not fully credible on its own. The BF method perfectly embodies this by weighting the empirical claims development with an *a priori* estimate of the ultimate claims. It is often conceptualised as a credibility approach that combines the chain ladder method (representing observed experience) with a "naive ultimate loss ratio method" (representing the prior expectation). This principled blending ensures that the reserve estimate is both responsive to emerging experience and stable due to the influence of the prior belief.

#### **B. Integration with Stochastic Reserving Models**

The BF method has a prominent role in **stochastic reserving**, particularly in its **Bayesian form**. In Bayesian statistics, a "prior distribution" (which captures initial beliefs about a parameter) is combined with the "likelihood" (reflecting probabilities from data) to produce a "posterior distribution". In the Bayesian BF model, the independent measure of exposure (e.g., the loss ratio used for the *a priori* estimate) is treated as a random variable following a prior probability distribution, rather than a fixed value.

This allows the Bayesian BF model to:

* **Quantify Parameter Uncertainty**: Explicitly account for the uncertainty inherent in the prior estimate by defining it as a distribution.  
* **Provide Complete Predictive Distributions**: Unlike some analytical methods that only provide a mean and variance, Bayesian methods can yield a full predictive distribution of the ultimate reserve, offering more comprehensive insights into confidence intervals and extreme values.  
* **Explicitly Show Judgements**: The influence of subjective judgements (e.g., choice of prior distribution) is made transparent, which is often implicit in other methods.

Mack has suggested that the Bayesian model is a more statistically superior credibility approach, being a weighted version of the BF method and the chain ladder method, provided the naive loss ratio itself is a credible estimate. This further highlights how the principles of credibility extend and refine the BF method.

#### **C. Link to Other Actuarial Subjects**

The fundamental concepts underpinning the Bornhuetter-Ferguson method, including credibility theory and the use of claims triangulations, are built upon knowledge assumed from earlier Core Principles subjects such as CM2, CS1, and CS2 (or the former CT6). For SP7, it is essential to have a solid understanding of these foundational principles as the course delves deeper into their practical application and evaluation within the general insurance reserving and capital modelling landscape. The method is also commonly mentioned in pricing contexts in SP8, where similar considerations for data limitations and a priori expectations apply.

---

This structured breakdown should provide a robust understanding of the principle behind the Bornhuetter-Ferguson method for your SP7 studies\! Keep practicing those questions to embed the concepts.

