Right, actuaries\! Let's get straight into the heart of the Burning Cost Approach (BCA) within General Insurance Pricing, specifically focusing on the critical element of **assumptions** that underpin this method. As your Specialist Actuarial Note Builder and Exam Coach for SP8, I'll guide you through the intricacies, drawing directly from our core material.

### **📗 Chapter 14: Rating using Frequency-Severity and Burning Cost Approaches (and related chapters)**

#### **The Burning Cost Approach: A Foundation in Pricing**

The Burning Cost Approach is a fundamental method used to determine a risk premium, often serving as a starting point for pricing various types of insurance and reinsurance. It is commonly employed within the "cost plus" approach to ratemaking, aiming to estimate the expected cost of claims for a future policy period.

At its core, the BCA calculates the risk premium as the actual cost of claims incurred during a past period, expressed as an annual rate per unit of exposure. Conceptually, this is simply the average claim cost per year, per unit of exposure. Formally, the burning cost premium (BCP) is defined as: $$ \\text{Burning Cost Premium (BCP)} \= \\frac{\\sum \\text{Claims}}{\\text{Total Exposed to Risk}} $$

This method can be applied to rate an individual risk or a portfolio of similar risks.

#### **Underlying Assumptions of the Burning Cost Approach**

The fundamental principle of the Burning Cost Approach is its reliance on historical aggregate claims data. This reliance immediately introduces several explicit and implicit assumptions:

1. **Past Experience as a Proxy for Future:** The most significant underlying assumption is that **past historical claims experience is a reliable and direct indicator of future claims experience**. This is explicitly stated in the definition of the method, which calculates the risk premium based "entirely on historical data". In its most basic form, this assumes that the future claims environment will be similar to the past, encompassing factors like claims frequency, severity, and development patterns.

2. **Stability of Underlying Conditions:** In its crudest application, the Burning Cost Approach assumes **no material changes in the claims environment** between the historical period and the future rating period. This means it makes:

   * **No allowance for future inflation**. This assumes that the monetary value of claims will not increase due to inflation.  
   * **No explicit allowance for development of losses to ultimate** (i.e., for IBNR – Incurred But Not Reported – and outstanding claims). This implicitly assumes that historical claims data is already at its ultimate cost or that the pattern of development will remain consistent and fully accounted for in the historical aggregation.  
   * **No explicit allowance for past inflation or other trending adjustments**. This means it assumes that the historical claim costs are already at the appropriate level for the future.  
3. **Aggregate Data Sufficiency and Lack of Granularity:** The method fundamentally "ignores the number of claims" (frequency) and directly projects total claims relative to total exposure. This implicitly assumes that the **aggregate claims experience is sufficient for pricing** and that a more granular breakdown into frequency and severity components is not necessary or will not provide significantly better insights for the purpose at hand.

4. **Proportionality of Exposure Base:** A good exposure base is assumed to be **directly proportional to expected loss, practical to use, and consistent over time**. When an exposure base is chosen, the assumption is that it accurately reflects the underlying risk and that claims costs scale linearly with this measure.

#### **Data Requirements and Their Link to Assumptions**

To apply the Burning Cost Approach, actuaries primarily need reliable and relevant policy and claims data.

* **Policy Data:** Essential for calculating overall exposure or splitting it by risk groups, including policy dates and rating/exposure details.  
* **Claims Data:** Necessary for estimating the ultimate cost of claims. Often, only aggregated claims data by policy year is available when this method is used. Ideally, this data should be gross of reinsurance and "from the ground up" (FGU), meaning it includes all claims, regardless of size, and their original amounts.

The quality and quantity of this data are crucial. When data is limited, actuaries must understand the impact and examine the sensitivity of results to assumptions. The less granular the data, the more reliance is placed on the underlying assumptions of stability and consistency, as fewer adjustments can be made.

#### **Practical Considerations and Adjustments: Refining the Assumptions**

While the basic Burning Cost Approach can be very crude, it is rarely used in practice without significant adjustments. These adjustments directly address and refine the initial simplifying assumptions, making the historical data more relevant for future premium estimation:

1. **Developing Losses to Ultimate:** To counter the assumption that historical claims are already ultimate, claims information should be **developed to their ultimate values**. This involves using standard reserving techniques such as the chain ladder or Bornhuetter-Ferguson methods to account for claims reported but not fully settled, and claims incurred but not yet reported (IBNR) or incurred but not enough reported (IBNER). If individual loss information is not available, IBNR factors may be calculated from aggregate risk data or a book of business.

2. **Trending (or On-leveling):** To adjust for the assumption that past conditions are identical to future ones, historical data needs to be **trended** to make it relevant for the future period when new premium rates will apply. This involves adjusting for inflation (past and future), changes in economic conditions, legal reforms, technical changes, policy conditions, underwriting practices, and shifts in business volumes or structure. When frequency and severity cannot be separated (as is common in basic BCA), the aggregate data is adjusted. For instance, if only aggregate data is used, an average loss occurrence date might be assumed for projection purposes.

3. **Treatment of Large and Catastrophe Losses:** Catastrophe claims are typically **omitted from the primary burning cost analysis and handled separately**, often using catastrophe modelling systems, due to their infrequent and extreme nature which distorts historical averages. For large non-catastrophe losses, actuaries may:

   * Omit them from the analysis and allow for them separately in the risk premium.  
   * Truncate them at a set point and spread the excess cost across the larger portfolio.  
   * Remove them altogether. The decision depends on the expected recurrence of such claims. This helps mitigate the assumption that historical "noise" or extreme events are representative of future "typical" experience.  
