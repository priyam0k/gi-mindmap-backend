**Types of Reserves: A Foundational Overview**

Firstly, let's contextualise IBNR. In general insurance, insurers set aside funds, known as **technical reserves (or insurance reserves)**, to meet their future obligations to policyholders. These are typically the largest liabilities on an insurer's balance sheet.

These technical reserves can be broadly categorised based on the timing of the underlying events:

1. **Liabilities for Past Events:** These relate to accidents or losses that occurred *before or at the accounting date*. This category primarily encompasses **outstanding claims reserves**.  
2. **Liabilities for Future Events:** These relate to future insurance cover from policies for which premiums have already been received, essentially covering **unexpired risks**. This leads to the **Unearned Premium Reserve (UPR)** and, if applicable, the **Additional Unexpired Risk Reserve (AURR)**.

Our focus today, IBNR, falls squarely within the 'liabilities for past events' category, specifically as a component of the outstanding claims reserve.

---

### **1\. Incurred But Not Reported (IBNR): Definition and Components**

The **outstanding claims reserve (OCR)** is the primary component of technical reserves related to past events. While sometimes presented as a total figure, it can be split into several detailed components:

* **(a) Reserve for outstanding reported claims:** This is the estimated reserve needed to settle claims that the company *already knows about* at the accounting date. These are claims that have occurred and been reported, but not yet fully settled.  
* **(b) Reserve for Incurred But Not Reported (IBNR) claims:** This is the reserve needed to cover claim payments for incidents which have *happened*, but have *not been reported* to the insurance company on or before the accounting date.  
* **(c) Reserve for Incurred But Not Enough Reported (IBNER):** This reserve is needed to cover expected increases (or decreases) in estimates for claims *already reported*. This means that while the claim is known, its full extent or ultimate cost is still developing.  
* **(d) Reserve for re-opened claims:** This is an additional reserve for claims that the insurer treated as fully settled but might require further payments later.  
* **(e) Reserve for claims handling expenses:** This covers additional expenses (e.g., legal fees) incurred in settling claims across all the above categories.

It's crucial to note that even if an insurer doesn't explicitly show reserves split into all these categories, they must still hold reserves to cover all these items implicitly within broader categories (e.g., IBNER might be included in IBNR, or re-opened claims within outstanding reported claims).

---

### **2\. Reasons for IBNR: Delays in the Claims Process**

The very existence of IBNR is fundamentally driven by delays in the claims lifecycle. There are two main types of delays:

* **Reporting Delays:** This is the time between when an event occurs and when the insurance company is notified. For certain industrial diseases (e.g., asbestos-related diseases, industrial deafness), it can take many years for the condition to emerge and be reported, leading to **considerable reporting delays**. This is the direct cause of 'pure IBNR'.  
* **Settlement Delays:** This refers to the time it takes to fully settle a claim once it has been reported. While not directly causing IBNR, it contributes to the overall need for outstanding claims reserves.

The impact of these delays is significantly higher for **long-tailed classes of business**, such as employers' liability, product liability, and professional indemnity, where claims may not emerge for many years. Conversely, **short-tailed classes** like household contents typically have much smaller IBNR due to quicker reporting.

---

### **3\. Distinguishing IBNR from IBNER**

As a budding SP7 actuary, it's vital to clearly differentiate IBNR from IBNER, as they address distinct components of unknown liabilities:

* **IBNR (Incurred But Not Reported):** Focuses on claims that have *occurred* but are *completely unknown* to the insurer at the valuation date. These claims have not yet entered the insurer's system.  
* **IBNER (Incurred But Not Enough Reported/Reserved):** Deals with claims that are *already known* (reported) but for which the initial estimates are expected to be revised (increased or decreased) as more information becomes available or as the claim develops. This is essentially a correction to initial case estimates.

Some general insurance practitioners might use the terms "reported claims" and "incurred claims" interchangeably, and "incurred claims" themselves can have different definitions (e.g., paid plus reported outstanding, or paid plus all outstanding including IBNR). As an actuary, you must *always clarify the definition* being used for "incurred claims" to avoid misinterpretation.

---

### **4\. Estimation Methods for IBNR**

Estimating outstanding claims, including IBNR, is a core actuarial task.

#### **4.1 General Approaches**

Insurers typically use a combination of two main approaches:

* **Case-by-case estimation:** This involves setting an individual estimate for each *known* outstanding claim. While suitable for reported claims, it *cannot* be used for IBNR because, by definition, these claims are unknown to the insurer.  
* **Statistical methods:** These methods use historical claims data patterns to project future development of claim totals. These are **more useful for IBNR estimation**, especially for classes with many claims and stable patterns (e.g., private motor). Actuarial input is more likely to be used in statistical estimation.

