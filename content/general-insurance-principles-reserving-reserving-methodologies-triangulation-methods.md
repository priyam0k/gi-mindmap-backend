## **📗 Chapter 15: Triangulation Methods in General Insurance Reserving**

### **0.0 Introduction to Reserving Methodologies**

In the world of General Insurance, reserving is not merely an accounting exercise; it's a critical actuarial investigation aimed at quantifying the expected future claim payments and related expenses for past events and unexpired risks. Actuaries determine these liabilities for a myriad of purposes, each demanding a specific valuation basis and set of assumptions:

* **Published Accounts:** To present a true and fair view of the insurer's financial position, often requiring a going concern basis, best estimate, and/or discounted reserves, adhering to specific legislation and accounting principles like IFRS 17 or Solvency II.  
* **Supervisory Solvency:** To demonstrate adequate capital to regulators, often demanding a prudent basis or a discounted best estimate plus a risk margin (e.g., under Solvency II) to protect policyholders.  
* **Internal Management Purposes:** To provide realistic insights into business performance, profitability, and to inform strategic decision-making, typically using a best estimate basis, often complemented by sensitivity testing.  
* **Tax Liabilities:** To ascertain the correct tax payments, guided by specific tax regulations that may include penalties for over-reserving.  
* **Sale or Purchase of a Company/Portfolio:** To value the liabilities in M\&A transactions, where the purchaser may adopt a more pessimistic view than the vendor due to commercial implications.  
* **Commutation or Transfer of Liabilities:** To negotiate a settlement for a block of business or transfer liabilities, with considerations similar to M\&A but also impacted by financial strength and local regulations.  
* **Testing Adequacy of Case Estimates:** To compare actual claim payments against previous estimates, informing future assumption changes.

Reserving methodologies can broadly be categorised into:

* **Case Estimates:** Individual assessment of reported claims.  
* **Statistical Methods:** Employing historical data patterns to project future claims, particularly useful for high-frequency, stable classes. Triangulation methods fall into this category.  
* **Exposure-Based Methods:** Relating claims to a measure of exposure, often used for new lines or latent claims.

### **1.0 Triangulation Methods: The Core of Statistical Reserving**

Triangulation methods are a cornerstone of statistical reserving, providing a structured approach to project future claim developments based on historical data patterns. They are founded on the assumption that future claim development will follow past patterns. While powerful, they are imperfect representations of complex claim processes and require a thorough understanding of data and their inherent limitations.

The main triangulation methods include:

* **Chain Ladder Method (CLM)**  
* **Bornhuetter-Ferguson (BF) Method**  
* **Average Cost Per Claim (ACPC) Method**

### **1.1 General Issues Affecting Reserving Work Using Triangulations**

Before diving into specific methods, it's crucial to acknowledge the general issues that can affect reserving work using triangulations and how to manage them effectively.

#### **1.1.1 Understanding the Data**

The success of any triangulation method hinges on a deep understanding of the available data, including its limitations, strengths, and weaknesses. This comprehension guides the selection of methods and the appropriate grouping of data. Errors in data can seriously distort projections, leading to incorrect reserve values.

#### **1.1.2 Types of Run-off Triangles**

Claims data are typically tabulated in run-off triangles or development tables, where rows represent "origin years" (e.g., accident, underwriting, policy, or reporting year) and columns represent "development periods".

* **Incremental vs. Cumulative Amounts:** Triangles can display incremental amounts (claims paid/incurred in each period) or cumulative amounts (total claims accumulated to a given development period). The chain ladder method typically uses cumulative amounts to derive link ratios.

* **Cohort Definitions:**

  * **Underwriting Year:** Groups claims by the year the policy was underwritten. This implicitly includes IBNR, recoveries, and reopened claims, provided they are allocated to the correct underwriting year.  
  * **Accident Year:** Groups claims by the year the accident/event occurred.  
  * **Policy Year:** Groups claims by the year the policy incepted.  
  * **Reporting Year:** Groups claims by the year the claim was reported to the insurer. A key disadvantage is that projections based on reporting year will *not* allow for pure IBNR (claims not yet reported by year-end), requiring a separate estimate for these.  
  * **Calendar Year:** Groups claims by the year they were paid or incurred. Some latent claims (e.g., APH) exhibit calendar year development effects, making traditional triangulation methods (which rely on origin year development) unsuitable.  
