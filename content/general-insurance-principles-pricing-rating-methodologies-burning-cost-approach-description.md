Alright, aspiring SP8 actuaries, let's delve into the Burning Cost Approach, a fundamental pricing methodology in general insurance. As your Specialist Actuarial Note Builder and Exam Coach, I'll guide you through its description, inner workings, and practical applications, drawing directly from our core SP8 material.

### **📗 Chapter 14: Rating using Frequency-Severity and Burning Cost Approaches (and related chapters)**

#### **The Burning Cost Approach: A Core Pricing Method**

The Burning Cost Approach is one of the key pricing approaches you must master for SP8, alongside the frequency/severity methods and original loss curves. It is commonly utilised within the 'cost plus' approach to ratemaking, aiming to estimate the expected cost of claims for the future policy period, which then forms the basis of the risk premium.

#### **Description of the Burning Cost Approach**

At its core, the Burning Cost Approach is a straightforward method for determining a risk premium. It calculates the risk premium as the **actual cost of claims during a past time period, expressed as an annual rate per unit of exposure**. You can conceptually think of it as simply the average claim cost per year, per unit of exposure.

More formally, the burning cost is typically defined by the following formula: $$ \\text{Burning Cost Premium (BCP)} \= \\frac{\\sum \\text{Claims}}{\\text{Total Exposed to Risk}} $$

Unlike the frequency-severity approach, the burning cost method primarily **uses historical aggregate claims data and does not explicitly make use of the number of claims (frequency)**. It directly projects the total claims relative to the total exposure to arrive at the risk premium. This method can be applied to rate an individual risk or a portfolio of similar risks.

#### **Key Characteristics and Underlying Assumptions**

1. **Simplicity and Directness:** The burning cost approach is generally considered simpler and more direct compared to other methods, such as the pure premium method for overall rate indication or the frequency-severity approach. Its ease of calculation requires relatively little data, making it quicker to perform.  
2. **Reliance on Aggregate Data:** The method fundamentally operates on aggregated historical claims data. While individual case estimates might be incorporated, it doesn't break down losses into frequency and severity components in its basic form.  
3. **Historical Basis:** The calculation is based entirely on historical data, often using a simple regression model. This implicitly assumes that past experience is a reasonable indicator of future experience, especially if no explicit adjustments are made.  
4. **Implicit Allowance for Trends:** In its crudest form, the burning cost approach may make **no allowance** for future inflation, development of losses to ultimate (IBNR and outstanding claims), or even past inflation or other trending adjustments. This can lead to significant understatement of the ultimate position and potentially higher-than-planned loss ratios.

#### **Data Requirements**

For the burning cost approach, you primarily need reliable and relevant policy data and claims data.

* **Policy Data:** This is crucial for calculating the overall exposure or splitting it within risk groups. It includes dates on cover, and details of all rating factors and exposure measures.  
* **Claims Data:** This is required to estimate the ultimate cost of claims. Often, only aggregated claims data by policy year is available when this method is used. If available, details of large and catastrophic claims should be captured separately for different treatment. Ideally, data should be gross of reinsurance and "from the ground up".

The quality and quantity of data are paramount for the quality of the final rates. When data is limited, actuaries must understand the impact and examine the sensitivity of results to assumptions.

#### **Practical Considerations and Adjustments**

While the basic burning cost approach can be very crude, it can be refined through various adjustments to make historical data relevant for estimating future premiums.

1. **Developing Losses to Ultimate:** Unless a very crude approach is taken, the claims information should be developed to their ultimate values. This involves using standard reserving techniques such as the chain ladder or Bornhuetter-Ferguson methods to account for reported but not fully settled claims, and claims incurred but not yet reported (IBNR). For reinsurance business, this also includes incurred but not enough reported (IBNER) development.  
2. **Trending:** Historical data needs to be adjusted to make it relevant for the future period when new premium rates will apply. This process, often called 'trending' or 'on-leveling', accounts for changes in various factors. While the frequency-severity approach applies separate frequency and severity trends, the burning cost approach, when trends cannot be separated, adjusts the aggregate data. Factors influencing trends include economic (inflation, conditions), legal (legislation, court rulings), technical changes, insurance-related factors (policy conditions, underwriting), and changes in business volumes or structure.  
3. **Treatment of Large and Catastrophe Losses:** Catastrophe claims are usually omitted from the primary burning cost analysis and handled separately, often using outputs from catastrophe modelling systems due to their infrequent and extreme nature. For large non-catastrophe losses, actuaries may:  
   * Omit them from the analysis and allow for them separately in the risk premium.  
   * Truncate them at a set point and spread the excess cost across the larger portfolio.  
   * Remove them altogether. The decision depends on the expected recurrence of such claims.  
