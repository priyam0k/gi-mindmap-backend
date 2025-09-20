Of course. As your SP8 Exam Coach, let's build a structured note on the specific **Data Quality Issues of Errors, Omissions, and Distortions**. This is a crucial topic for the exam, as the quality of the final rates depends largely on the quality and quantity of data available. Understanding these issues is fundamental to applying any pricing methodology correctly.

### **📗 Data Quality Issues: Errors, Omissions, and Distortions**

The entire ratemaking process is **prospective**, using historical data to estimate future costs. The principle of "Garbage In, Garbage Out" (GIGO) is paramount; even the most sophisticated pricing models will produce flawed results if based on poor data. Professional standards, such as the Actuarial Standard of Practice No. 23 in the US, require actuaries to review data for reasonableness, appropriateness, and comprehensiveness before use.

Errors, omissions, and distortions can corrupt the data at any stage of its lifecycle—from initial capture and entry to storage and retrieval—leading to significant pricing inaccuracies and the risk of adverse selection. Let's break down the sources of these issues as outlined in the provided material.

#### **🔹 1\. Errors in Data Capture and Entry**

These are fundamental errors that can corrupt the data at its source. A robust information system with built-in integrity checks is the primary defence against them.

* **Wrong Policy or Claim Number:** Allocating details to the incorrect record corrupts the data for both the correct and incorrect policy/claim. Check digits can help prevent transcription errors.  
* **Wrong Dates:** Incorrectly entering the date of loss can allocate a claim to the wrong accident year. Similarly, confusing the report date with the loss date (or vice versa) can distort analyses, particularly for claims-made vs occurrence policies.  
* **Wrong Risk Details:** An error can occur if the risk characteristics in effect at the time of data entry are recorded, rather than those in effect at the date of loss. To mitigate this, a good system design principle is to capture stable data elements, like a driver's date of birth, from which a changing characteristic like age can be reliably derived.  
* **Inconsistent Coding:** The coding used for rating factors may vary from company to company, which is a key issue when using external industry-wide data.  
* **Omissions:** Essential information may be omitted if data fields are not made mandatory in the information system.

#### **🔹 2\. Systemic and Procedural Distortions**

Changes in an insurer's internal procedures or systems over time can introduce significant distortions into historical data, making it difficult to perform reliable trend and development analysis.

* **Changes in Claim Handling Procedures:** Altering internal rules can affect data quality. This includes changes in:  
  * **The definition of a claim:** Changes to when a notified loss is formally accepted and recorded as a claim can affect recorded claim counts, the number of nil claims, and the speed of notification.  
  * **Claim closure rules:** Inconsistent practices regarding when a claim file is closed can affect the apparent development of claims cohorts.  
  * **Treatment of reopened claims:** It is critical that reopened claims are not treated as new claims, as this would distort claim frequency and misallocate the loss to the wrong origin year.  
* **Changes in Case Reserving Philosophy:** A shift in case reserving approach, for example from a prudent to a realistic basis (or vice versa), can significantly distort incurred loss development patterns and make historical data less comparable over time.  
* **Legacy Systems:** Many established insurers operate with outdated legacy systems, which may be a patchwork of incompatible systems inherited through mergers. This can lead to inconsistent data definitions and coding, and an inability to access detailed historical data necessary for modern pricing techniques. For example, older systems may have only stored inception-to-date totals rather than a full transaction history, severely limiting actuarial analysis.

#### **🔹 3\. Distortions from Data Aggregation and Processing**

Even if the transactional data is correct, issues can arise when the data is processed and aggregated for analysis.

* **Processing Delays:** Backlogs or changes in the speed at which claims are processed will distort development patterns.  
* **Large and Catastrophic Claims:** The presence (or absence) of unusually large losses (shock losses) or catastrophe losses can distort any analysis unless they are identified and adjusted for appropriately. It is best practice to tag catastrophe claims with an event identifier in the claims database so they can be isolated.  
* **Partial Payments and Recoveries:** Inconsistent handling of multiple partial payments on a single claim can distort claim counts and severities. Similarly, if recoveries from **salvage and subrogation** are not correctly tracked and linked to the original claim, the net cost of the claim will be overstated.  
* **Changes in Mix of Business:** A shift in the types of policies being written can distort historical trends if not properly accounted for.

#### **🔹 4\. Issues Specific to External Data**

While external data is a valuable supplement, especially for new products, it comes with its own set of quality challenges.

* **Heterogeneity:** Industry-wide data aggregates experience from many different companies. These companies may have different target markets, underwriting rules, claim handling procedures, and expense levels, making the aggregated data not directly relevant or comparable to a specific insurer's portfolio.  
* **Timeliness and Detail:** External data is often more out-of-date and less granular than internal data due to the time required for collection, collation, and distribution.  
* **Incomplete Competitor Information:** When using competitor rate filings, it can be very difficult to get a complete picture of their rating