* **Development Periods:** While yearly development periods are common, shorter periods (e.g., quarterly) may be necessary to observe and manage seasonal effects or for quarterly reporting requirements. However, longer periods (e.g., annual) might provide a better view of overall trends, especially when quarterly data is volatile.

* **Using Parallelograms or Trapeziums:** Standard run-off triangles have sparse data in the tail, relying heavily on limited data points. Including data from older, fully run-off origin years (forming a parallelogram or trapezium) can reduce over-reliance on a single piece of data in the tail.

#### **1.1.3 Data Grouping and Heterogeneity**

To achieve credible estimates, data should be subdivided into relatively homogeneous groups, meaning claims within a group share similar reporting, settlement, and inflationary characteristics. This is crucial because statistical methods assume stable claims development patterns across cohorts.

* **Examples of Groupings:** Class of business (e.g., property vs. liability), claim development patterns (delay to reporting/settlement), size of loss, legal environment, property damage/personal injury, personal/commercial risks, primary/excess layers.  
* **Minimising Distortions:** Data can be subdivided or combined to minimise the distorting effects of operational or procedural changes within the insurer (e.g., changes in claims handling practices or IT systems). This might involve basing link ratios only on data from *after* the change or applying subjective adjustments.

#### **1.1.4 Treatment of Large Losses and Non-Standard Risks**

Large or unusual claims can significantly distort triangulation methods. Therefore, it's often necessary to analyse them separately from the main data triangles, as their development profile may differ from "attritional claims".

* **Methods for Large Losses:**  
  * **Individual Case-by-Case Basis:** Highly experienced assessors evaluate each large loss. While time-consuming, it leverages all known data and qualitative factors. However, it cannot estimate IBNR, requiring a separate allowance. It's also difficult to ensure consistency or produce estimates on a range of bases.  
  * **Capping/Excluding:** Large losses can be capped at a certain level, with the excess projected separately, or removed entirely from the attritional triangle. The cap should be indexed for inflation.  
  * **Separate Triangles:** Creating distinct triangles for large losses and non-large losses.  
  * **Exposure-Based Methods:** Particularly useful at early stages of development or for one-off events, involving "bottom-up" (policy-by-policy) or "top-down" (overall portfolio assessment) approaches.  
* **Latent Claims:** Types of claims like Asbestos, Pollution, and Health hazards (APH) are particularly challenging. Their emergence pattern often relates to calendar years rather than origin years, rendering traditional chain ladder methods unsuitable.  
  * **Alternative:** Survival ratios (e.g., three-year survival ratio) and exposure-based methods are typically used. Further detail is explored in SA3.

#### **1.1.5 Other Issues and Distortions**

Several other factors can impair the effectiveness of statistical methods by invalidating their underlying assumptions:

* **Changes in Procedures:** Shifts in claims handling, data recording, or reserving philosophies can distort development patterns. Adjustments or reliance on data *after* the change may be necessary.  
* **Market-wide Initiatives:** External events (e.g., natural catastrophes) can trigger industry-wide efforts that impact claims reporting/settlement, requiring careful consideration in reserving.  
* **Developments in Business, Economic, and Legal Environment:** Inflation (court awards vs. price/earnings), changes in policy terms, legislative reforms (e.g., Ogden rate changes in the UK), and changes in competition can all affect claim development.  
* **Underwriting Cycle:** The position in the underwriting cycle can influence claims development patterns, particularly making them longer in soft markets.  
* **Lack of Data:** Insufficient or sparse data is a pervasive problem, often necessitating benchmark factors from industry data or other sources. Judgement is critical when benchmarks differ from the business being analysed (e.g., classes, terms, geography, reserving basis).  
* **Actuarial Judgement:** Given the complexities and potential distortions, actuarial judgement is paramount throughout the reserving process, from selecting methods and making adjustments to assessing the reasonableness of final estimates. Diagnostic tests, benchmarks, and past experience are crucial tools for this.

### **2.0 Main Triangulation Methods in Detail**

Let's now drill down into the mechanics and specific considerations for each of the core triangulation methods.

#### **2.1 Chain Ladder Method (CLM)**