4. **Credibility Weighting:** To address the assumption of sufficient data or full reliance on the subject's own data, the burning cost estimate can be **credibility-weighted with other, broader data sources** (e.g., market data or a larger group's experience). This is particularly important when the historical data for a specific risk is sparse or lacks statistical credibility.

5. **Exposure Measure Refinement:** While the core assumption is proportionality, the selection of the exposure measure itself requires careful consideration to ensure it remains proportional to expected loss and consistent over time. For example, adjusting premiums to an "as-if" basis to make them consistent with inflation-adjusted claims.

6. **Underwriting Expense Provisions:** When building the total premium, allowances for underwriting expenses are added. The methods for deriving these provisions have their own set of assumptions about how expenses relate to premium or exposure:

   * **All Variable Expense Method:** Assumes all expenses are a **constant percentage of premium**, directly varying with it. This is a strong assumption that can understate premium for small risks and overstate for large ones, as it ignores fixed expenses.  
   * **Premium-based Projection Method:** Distinguishes fixed and variable expenses but still allocates fixed expenses as a ratio to premium.  
   * **Exposure/Policy-based Projection Method:** Assumes **fixed expenses are constant per exposure or policy count**, rather than varying with premium. This approach helps mitigate the distortion of the "All Variable" method but still requires actuarial judgement to account for economies of scale if expenses do not increase proportionally with exposures.  
7. **Reinsurance Costs:** While the basic BCA might be performed on a direct basis, increasingly, ratemaking analyses are performed on a **net basis, considering reinsurance costs**. For proportional reinsurance, if it cedes the same proportion of premium and losses, explicit consideration may not be needed. For non-proportional, the burning cost calculation would apply reinsurance terms to historical losses after trending and development. This requires assumptions about the applicability of past reinsurance structures to future periods.

#### **Advantages and Disadvantages Tied to Assumptions**

The inherent assumptions of the Burning Cost Approach contribute to both its strengths and weaknesses:

**Advantages:**

* **Simplicity and Ease of Understanding:** Its straightforward nature, often relying on aggregated data, makes it easy to implement and explain to non-technical stakeholders. This simplicity arises directly from its more basic underlying assumptions.  
* **Lower Data Requirements:** It generally requires less granular data compared to frequency-severity methods, as it operates on aggregate claims, reducing the need for detailed claim number information. This makes it suitable when detailed data is unavailable.  
* **Efficiency:** It is quicker to perform than more complex actuarial methods.  
* **Direct Reflection of Experience:** It allows for the direct experience of an individual risk or a portfolio of similar risks to be considered.

**Disadvantages:**

* **Lack of Granularity/Insights:** By focusing solely on aggregate claims, it "ignores the number of claims" and "loses much of the information on trends being experienced by not considering frequency and severity separately". This limits the understanding of underlying drivers of loss and trends, as it oversimplifies the claims process.  
* **Understating Ultimate Position:** If crucial adjustments for inflation, trends, and claims development (IBNR, IBNER) are not applied, the approach will "understate the ultimate position," leading to rates that result in higher-than-planned loss ratios. This is a direct consequence of the crude 'past equals future' assumption without modification.  
* **Sensitivity to Data Fluctuations:** Its reliance on historical data means it can be highly sensitive to unusual or one-off events (e.g., large claims not adjusted for) in the experience period if not adequately treated, potentially distorting the projected premium.  
* **Heterogeneity Distortion:** For classification ratemaking, a univariate pure premium (burning cost) approach can be distorted if it assumes a uniform distribution of exposures across other rating variables, potentially "double counting" effects.  
* **Not Suitable for Low-Frequency, High-Severity Risks (without heavy adjustments):** For catastrophe risks, observed historical losses may not reflect true underlying risks, as the observation period might be shorter than the return period of the losses. Without the robust adjustments mentioned, the basic BCA's historical assumption fails for such events.  
* **Subjectivity of Adjustments:** While simple, the choices regarding adjustments (e.g., selection of base period, treatment of large claims, trending factors) often require considerable actuarial judgement. The initial crude assumptions are replaced by subjective, yet necessary, adjustments.

#### **Use Cases for the Burning Cost Approach**

Despite its limitations, the BCA is particularly useful in specific scenarios where its underlying simplicity and lower data requirements are advantageous:

* **New Lines of Business:** Appropriate when there is no internal historical data, necessitating estimates based on external data or judgement.  
* **Sparse Data:** Commonly used when historical data for a risk is too sparse to derive a credible price using more complex techniques, such as for **excess of loss reinsurance pricing** where lack of data may prohibit a frequency-severity approach.  
* **Large Commercial Risks:** Applied in pricing large commercial risks where historical experience can be used to derive an individual rate.  
* **Starting Point:** Serves as a simple starting point for pricing various types of insurance and reinsurance.  
* **Experience Rating:** Forms the basis of some experience rating systems where premium adjustments are based on the total cost of claims incurred for a policyholder over a defined period.

In conclusion, while the Burning Cost Approach offers a pragmatic and accessible method for general insurance pricing, its utility is critically dependent on understanding and appropriately managing its inherent assumptions. Actuaries must exercise significant professional judgement to transform a simple historical average into a credible prospective risk premium by diligently applying necessary adjustments for development, trends, and exceptional losses.

