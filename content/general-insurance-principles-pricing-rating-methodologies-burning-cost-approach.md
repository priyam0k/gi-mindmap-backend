Alright team, let's dive deep into the Burning Cost Approach (BCA) and solidify its place within our arsenal of general insurance rating methodologies. As Specialist Actuarial Note Builders and Exam Coaches for SP8, it's crucial for us to not just memorise definitions, but truly understand the mechanics, applications, and comparative strengths of each technique.

#### **1.1 Definition and Core Concept**

At its heart, the Burning Cost Approach calculates the risk premium by taking the actual cost of claims during a past period, expressed as an annual rate per unit of exposure. You can think of it quite simply as an average claim cost per year, per unit of exposure. The fundamental formula for burning cost is the sum of claims divided by the total exposure to risk (∑ Claims / Total Exposed to Risk). This method typically *ignores* the number of claims, focusing instead on the aggregate total cost of claims.

The BCA is essentially an experience rating approach, meaning it uses the historical claims experience to derive a rate. It can be applied to rate an individual risk or a portfolio of similar risks. The concept of the "pure risk premium" (the amount required to cover the expected claim amount only, without allowance for expenses or profit) is a foundational element that the burning cost approach directly estimates.

#### **1.2 Context within Rating Methodologies: The Cost-Plus Approach**

The SP8 syllabus largely concentrates on the 'cost-plus' approach to pricing. This framework involves setting the price based on a statistically driven analysis, using the expected cost of claims, which are then appropriately loaded for expenses, profit, and so on. The BCA is a prime example of this 'cost-plus' approach, providing a simple method for determining the *pure risk premium* – the expected cost of claims in the period for which the premiums will apply.

The overall objective of ratemaking is to determine rates that will produce premium for a future policy period equivalent to the sum of the expected costs (i.e., losses and expenses) and the target underwriting profit. The pure premium method, one of the two main overall rate level methods discussed in Chapter 8, determines an indicated average rate and directly uses projected average loss and loss adjustment expenses per exposure, without requiring premium at current rate level. This aligns well with the burning cost, which is a direct measure of average loss per exposure.

After calculating the pure risk premium using BCA, various loadings are applied to arrive at the 'office premium'. These loadings typically account for:

* Cost of reinsurance  
* Expenses (including commission)  
* Profit and contingencies (i.e., return on capital)  
* Investment income (as a deduction, as a more sophisticated approach allows for the expected level of investment income under current investment conditions by discounting expected future claims and expenses to the date premium is received).  
* Tax

#### **1.3 Assumptions and Data Requirements**

The data required for the BCA, similar to any cost-plus approach, includes policy data (for exposure and identifying characteristics of each risk group) and claims data (for estimating the ultimate cost of claims). Specifically for BCA, policy data is needed to calculate overall exposure or the split within each risk group, requiring information on dates on cover and all rating factor and exposure measure details for each policy.

A crucial aspect of BCA is that it is often used when *less data is available*, sometimes only aggregated claims data by policy year. This contrasts with more data-intensive methods like the frequency-severity approach that require individual loss data. Even if only aggregated data is available, it is often possible to obtain details of large and catastrophic claims to remove and treat differently.

A crucial assumption is that historical experience, after adjustments, is representative of future costs. However, the raw, unadjusted burning cost approach might operate without any explicit allowance for:

* Future inflation  
* Development of losses to obtain ultimate claims (including IBNR and outstanding claims)  
* Past inflation or other trending adjustments

This is a significant point for your exam, as it highlights the simplicity but also the potential crudeness of the method if not properly refined.

#### **1.4 Adjustments and Practical Considerations**

To make the historical burning cost relevant for estimating future premium, several adjustments are essential to transform the "actual cost of claims" into a reliable predictor for the future:

