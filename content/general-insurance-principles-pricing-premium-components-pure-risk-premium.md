Alright team, let's break down the concept of the 'Pure Risk Premium' within the broader context of 'Premium Components' for SP8. As your Specialist Actuarial Note Builder and Exam Coach, my goal is to ensure you grasp this fundamental principle thoroughly. This is a core part of your syllabus, so let's build these notes logically and sequentially, just as you'd approach a complex exam question.

---

### **SP8: General Insurance Pricing Specialist Principles \- Structured Notes**

#### **Chapter 1: The Core Concept of Pure Risk Premium**

At the heart of general insurance pricing lies the **Pure Risk Premium**, also frequently referred to as **Loss Cost** or **Burning Cost**. This is the fundamental amount of premium that is required to *exactly* cover the expected cost of claims alone. It is "purely" attributable to loss. Crucially, it makes no initial allowance for expenses, profit, or other loadings.

For example, if a policy has a 10% probability of a £1,000 claim and no claim otherwise, the pure risk premium would be £100.

#### **Chapter 2: Pure Risk Premium vs. Office Premium (The Full Price)**

It's vital to understand that the Pure Risk Premium is *not* the final price the insured pays. The actual market price, known as the **Office Premium** or **Technical Premium**, is derived by adding various loadings to the Pure Risk Premium. These loadings cover elements beyond just the expected claims.

The final output of the ratemaking process is the information necessary to modify existing rating manuals or create new ones, which then inform how the premium is calculated based on a given rate per unit of risk exposed.

#### **Chapter 3: Deriving the Pure Risk Premium \- Methods and Components**

The determination of the pure risk premium is often the major part of the actuarial work in ratemaking. It primarily involves estimating future loss and loss adjustment expenses (LAE).

##### **3.1 Methods for Calculation**

The sources outline two main approaches for calculating the pure risk premium:

###### **3.1.1 Frequency-Severity Approach**

This approach involves estimating the expected claim **frequencies** (number of claims per exposure) and **severities** (average cost per claim) separately, and then combining them to determine the expected loss cost.

* **Formulaic Representation:** Pure risk premium \= Expected claim frequency × Expected cost per claim.  
  * For instance, in private motor insurance, if the expected claim frequency is 25% per vehicle-year and the expected cost per claim is £1,200, the pure risk premium per vehicle-year is £300 (0.25 × £1,200).  
* **Application:** This method is particularly useful where excesses, deductibles, or limits apply. It's commonly used for commercial risks, especially in liability classes, where a single risk can give rise to numerous claims.  
* **Data Requirements:** It requires more granular data to parameterise separate frequency and severity distributions compared to aggregate methods.  
* **Advantages:** It provides information about how both claim numbers and claim amounts are expected to develop, helps identify and allow for distortions, and spot/project trends. It's also suitable for combining with other projection techniques like chain ladder and Bornhuetter-Ferguson.

###### **3.1.2 Burning Cost Approach**

This is a simpler, direct method that calculates the risk premium as the actual cost of claims during a past time period, expressed as an annual rate per unit of exposure. It essentially takes the total claims divided by the total exposure to risk.

* **Application:** Often used as a starting point for pricing certain types of insurance and reinsurance. It's also used for pricing excess of loss reinsurance contracts.  
* **Limitations:** It tends to ignore trends like claims inflation and can understate the ultimate position by comparing current exposure with current incurred claims, potentially leading to higher-than-planned loss ratios if not adjusted. It can also lose information on trends by not considering frequency and severity separately.  
* **Data Requirements:** Requires historical claims experience, adjusted for past inflation and developed to ultimate levels (including IBNR and outstanding claims).

##### **3.2 Components of the Premium Rate**

The sources highlight that the pure risk premium, when expressed per unit of exposure, can be broken down into:

* Total claim amount / Total exposed to risk.  
* This can further be disaggregated as: (Number of claims / Exposure) × (Total claim amount / Number of claims), which corresponds to **Expected claim frequency × Expected cost per claim**.  
* For certain classes like household contents, where expressing claim frequency per unit of exposure feels "odd" (e.g., 2% per £1,000 sum insured), it can be broken down into three factors:  
  * Claim frequency per policy.  
  * Average unit of exposure per policy.  
  * Average cost per claim.