The Chain Ladder Method (also known as the Link Ratio method) is a widely used technique due to its simplicity and applicability across various datasets.

* **Description:** It projects future claim payments or incurred amounts by calculating "link ratios" (or development factors) from historical cumulative claim data. A link ratio for a given development period is the ratio of cumulative claims up to that period compared to the previous period. These ratios are then applied to the most recent diagonal of the triangle to project future values.  
  * **Key Assumptions:**  
    1. **Stable Development Patterns:** The fundamental assumption is that historical claims development patterns will continue unchanged into the future for all cohorts.  
    2. **Homogeneous Data:** The data should be homogeneous, meaning claims should share similar reporting, settlement, and inflationary characteristics across origin periods.  
    3. **Credible Volume of Data:** Sufficient data volume is needed to ensure the credibility of the estimated link ratios.  
* **Analysis and Selection of Link Ratios:** Actuaries must carefully analyse historical link ratios, looking for trends (e.g., calendar year effects), unusual values, or cohorts that deviate. Understanding the underlying reasons for such anomalies (e.g., late reported losses, processing errors) is essential to decide whether to include them in the projection. Particular care is needed in the tail of the triangle, where a single unusual link ratio can disproportionately impact estimates.  
* **Paid vs. Incurred Modelling:** CLM can be applied to both paid claims data and incurred claims data (paid claims plus case estimates).  
  * **Paid CLM:** Uses actual cash payments. More objective, less influenced by reserving philosophy. Can be volatile for some classes.  
  * **Incurred CLM:** Uses reported incurred amounts (paid \+ case estimates). Reflects changes in case reserving practices, but also subject to assessor prudence.  
  * **Judgement:** It's often useful to perform both analyses and compare results to gain insights and select the most appropriate approach.  
* **Issues Arising with CLM:**  
  * **Unusually Heavy/Light Experience:** If an origin year has unusually high or low claims experience early in its development, simply applying development factors can lead to over or underestimation of the ultimate reserve.  
  * **Subrogation and Recoveries:** If triangles are constructed net of recoveries (e.g., salvage, subrogation), link ratios might fall below one, which needs careful consideration in business normally showing increasing cumulative patterns. Separate projection of recoveries is often recommended.  
  * **Pure IBNR:** As noted earlier, if claims are grouped by reporting year, CLM will *not* project pure IBNR, requiring a separate estimate.  
* **Strengths of CLM:**  
  * **Wide Applicability:** Can be applied to a diverse range of data, provided it can be arranged into a development triangle.  
  * **Simplicity:** Relatively easy to understand and implement.  
  * **Provides a Base:** Often serves as a starting point for more complex models.  
* **Weaknesses of CLM:**  
  * **Sensitivity to Distortions:** Highly susceptible to changes in underlying patterns (e.g., inflation, changes in business mix, claims handling).  
  * **Limited Information for Immature Years:** For very immature years, if claims activity is minimal, it might project a zero ultimate, which is unrealistic.  
  * **Does Not Quantify Uncertainty:** Traditionally produces a single point estimate, not a distribution of outcomes or confidence intervals. Stochastic extensions (like bootstrapping the ODP model) address this.  
* **Methods Related to CLM:**  
  * **Inflation-Adjusted Chain Ladder Method:** Explicitly allows for future claims inflation by deflating historical data, projecting in real terms, and then reinflating. Choice of index is crucial.  
  * **Berquist-Sherman Method:** Adjusts historical development data for changes in claim settlement speed or case reserving adequacy to ensure consistency with current practices. This involves restating paid or incurred claims data.

#### **2.2 Expected Loss Ratio Method**

This is a simpler, exposure-based method that can be used independently or as a component of the Bornhuetter-Ferguson method.

* **Description:** The method estimates ultimate claims by applying a chosen historical or expected loss ratio to the earned premiums of an origin period.  
* **When to Use:** Particularly useful when historical claims data is sparse, unreliable, or non-existent (e.g., for a new line of business). It also serves as a quick cross-check for other methods.  
* **Issues:**  
  * **Ignores Emerging Experience:** A major limitation is its reliance on a pre-determined loss ratio without incorporating any actual claims experience for the origin period to date.  
  * **Subjectivity:** The underlying assumptions, especially the selected loss ratio, can be subjective, potentially based on "soft information" like an underwriter's opinion, requiring careful validation.

