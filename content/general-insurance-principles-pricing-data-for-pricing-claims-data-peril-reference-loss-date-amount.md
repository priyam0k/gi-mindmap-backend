Of course. Let's build a comprehensive, structured note on the crucial components of the **Claims Database** – specifically focusing on perils, reference identifiers, loss dates, and financial amounts – within the wider context of General Insurance Pricing. A thorough understanding of this topic is vital for SP8, as the claims database provides the 'loss' component of the fundamental insurance equation, which is the primary statistic actuaries are trying to predict.

### **📗 Claims Data in the Context of Data for Pricing**

In ratemaking, the ultimate cost of an insurance policy is unknown at the time of sale. Actuaries must therefore use historical data to project future expected costs. Alongside the policy database, the **claims database** is a critical source of internal risk information. It captures detailed transactional information for each claim, allowing actuaries to link losses back to the specific policies, risks, and characteristics that generated them. Without a robust and detailed claims database, it is impossible to perform accurate pricing analysis.

#### **🔹 1\. Structure of a Claims Database**

Most insurers maintain a claims database that is separate from their policy database. In a typical claims database, each record represents a specific transaction tied to a particular claim, such as a payment or a change in reserve. The fields within each record provide the essential explanatory information. Let's examine the key fields as described in the sources.

#### **🔹 2\. Key Data Fields in the Claims Database**

A well-specified claims database is essential for linking losses to the correct premium and exposure data, which is a foundational requirement for ratemaking.

##### **🔸 2.1 Reference Identifiers (Linking Data)**

To accurately match losses with the policies and risks that generated them, a system of unique identifiers is crucial. These identifiers bridge the gap between the policy database and the claims database.

* **Policy Identifier:** A unique identifier for the insurance policy under which the claim is made. This is the primary link back to the policy database.  
* **Risk Identifier(s):** For products insuring multiple risks on a single policy (eg, different vehicles or drivers on a personal auto policy), specific risk identifiers are necessary to match the claim to the correct insured item or person within that policy.  
* **Claim Identifier:** A unique identifier assigned to each specific claim. This number is used for all subsequent transaction records related to that same claim, ensuring that all payments and reserve changes are correctly grouped.  
* **Claimant Identifier:** A unique identifier for each specific claimant on a claim, which is particularly important in liability cases where multiple third parties may be involved.  
* **Event Identifier:** This field is used to tag claims associated with a specific extraordinary event, such as a catastrophe (eg, a hurricane or earthquake). This allows these atypical losses to be tracked separately and excluded from standard analyses to avoid distorting the underlying experience.

##### **🔸 2.2 Relevant Loss Dates**

The timing of a loss is critical for aggregating data correctly for analysis (eg, by accident year) and for understanding reporting and settlement lags. The claims database must capture several key dates:

* **Date of Loss:** Also known as the accident date or occurrence date, this is the date the event that caused the loss took place. It is the primary date used for **accident year** data aggregation. For some perils, the loss may result from continuous exposure, in which case the accident date is often defined as the date the damage became apparent.  
* **Report Date:** This is the date the insurer was first notified of the claim. Claims that have occurred but have not yet been reported are known as Incurred But Not Reported (IBNR) claims. The report date is the coverage trigger for claims-made policies and is used for **report year** data aggregation, which is common in lines like medical malpractice.  
* **Transaction Date:** Each record in the claims database has a transaction date, which specifies when that particular activity (eg, a payment, reserve change, or status change) occurred.

##### **🔸 2.3 Peril / Claim Characteristics (Cause of Loss)**

To perform granular pricing analysis and understand the drivers of loss, it is vital to capture details about the cause of the loss.

* **Peril / Cause of Loss:** The claims database should track losses by coverage, peril, or type of loss. For example, in homeowners insurance, claims might be categorised as fire, theft, flood, or subsidence. In personal auto, claims are separated by coverage, such as bodily injury, property damage, comprehensive, and collision. This level of detail allows actuaries to:  
  * Analyse trends for specific perils, which may differ significantly from the overall trend.  
  * Price optional coverages or endorsements accurately.  
  * Exclude specific perils from an analysis where required (eg, removing catastrophe-related losses).  
* **Other Claim Characteristics:** Companies may also collect other details such as the type of injury or physician information for liability claims. While interesting for claims or reserving studies, this information is only useful for pricing if it is known for all policyholders at the time a quote is generated.

##### **🔸 2.4 Financial Amounts (Loss and Expenses)**

The core purpose of the claims database is to track the financial cost of claims. These amounts are the "Losses" and "LAE" in the fundamental insurance equation.

* **Paid Loss:** These are the amounts that have actually been paid to claimants. Payments should be tracked separately by coverage or peril if applicable.  
* **Case Reserve:** This is an estimate of the amount of money required to ultimately settle a specific, reported claim, excluding any payments already made. The case reserve is adjusted as more information becomes known about the claim.  
* **Allocated Loss Adjustment Expenses (ALAE):** These are claim-related expenses that can be directly attributed to a specific claim, such as fees for outside legal counsel. ALAE payments (and case reserves, if set) are included on the claim database.  
* **Salvage and Subrogation:** These are recoveries that offset the loss payment.  
  * **Salvage** is money recovered from selling damaged property that the insurer takes ownership of after settling a claim.  
  * **Subrogation** is money recovered from a third party who was at fault for the loss. These recoveries are tracked and linked to the original claim, effectively acting as negative paid losses.

A key metric derived from these fields is **Reported Loss** (also called case incurred loss), which is the sum of paid losses and the current case reserve for a claim.

#### **🔹 3\. Conclusion: The Foundation for Loss Analysis**

The claims database provides the raw data that, once linked to the policy database and aggregated, allows actuaries to calculate essential pricing metrics like frequency, severity, and pure premium. The detail and quality of the data captured—from unique identifiers linking claims to policies, to the specific dates and financial transactions—directly impacts the reliability of the final rates. Without a claims database that accurately records what happened (peril), to whom (identifiers), when (dates), and for how much (amounts), an insurer cannot effectively manage its pricing, avoid adverse selection, or ensure long-term profitability.

