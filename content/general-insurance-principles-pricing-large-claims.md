Of course. As your SP8 Exam Coach, let's construct a comprehensive, structured note on the treatment of **Large Claims** (also referred to as shock losses) within the critical context of **Data Quality Issues**. This is a highly important topic for the SP8 exam. Failure to properly identify and adjust for large, non-recurring losses can introduce significant instability into the ratemaking process, leading to rates that fluctuate wildly and are poor predictors of future underlying costs. The principle of "Garbage In, Garbage Out" (GIGO) applies here; unadjusted data containing shock losses can corrupt pricing models and produce flawed results.

### **📗 Data Quality Issues: Large Individual Claims (Shock Losses)**

When using historical data to project future costs, actuaries must ensure the data is a reliable and relevant predictor. Excessively large individual losses, often called shock losses, happen infrequently but are an expected part of the insurance world. Examples include a large multi-claimant liability claim, a total loss on an exceptionally high-valued home, or a total permanent disability claim for a young worker.

While a very large portfolio can sometimes absorb the effects of these shock losses, their inclusion in a smaller portfolio's ratemaking analysis can introduce significant instability and distort the results.

#### **🔹 1\. The Problem: Why Large Claims are a Data Quality Issue**

Including actual, unadjusted shock losses in a standard ratemaking analysis can severely compromise the quality and relevance of the historical data for several reasons:

* **Rate Volatility**: Indicated rates may increase significantly immediately after a year with shock losses and decrease just as sharply when those losses fall out of the experience period. This creates undesirable volatility in the premium rates charged to consumers.  
* **Distortion of Analyses**: The presence (or absence) of unusually large claims is likely to distort any analysis unless a suitable adjustment is made.  
  * **Loss Development**: If an extraordinary loss is reported immediately and its ultimate value is reflected early, it can dampen development patterns for that accident year. Conversely, if it is reported late, it can create an artificially high link ratio, distorting the entire development analysis.  
  * **Trend Analysis**: If large losses are not removed from trend data, they can distort the underlying frequency and severity trends. For example, a single large claim will significantly impact severity for a given period.  
  * **Classification Ratemaking**: An extraordinary loss will only impact one level of a rating variable being analysed (eg one territory). Its inclusion would disproportionately affect that level's experience and lead to unreliable relativities.

The core issue is that the historical occurrence of a shock loss is not a good predictor of its future occurrence in a specific year. Therefore, a more stable, long-term approach is required.

#### **🔹 2\. The Solution: Adjusting Historical Loss Data**

To prevent these distortions, the standard actuarial procedure is to remove the distorting portion of large losses from the historical data and replace it with a provision that reflects the long-term expectation of such losses.

##### **🔸 2.1 Identifying and Removing Large Losses**

The first step is to identify and separate large losses from the more predictable "attritional" claims.

* **Establishing a Threshold**: A predetermined threshold is used to cap individual losses. The portion of a claim above this threshold is considered the "excess" or shock loss portion and is removed from the main analysis.  
* **Determining the Threshold**: The actuary must determine a threshold that balances two competing goals: including as much of the loss experience as possible while minimizing volatility. Methods include:  
  * **Basic Limits**: Capping losses at the "basic limit," which is the lowest level of insurance offered and often corresponds to the limit associated with the base rate. If this is done, the premium used in a loss ratio analysis must also be adjusted to a basic limits basis.  
  * **Statistical Thresholds**: Examining the size-of-loss distribution and setting the threshold at a specific high percentile, such as the 99th percentile of either claim counts or loss amounts.  
  * **Percentage of Policy Limit**: For property insurance where the policy limit varies, a fixed dollar threshold may be inappropriate. Instead, a threshold that is a percentage of the amount of insurance can be used.

It is crucial that any large claims removed from the base data are allowed for later to avoid understating the total expected costs.

##### **🔸 2.2 Calculating an Average Expected Large Loss Provision**

Once the excess portion of shock losses is removed, it must be replaced with a stable, long-term provision.

* **Long-Term View**: The provision is calculated based on a longer-term view of the effect of such events. The period should be long enough to produce a stable and reasonable estimate without being so long that the older data becomes irrelevant (eg due to higher jury awards in modern times). A 10-year period for large fire losses or a 20-year period for a small personal umbrella insurer are given as examples.  
* **Excess Loss Factor Method**: A common procedure is to calculate the long-term average ratio of excess losses (the part of claims above the threshold) to non-excess losses (the part below). This ratio is then used to create an "excess loss factor" which is applied to the non-excess losses for each year in the current experience period. This method implicitly assumes that while the proportion of excess losses is volatile in the short run, it is stable over a sufficiently long period.

##### **🔸 2.3 Important Technical Considerations**

* **Interaction with Loss Trending**: The procedure for separating large losses should ideally be performed on loss data that has already been trended to future cost levels. This is because inflation has a **leveraged effect** on excess loss layers—a uniform trend on ground-up losses results in a much higher trend on the excess portion. Ignoring this can introduce bias into the excess loss procedure.  
* **Separate Analysis**: Large losses are likely to have different development patterns than attritional claims. It is normal practice to remove them from the main development triangles and project them separately. Similarly, in a frequency-severity analysis, they should be removed from both the frequency and severity data and allowed for separately later.

In summary, large individual claims represent a significant data quality challenge because their infrequent and severe nature can introduce extreme volatility into pricing analyses. The standard practice of capping these losses at a threshold, removing the excess portion from the core historical data, and replacing it with a stable, long-term expected provision is a crucial step in preparing reliable and relevant data for ratemaking.