1. **Inflation/Trending:** Historical data needs to be adjusted for economic and social inflation (e.g., changes in judicial decisions, litigiousness) to reflect current cost levels. This involves inflating base values to the present day using known inflation rates and then projecting to the future using estimated future inflation rates. While frequency-severity approaches apply separate frequency and severity trends, for BCA, where these aren't separated, both the exposure and the claims data should be adjusted. Different approaches to trending can be taken, and the level of accuracy will vary, with some crude approaches making no adjustments at all.  
2. **Loss Development:** Unless a very crude approach is being taken, the claims information used for burning cost should be developed to ultimate values, including IBNR (incurred but not reported) and IBNER (incurred but not enough reported) claims. Standard reserving techniques, such as the chain ladder or Bornhuetter-Ferguson methods, could be used to calculate the ultimate overall claims for each development year. Since individual loss information might not be available, IBNR factors might be calculated from either the individual risk data or the aggregated results of a book of business.  
3. **Large/Catastrophe Losses:** Catastrophe claims are usually omitted from the analysis because their low frequency and high severity can distort the underlying risk, and they are typically modelled using specialised catastrophe modelling systems. For large non-catastrophe losses, actuaries might omit them from the analysis and allow for them separately in the risk premium, or truncate large claims at a set point and spread any cost above this level across the larger portfolio of risks. The decision depends on the extent to which such claims are expected to recur during the exposure of the new rating series.  
4. **Policy Conditions:** Adjustments to premiums will also be required when an individual policyholder alters the basis of risk.  
5. **Data Quality:** Even with limited data, efforts should be made to ensure it is reliable and relevant. Incomplete, inaccurate, or sparse data can lead to issues like unprofitable or uncompetitive rates, or anti-selection. Erroneous data can also lead to false accounting, inappropriate reserving, wrong pricing, and general management mistakes.

In practice, the construction of the burning cost, like most actuarial methods, can be difficult due to uncertainties in estimating and/or selecting appropriate curves or assumptions. Judgement becomes key, especially when data is sparse, and it's important to monitor emerging results closely.

#### **1.5 Advantages and Disadvantages**

When comparing the BCA to other methods, particularly the frequency-severity approach, several points emerge for exam readiness:

**Advantages of Burning Cost Approach:**

* **Simplicity:** It's generally easy to understand and communicate, particularly to non-technical colleagues.  
* **Less Data Intensive:** Requires relatively little data, often only aggregated claims data, making it useful when detailed data is scarce or if individual case estimates are unavailable.  
* **Quicker:** It is a quicker method to perform compared to more complex approaches.  
* **Experience-Focused:** Allows for the direct use of an individual risk's or portfolio's actual experience.  
* **Consistency:** The loss costs obtained should be internally consistent.  
* **Utility with Sparse Data:** Particularly useful where little or no credible loss data is available, such as for high excess layers.

**Disadvantages of Burning Cost Approach:**

* **Ignores Underlying Process:** It doesn't mirror the underlying claims generation process (frequency and severity), which can lead to a less granular understanding of risk drivers.  
* **Potential for Understatement:** If unadjusted for inflation, trends, and development (IBNR/IBNER), it can significantly understate the ultimate loss position, leading to higher-than-planned loss ratios. This is a critical point that needs careful consideration.  
* **Loss of Information on Trends:** By not considering frequency and severity separately, much information on specific trends (e.g., changes in accident frequency vs. average claim cost) might be lost.  
* **Less Accuracy:** Generally considered less accurate than the frequency-severity approach, especially for complex insurance structures.  
* **Subjectivity:** Can be highly subjective if not adequately adjusted, and the assumptions (e.g., selection of base period or inflation rates) require careful judgement.

#### **1.6 Applications of Burning Cost Approach**

The BCA finds its primary applications in situations where data limitations or the nature of the risk make more complex methods impractical:

* **Individual Commercial Risks:** It's a common method for rating single commercial risks.  
* **Excess of Loss Reinsurance:** Frequently used for pricing excess of loss (XL) reinsurance contracts, especially for higher layers where claims data is sparse or changes in contract structure are hard to assess. This is because the claims experience for such business is highly volatile, limiting reliance on historical data.  
* **Stop Loss Reinsurance:** Similar to other XL reinsurance, stop loss contracts are priced using methods akin to BCA, often involving modelling loss ratios from historical experience.  
* **New Lines of Business:** When a company introduces a new product and has insufficient internal historical data, BCA (or a variant thereof) can be used, possibly supplemented by external or bureau data.

