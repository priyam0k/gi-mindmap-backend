### **Types of Reserves within the Larger Context of Reserving**

Reserving is a core activity for general insurance actuaries, with its primary focus being to determine a point estimate of the best estimate reserves. However, it is crucial to communicate to the users of actuarial work the inherent uncertainties surrounding these best estimates, often using sophisticated methods like stochastic reserving techniques. The ultimate goal is to provide actionable information that supports the effective management and strategic direction of the company \[IAI\_SA3-Syllabus-2023\_Final, P.2\].

The choice of reserving methodology and assumptions heavily depends on the *purpose* for which the reserves are required. This leads directly to the various types of reserves an insurer may hold.

#### **1\. Purposes for Calculating Reserves**

A general insurer needs to estimate its liabilities for a variety of purposes, each potentially requiring a different reserving basis and set of assumptions:

* **Published Accounts:** These are prepared to provide information to shareholders, typically on a going concern basis, aiming for a true and fair view of the financial position. The basis may vary depending on the applicable accounting standards (e.g., IFRS 4, IFRS 17, UK GAAP, Solvency II).  
* **Solvency Supervision / Statutory Returns:** These accounts are required to demonstrate to supervisory authorities that the company can meet its obligations to policyholders. Under Solvency II, technical provisions comprise a best estimate plus a risk margin, and are required to be discounted. Examples of such reports include quarterly solvency margin reports and annual accounting and statutory returns. These often involve specific Quantitative Report Templates (QRTs) which analyze assets, technical provisions (TPs), other liabilities, premiums, and expenses at company and class-of-business levels.  
* **Internal Management Accounts:** The goal here is to give a realistic view of the company's financial condition to internal decision-makers. These typically use a best estimate basis, but also incorporate sensitivity testing to understand the impact of various scenarios. They may require more detailed, granular data than external reports \[SA3\_Combined\_Notes, P.2\].  
* **Tax Purposes:** Reserves for tax purposes must adhere to the specific tax regulations of the relevant country. Tax authorities may scrutinize over-reserving to avoid lower tax payments.  
* **Valuation for Sale or Purchase:** In a merger and acquisition (M\&A) context, both purchaser and seller will form a view on the adequacy of booked reserves, often resulting in the purchaser taking a more pessimistic or prudent view than the vendor.  
* **Negotiating a Commutation:** Similar to sale or purchase valuations, but with additional considerations such as reinsurance recoveries, the importance of the commutation, and the financial strength of the parties involved.  
* **Transfer of Liabilities:** For transfers between companies (within or outside a group), similar considerations to sale/purchase apply, along with specific country regulations (e.g., ensuring "arm's length" transactions within a group).  
* **Estimating Claims Costs for Premium Rating:** Reserving calculations are an intermediate step in the premium rating process, though this is covered in more detail in Subject SP8.  
* **Testing Adequacy of Case Estimates:** Comparing eventual claim out-turns with earlier estimates (actual versus expected) helps assess the accuracy of previous reserving exercises.

#### **2\. Core Types of Technical Reserves**

Technical reserves, also known as insurance reserves, are amounts set aside in respect of expected claim payments to policyholders, plus related expenses. They represent liabilities on the insurer's balance sheet. These liabilities can be broadly categorized as relating to past events or future events.

##### **2.1. Reserves for Outstanding Claims (Past Events)**

These reserves cover liabilities for accidents or losses from events that have occurred prior to the accounting date. They typically include several components:

* **Reserve for Outstanding Reported Claims:** This is the estimated reserve needed to settle claims that the company is already aware of at the accounting date. It primarily accounts for *settlement delays*.  
* **Reserve for Incurred But Not Reported (IBNR) Claims:** This reserve covers claims for incidents that have happened but have not yet been reported to the insurer by the accounting date. It accounts for *reporting delays*. Individual estimates cannot be used for IBNR, and statistical techniques are more useful for classes with numerous claims and stable numbers/amounts. IBNR may need to be calculated separately when outstanding claims reserves are based on case estimates or reporting year cohorts, or for specific statutory/management reporting needs.  
* **Reserve for Incurred But Not Enough Reported (IBNER):** This reserve covers expected increases (or decreases) in estimates for claims already reported. Such changes can result from either reporting or settlement delays. For direct writers, IBNER is often implicit, but reinsurers may hold it explicitly due to greater uncertainty in original estimates.  
* **Reserve for Re-opened Claims:** This is an additional reserve for claims that were previously treated as fully settled but may require further payments. The cause of re-opening determines whether it's due to reporting or settlement delay.  
* **Reserve for Claims Handling Expenses:** This reserve accounts for additional expenses incurred in settling claims (e.g., legal fees). These can be split into Allocated Loss Adjustment Expenses (ALAE) and Unallocated Loss Adjustment Expenses (ULAE). This reserve can be affected by both reporting and settlement delays.

##### **2.2. Reserves for Unexpired Policies (Future Events)**

These reserves relate to liabilities for future insurance cover from policies for which premiums have already been received but the exposure period extends beyond the accounting date.