#### **Chapter 4: Adjustments and Considerations for Pure Risk Premium Analysis**

When calculating the pure risk premium, several critical adjustments and considerations must be made to ensure accuracy and relevance for future policy periods.

##### **4.1 Data Collection and Adjustment**

The process begins with collecting reliable and relevant policy and claims data. This data then needs to be adjusted and grouped.

* **Internal vs. External Data:** Internal historical data is generally preferred, but external data (e.g., industry data, competitor information, reinsurer data, publicly available information like flood data) is invaluable, especially for new products or sparse internal data.  
* **Data Quality:** Be aware of potential data errors, such as inaccurate claim/policy details. The quality and quantity of data significantly impact the quality of the final rates.  
* **Grouping Data:** Data should be grouped into homogeneous risk categories for credible estimates. Different claim types (e.g., property damage, bodily injury) or perils (e.g., flood, theft) may need separate modeling due to differing rating factors and trends.

##### **4.2 Treatment of Large and Catastrophe Claims**

Catastrophic and large non-catastrophe claims are often removed from the attritional (normal) claims data for reliable analysis due to their distorting effect and unique development profiles. However, their expected cost must still be reflected in the premium.

* **Catastrophe Losses:** These are highly volatile, and their pricing heavily relies on proprietary catastrophe models (e.g., RMS, AIR, EQECAT), which are discussed in detail in Chapter 21\. Appendix B provides an example of deriving a non-modeled catastrophe pure premium.  
* **Large (Non-Catastrophe) Losses:** For these, actuaries might omit them from the analysis and allow for them separately, or truncate them at a set point and spread the excess cost across a larger portfolio of risks. The "basic limit" concept is relevant here; rate level indications might assume all insureds choose the basic limit, and the effect of losses beyond this limit is considered in classification ratemaking.

##### **4.3 Trends and Future Projections**

The pure risk premium must reflect future conditions, which requires trending historical data.

* **Inflation:** Historical data needs to be inflated to the present day using known inflation rates and then projected into the future using estimated future inflation rates. This is crucial for inflation-sensitive exposure bases like payroll or gross revenue.  
* **Frequency and Severity Trends:** Changes in the likelihood and average cost of claims, as well as changes in exposure levels, are considered. These can be projected separately, or underlying elements of risk in the base data can be separated, projected, and then combined with explicit assumptions about the future mix of these risks.  
* **Policy Conditions:** Changes in policy conditions, such as perils covered, limits, or excesses, must be accounted for. If a new peril is introduced, external data may be needed to approximate the likely cost.  
* **Exposure Trend:** For exposure bases expressed in monetary units (e.g., sum insured), these need to be projected at an appropriate inflation rate to the midpoint of the exposure period under the new rates.

##### **4.4 Actuarial Control Cycle & Assumptions**

The estimation process for the pure risk premium is an application of the actuarial control cycle. It involves:

* Collecting and adjusting data.  
* Selecting and analyzing an appropriate rating model.  
* Setting and testing assumptions (e.g., for goodness of fit, likelihood probability).  
* Running the model to estimate future claims costs.  
* Performing sensitivity and scenario testing to check validity.  
* It's vital to acknowledge process, model, and parameter uncertainty, and not to blindly exclude "abnormal" claims that might turn out to be normal.

#### **Chapter 5: Loadings to Convert Pure Risk Premium to Office Premium**

Once the Pure Risk Premium is estimated, various loadings are applied to arrive at the Office Premium, which is the actual price charged to the policyholder.

##### **5.1 Reinsurance Costs**

Reinsurance is insurance purchased by primary insurers to transfer some financial risk. The cost of reinsurance is incorporated into the premium rate, either as a net cost (if the premium is based on a gross risk premium) or as a gross cost (if based on a net risk premium). As reinsurance costs have increased, some ratemaking analyses are now performed on a net basis.

##### **5.2 Expenses**

Expenses represent a significant portion of insurance costs.

