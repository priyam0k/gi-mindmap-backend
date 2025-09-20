Of course. As your Specialist Actuarial Note Builder and Exam Coach, let's construct a detailed, structured note on the crucial topic of **Internal Data**. A deep understanding of internal data is non-negotiable for the SP8 exam, as it forms the primary input for most pricing analyses. The quality of your final rates depends largely on the quality and quantity of the data available.

### **📗 Internal Data in the Context of Data for Pricing**

For an insurer pricing existing insurance products, internal historical data is the most important resource. The entire ratemaking process is **prospective**, aiming to set rates so that the premium for a future period will be adequate to cover expected losses, expenses, and a target underwriting profit. To achieve this, actuaries must use relevant historical data to project these future costs. Therefore, it is imperative that an insurer collects and maintains pertinent and consistent historical data to facilitate a robust pricing review.

Internal data typically falls into two categories:

1. **Risk Information**: Granular data about exposures, premiums, claim counts, losses, and explanatory characteristics about the policy or the claim. This is usually stored in separate policy and claim databases.  
2. **Accounting Information**: Aggregate-level data, such as underwriting expenses and unallocated loss adjustment expenses (ULAE), which cannot be assigned to specific policies.

This note will focus on the first category: the risk information contained within the policy and claim databases.

#### **🔹 1\. The Policy Database: Capturing Premium, Exposure, and Risk Characteristics**

The policy database contains detailed records for individual policies or their subdivisions (eg, a specific vehicle, coverage, or industry classification). This granular information is essential for almost all pricing analyses, from overall rate level reviews to highly detailed multivariate modelling like GLMs.

##### **🔸 1.1 Structure of a Policy Database Record**

How a record is defined depends on the product's exposure measure and how the premium is calculated. For example:

* **Homeowners Insurance:** A record might represent one home insured for an annual policy period.  
* **Personal Auto Insurance:** Records are often created for each individual vehicle, coverage, and sometimes even each operator, meaning a single policy can generate many records.  
* **U.S. Workers Compensation:** Records are typically maintained at the industry classification level, based on payroll.

Crucially, records must also be subdivided to reflect any mid-term policy changes, such as a change in deductible or a cancellation. This creates separate transaction records for the partial policy periods before and after the amendment, ensuring premium and exposure are correctly matched to the risk characteristics in effect at the time. For statistical analysis, these transactions would be aggregated into "net" records representing the distinct periods.

##### **🔸 1.2 Key Data Fields in the Policy Database**

For each record, a comprehensive set of data fields is required for ratemaking:

* **Identifiers:**

  * **Policy Identifier:** A unique number for the policy as a whole.  
  * **Risk Identifier(s):** For policies with multiple risks (eg, different vehicles), unique identifiers are needed to correctly link claims to the specific risk.  
* **Relevant Dates:**

  * Original policy effective and termination dates.  
  * The effective date of any mid-term amendments.  
* **Premium & Exposure Information:**

  * **Written Premium:** The premium associated with each transaction, often broken down by coverage. This is the price the insured pays for the coverage.  
  * **Written Exposure:** The basic unit of risk underlying the premium, such as a "house-year" for homeowners insurance.  
  * From this transactional data, **earned** and **in-force** figures can be calculated for analysis.  
* **Risk Characteristics:**

  * This includes all **rating variables** (eg, driver age) and **underwriting variables** used to assess and price the risk.  
  * **Capturing Stable Data:** It is best practice to capture stable data points. For instance, storing a driver's **date of birth** is more reliable than their age, as age changes over time while the date of birth does not. The age can be derived as needed, improving data consistency and quality.

#### **🔹 2\. The Claims Database: Capturing Loss and LAE Information**

The claims database, typically separate from the policy database, captures detailed transactional information about each claim. Each record generally represents a specific transaction, such as a payment or a change in reserve.

##### **🔸 2.1 The Importance of Linking Claims to Policies**

A fundamental requirement for ratemaking is to accurately link losses with the premium and exposure data from the policy that generated them. This is achieved through a system of unique identifiers stored in the claims database:

* **Policy and Risk Identifiers:** To match the claim to the correct policy and specific risk (eg, vehicle) within that policy.  
* **Claim and Claimant Identifiers:** To uniquely identify each specific claim and each individual making a claim under it.  
* **Event Identifier:** A field to tag claims associated with a specific catastrophe (eg, a hurricane), allowing these atypical losses to be isolated from standard analyses.

##### **🔸 2.2 Key Data Fields in the Claims Database**

In addition to linking identifiers, the following fields are critical for pricing:

* **Relevant Loss Dates:**

  * **Date of Loss (or Accident Date):** The date the event causing the loss occurred. This is the primary date used for **accident year** aggregation.  
  * **Report Date:** The date the insurer was first notified of the claim. This is the coverage trigger for **claims-made** policies.  
* **Claim Status and Characteristics:**

  * **Status:** Fields to track whether a claim is open, closed, or re-opened.  
  * **Peril / Cause of Loss:** Detail on the specific coverage or peril (eg, fire, theft, collision) allows for more granular analysis of loss trends and the pricing of optional coverages.  
* **Financial Amounts (Losses and LAE):**

  * **Paid Loss:** The amount of compensation that has actually been paid to the claimant.  
  * **Case Reserve:** An estimate of the amount required to ultimately settle a specific reported claim, excluding payments already made.  
  * **Reported Loss (Case Incurred Loss):** The sum of Paid Losses and the current Case Reserve for a claim.  
  * **Allocated Loss Adjustment Expenses (ALAE):** Claim-related expenses that can be directly attributed to a specific claim, such as external legal fees. These are included on the claim database.  
  * **Salvage and Subrogation:** Recoveries that offset the loss payment. Salvage is money recovered from selling damaged property, while subrogation is money recovered from a third party who was at fault.

#### **🔹 3\. Conclusion: The Foundation of Actuarial Analysis**

In summary, the internal policy and claims databases are the bedrock of the ratemaking process. They provide the raw, transactional data on premiums, exposures, and losses that, once aggregated and adjusted, allow the actuary to project future costs and set adequate, equitable rates. The detail and quality of this internal data directly impact the reliability of the pricing analysis and, ultimately, the insurer's ability to remain profitable and avoid adverse selection. As noted in the SP7 and SA3 syllabuses, these data principles are foundational not only for pricing (SP8) but also for reserving (SP7), capital modelling, and advanced strategic applications (SA3).