#### **2.3 Bornhuetter-Ferguson (BF) Method**

The Bornhuetter-Ferguson method effectively blends the stability of the loss ratio method with the responsiveness of the chain ladder method.

* **Description:** It is considered a "credibility estimate," taking a weighted average between an expected level of claims (from the loss ratio method) and a projection of ultimate claims based on actual experience to date (from the chain ladder method). It assumes that claims yet to emerge will follow an expected pattern (often a complement of the chain ladder development pattern), while claims already emerged are taken at their actual value.  
  * **Formula (for estimated ultimate claim amount):** `Ultimate Claims (BF) = Current Incurred/Paid Claims (C) + Expected Ultimate Claims (LR) * (1 - % Developed (p))` Where `p` is the proportion of claims currently incurred/paid, and `LR` is the initial expected ultimate claim amount (often derived from a loss ratio).  
* **When to Use:**  
  * **Immature Data:** Most valuable when claims data for a particular cohort is very sparse or at an early stage of development. In such cases, a pure chain ladder might produce extreme (e.g., zero or excessively high) results based on limited experience.  
  * **Long-Tailed Portfolios:** Useful for lines with very slow development (e.g., liability excess of loss reinsurance) where data remains immature for many years.  
  * **Blending Experience and Exposure:** Provides a robust approach when a blend of actual experience and an independent, exposure-based estimate is appropriate.  
* **Strengths of BF:**  
  * **Stability for Immature Years:** Less dependent on the actual claims experience to date than CLM for early development, as it relies partly on a prior estimate. This helps to avoid projecting a zero ultimate where no claims have yet emerged.  
  * **Combines Advantages:** Incorporates both observed development and an initial expectation of ultimate losses.  
* **Weaknesses of BF:**  
  * **Reliance on Prior Estimate:** The result can be heavily dependent on the "prior estimate" (the initial expected ultimate claim amount), especially in early development stages.  
  * **Difficulty in Obtaining Prior Estimate:** Gathering reliable information for this prior estimate can be challenging.  
  * **Negative Tail Development:** If data develops with a negative tail, the assumed percentage developed might be unsuitable as a weight, potentially requiring different weighting or reliance on paid development.

#### **2.4 Average Cost Per Claim (ACPC) Method**

The ACPC method is a family of approaches that separates claims into frequency (number of claims) and severity (average cost per claim) components.

* **Description:** It calculates the ultimate claims by multiplying the projected ultimate number of claims by the projected ultimate average claim size. It is flexible, allowing variations in how frequency and severity are defined (e.g., incurred, reported, or settled claims, origin year, development year, or calendar year averages).  
* **Interplay with Other Methods:** ACPC can incorporate CLM or BF methods to project ultimate claim numbers for recent years. Conversely, an ACPC ultimate can serve as a prior for the BF method.  
* **When to Use:** Useful when aggregate modelling methods cannot adequately capture specific data features. For example, it can distinguish whether inflation is driven by an increase in claim frequency or average claim size, which aggregate models cannot.  
* **Issues Arising with ACPC:**  
  * **Claim Numbers:** Requires careful consideration of claim definitions (e.g., reported claims, nil claims) and consistency over time.  
  * **Technical Considerations:**  
    * **Large Claims:** As with other methods, large claims can distort the analysis. They can be excluded or capped, with a separate model for the large losses.  
    * **Payment Patterns:** Influenced by acceleration or slowing of payments/settlements, requiring adjustments similar to Berquist-Sherman.  
    * **Benchmarks:** Average claim sizes can be benchmarked against industry data.  
    * **Cross-Subsidies:** Using a trended average claim amount can introduce cross-subsidies between origin years.  
* **Strengths of ACPC:**  
  * **Clarity:** Easy to understand and communicate, providing insights into both claim numbers and amounts.  
  * **Data Availability:** Data for direct business is generally available.  
  * **Flexibility:** Can be combined with other projection techniques (CLM, BF).  
  * **Volatile Data:** Helpful for explaining volatile data/results, especially for small lines of business or reinsurance.  
  * **Resilience to Protocol Changes:** Can be applied to settled claims even if reserving protocols have changed.  
  * **Latent Claims:** Useful for estimating latent claims by making explicit assumptions about average claim size, long-term inflation, and expected claim numbers.  
  * **Targeted Adjustments:** Enables more accurate adjustments where impacts are specific to frequency or severity.

