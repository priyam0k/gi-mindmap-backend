Right, my future SP7 Actuarial Specialist, let's dive deep into the fascinating, yet often challenging, world of **Large Losses** and how they impact **Data for Reserving**. This isn't just about crunching numbers; it's about understanding the underlying dynamics that can make or break an insurer's financial stability.

### **1\. The Nature of Large Losses and Their Significance in Reserving**

At the heart of a reserving exercise is the objective to determine a point estimate of the best estimate reserves. However, the reality is that the actual reserve required will inevitably differ from this estimate. This is where the concept of "large losses" becomes critically important.

A **large loss** can be broadly defined as a risk or a group of risks that are, to some extent, unique, requiring calculations to be applied once to that specific risk. Unlike typical "attritional claims" (which are normal, non-large claims), large losses possess distinct characteristics that necessitate special handling in the reserving process. They are expected to have different frequency and severity distributions, and crucially, different claims development patterns compared to attritional and catastrophic claims. For instance, a large windstorm claim might develop at a different rate than a large flood claim, even within the same property book of business. Some of the most notorious classes of large losses are latent claims, such as those arising from asbestos, pollution, and health hazards (APH), where the full extent and cost may not materialise until many years after the initial exposure or event. Such claims can have extremely long reporting delays, making their future development inherently uncertain.

The inherent uncertainty surrounding the liability for outstanding claims means that any aspect of the insurer relying on these estimates, such as profitability, is also subject to uncertainty. This is particularly true for long-tail classes of business, where claims reserves are generally larger and the uncertainty is greater.

### **2\. Impact of Large Losses on Data for Reserving**

The presence of large losses significantly impacts the data used for reserving, and if not handled appropriately, can lead to serious distortions in reserve estimates.

* **Distortion of Data Triangles**: It is normal practice to remove large claims from the claims development triangles when projecting attritional losses. If these claims are left unadjusted in aggregate data, they can distort the experience of the risk group and cause problems in reserving, as they often develop differently from attritional claims.  
* **Increased Volatility**: If the threshold for what constitutes a large claim is set too low, a large quantity of data will be excluded from the attritional claims triangulation, reducing its credibility. Conversely, if the threshold is set too high, more large claims are included, increasing the volatility of the projection.  
* **Lack of Credible Historical Data**: Due to their infrequent and unique nature, there is often a lack of sufficient historical data to accurately model the development of large losses. This issue is particularly acute for "Events Not In Data" (ENIDs), where a risk of large losses exists but has not been experienced historically. Relying purely on historical data in such cases can lead to an underestimation of variability.  
* **Data Peculiarities**: Sparse data sets and peculiarities (e.g., missing or erroneous data) are problematic for stochastic methods, as small changes can lead to significant shifts in the distribution of outcomes. For example, negative values in incremental claims data (due to downward revisions of case estimates, salvage, or reinsurance recoveries) can limit the applicability of certain models like log-normal.

### **3\. Reserving Methods and Considerations for Large Losses**

Given their unique characteristics and impact on data, large losses require specific methods and considerations in reserving.

#### **3.1 Defining "Large"**

The definition of a "large loss" is crucial and can vary. It might be set as claims over a particular threshold, which could differ by peril and be tied to the reinsurance programme's retention limit. This ensures that the projection of net-of-reinsurance claims is more manageable. It is also important to consider indexing this large loss limit annually for inflation to maintain consistency over time, preventing inconsistent numbers of "large" claims in different years of account.

#### **3.2 Specific Reserving Approaches**

* **Separate Analysis**: The common practice is to remove large claims from the main claims development and project them separately from attritional losses. This separation allows for more appropriate methods for each type.  
* **Individual Case-by-Case Estimation**: For very large or unique claims, individual case-by-case analysis is often preferred, particularly when statistical models are unreliable. This requires experienced case assessors and can be time-consuming. A key limitation is that it cannot produce estimates for Incurred But Not Reported (IBNR) claims, as these are unknown to the insurer.  
* **Exposure-Based Methods**: These methods are generally used for latent claims where past claims data is not suitable because the development pattern is unlikely to bear a clear relationship to the period since occurrence. They involve making assumptions about the volatility of future claim numbers and their average cost, modelling these distributions separately before combining them for the total claim amount.  
* **Claims Development Methods**: While standard methods like chain ladder can be adapted, large claims should ideally be projected from their actual date of loss rather than the origin period start. This ensures consistency in comparing their development. Catastrophe losses, for example, tend to develop more quickly due to increased focus from adjusters and policyholders, necessitating separate review.  
* **Benchmarks**: When internal data is limited, especially for new lines of business or high-layer excess of loss reinsurance, market benchmarks or benchmarks from similar books of business can be applied to estimate reserves. These can include cumulative paid/incurred development patterns, development (link) ratios, and loss ratios.  
* **Stochastic Development Methods**: For allowing for variation in individual ultimate loss amounts, stochastic methods can be used. However, given the scarcity of data for extreme events, estimating the tail of the distribution requires extreme care. Simplifying assumptions, reasonable for the central distribution, may break down at the extremes.

#### **3.3 The Role of Claims Watchlists**

