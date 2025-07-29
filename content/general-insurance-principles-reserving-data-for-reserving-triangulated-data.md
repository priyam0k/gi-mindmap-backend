All right, future SP7 specialists, let's build some solid notes on a cornerstone of General Insurance Reserving: **Triangulated Data** and its broader context within **Data for Reserving**. This is absolutely fundamental for understanding how we quantify insurance liabilities, so pay close attention\!

### **1\. The Crucial Role of Data in General Insurance Reserving**

As actuaries in general insurance, our primary objective in reserving is to estimate the ultimate cost of claims that have already occurred, whether reported or not, along with related expenses. This is not an exact science, and our estimates heavily rely on comprehensive and reliable data. Without adequate data, our reserving calculations can be incorrect, leading to distorted reported results, improper tax payments, and crucially, inappropriate management decisions regarding reinsurance purchasing or investment strategy.

The quality and quantity of data are paramount for both reserving and capital modelling. Data must be of sufficient quality, meaning it should be free from errors and suitable for assessing risks. While some data requirements overlap with pricing (covered in SP8), SP7 focuses specifically on data for reserving and capital modelling.

#### **1.1 Sources of Data**

We primarily rely on:

* **Internal Data:** This is the insurer's own past experience, including policy information, premium details, and claim information collected from proposal forms and claim forms.  
* **External Data:** This comes from industry-wide schemes (like the ABI or Lloyd’s of London in the UK, or RAA/ISO in the US), reinsurers, or publicly published accounts. External data can provide benchmarks and increase the volume of data available for analysis, especially for small or newly established companies. However, caution is needed due to potential heterogeneity and outdatedness.

#### **1.2 General Issues Affecting Data Quality**

Several factors can compromise data quality and quantity, impacting reserving work:

* **Poor Quality Data:** Inaccurate policy or claim details (e.g., claim dates before policy inception).  
* **Inconsistent Data:** Changes in claim recording procedures over time can lead to inconsistencies.  
* **Incomplete and Non-existent Data:** This is common for new classes of business or when writing in new territories.  
* **Inadequate Data from Third-Party Claims Handlers:** Outsourcing claims handling can lead to difficulties in checking data validity, inconsistent recording across handlers, and delays in data transfer to the insurer.  
* **Legacy Systems:** Older insurers or those resulting from mergers may face difficulties integrating systems with different data items and structures.  
* **Integrity of Systems:** Lack of proper checks (e.g., ensuring data is entered once only and correctly, regular backups) can lead to corruption.  
* **Grouped Bordereaux Data (Reinsurance):** For treaty reinsurance, detailed individual risk data may not be available, limiting the reinsurer's ability to analyse experience. Also, cedants may fail to notify reinsurers of claims in a timely manner if they don't believe the retention will be breached.  
* **Reorganisation of Class Structure:** This can make it difficult to assemble historical data in new class definitions, leading to missing diagonals in triangles.

### **2\. Specific Data Requirements for Reserving**

To accurately estimate claims reserves, a wide array of detailed information is required.

* **Dates of Reporting and Occurrence:** Essential for determining IBNR claims and applying appropriate methodologies.  
* **Claim Payments and Case Estimates:** Whether at a class or more aggregated level, actual paid amounts and estimates for outstanding claims are needed. The consistency of gross and net data (after recoveries) should be checked.  
* **Premiums:** Earned premiums for accident year cohorts and written premiums for underwriting year cohorts are crucial for loss ratio calculations.  
* **Number of Claims:** Information on reported, reopened, and closed claims is necessary, often split by claim type.  
* **Measures of Exposure:** Beyond premiums, measures like turnover, payroll, or vehicle-years are used for exposure-based statistical methods.  
* **Allowance for Recoveries:** Understanding if data is gross or net of salvage, subrogation, and reinsurance recoveries is critical. Ideally, these should be projected separately as their patterns may differ from gross payments.  
* **Claims Handling Expenses:** Clarity is needed on whether data includes or excludes claims handling costs.

### **3\. Triangulated Data: The Heart of Many Reserving Methods**

Triangulated data, often referred to as run-off triangles or development tables, form the bedrock for many traditional reserving methods like the Chain Ladder, Bornhuetter-Ferguson, and Average Cost Per Claim. These tables organise claims data (incremental or cumulative) by **origin period** (rows) and **development period** (columns).

#### **3.1 Claim Cohorts**

The choice of cohort is fundamental as it dictates how claims are grouped and how different reserve components are captured:

* **Accident Year:** Claims are grouped by the year the claim event (accident) occurred. This approach automatically allows for IBNR, recoveries, and reopenings belonging to that cohort, provided new claims and reopenings are allocated correctly.  
* **Reporting Year:** Claims are grouped by the year they were reported to the insurer. This method typically excludes pure IBNR (claims not yet reported at year-end), which would need to be estimated separately. Its development is usually quicker than accident or underwriting year.  
* **Underwriting Year:** Claims are grouped by the year the policy was underwritten. Similar to accident year, it includes IBNR, recoveries, and reopened claims if emergence is allocated correctly.

It's vital to note that while each method produces an estimate, they are expected to converge towards similar figures for reserves as they approach the extremes of the development table.

#### **3.2 General Issues with Triangulations**