### **3.0 Comparison of Results from Different Methods**

It is **always advisable** to use more than one reserving method, if data permits, to project reserves. This often involves a combination of paid and incurred methods, or different triangulation techniques (CLM, BF, ACPC).

* **Divergence Analysis:** When results from different methods diverge, the actuary must thoroughly investigate the reasons:  
  * **Modelling Properties:** What specific properties of the claims experience is each method capturing or missing?  
  * **Driving Data Points:** Are specific data points or outliers causing the divergence?  
  * **Sensible Trends:** Are the projected trends across cohorts sensible for each method?  
  * **Consistency Checks:** Look for inconsistencies, e.g., paid projections consistently higher than incurred, or an incurred projection yielding an ultimate less than paid-to-date (unless recoveries are the reason).  
* **Final Selection:** The final reserve estimate may be the one that best reflects the underlying behaviour of claims, or it could be a weighted average of several methods (e.g., the Benktander method).

### **4.0 Recoveries: Gross vs. Net Considerations**

Most reserving discussions focus on gross reserves, but for solvency and published accounts, reserves must often be presented net of recoveries. This introduces additional complexity to triangulation methods.

#### **4.1 Types of Recoveries**

Recoveries generally fall into two categories:

* **Salvage and Subrogation:** Recoveries from selling damaged property for scrap (salvage) or from other parties legally responsible for a claim (subrogation).  
* **Reinsurance:** Recoveries from reinsurance arrangements.

#### **4.2 Salvage and Subrogation Recoveries**

It is crucial to understand if the data provided is gross or net of salvage and subrogation recoveries.

* **Separate Projection Recommended:** Wherever possible, these recoveries should be projected separately from gross amounts, as their payment patterns differ from gross claims. Failing to do so can lead to over- or under-reserving.  
* **Data Issues:** If case estimates for recoveries are not maintained, payment-based methods must be used. Incurred analyses may be challenging as reported incurred data won't accurately reflect recoveries without explicit case estimates for them.

#### **4.3 Reinsurance Recoveries**

Reinsurance recoveries can be a significant proportion of gross reserves, especially for non-proportional (e.g., Excess of Loss, XL) covers.

* **Gross vs. Net Triangles:** While it's possible to analyse net-of-reinsurance triangles, it is generally recommended to calculate ceded reserves separately and subtract them from gross reserves to derive net reserves.  
* **Reasons for Separate Calculation:**  
  * **Program Changes:** Reinsurance programs can change year-to-year, which has a more severe and harder-to-model impact on net data than on gross data.  
  * **Consistency:** For programs representing a small proportion of reserves, a direct net analysis might yield results inconsistent with gross reserves.  
* **Dealing with Sparse Reinsurance Data:** Reinsurance business often has sparse data due to its low frequency/high severity nature or specific contract terms.  
  * **Bornhuetter-Ferguson:** The BF method can be particularly useful where there are many zeroes in the triangle, or for less developed years, as reinsurance development patterns are often longer than direct business.  
  * **Specific Application to Large Losses:** For large losses where the threshold is below the reinsurance retention, the reinsurance program can be applied specifically to each large loss, factoring in IBNER and capital modelling insights.

### **5.0 Triangulation Methods in the Larger Context of Reserving**

Triangulation methods are foundational, but they do not operate in a vacuum. Their application is deeply intertwined with other aspects of reserving and capital modelling.

#### **5.1 Accounting and Regulatory Basis**

The chosen reserving basis (which dictates whether to discount, hold explicit risk margins, or aim for prudence) directly influences the interpretation and application of triangulation methods. For example, Solvency II and IFRS 17 explicitly require discounting of reserves and the calculation of a best estimate plus a risk margin. Triangulation methods often provide the "best estimate" component, with other techniques layering on the risk margin or range.

#### **5.2 Uncertainty and Stochastic Reserving**

Traditional triangulation methods (CLM, BF, ACPC) typically produce a single point estimate. However, the real reserve required will almost certainly differ from this estimate due to inherent uncertainties. This is where stochastic reserving processes become vital.

