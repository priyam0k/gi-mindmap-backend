### **Section 1: Introduction to Technical Reserves**

As a General Insurance Actuary, one of your primary responsibilities is to meticulously value the insurer's liabilities. These liabilities are broadly categorized into **Technical Reserves** (or **Insurance Reserves**). These are the amounts set aside for expected claim payments to policyholders, along with their related expenses. Understanding their composition is fundamental to assessing an insurer's financial health and solvency.

Technical reserves are typically split into two main categories based on the timing of the events they cover:

* **Past Events:** Liabilities (claims plus expenses) related to accidents or losses that occurred *prior* to the accounting date.  
* **Future Events:** Liabilities (claims plus expenses) related to future insurance coverage from policies for which premiums have already been received, covering the unexpired exposure.

Our focus today, **Outstanding Reported Claims**, falls squarely into the 'Past Events' category, representing a significant portion of the total technical reserves.

---

### **Section 2: Outstanding Reported Claims – Definition and Components**

The **Outstanding Claims Reserve (OCR)**, also referred to as the Outstanding Claims Provision, is the first of the two main components of the technical reserves relating to past events. It may be presented as a single total figure or further subdivided into several components.

The most direct component is the **Reserve for Outstanding Reported Claims**. This is the estimated reserve specifically needed to settle claims that the company is *already aware of* at the accounting date.

However, the broader concept of Outstanding Claims Reserve typically includes other elements related to past events that have not yet been fully settled or realized:

* **Incurred But Not Reported (IBNR) Claims Reserve:** This reserve is crucial for claims where the incident has occurred, but the insurer has *not yet been notified* by the accounting date.  
* **Incurred But Not Enough Reported (IBNER) Reserve:** This covers expected increases (or decreases) in estimates for claims that have *already been reported*. It reflects the development of known claims as more information becomes available.  
* **Re-opened Claims Reserve:** This allows for claims that the insurer previously treated as fully settled but which may require further payments in the future. Insurers vary significantly in their "claim closure" definitions, impacting the need for this reserve.  
* **Claims Handling Expenses Reserve:** Costs incurred in settling claims (e.g., legal fees) for all the above categories may be held separately or implicitly within the claim reserves.

Even if an insurer's accounts only explicitly show "Outstanding Reported Claims" and "IBNR," they should still hold reserves to cover all these underlying items. For instance, the re-opened claims reserve might be part of the outstanding reported claims, and IBNER might be embedded within IBNR.

---

### **Section 3: Estimation Approaches for Outstanding Claims Reserves**

Estimating outstanding claims reserves is inherently uncertain because the exact future payments are unknown. Actuaries use estimates to set aside these liabilities, employing two distinct approaches:

1. **Case Estimates (or Case-by-Case Estimation):** This involves making estimates of the liability for each individual outstanding claim.  
   * **Advantages:** This approach can utilize *all known data* on outstanding claims. Experienced and skilled assessors can weigh qualitative factors influencing the claim amount. It provides greater management control over total claims reserves and picks up new trends more quickly than statistical methods.  
   * **Disadvantages:** Case estimates *cannot* be used for IBNR claims because, by definition, the insurer is not yet aware of them. Assessors may not use consistent inflation rates, and it can be hard to produce estimates on a range of possible bases. It is also resource-intensive. Outsiders without access to individual claim data cannot use this method.  
2. **Statistical Techniques:** These methods are used to estimate the total outstanding payments for the entire portfolio.  
   * **Advantages:** Statistical techniques are more useful for classes of insurance with a *large volume of claims* (e.g., private motor) and where there is *stability in the numbers and amounts of claims*. They are essential for IBNR estimation.  
   * **Disadvantages:** These methods can be distorted by data issues or changes in underlying patterns. They may not fully capture all sources of variability.

In practice, insurers typically use a **combination** of both case estimates and statistical techniques. For instance, case estimates might be used for large, complex claims, while statistical methods are applied to the aggregated data for attritional (smaller, more frequent) claims.

---

### **Section 4: Factors Influencing Estimation and Uncertainty in Outstanding Reported Claims**