In practice, particularly in markets like London, it's common to maintain "claims watchlists" for claims under close monitoring where the case reserve might not accurately represent the likely ultimate cost. Reasons include significant uncertainty in value (e.g., D\&O claims), avoiding legal prejudice, or differing views from the lead insurer. Actuaries should discuss these with the claims team to ensure that reserving estimates, including additional IBNR, adequately cover these potential large losses. It's crucial to consider if existing development patterns already account for the timing of losses moving from monitoring to case estimates.

### **4\. Interaction with Reinsurance**

Large losses are often a primary driver for purchasing reinsurance, especially excess of loss (XL) cover.

* **Reinsurance Recoveries**: When a large loss occurs, reinsurance recoveries can be significant. It is preferable to project salvage, subrogation, and reinsurance recoveries separately from gross amounts, as their payment patterns differ. For non-proportional (XL) reinsurance, the estimation of net reserves is more complex due to the differing nature of the gross and net claims results.  
* **Indexed Attachment Points**: When applying reinsurance programs to individual gross losses, it's vital to consider whether the attachment point and/or limit are indexed. For long-tailed claims like bodily injury, inflation can erode reinsurance recoveries if the attachment point is not indexed.  
* **Reinsurer Profitability**: For Risk XL treaties, the reinsurer's ultimate loss ratio is very sensitive to large losses. An increase in the cedant's gross loss ratio due to a large loss can lead to a disproportionately larger increase in the reinsurance loss ratio.

### **5\. Data Requirements and Quality for Large Losses**

For effective reserving of large losses, specific data requirements and a keen eye on data quality are paramount.

* **"From the Ground Up" Data**: Individual loss information should ideally be obtained "from the ground up" (FGU), meaning all claims, no matter how small, and their original amount, gross of reinsurance. This provides a complete picture, especially critical when dealing with deductibles or limits.  
* **Policy-Level Detail**: For exposure-based reserving, information on each policy is needed, including policy limits, excesses, start/end dates, insured perils, exclusions, company share of total risk (for London Market), paid claims, reported outstanding claims, and dates of reporting/occurrence. This level of detail is necessary to perform detailed analyses.  
* **Consistency and Reconciliation**: Claims data obtained for reserving must be reconciled with accounting records and the general ledger to ensure consistency. It should also be compared with historical data to identify unusual movements.  
* **Handling Data Peculiarities**: Errors, omissions, or distortions (e.g., wrong claim number, policy number, return premiums recorded as claims) can significantly distort development patterns. Actuaries must investigate and make appropriate allowances for such distortions.  
* **Limited Data Situations**: When data is sparse, or for new books of business, external data sources like industry-wide schemes, reinsurers' data, or published accounts become invaluable to supplement internal data and provide benchmarks. However, relying on industry data introduces potential distortions due to heterogeneity (e.g., differences in policies, target markets, sales methods).

### **6\. Actuarial Judgement and Communication of Uncertainty**

The complexities surrounding large losses underscore the vital role of actuarial judgement and transparent communication.

* **Judgement over Mechanical Application**: Actuaries must apply significant judgement during the reserving process, moving beyond the mechanical application of triangulation methods to data. This includes assessing the reasonableness of results through diagnostic tests, benchmarks, and past experience.  
* **Underestimation of Variability**: It is widely acknowledged that many stochastic reserving methods based on historical data (like Mack and bootstrapping) tend to underestimate the underlying variability of reserves, as past data may not capture all future sources of variability (e.g., changes in Ogden discount rate, court judgments, prolonged inflation).  
* **Communication**: Clearly communicating the outputs of a stochastic reserving exercise, including limitations, assumptions, and materiality of judgements, is an important part of the process. This involves explaining what elements are included in the best estimate (e.g., ALAE, ULAE, net/gross of reinsurance, salvage/subrogation, bad debt) and providing a range of possible outcomes using stochastic models, scenario tests, or alternative assumptions. For management, a range of best estimates or reasonable outcomes can be useful for assessing resilience and reinsurance purchasing decisions.

### **7\. Connection to Capital Modelling**

Understanding and modelling large losses are fundamental to capital modelling.

* **Quantifying Reserving Risk**: Stochastic reserving techniques are commonly used to determine quantitative estimates of the volatility in reserves as an input to capital models, helping to assess reserve adequacy and allocate capital.  
* **Risk Categorisation**: For capital modelling, gross underwriting risk is often divided into attritional, large, and catastrophe claims, each modelled separately. Catastrophe modelling software (e.g., RMS, AIR, EQECAT) is crucial here, especially for low-frequency, high-severity risks where traditional methods are inadequate.  
* **Frequency-Severity Modelling**: For capital modelling, large claims are generally modelled on a frequency-severity basis, using distributions like Poisson/negative binomial for frequency and log-normal/Weibull/Pareto for severity.  
* **Stress Testing**: Stress tests are used to quantify the effect of varying parameters, such as a large loss or a catastrophe event, on liquidity risk and overall capital requirements. The impact of operational risks crystallising into catastrophic losses is also a concern.

In summary, my actuary-in-training, dealing with large losses in reserving is a complex but vital aspect of general insurance. It demands not just technical proficiency in various modelling techniques but also a deep understanding of data nuances, the influence of external factors, the interplay with reinsurance, and the critical application of professional judgement to ensure robust and reliable financial reporting and capital management. Keep those models sharp, but never forget the art of actuarial reasoning\!