* **Uses of Stochastic Reserving:** To assess the likely error in a best estimate, provide confidence intervals, quantify volatility for capital models, assess reserve adequacy, compare estimates, monitor performance, and allocate capital.  
* **Sources of Uncertainty:**  
  * **Process Uncertainty:** Inherent randomness in future claims (amount, frequency, timing), changes in business mix, or demand surges.  
  * **Parameter Uncertainty:** Uncertainty arising from estimating the parameters used in the model, often due to poor quality, inconsistent, or incomplete data. Small changes in numbers can significantly alter outcomes for stochastic models.  
  * **Model Uncertainty (Specification Error):** Arises because models are simplifications of complex underlying systems, and the chosen model may not fully reflect reality (e.g., CLM not allowing for calendar year effects). Stochastic methods can only reflect variability in historical data, potentially underestimating true variability.  
* **Stochastic Methods Building on Triangulations:**  
  * **Mack's Model:** Similar framework to CLM, producing an estimate of variance but not a precise distribution. Key assumptions include stable run-off patterns, independent incremental claim amounts, and variance proportional to the mean.  
  * **Over-Dispersed Poisson (ODP) Model & Bootstrapping:** ODP is a GLM applied to claims triangles where the mean equals the deterministic CLM estimate. Bootstrapping involves repeatedly sampling with replacement from historical residuals (actual minus fitted values) to create pseudo-datasets, refitting the model, and building a distribution of reserve outcomes. This captures both parameter and process uncertainty. Bootstrapping is a generic technique, but commonly applied to ODP for reserving.  
  * **Bayesian Methods:** Assume model parameters conform to a prior distribution, which is combined with data (likelihood) to produce a posterior distribution, offering a complete predictive distribution of the ultimate reserve. The choice of prior is subjective and can heavily influence the posterior.  
* **Communication of Uncertainty:** It's vital to clearly define and communicate the 'best estimate' (typically the mean of all possible outcomes), and the range of possible outcomes to stakeholders. Actuaries use ranges (e.g., range of best estimates, range of plausible outcomes), scenario tests (for extreme events), and alternative assumptions (for parameter uncertainty) to quantify and communicate this.

#### **5.3 Data Requirements and Quality**

The effectiveness of triangulation methods (and indeed any reserving method) is profoundly impacted by data quality.

* **Types of Data:** Policy information, premium data, and claim information (dates of reporting/occurrence, amounts, claim status) are essential.  
* **Homogeneity:** Data must be sufficiently detailed to be split into homogeneous groups.  
* **Impact of Inadequate Data:** Incorrect data leads to distorted projections, inaccurate reserves, flawed profitability assessments, and potential tax errors.  
* **External Data:** Industry-wide data (e.g., from ABI, Lloyd's) can provide benchmarks, especially for small or new insurers, but careful consideration of heterogeneity is needed. Reinsurers can also be a source of data.

#### **5.4 Assessment of Reserving Results (Chapter 17 Link)**

After applying triangulation methods, actuaries must assess the reasonableness of the results.

* **Diagnostics:** Various measures are used to interpret data and results, test methodologies, and verify assumptions. Examples include changes in loss ratios (paid, incurred, ultimate), IBNR to premium/case estimate ratios, average outstanding case estimates, and reinsurance to gross ratios.  
* **Analysis of Emerging Experience:** Comparing actual experience to expected outcomes (e.g., "Actual versus Expected" analysis) is critical to decide if assumptions or methodology need updating.  
* **Professional Judgement:** The final selection of results relies heavily on actuarial judgement, experience, and collaboration with management and underwriting/claims teams. Considerations like materiality, purpose of the exercise, and regulatory requirements guide decisions on adjustments.

In conclusion, dear student, triangulation methods—Chain Ladder, Bornhuetter-Ferguson, and Average Cost Per Claim—are indispensable tools in your SP7 arsenal. They provide the quantitative backbone for reserving. However, their effective application requires keen actuarial judgement, a deep understanding of data quality and potential distortions, and a clear awareness of their limitations, especially when quantifying the complex uncertainties inherent in general insurance liabilities. Always remember to validate your outputs, communicate clearly, and stay abreast of evolving best practices and regulatory requirements. Keep practising those problem-solving skills\!