4. **Effective vs. Indexed Burning Cost:** The burning cost can be calculated using unadjusted data (effective burning cost) or indexed data (indexed burning cost). The latter incorporates adjustments for inflation.  
5. **Exposure Measure:** A suitable exposure measure is essential, such as policy count or premium net of acquisition costs. For personal lines, earned car years or house years are common. For workers compensation, payroll is typically used. It's vital that the exposure base is proportional to expected loss, practical, and consistent over time.  
6. **Coordination of Trends:** When determining the overall rate level, ensuring consistency in trending across all components (exposure, premium, and loss) is important, particularly for lines with inflation-sensitive exposure bases.

#### **Use Cases and Applications**

The Burning Cost Approach is particularly useful in specific scenarios:

* **New Lines of Business:** It is often appropriate for pricing new lines of business or in situations where premium at the current rate level is difficult to calculate.  
* **Sparse Data:** It is commonly used when historical data for a risk is too sparse to derive a credible price using more complex techniques. This is frequently the case for **excess of loss reinsurance pricing**, where a lack of data may prohibit a frequency-severity approach.  
* **Large Commercial Risks:** It is applied in pricing large commercial risks where historical experience can be used to derive an individual rate.  
* **Starting Point for Pricing:** It serves as a simple starting point for pricing various types of insurance and reinsurance.  
* **Experience Rating:** It forms the basis of some experience rating systems where premium adjustments are based on the total cost of claims incurred for a policyholder over a defined period.

#### **Advantages of the Burning Cost Approach**

* **Simplicity and Ease of Understanding:** It is straightforward to implement and relatively easy to explain to non-technical colleagues.  
* **Lower Data Requirements:** It needs relatively little data compared to more granular methods like frequency-severity. Often, aggregated claims data is sufficient.  
* **Efficiency:** It is quicker to perform than more complex actuarial methods.  
* **Direct Reflection of Experience:** It allows for the direct experience of an individual risk or a portfolio of similar risks to be considered.  
* **Internal Consistency:** When appropriately applied, the loss costs obtained should be internally consistent.

#### **Disadvantages and Limitations**

Despite its simplicity, the Burning Cost Approach has notable limitations:

* **Lack of Granularity/Insights:** By focusing solely on aggregate claims, it "ignores the number of claims" and "loses much of the information on trends being experienced by not considering frequency and severity separately". This limits the understanding of underlying drivers of loss.  
* **Understating Ultimate Position:** If the approach does not properly account for inflation, trends, and claims development (IBNR, IBNER), it will likely "understate the ultimate position," leading to rates that result in higher-than-planned loss ratios.  
* **Sensitivity to Data:** Its reliance on historical data means it can be highly sensitive to unusual or one-off events in the experience period if not adequately adjusted.  
* **Heterogeneity Distortion:** For classification ratemaking, the univariate pure premium (burning cost) approach can be distorted if it assumes a uniform distribution of exposures across other rating variables, ignoring correlations and potentially "double counting" effects.  
* **Not Suitable for Low-Frequency, High-Severity Risks (without adjustments):** For catastrophe risks, observed historical losses may not reflect true underlying risks, as the observation period might be shorter than the return period of the losses. Traditional burning cost methods are less appropriate for such low-frequency, high-severity events.  
* **Subjectivity:** While simple, the choices regarding adjustments (e.g., selection of base period, treatment of large claims, trending factors) often require considerable actuarial judgement.

In essence, while the Burning Cost Approach provides a robust and practical starting point, particularly when data is sparse, actuaries must exercise significant judgement and apply appropriate adjustments to transform a simple historical average into a credible prospective risk premium.