* **Types:** These include acquisition costs (e.g., commission), policy administration costs, claim handling costs (Loss Adjustment Expenses \- LAE), and overheads. LAE is often included with losses when calculating pure premium or loss ratios.  
* **Fixed vs. Variable:** Expenses can be categorized as fixed (constant per risk) or variable (percentage of premium).  
  * The "All Variable Expense Method" treats all expenses as a constant percentage of premium, which can distort rates by understating premium needs for small policies and overstating for large ones.  
  * The "Premium-based Projection Method" separates fixed and variable expenses, often deriving fixed expenses as a percentage of premium, which can then be converted to a per-exposure amount for the pure premium approach. This method can still create inequitable rates for regional carriers if countrywide ratios are used.  
  * The "Exposure/Policy-based Projection Method" is another procedure for deriving expense provisions.  
* **Analysis:** Expense analysis involves allocating direct and indirect expenses. It's crucial to include likely future expenses and exclude exceptional past expenses.

##### **5.3 Profit Provision / Cost of Capital**

Insurers aim for a target underwriting profit, which is a key component of the fundamental insurance equation.

* **Purpose:** This loading contributes to the servicing of the insurer’s capital, ensuring it achieves a required return. It can also be seen as a compensation for the "capital call cost" – the risk loading for potential erosion of capital through transfer to reserves and eventual payout in claims.  
* **Determination:** The profit loading can be derived from a profit target (e.g., as a percentage of premiums), a target return on capital (ROC) or return on equity (ROE), or a target loss/combined ratio. Riskier lines of business typically require higher profit margins.  
* **Mathematical Inclusion:** In the pure premium method, the profit provision (along with variable expenses) is included in the denominator as a "permissible loss ratio" (1 \- variable expense % \- target profit %).

##### **5.4 Investment Income**

Premiums collected by insurers generate investment income before claims and expenses are paid out. This investment income is typically treated as a "negative loading," reducing the premium charged to the insured. This is more significant for long-tailed lines of business where there's a longer period between premium payment and claim settlement.

##### **5.5 Tax and Dividends**

Allowances for tax and dividends (payments to shareholders) also form part of the overall premium calculation. The treatment of investment return (gross or net of tax) depends on the company's tax structure.

#### **Chapter 6: Final Rate Determination and Practicalities**

After the technical calculation of the pure risk premium and the application of loadings, the final rates are determined, taking into account broader business considerations.

##### **6.1 Rating Manuals**

The rating manual is the official document containing the rules, rate pages, rating algorithms, and underwriting guidelines necessary to classify each risk and calculate the premium. The final rates derived from the ratemaking process are used to modify existing manuals or create new ones.

##### **6.2 Exposure Bases**

An **exposure** is the basic unit measuring a policy's exposure to loss, serving as the basis for premium calculation.

* **Criteria for Selection:** A good exposure base should be directly proportional to expected loss, practical, and consistent with industry standards.  
* **Types:** Exposures can be written, earned, unearned, or in-force. Aggregation methods include calendar year and policy year.  
* **Large Commercial Risks:** These may use composite rating or loss-rated composite rating, where a proxy measure gauges overall exposure change.

##### **6.3 Overall Rate Level Indication Methods**

Two primary methods combine the estimated components of the fundamental insurance equation (premium, loss, expense) to ascertain the appropriate overall rate level or rate level change for a future policy period.

* **Pure Premium Method:** Projects average loss and LAE per exposure and average fixed expenses per exposure, then adjusts for variable expenses and target profit. It determines an *indicated average rate*. It is preferable if premium data is unavailable or difficult to calculate accurately, and *must* be used for new lines of business with no current rates to adjust.  
* **Loss Ratio Method:** Relies on the projected loss ratio (projected ultimate losses and LAE divided by projected premium at current rate level). It calculates an *indicated change* to currently charged rates. It requires premium at current rate level.  
* **Equivalency:** The two methods are mathematically equivalent but offer advantages/disadvantages in certain circumstances.  
* **Premium Adjustments:** For loss ratio analysis, historical premium data often needs adjustments for current rate level, premium development (due to premium audits), and premium trend. These adjustments are not *required* for the pure premium approach, though they may still be calculated for comparison.

##### **6.4 Classification Ratemaking**

While overall rates ensure aggregate adequacy, **classification ratemaking** focuses on ensuring equity at the individual risk or risk segment level. This involves grouping risks with similar loss potential and charging different manual rates based on their characteristics, known as **rating variables**.