* **Unearned Premium Reserves (UPR):** This is a retrospective assessment, holding a portion of premiums proportionate to the unexpired exposure (e.g., half the premium for half the term remaining). It covers claims and expenses for future accounting periods from premiums already received.  
* **Unexpired Risk Reserve (URR):** This is a prospective assessment of the amount needed to cover claims and expenses from the unexpired risks. Under Solvency II (in the UK and other EU countries) and IFRS 17, insurers estimate reserves for unexpired exposures using this prospective approach.  
* **Additional Unexpired Risk Reserve (AURR):** This is the excess of URR over UPR (net of deferred acquisition costs), subject to a minimum of zero. An AURR indicates that the company believes it has been writing business on unprofitable terms. Accounting regulations usually dictate that AURR should be held at an entity level, but companies can choose a different granularity based on internal policy. An AURR is based on known information at the balance sheet date and is not typically required for post-balance sheet events like natural catastrophes.

##### **2.3. Other Technical Reserves**

Beyond claims and unexpired policy reserves, other technical reserves may be held:

* **Claims Equalisation Reserve:** This reserve is used to smooth year-to-year profits from volatile insurance business. In profitable years, money is transferred in; in unprofitable years, it is transferred out, reducing profit volatility. Some countries allow transfers to these reserves to be tax-deductible.  
* **Catastrophe Reserve:** Similar to claims equalisation reserves, these are held to mitigate the impact of large, infrequent catastrophic events. Transfers to these reserves might also be allowable against taxable profit in some jurisdictions.

#### **3\. Relationship to the Balance Sheet: Free Reserves**

The **Free Reserves** (also known as free assets, solvency margin, shareholders’ funds, or capital employed) represent the excess of an insurer’s assets over its technical and other liabilities. The size of these free reserves is a critical determinant of several aspects of the insurer's operations, including:

* The amount of business the company can reasonably write and the size of risks undertaken.  
* The amount of risk within its investment strategy, allowing for greater investment freedom with higher free reserves.  
* The need for reinsurance.  
* The scope for competitive pricing.

#### **4\. Key Considerations in Reserving and Communication**

Reserving is not an exact science; different actuaries might arrive at different best estimates due to inherent judgment.

* **Best Estimate Definition:** A "best estimate" reserve is typically understood as the expected value (mean) of the outstanding liabilities, accounting for model, parameter, and process uncertainty. It should not contain explicit margins.  
* **Uncertainty and Communication:** It is no longer sufficient to provide single point estimates without gauging the size of prediction errors. Sources of uncertainty include:  
  * **Process Uncertainty:** Inherent randomness in claims experience (e.g., amount, frequency, timing of individual claims).  
  * **Parameter Uncertainty:** Uncertainty arising from the estimation of model parameters due to data limitations (e.g., poor quality, inconsistency, incompleteness, non-existence).  
  * **Model Uncertainty (Specification Error):** Arises because actuarial models are simplifications of complex underlying systems and may not fully reflect all features (e.g., chain ladder not allowing for calendar year effects). Actuaries must communicate the outputs of reserving exercises, including limitations, assumptions, and materiality of judgments. This often involves providing ranges of possible outcomes using:  
  * **Stochastic Models:** Quantify uncertainty by modeling the claims run-off and its variations, providing confidence intervals and distributions of possible outcomes.  
  * **Scenario Tests:** Explore the impact of plausible adverse or favorable events (e.g., latent claims, reinsurer defaults, changes in inflation) on reserves.  
  * **Alternative Sets of Assumptions:** Using different reasonable assumptions to derive a range of best estimates or plausible outcomes. The communication should clearly define the type of range (e.g., range of best estimates, range of possible outcomes, range of reasonable outcomes) and the elements included in the reserves (e.g., gross/net of reinsurance, ALAE/ULAE, salvage/subrogation).  
* **Discounting:** Under Solvency II and IFRS 17, reserves are required to be discounted to allow for the time value of money, using risk-free interest rates. Not discounting effectively adds implicit margins, making it harder to assess prudence. Discounting of reserves, premium provisions, and expense provisions, along with input into Asset-Liability Matching (ALM) strategies, is crucial.  
* **Granularity:** The level of detail at which reserves are calculated (company, class of business, individual policy, or claim event) depends on the purpose of the analysis. For example, management accounts often require more granular data \[SA3\_Combined\_Notes, P.2\].  
* **Inflation:** Reserving must allow for future inflation, which can be implicit (if the method assumes past inflation patterns continue) or explicit (adjusting for specific inflation rates like court award inflation). This includes claims inflation.

In conclusion, the "types of reserves" are deeply intertwined with the "purpose of reserving" within general insurance. Actuaries play a pivotal role in not only calculating these reserves accurately but also in communicating the underlying assumptions, methodologies, and inherent uncertainties to various stakeholders for informed decision-making. This requires a nuanced understanding of financial reporting, regulatory requirements, and the dynamic nature of insurance liabilities.