The estimation of outstanding reported claims, and the broader technical reserves, is profoundly affected by various factors, leading to inherent uncertainty. This uncertainty is generally greater for long-tail classes of business.

#### **4.1 Claim Characteristics and Delays**

Outstanding reported claims are primarily affected by **settlement delays**. The time it takes for claims to be settled can vary significantly:

* **Short-tail vs. Long-tail:** Property damage claims, for example, are generally settled more quickly ("short-tail") than bodily injury claims, especially in liability classes, which are typically "long-tail" business. Long-tail business means a sizeable proportion of total claim payments take a long time to settle.  
* **Size of Claims:** Large claims inherently take longer to settle than smaller ones.  
* **Legal Environment:** The legal environment can significantly impact claim settlement and development patterns, varying by country.

#### **4.2 Data Quality, Consistency, and Issues**

The quality of claims data is paramount for accurate reserve estimation. Poor data can lead to serious distortions in projections and incorrect reserve values.

* **Sources of Data Error:** These can include wrong claim numbers, wrong policy numbers, incorrect risk details, wrong claim dates, changes in claims handling procedures, incorrect payment dates, wrong claim type, issues with case estimates, processing delays, and inappropriate treatment of large claims or inflation.  
* **Inconsistent Case Reserving:** Changes in claims handling processes, product cover levels, or legislation can lead to inconsistencies in historical case reserving data. A change in case estimate philosophy (e.g., from prudent to realistic) can distort run-off patterns.  
* **Processing Delays:** Alterations in the rate at which claims are processed (e.g., backlogs, clear-outs, staff shortages) can distort claims development patterns.  
* **Data Storage Protocols:** Changes in how claims data is stored (e.g., gross vs. net of reinsurance, inclusion/exclusion of claims handling costs) require adjustments to maintain consistency in historical data.

#### **4.3 Case Estimate Philosophy**

Each company has its own case estimate philosophy and guidelines for claims assessors. Some may require estimates to be as realistic as possible, while others prefer a degree of prudence to avoid future deterioration in the overall reserve. This philosophy directly impacts the reported outstanding claims reserve.

#### **4.4 Large and Exceptional Claims**

Large claims pose a significant challenge because they often exhibit different frequency and severity distributions, and development patterns, compared to attritional claims.

* **Separate Modelling:** It is normal practice to remove large claims from the main development data and project them separately. This is because if left unadjusted, they can distort the experience of the risk group and triangulations.  
* **Definition of "Large":** The definition can be based on a monetary threshold (which may vary by peril and be linked to reinsurance programs) or subjective management decision. This threshold might need to be indexed over time to account for inflation.  
* **Uncertainty:** There can be uncertainty in defining a "large claim" and a lack of data on how such claims will develop. Actuaries may add a loading to reflect an absence of large reported claims.  
* **Impact on Capital:** Large claims analysis is a key driver for capital requirements and reinsurance decisions.

#### **4.5 Reopened Claims**

Claims can be reopened for various reasons, such as the insurer's closure definition or the emergence of further liability. It is important to record the original date of closure to analyze the percentage of claims reopened and the average time from closure to reopening. This impacts the ultimate cost of past events.

#### **4.6 Claims Handling Expenses**

Expenses directly attributable to a particular claim (Allocated Loss Adjustment Expenses \- ALAE) are typically included in claims data and projected implicitly. Unallocated Loss Adjustment Expenses (ULAE) are more general claims management costs. The reserve for these expenses might be held separately or integrated with the main claim reserves.

#### **4.7 Reinsurance Recoveries**

Technical reserves, including outstanding reported claims, are often required to be presented *net of recoveries* for solvency and published accounts. Recoveries can come from salvage and subrogation or reinsurance.

* **Separate Projection:** It is generally recommended to calculate ceded reinsurance reserves separately and subtract them from gross reserves, especially for excess of loss (XL) reinsurance, as reinsurance programs can change and distort net data.  
* **Case Estimates for Recoveries:** Insurers may or may not establish case estimates for salvage and subrogation recoveries. If not, payment-based methods are necessary.  
* **Reinstatement Premiums:** These additional payments to restore reinsurance cover should be recorded, often allocated to the claims that necessitated the reinstatement.

