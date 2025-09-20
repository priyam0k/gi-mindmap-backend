Excellent question. As your SP8 Exam Coach, let's build a comprehensive note on Expense Analysis and Allocation. This is a critical actuarial investigation for pricing, as expenses are a key component of the fundamental insurance equation. While losses and LAE often represent the largest cost, underwriting expenses can significantly impact profitability and rate adequacy. An effective pricing strategy requires a robust methodology for projecting and allocating these costs.

### **Actuarial Investigations: Expense Analysis & Allocation**

Actuarial investigations into expenses aim to project the costs associated with acquiring and servicing policies for a future period and to allocate these costs appropriately within the premium structure. This process is essential for balancing the fundamental insurance equation: `Premium = Losses + LAE + UW Expenses + UW Profit`.

#### **1\. Underwriting Expense Categories**

Insurers typically classify underwriting expenses (also called operational and administrative expenses) into four main categories:

* **Commissions and Brokerage:** These are amounts paid to agents or brokers for generating business, usually calculated as a percentage of written premium. The rates can vary for new versus renewal business or be contingent on the volume or quality of business written.  
* **Other Acquisition Costs:** These are non-commission expenses incurred to acquire business. Examples include media advertising, mailings to prospective insureds, and the salaries of sales staff who are not on commission.  
* **General Expenses:** This category covers the remaining operational costs, such as the upkeep of the home office, building maintenance, and salaries for non-sales and non-claims staff (like actuaries).  
* **Taxes, Licenses, and Fees:** This includes all taxes (excluding federal income tax), such as premium taxes, and miscellaneous fees like licensing fees paid by the insurer.

Loss Adjustment Expenses (LAE) are handled separately as they relate to the cost of settling claims. They are divided into Allocated Loss Adjustment Expenses (ALAE), which can be tied to a specific claim, and Unallocated Loss Adjustment Expenses (ULAE), which cannot. ULAE, like underwriting expenses, must be tracked at an aggregate level and allocated for ratemaking purposes.

#### **2\. Fixed vs. Variable Expenses: The Core Distinction**

For ratemaking analysis, actuaries often further divide underwriting expenses into two groups:

* **Variable Expenses:** These expenses vary directly with the premium, meaning they are a constant percentage of the premium. Commissions and premium taxes are classic examples.  
* **Fixed Expenses:** These are assumed to be a constant dollar amount per risk or policy, regardless of the premium size. Costs like policy issuance, data entry, and general overhead often fall into this category.

Recognising this distinction is crucial. Treating all expenses as variable (a percentage of premium) can lead to inequitable rates, where risks with small premiums are undercharged for their fixed costs, and risks with large premiums are overcharged.

#### **3\. Methodologies for Projecting & Allocating Expenses**

The sources outline three primary methods for deriving expense provisions for ratemaking. The choice of method depends on the significance of fixed expenses and the desired accuracy.

**3.1 All Variable Expense Method**

* **Concept:** This traditional method treats all underwriting expenses as variable, assuming they are a constant percentage of premium. It is still used for commercial lines where variable expenses like commissions dominate the total expense load.  
* **Process:** Historical calendar year expenses for each category are divided by a corresponding historical premium base to get an expense ratio. The choice of premium base—written or earned—is important:  
  * **Written Premium** is used for expenses incurred at the start of a policy (eg, commissions, other acquisition, taxes) to better match the expense payment to the premium associated with it.  
  * **Earned Premium** is used for expenses incurred throughout the policy term (eg, general expenses).  
* **Distortions:** As noted earlier, this method creates cross-subsidies between low-premium and high-premium risks. To mitigate this, insurers might implement expense constants or premium discount structures for larger policies.

**3.2 Premium-Based Projection Method**

* **Concept:** This method improves upon the "All Variable" approach by explicitly splitting expenses into fixed and variable components. However, it still projects both components as a percentage of historical premium.  
* **Process:**  
  1. Calculate an overall expense ratio for each category (eg, General Expenses ÷ Earned Premium).  
  2. Split this ratio into fixed and variable portions based on assumptions or internal studies (eg, assume 75% of general expenses are fixed).  
  3. The resulting fixed expense *ratio* is then used in the rate indication formula.  
* **Distortions:** Since fixed expenses do not truly vary with premium, this method is prone to distortion if historical and projected average premium levels differ materially. This can be caused by rate changes, shifts in the mix of business (premium trend), or significant variations in average premium across different states.

**3.3 Exposure/Policy-Based Projection Method**

* **Concept:** This is the most refined method. It treats variable expenses as a percentage of premium but calculates fixed expenses as a constant dollar amount per exposure or per policy.  
* **Process:**  
  1. Split historical expenses into fixed and variable dollar amounts.  
  2. Calculate the **variable expense ratio** by dividing variable expenses by the appropriate premium base (written or earned).  
  3. Calculate the **average fixed expense per exposure/policy** by dividing fixed expenses by the corresponding historical exposures or policy counts.  
* **Advantages:** This method avoids the distortions inherent in the other two approaches because it correctly models the nature of fixed costs. It is less susceptible to distortions from changes in average premium levels.

#### **4\. Trending Expenses**

Just like losses, fixed expenses are subject to inflationary pressures over time and must be trended to the future period when rates will be in effect.

* **Variable expenses**, being a percentage of premium, do not require separate trending. They automatically adjust as the premium level changes.  
* **Fixed expenses**, being a dollar amount per exposure/policy, need to be trended.  
  * **Trend Selection:** While internal expense data can be used, many companies supplement this with external government indices like the Consumer Price Index (CPI) or Employment Cost Index due to the volatility of their own data.  
  * **Trend Period:** The trend period depends on when the expense is incurred:  
    * Expenses incurred at the **onset** of a policy are trended from the average written date of the historical period to the average written date of the future policy period.  
    * Expenses incurred **throughout** the policy are trended from the average earned date of the historical period to the average earned date of the future policy period. This results in a longer trend period.

#### **5\. Allocating ULAE and Other Considerations**

* **ULAE Allocation:** Since ULAE cannot be assigned to specific claims, it must be allocated. A simple method is to calculate the historical ratio of calendar year paid ULAE to calendar year paid loss and ALAE. This factor is then applied to the projected ultimate loss and ALAE to incorporate the ULAE provision. This assumes ULAE trends and develops at the same rate as losses and ALAE.  
* **Data Granularity:** For countrywide carriers, country-level data is typically used for general and other acquisition expenses. State-specific data is preferred for commissions (if they vary by state) and is necessary for taxes, licenses, and fees, which vary by jurisdiction.  
* **Non-Recurring Expenses:** If the historical period includes extraordinary, non-recurring expenses (eg, a major IT system overhaul), the actuary must use judgment to decide whether and how to reflect this cost in future rates, perhaps by spreading the impact over several years.

In conclusion, expense analysis is a detailed actuarial investigation that requires careful data segmentation, methodological choice, and judgment. Selecting the most appropriate projection and allocation method is crucial for ensuring that the final premium is adequate to cover all costs and achieve the insurer's profit targets.