While powerful, triangulations are imperfect representations of the claims process and come with a host of issues that actuaries must skillfully navigate.

##### **3.2.1 Data Homogeneity vs. Credibility**

A constant challenge is balancing the need for data to be homogeneous (similar characteristics like class of business, claim type, legal environment) with ensuring sufficient volume for credibility. Splitting data too finely can lead to sparse data and unreliable results, whereas too much aggregation can mask underlying trends and heterogeneity.

##### **3.2.2 Distortions in Data**

Distortions can invalidate the core assumption that future claims development will follow past patterns. Actuaries must identify and make appropriate allowances for these:

* **Changes in Terms and Conditions:** Policy changes (e.g., new risks covered, exclusions) can alter claims experience.  
* **Changes in Business Mix:** Significant shifts in portfolio composition can unpredictably change development patterns.  
* **Changes in Claims Handling Procedures:** Alterations in how claims are processed (speed of settlement, case reserving philosophy, online portals) can impact reported/paid patterns and case reserve adequacy.  
* **Market-wide Initiatives:** External factors, such as industry efforts to speed up reporting, can distort patterns.  
* **Developments in Economic and Legal Environment:** Inflation (price, wage, medical, court award), legislation, and court rulings can significantly alter claim costs and development.  
* **Large and Exceptional Claims:** These claims can heavily distort development patterns due to their size and often different development characteristics from attritional claims. It's often necessary to analyse them separately, removing or capping them in attritional triangles, but ensuring the final reserve accounts for them.  
* **Latent Claims (e.g., Asbestos, Pollution, Health hazards):** Triangulation methods are generally *not* suitable for latent claims due to their unique, often calendar-year-driven emergence patterns and long tails. Exposure-based methods are usually preferred.  
* **Reopened Claims:** Payments for reopened claims should be allocated to their original risk group and claim year to avoid distorting current experience.  
* **Link Ratios Less Than One:** This can occur due to conservative case reserves, subrogation, or salvage recoveries, and their appropriateness needs careful consideration.  
* **Unusually Heavy/Light Experience:** A particular origin year might have unusually high or low claims, which, if not adjusted for, can lead to over or underestimation of ultimate values when using chain ladder.

##### **3.2.3 Incomplete Triangles**

Sometimes, full historical triangles are unavailable due to legacy systems, or older cohorts are not fully developed. In such cases, approximations are needed, and the materiality of such assumptions must be communicated.

### **4\. Purpose and Application of Triangulated Data in Reserving**

The primary purpose of triangulated data is to serve as input for statistical reserving methods that project future claim payments.

* **Projection to Ultimate:** Methods like Chain Ladder and Bornhuetter-Ferguson use historical development patterns from triangles to project future claims and estimate the ultimate cost.  
* **IBNR Estimation:** While reporting year cohorts exclude IBNR, accident and underwriting year cohorts aim to automatically include it.  
* **Understanding Trends:** Triangles help actuaries spot trends in claim frequency and severity.  
* **Stochastic Reserving:** Triangulated data is essential for stochastic models (e.g., Mack, ODP, bootstrapping) which derive not just a point estimate but also a distribution of possible outcomes, quantifying reserve uncertainty.

### **5\. The Indispensable Role of Actuarial Judgement**

Given the inherent complexities and potential distortions in triangulated data, actuaries cannot simply apply methods mechanically. **Actuarial judgement is paramount**.

* **Data Peculiarities:** Judgement is required to cope with sparse data or peculiarities.  
* **Assumption Selection:** Actuaries must justify and document the rationale for selecting assumptions, especially critical ones, and consider known limitations.  
* **Validation:** After estimating reserves, actuaries must apply judgement to assess the reasonableness of the results using various diagnostics (e.g., loss ratios, paid to incurred ratios, average outstanding case estimates, residuals). Reconciliation with deterministic results, graphical reviews, and back-testing are common validation approaches.  
* **Communication of Uncertainty:** The actuary must clearly communicate the best estimate, the uncertainties around it (process, parameter, model uncertainty), and any ranges (e.g., from stochastic models, scenario tests, or alternative assumptions) to stakeholders like management and regulators.

### **6\. Link to Capital Modelling**

The quality of data and the robustness of reserving calculations, often relying on triangulated data and sophisticated stochastic models, directly impact capital modelling.

* **Reserve Risk Quantification:** Stochastic reserving techniques are commonly used to determine quantitative estimates of the volatility in reserves as an input to capital models.  
* **SCR Calculation:** Data quality is relevant for the Solvency Capital Requirement (SCR) assessment, ensuring a consistent approach across Pillar 1 quantitative requirements. The capital impact of reserving risk is the difference between the eventual cost at the firm's chosen risk tolerance and the current best estimate reserves.  
* **Dependency Modelling:** When aggregating results across multiple lines of business for a company-wide capital model, understanding and modelling dependencies (e.g., using copulas) between various risk types (underwriting risk, reserving risk) is critical. This ensures variability is not underestimated.

In essence, triangulated data, supported by rigorous analysis and sound actuarial judgement, provides the essential foundation for estimating and understanding general insurance liabilities, which then feeds directly into robust capital assessment. As an SP7 student, mastering the nuances of triangulated data and its implications is absolutely critical for your success\!