#### **4.8 Allowance for Future Inflation**

All elements of reserves should account for future cost escalation. This allowance can be explicit or implicit, with implicit approaches assuming past inflation patterns continue. Actuaries must consider different inflation types (e.g., price inflation for property, earnings inflation, and court award inflation for liability claims).

#### **4.9 Actuarial Judgement and Communication of Uncertainty**

Reserve figures are estimates, and any work based on them must recognize the underlying uncertainty.

* **Role of Judgement:** Actuarial judgment is essential throughout the reserving process, particularly when data is imperfect, or assumptions change. It is needed to assess the reasonableness of results using diagnostics, benchmarks, and past experience.  
* **Communication:** Communicating the outputs of a stochastic reserving exercise, including limitations, assumptions, and materiality of judgments, is vital. This includes clarifying what is meant by a "best estimate" reserve and the range of possible outcomes.

---

### **Section 5: Outstanding Reported Claims in the Wider Financial Context**

Outstanding Reported Claims do not exist in isolation; their estimation and impact are integral to various financial and regulatory aspects of a general insurer.

#### **5.1 Relationship with Other Reserves**

* **IBNR and IBNER:** As discussed, Outstanding Reported Claims form a triad with IBNR and IBNER to cover all claims originating from past events. Modelling IBNER and pure IBNR separately provides insights into whether changes in reserves are due to new claims or adjustments to existing estimates.  
* **Unexpired Risk Reserve (URR) and Additional Unexpired Risk Reserve (AURR):** While OCRs deal with *past* events, UPR and URR cover liabilities for *future* claim events from policies with unexpired coverage. AURR is set up if the URR (prospective estimate of future claims/expenses) exceeds the UPR (retrospective portion of premium). This indicates unprofitable business on the books.

#### **5.2 Financial Reporting and Solvency**

The calculation of outstanding reported claims is central to an insurer's financial and regulatory reporting.

* **Published Accounts:** These are prepared to inform shareholders and are typically done annually, semi-annually, or quarterly. The basis (IFRS 4, IFRS 17, Solvency II, UK GAAP, etc.) influences whether a "going concern" basis, "true and fair view," "best estimate," or discounted basis is used.  
* **Solvency Supervision Accounts:** These are for local regulators, demonstrating the company's ability to meet policyholder obligations. Under Solvency II, technical provisions (including outstanding reported claims) are a discounted best estimate *plus a risk margin*.  
* **Internal Management Accounts, Business Plans, and Budgets:** For these, a "best estimate" basis is generally preferred to provide a realistic financial view, often supplemented with sensitivity analyses.  
* **Tax Purposes:** Reserves for tax purposes may differ from published accounts due to specific tax regulations in the relevant country. Tax authorities may scrutinize over-reserving.  
* **Sale or Purchase / Transfer of Liabilities:** In M\&A or portfolio transfers, the valuation of liabilities, including outstanding reported claims, is critical. The purchaser often takes a more prudent (pessimistic) view than the vendor. Local regulations also play a significant role.

#### **5.3 Relationship with Free Reserves and Solvency Margin**

**Free Reserves** (also known as free assets, solvency margin, shareholders' funds, or capital employed) represent the excess of assets over technical liabilities.

* **Safety Margin:** The solvency margin acts as a safety buffer against uncertainty in future claim costs and asset values. If claims exceed reserves, free reserves are used to cover the shortfall.  
* **Capital Requirements:** The amount of capital held is subject to minimum regulatory requirements. Classes with greater uncertainty and variability in future claims, such as long-tail liability business, generally require larger capital. This highlights the direct link between the accuracy and uncertainty of outstanding reported claims and an insurer's capital needs.

---

In summary, the **Outstanding Reported Claims** reserve is not just a line item on a balance sheet; it's a dynamic, estimated quantity central to a general insurer's operations. Its accuracy profoundly impacts financial reporting, solvency, capital adequacy, and strategic decision-making. As an SP7 actuary, your ability to understand its components, the complexities of its estimation, the various factors influencing its uncertainty, and its interconnectedness with other financial elements will be paramount to your success. Keep honing that actuarial judgment, and you'll navigate these complexities with confidence\!