* **Importance:** Failure to recognize risk differences leads to inequitable rates and adverse selection, where lower-risk insureds leave for more competitively priced policies elsewhere.  
* **Methods for Rate Differentials:**  
  * **Univariate Methods:** Examine the loss experience (pure premium or loss ratio) of levels within each rating variable.  
    * **Pure Premium Approach:** Compares expected pure premiums for each level of a rating variable to determine indicated relativities. It assumes a uniform distribution of exposures across other rating variables, which can lead to distortion if exposure correlations exist (e.g., disproportionate number of high-value homes in a territory).  
    * **Loss Ratio Approach:** Compares loss ratios for each level to the total loss ratio to determine adjustments to current relativities. It helps adjust for distributional bias.  
    * **Adjusted Pure Premium Approach:** Attempts to minimize distributional bias by adjusting exposures by the exposure-weighted average relativity of all other variables.  
  * **Multivariate Techniques:** Extensions of univariate methods that address their shortcomings by accurately accounting for the effect of multiple rating variables simultaneously. Generalized Linear Models (GLMs) are a commonly used multivariate method. They can model claim frequency and severity separately, and their outputs (theoretical risk premiums) need further adjustment for market factors.  
* **Criteria for Rating Variables:** Statistical (e.g., direct proportionality to loss), operational (e.g., data availability, practicality), social (e.g., public acceptance), and legal (e.g., non-discriminatory) criteria are considered.

##### **6.5 Credibility Procedures**

Credibility theory blends observed experience (direct data) with broader, more stable experience (ancillary data or complement of credibility) to produce a more reliable estimate, particularly when the observed data is sparse or volatile.

* **Classical Credibility:** Determines how much weight (credibility) to assign to an observed value based on the volume of data (e.g., number of claims) relative to a "full credibility standard".  
* **Bayes Credibility (e.g., Bühlmann-Straub Model):** Offers a theoretical framework for blending different data sources, providing a credibility-weighted estimate as a weighted average of observation and other information.  
* **Complement of Credibility:** This is the related data that is blended with the original actuarial estimate. Desirable qualities include independence from the observed experience, logical relationship, and availability. Examples include loss costs of a larger group, trended present rates, or competitor rates.  
* **Practical Uses:** Credibility models are widely used in experience rating plans. They help decide how much to charge an individual risk for its own past experience, especially for large or unusual claims.

##### **6.6 Rating Mechanisms for Large Commercial Risks**

For large commercial risks, traditional manual ratemaking may not be feasible due to heterogeneity and the availability of individual risk experience. Special techniques are employed:

* **Experience Rating:** The premium for an individual risk depends, at least in part, on its actual claims experience. It can be prospective or retrospective, and based on claim numbers or amounts.  
* **Schedule Rating:** Alters the manual rate based on subjective characteristics of the risk not captured by the manual rates or experience rating.  
* **Loss-Rated Composite Risks:** Premium is calculated based on the individual risk's historical loss experience, without standard rating algorithms. The implicit exposure base is the risk itself.  
* **Large Deductible Policies:** Priced similarly to standard deductible policies but with special considerations for ALAE treatment and profit margins reflecting increased risk.  
* **Retrospective Rating:** Uses the individual entity's experience *during the policy period* to establish the final rate, within a predetermined minimum and maximum premium range.

##### **6.7 Other Influences on Final Rates**

Beyond technical actuarial indications, company management considers various factors when determining actual rates:

* **Regulatory Constraints:** Regulators may require filing rates, impose rate maxima/minima, or restrict rating factors.  
* **Operational Constraints:** System capabilities, administrative costs, and the sophistication of sales and quoting systems can influence rating decisions.  
* **Market Conditions:** Competition, market share goals, competitive comparisons (e.g., base rate advantage, individual risk competitiveness), and price elasticity of demand are crucial. Insurers may deviate from theoretical rates to gain/maintain market share or maximize profit in specific segments.  
* **Company Strategy:** Availability of capital, reinsurance capacity, and desired return on capital also influence pricing.

---

By structuring your understanding in this detailed and sequential manner, you'll be well-equipped to tackle any SP8 exam question on Pure Risk Premium and its context within premium components. Keep practicing those numerical examples in the appendices – they really bring these concepts to life\!

