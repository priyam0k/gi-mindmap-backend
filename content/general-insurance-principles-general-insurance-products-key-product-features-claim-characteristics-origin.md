As your Specialist Actuarial Note Builder and Exam Coach, let's construct a detailed note sequence on the concept of **Origin** (or **Claim Cohorts**), positioning this topic within the larger context of **Claim Characteristics**. Understanding the origin of claims is a foundational skill for both SP8 pricing and SP7 reserving, as it dictates how data is grouped for analysis and projection \[SP7.pdf, SP8.pdf\]. The choice of origin cohort fundamentally shapes the actuarial investigation \[SP7.pdf, SP8.pdf, SP752.pdf\].

### **The Larger Context: Key Product Features**

When analysing any general insurance product, one of the six key features is its **Claim Characteristics**. This feature describes how claims arise, are reported, and are settled \[SP7.pdf, SP8.pdf\]. A crucial part of this analysis is deciding how to group claims data into cohorts of common origin to enable a consistent and meaningful investigation over time \[SP7.pdf, SP752.pdf, SP8.pdf\]. An inconsistent comparison of claims and exposure can lead to flawed analysis \[SP7.pdf, SP8.pdf, SP752.pdf\].

### **1\. Defining Origin (Claim Cohorts)**

The **origin period** (or cohort) is the basis used to group claims together for analysis, particularly for use in run-off triangles \[SP7.pdf, SP8.pdf, SP752.pdf\]. The choice of grouping is critical and can lead to different results \[SP7.pdf, SP8.pdf, SP752.pdf\]. The period used can be a year, quarter, or month depending on the business and the desired granularity \[SP7.pdf, SP8.pdf, SP752.pdf\].

The sources describe three main ways to group claims by origin:

1. **Accident Year**  
2. **Underwriting Year** (also known as Policy Year or Year of Account)  
3. **Reporting Year**

Let's examine each in detail.

---

### **2\. Accident Year Origin**

* **Definition:** Claims are grouped according to the year (or other period) in which the **claim event or 'accident' occurred** \[SP7.pdf, SP8.pdf, SP752.pdf\].

* **What it Captures:** When used in a claims run-off projection, this origin cohort automatically allows for all claims arising from events in that period, including Incurred But Not Reported (IBNR) claims, recoveries, and reopened claims \[SP7.pdf, SP8.pdf, SP752.pdf\].

* **Advantages for Actuarial Analysis:**

  * **Homogeneity:** All claims in an accident year cohort stem from the same exposure period and are therefore subject to the same underlying risk environment (eg, weather conditions, economic factors) \[SP7.pdf, SP8.pdf, SP752.pdf\]. This makes it easier to relate variations between cohorts to specific influences operating at that time \[SP7.pdf, SP8.pdf, SP752.pdf\].  
  * **Accounting Alignment:** This approach aligns naturally with the accounting year, making it easier to compare emerging losses with the charges made in that period's financial statements \[SP7.pdf, SP8.pdf, SP752.pdf\].  
  * **Exposure Measure:** The natural exposure measure for this origin is **earned premium**, which aligns well with the accident year concept \[SP7.pdf, SP8.pdf, SP752.pdf\].  
* **Disadvantages and Challenges:**

  * The full number and amount of claims are not known until the last claim is reported, which can take a long time for long-tail classes \[SP7.pdf, SP8.pdf, SP752.pdf\].  
  * Defining the "accident date" can be difficult for some perils, such as subsidence or industrial diseases like asbestosis, which occur over a prolonged period \[SP7.pdf, SP8.pdf, SP752.pdf\]. In these cases, rules must be established to allocate the claim consistently across different origin years \[SP7.pdf, SP8.pdf, SP752.pdf\].

---

### **3\. Underwriting Year Origin**

* **Definition:** Claims are grouped according to the year (or other period) in which the **policy covering the claim incepted** (ie, commenced), irrespective of when the claim event occurred \[SP7.pdf, SP8.pdf, SP752.pdf\].

* **What it Captures:** A projection on this basis includes the reserves for outstanding claims (IBNR, IBNER, reopened) as well as the **reserve for unexpired risks** \[SP7.pdf, SP8.pdf, SP752.pdf\]. This is because an annual policy written on 31 December 2023 will have claims occurring throughout 2024, all of which belong to the 2023 underwriting year \[SP7.pdf, SP8.pdf, SP752.pdf\].

* **Advantages for Actuarial Analysis:**

  * **Pricing Alignment:** It allows the actuary to track the total outcome of all policies written in a given year, making it ideal for testing the adequacy of the premium rates charged during that period \[SP7.pdf, SP8.pdf, SP752.pdf\].  
  * **Consistency of Terms:** The terms, rates, and conditions of policies are often more stable by underwriting year than by accident year \[SP7.pdf, SP8.pdf, SP752.pdf\].  
* **Disadvantages and Challenges:**

  * The development tail is longer. It can take up to two years from the beginning of an underwriting year before all claim events have even occurred for annual policies, with reporting and settlement delays extending this further \[SP7.pdf, SP8.pdf, SP752.pdf\].  
  * Claims within a single underwriting year cohort will have occurred over a wider risk period (at least two accident years), making the development patterns more complex in the early stages \[SP7.pdf, SP8.pdf, SP752.pdf\].  
* **Common Application:** This is the most commonly used approach for **reinsurance**, **Lloyd's** business, and other London Market classes \[SP7.pdf, SP8.pdf, SP752.pdf\].

---

### **4\. Reporting Year Origin**

* **Definition:** Claims are grouped according to the year (or other period) in which they are **reported to the insurer**, irrespective of when the policy incepted or the accident occurred \[SP7.pdf, SP8.pdf, SP752.pdf\].

* **What it Captures:** By definition, a projection on this basis **does not allow for pure IBNR**, as no further claims can be added to the cohort after the end of the reporting period. The run-off triangle only projects the future development of claims already known to the insurer \[SP7.pdf, SP8.pdf, SP752.pdf\].

* **Advantages for Actuarial Analysis:**

  * It provides a fixed group of claims to track, which helps in monitoring the development of notified claims and assessing the delay before reliable estimates can be made for known claims \[SP7.pdf, SP8.pdf, SP752.pdf\].  
* **Disadvantages and Challenges:**

  * **No IBNR:** The major disadvantage is that a separate, explicit allowance must be made for IBNR claims, as the projection method does not capture them \[SP7.pdf, SP8.pdf, SP752.pdf\].  
  * **Heterogeneity:** The claims within a reporting year cohort will have come from several different exposure periods (underwriting years) and accident years, each with different premium rates, policy terms, and risk environments. This makes the data very heterogeneous and difficult to interpret \[SP7.pdf, SP8.pdf, SP752.pdf\].  
  * **Exposure Measure:** There is no natural exposure base that corresponds to this origin definition \[SP7.pdf, SP8.pdf, SP752.pdf\].

In summary, the choice of origin is a critical first step in any claims analysis. The Accident Year is often preferred for direct business due to its alignment with exposure periods, while the Underwriting Year is standard for reinsurance and for monitoring pricing adequacy. The Reporting Year is less common for ultimate reserve estimation due to its exclusion of IBNR but can be useful for analysing the development of known claims.