#### **1.7 Relationship to Other Rating Methodologies and Concepts**

Understanding BCA's place requires comparing it with other key methodologies:

* **Frequency-Severity Approach (F-S):** The F-S approach assesses expected loss cost by estimating and combining expected claim frequencies and severities. It explicitly models the underlying process (claims occurring with a certain frequency and each having a value), which is readily understood by underwriters. This method requires more onerous data (both quality and quantity) and expertise, making it more time-consuming. While BCA ignores the number of claims, F-S separates these components, allowing for distinct analysis of frequency and severity trends. When data is plentiful and reliable, F-S is often preferred for its greater accuracy and deeper understanding of risk drivers.

* **Generalised Linear Models (GLMs) and Multivariate Models:** GLMs and other multivariate techniques are advanced statistical methods that consider all rating variables simultaneously, automatically adjusting for exposure correlations, and attempting to remove unsystematic effects (noise) from the data. They provide valuable model diagnostics and can incorporate interactions between variables. BCA, being a simpler, often univariate method, does not inherently adjust for these complex interdependencies and can be distorted by exposure correlations. While GLMs are widely used for personal lines and small commercial risks due to their sophistication and transparency, BCA remains relevant where the data volume, detail, or complexity doesn't support a full GLM analysis. Multivariate approaches are often preferred to address distortions inherent in univariate techniques.

* **Credibility Theory:** Credibility theory blends estimates based on observed (subject) experience with external or related experience, especially when subject data is limited or unstable. The BCA, as an experience-based method, often incorporates credibility concepts, particularly when the individual risk's experience is not fully credible. For instance, the Cape Cod method, a variation of BCA, is an objective way of deriving a weighted average where the weight applied to each year depends on the expected proportion of claims developed and proximity to the origin year. This helps to provide more stable estimates by blending sparse data with broader, more reliable information.

* **Exposure Rating:** The sources distinguish BCA as an 'experience rating' approach, which relies on the insured's own past data. In contrast, 'exposure rating' bases premium rates on the amount of risk (exposure) without using historical claims experience of that specific insured, often relying on external benchmarks. Exposure rating for property reinsurance, for example, heavily uses 'exposure curves' or 'first loss scales'.

* **Original Loss Curves (ILFs/First Loss Scales):** These are often used to infer prices for layers where data is too sparse to derive a credible experience rate, such as in excess of loss pricing. They are related to Increased Limit Factors (ILFs). While BCA is a direct calculation from aggregated historical losses, ILFs and original loss curves allow for the pricing of specific layers or limits based on the shape of the loss distribution, which is crucial when aggregate data for high layers is unreliable.

* **Catastrophe Models:** BCA, and traditional rating approaches generally, are far less appropriate for low-frequency, high-severity risks like catastrophes because observed losses may not reflect the true underlying risk over short historical periods, and some event scenarios may never have occurred previously. Catastrophe models are specialized tools that predict future losses from such events, often by simulating scenarios, and are the key tool for pricing property catastrophe reinsurance.

* **Relationship to Reserving:** While pricing and reserving have distinct purposes and assumptions, the BCA, particularly its underlying ultimate loss estimates, can inform the reserving process. For instance, rate indices derived from pricing monitoring exercises can be used to adjust a priori loss ratios (often called initial expected loss ratios) in Bornhuetter-Ferguson reserving methods, which combine an expected level of claims (from a loss ratio method) with a projection based on experience to date (from a chain ladder method).

In conclusion, the Burning Cost Approach, though simpler and potentially less accurate than its more sophisticated counterparts like the frequency-severity or GLM approaches, remains a valuable tool in the actuarial toolkit. Its primary strength lies in its applicability when data is limited or highly volatile, making it a pragmatic choice for individual commercial risks, new lines of business, and various forms of reinsurance. Understanding its advantages, limitations, and how it fits into the broader spectrum of pricing methodologies is absolutely essential for your SP8 success. Keep practising those applications\!