#### **4.2 Specific Statistical Techniques (and their considerations)**

While the SP7 syllabus assumes prior knowledge of the mechanics, it focuses on the underlying principles and practical issues. Key methods include:

* **Chain Ladder Method:** This traditional method relies on historical development patterns (link ratios) to project claims to ultimate. When using accident year cohorts (which group claims by the year the event occurred), the chain ladder method implicitly includes IBNR and IBNER. However, if using reporting year cohorts, pure IBNR will *not* be captured and needs separate estimation.  
* **Bornhuetter-Ferguson (BF) Method:** This is a credibility-weighted approach combining an initial expected loss ratio (a 'prior' estimate, often based on pricing assumptions) with observed claims development. It is particularly useful when data for recent cohorts is sparse, as it places more weight on the *a priori* expectation when experience is limited. It can be applied to both paid and incurred claims data.  
* **Average Cost Per Claim (ACPC) Method:** This method estimates ultimate claims by projecting both the ultimate number of claims and the average cost per claim. It provides insight into frequency and severity components, which can be beneficial for understanding volatile data.

#### **4.3 Challenges and Specific Considerations in IBNR Estimation**

* **Latent Claims:** These are claims arising from perils unforeseen when the policy was written, or claims that become known many years after the cause of loss (e.g., asbestos, pollution, health hazards). For such claims, traditional triangulation methods are often *not appropriate* due to their unpredictable emergence patterns and long reporting delays. They may exhibit a 'calendar year' development effect, influenced by factors like media publicity. Specific actuarial judgement and potentially different modelling approaches are required for these.  
* **Sparse or Inadequate Data:** For new lines of business, new territories, or high-layer excess of loss reinsurance, historical data may be limited or non-existent. In such cases, actuaries may need to rely on:  
  * Market benchmarks or industry data.  
  * Benchmarks from similar books of business.  
  * Qualitative methods and expert judgement.  
  * Simple ratio methods for IBNR, or delay tables.  
* **Large Losses/Catastrophes:** Individual large claims or catastrophes can distort development patterns. It is common practice to separate these from attritional losses and project them individually or with different methods, ensuring the IBNR calculation is not skewed.  
* **Data Quality and Consistency:** Changes in claims recording procedures, claims handling philosophy (e.g., initial case estimate practices), or reliance on third-party claims handlers can introduce inconsistencies and distortions in historical data, impacting IBNR projections. The actuary must investigate these and make appropriate adjustments.

---

### **5\. Uncertainty and Communication of IBNR**

One of the most critical aspects highlighted in the SP7 syllabus is the **uncertainty surrounding reserve estimates**, including IBNR.

* **Inherent Uncertainty:** The actual ultimate claims amount will almost certainly differ from our best estimate. This is due to various sources of uncertainty:  
  * **Process Uncertainty:** Random fluctuations in claims occurrence, severity, and timing; changes in business mix or external environment (e.g., legal, economic, social factors).  
  * **Parameter Uncertainty:** Errors in the assumptions used to parameterise the models, often stemming from poor data quality, inconsistency, or incompleteness. This includes uncertainty in inflation rates.  
  * **Model Uncertainty (Specification Error):** Arises from the choice or specification of the model itself, as models are simplifications of complex reality and may not capture all underlying features.  
* **Quantifying Uncertainty:** Stochastic reserving methods are used to assess this uncertainty and provide confidence intervals around the best estimate. These methods are crucial inputs for capital models. Approaches include:  
  * **Analytic methods:** Such as Mack's model and Over-Dispersed Poisson (ODP).  
  * **Simulation-based methods:** Like bootstrapping, which involves resampling from historical data to generate multiple pseudo-data sets and derive a distribution of reserves.  
  * **Scenario tests:** Involving setting alternative assumptions or stress tests to explore a range of plausible outcomes.  
* **Communication:** Communicating the outputs of a stochastic reserving exercise, including the limitations, assumptions, and materiality of judgements, is a key skill. The actuary must define terms clearly (e.g., "best estimate") and explain the extent to which the reserve ranges reflect various sources of uncertainty.

---

### **6\. IBNR in Different Reserving Purposes and Contexts**

The purpose of the reserving exercise heavily influences the choice of methodology and assumptions, including for IBNR:

* **Published Accounts:** May require reserves based on GAAP (Generally Accepted Accounting Principles) or IFRS 17\. Under IFRS 17 (effective 1 January 2023), reserves are discounted and include explicit risk margins, and require detailed disclosure of significant judgements.  
* **Solvency Supervision:** For regulatory reporting (e.g., Solvency II), reserves are typically discounted best estimates plus a risk margin. Solvency II requires claims and premium provisions to be calculated separately, with the former covering events already occurred (thus including IBNR). Regulators are particularly interested in the run-off risk and may require explicit disclosure of variability.  
* **Internal Management Accounts:** Often use best estimate to provide a realistic view of financial condition. A detailed breakdown of liabilities, including IBNR, can aid management decisions.  
* **Sale or Purchase of an Insurer (M\&A):** The valuation of liabilities, including IBNR, is critical. The purchaser may take a more pessimistic view of reserves than the vendor.  
* **Tax Purposes:** Tax authorities have specific rules on reserve deductibility, and over-reserving might be penalised as it delays profit emergence and tax payment. Justification for IBNR, especially for volatile classes like latent claims, is often required.  
* **Commutation:** Involves negotiating a lump sum payment to extinguish future liabilities for a block of business. Accurate IBNR estimation is critical for fair negotiation.

---

### **7\. Data Requirements and Reinsurance Impact on IBNR**

#### **7.1 Data for IBNR Estimation**

Reliable data is the backbone of any reserving exercise. For IBNR, specific data requirements include:

* **Dates:** Date of reporting and date of occurrence for each claim are crucial for determining IBNR extent.  
* **Claim Counts:** Information on reported claims, reopened claims, and closed claims is needed for methods like ACPC.  
* **Premium Data:** Earned premiums for accident year cohorts, or written premiums for underwriting year cohorts, are used in loss ratio calculations for methods like Bornhuetter-Ferguson.  
* **Homogeneity:** Data should be grouped into sufficiently homogeneous groups (e.g., by class of business, claim development patterns, size of loss, legal environment) to avoid distortions in IBNR projections.  
* **Detail:** Maintaining detailed individual loss information (gross of reinsurance, from the ground up) allows for more detailed analyses and adjustments for IBNR.

#### **7.2 Reinsurance and IBNR**

Reinsurance significantly impacts IBNR estimation, especially for non-proportional covers:

* **Gross vs. Net:** Reserves for solvency and published accounts are presented *net of recoveries*. However, it is generally recommended to calculate ceded reserves separately and subtract them from gross reserves, rather than using net-of-reinsurance triangles directly.  
* **Complexity of Non-Proportional Reinsurance:** For excess of loss (XL) cover, the estimation of net IBNR is more complex because reinsurance programs can change year-to-year and have a more severe impact on net data compared to gross. IBNR may be difficult to allocate to individual risks, especially for large London Market contracts.  
* **Reinsurance Recovery Delays/Defaults:** There's always a delay between gross claim payment and reinsurance recovery. Allowances for bad debt and potential irrecoverability of reinsurance amounts are necessary.  
* **Specific Modelling:** For large losses that are reinsured, the reinsurance program can be applied specifically to each large loss, factoring in IBNER as necessary. Stochastic modelling for capital purposes may also inform IBNR allowances for large losses.

---

### **8\. Actuarial Judgement and SP7 Implications**

I must stress that reserving, and IBNR estimation in particular, is not a mechanical process. It demands significant **actuarial judgement**:

* **Understanding Underlying Reasons:** Always seek to understand the reasons behind unusual data patterns or diagnostics, as these can significantly impact IBNR projections.  
* **Addressing Data Issues:** Be proactive in identifying and dealing with data errors, inconsistencies, and omissions, which are common and directly affect IBNR accuracy.  
* **Materiality:** Consider the materiality of losses and whether the projected IBNR is sufficient, especially for older years or specific large claims.  
* **Continuous Review:** Reserving is an iterative process. Regularly review emerging experience against expected outcomes and adjust IBNR assumptions as needed.  
* **Communication:** Clearly and effectively communicate the IBNR estimate, its underlying assumptions, the inherent uncertainties, and the limitations of the analysis to all stakeholders. Define your terms\!.

In essence, IBNR is a critical accounting provision reflecting future claim payments for past events that are currently unknown to the insurer. Its estimation relies heavily on statistical techniques and requires meticulous data analysis, careful consideration of various uncertainties (process, parameter, model), and robust actuarial judgment to ensure it adequately reflects the insurer's true obligations. Master this, and you're well on your way to acing SP7\!

