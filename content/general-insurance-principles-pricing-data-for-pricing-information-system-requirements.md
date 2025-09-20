Excellent question. A robust and well-designed information system is the backbone of the entire pricing process. Without one, actuaries cannot obtain the quality, granular data needed to build reliable models, set equitable rates, and ultimately ensure the insurer's profitability and solvency. Let's build a detailed, structured note on the requirements for such a system, drawing upon our sources.

### **📗 Information System Requirements in the Context of Data for Pricing**

For an insurer pricing existing products, internal historical data is the most important resource. The quality of the final rates depends largely on the quality and quantity of the data available, making the systems that capture, store, and manage this data a critical component of the ratemaking process.

#### **🔹 1\. The Core Purpose: Supporting Multiple Functions**

An insurer's information system must be designed to meet the needs of various departments, not just the actuarial function. These users include senior management, accounting, underwriting, claims, marketing, investment, and reinsurance departments. While each has different requirements, an ideal system is a **single, integrated data system** that can serve all functions. This integrated approach reduces the chances of data corruption, ensures consistency, improves control and access, and eliminates the time-consuming and error-prone process of reconciling data from different systems.

For actuarial pricing, the system's primary role is to provide detailed, accurate historical information on policies and claims that can be linked together and analysed.

#### **🔹 2\. Key Components of the Information System**

The system must effectively manage two main types of internal data: risk information and accounting information.

##### **🔸 2.1 Risk Information Databases**

Risk data, which includes granular details about policies, premiums, and claims, is typically stored in two separate but linked databases.

**A. The Policy Database** This database contains detailed records for individual policies or their subdivisions (eg, a specific vehicle or coverage). A robust policy database should have the following features:

* **Granular Record Definition:** Records should be defined at a level of detail appropriate for pricing, such as by coverage or individual risk (eg, vehicle). Crucially, the system must create new transaction records for any mid-term policy amendments (eg, a deductible change), capturing the partial exposure and premium applicable before and after the change. This is vital for accurately matching premium to the specific risk characteristics in effect at the time.  
* **Unique Identifiers:** The system must generate and store unique **policy identifiers** and **risk identifiers** (for multi-risk policies). These are essential for accurately linking claims data back to the correct policy and risk characteristics.  
* **Essential Data Fields:** For each record, the system must capture:  
  * **Relevant Dates:** Policy effective/termination dates and the effective date of any mid-term changes.  
  * **Premium and Exposure:** Written premium and written exposure must be recorded for each transaction, allowing for the subsequent calculation of earned and in-force figures.  
  * **Risk Characteristics:** All rating and underwriting variables must be captured. It is best practice to capture stable data elements from which rating variables can be derived (eg, storing **date of birth** instead of age) to improve data quality and consistency over time.

**B. The Claims Database** This database captures all transactional information for each claim. Key system requirements include:

* **Comprehensive Linking Identifiers:** To link claims to policies, the system must contain the corresponding **policy and risk identifiers** from the policy database. It should also generate unique **claim identifiers** for all transactions related to a single claim, and potentially **claimant identifiers** for liability cases. An **event identifier** is also crucial for tagging and isolating catastrophe-related claims.  
* **Key Dates:** The system must record the **date of loss**, the **report date**, and the transaction date for every payment or reserve change.  
* **Financial and Status Tracking:** For each transaction, the system needs fields for paid loss, case reserve, paid allocated loss adjustment expenses (ALAE), and any salvage or subrogation recoveries. It should also track the claim's status (open, closed, re-opened).

##### **🔸 2.2 Accounting Information Systems**

Some data, like Unallocated Loss Adjustment Expenses (ULAE) and other underwriting expenses (eg, advertising, office upkeep), cannot be assigned to individual policies. The information system must be able to track these costs at an aggregate level, usually by calendar year, allowing them to be allocated for ratemaking purposes.

#### **🔹 3\. System Design and Integrity Principles**

A good information system is not just about the data fields it contains; its overall design and operational integrity are paramount.

* **User-Centric Design:** The system's design process should involve all potential users to ensure it meets essential requirements and priorities. Data capture forms (proposal and claim forms) should be designed to gather information unambiguously and in a format that is easy to enter into the computer system.  
* **Data Integrity Checks:** To ensure data quality, the system must have robust checks to prevent errors. These include:  
  * **Check Digits:** For identifiers like policy numbers to prevent transcription errors.  
  * **Data Field Integrity:** Setting minimum and maximum values for numeric fields.  
  * **Mandatory Fields:** Ensuring essential information is not omitted.  
  * **Error Reports:** Generating reports on fatal errors (preventing record entry) and warnings.  
* **Data History and Accessibility:** The system must retain a full history of policy and claim records, including previous values before any endorsements or changes. While modern low-cost data storage makes this feasible, legacy systems were often limited, storing only inception-to-date totals, which severely limits actuarial analysis.  
* **Staff Training and Culture:** Even the best system is ineffective without well-trained staff who understand the importance of accurate data entry. Management must foster a culture that values data quality.

#### **🔹 4\. Overcoming System Limitations (Legacy Systems)**

In reality, many established insurers operate with **legacy systems**, which may be outdated, difficult to amend, or a patchwork of incompatible systems inherited through mergers. This poses significant challenges:

* It may not be possible to transfer all historical data to a new, better system.  
* Data definitions and coding may be inconsistent across different systems.  
* Actuaries are often forced to work with the available data and use judgement to make approximations and overcome deficiencies. A new system, while desirable, takes many years to accumulate enough historical data to become fully useful, especially for long-tailed lines of business.

In conclusion, an effective information system is a critical asset for an insurer. It must be designed not only to capture a comprehensive and granular set of linked policy and claim data but also to ensure the ongoing integrity, consistency, and accessibility of that data. For the pricing actuary, the quality of this system directly dictates the reliability of the pricing models and the resulting premiums.

