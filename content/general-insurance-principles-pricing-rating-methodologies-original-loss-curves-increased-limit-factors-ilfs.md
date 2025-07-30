Right, Actuarial Trainees, let's consolidate our understanding of Original Loss Curves (OLCs) and Increased Limit Factors (ILFs) within the broader spectrum of Rating Methodologies. This is a critical area for your SP8 exam, as it bridges the gap between theoretical pricing and practical application, especially when faced with data limitations.

### **Original Loss Curves / Increased Limit Factors (ILFs): Practical Considerations in Rating Methodologies**

As your SP8 Exam Coach, I want to emphasise that while our syllabus covers a range of sophisticated rating techniques, understanding OLCs and ILFs is fundamental, particularly for managing sparse data, which is a common real-world challenge. They fall under the **Rating bases and methodologies** section of your syllabus, a core area representing 35% of the content.

#### **1\. Definition and Core Concepts**

At its heart, the purpose of Original Loss Curves (OLCs) and Increased Limit Factors (ILFs) is to infer prices for layers of insurance coverage where the available historical data is simply "too sparse to derive a credible experience rate". This is a crucial distinction that highlights their utility in situations where more traditional, data-intensive methods might fail.

* **Terminology:** While the term 'original loss curves' is "rarely used in general insurance markets", you will commonly encounter related terms. For **property business**, these curves are often referred to as "first loss scales," "exposure curves," or "loss elimination functions". When they show the proportion allocated to an *excess* layer, they are also called "excess of loss scales". For **casualty (liability) business**, the prevailing term is "increased limit factors" (ILFs).  
* **Purpose and Application:** OLCs/ILFs are "frequently used for excess of loss pricing". However, their application extends beyond reinsurance to direct insurance, including "large loss loadings on full-value covers" or "consistent prices for different primary limits".  
* **Components Included:** These curves can be constructed to account for various components beyond just the pure loss cost. They can include "allocated loss adjustment expenses (ALAE) and possibly unallocated loss adjustment expenses (ULAE)" at each limit. Additionally, a "load for risk at each limit," which would typically be "greater for higher limits," can be incorporated.  
* **Mathematical Foundation:** Fundamentally, these curves are "closely related to the original loss distribution". Specifically, they are usually proportional to the **Limited Expected Value (LEV) function**. Key properties of the LEV function that carry over to these curves are that it is an "increasing function (or, strictly speaking, non-decreasing)" and it "increases at a decreasing rate (since S(x) is itself non-increasing), that is, it is a concave function". This means as the limit increases, the expected value of losses up to that limit increases, but the rate of increase slows down. An exception is XL scales, which are related to the complement of the LEV function, making them non-increasing and convex.

#### **2\. Application in Property XL Rating (Exposure Curves)**

For property business, OLCs are used in what is often called "exposure rating" for per-risk excess of loss (XL) treaties.

* **Relative Loss Severity:** A key concept here is the "relative loss severity" (Y \= X/M), where X is the random variable for loss severity and M is a measure of risk size (e.g., sum insured or MPL). This relative measure is used because it helps to ensure the curve is less dependent on the specific size of the risks, meaning a single curve can apply across various policy sizes within a homogeneous group.  
* **Rating Process:**  
  1. The reinsurer needs detailed information on the cedant's risk sizes (e.g., sums insured, MPLs) and premium income. This is often presented as a risk profile with original premiums by sum insured band.  
  2. An appropriate "exposure curve" is selected for each banding of sum insured. Different curves might be used for different perils or risk groupings to account for heterogeneity.  
  3. The "original full value loss cost estimate" is derived from the original premium and loss ratio.  
  4. The "treaty attachment and exit points" are expressed as a proportion of the sum insured, for use with the exposure curve.  
  5. The loss cost to the layer is then calculated using the selected curve.  
* **Catastrophe Losses:** It is a common practice to model the "nat-cat" (natural catastrophe) element of the loss cost separately, often using catastrophe models, and then add this to the cost of other perils. This is because catastrophe claims are typically excluded from traditional burning cost or frequency-severity analyses due to their low frequency and high severity, which can distort historical data.

#### **3\. Application in Casualty XL Rating (Increased Limit Factors \- ILFs)**

For casualty (liability) business, OLCs take the form of ILFs.

* **Key Difference from Property:** Unlike property business, "there is no easily definable upper limit on the possible severity of loss" in casualty insurance. Factors like court awards, insured's budget, and market practice influence limits purchased, rather than solely potential loss severity. Therefore, ILFs are typically "functions of a monetary amount" rather than a relative loss size.  
* **Reference to Basic Limit:** ILFs are usually expressed "with reference to the loss cost for a relatively low limit (the ‘basic limit’)".  
* **Calculation of Layer Cost:** To derive excess of loss prices using ILFs, you typically need an estimate of the loss cost at the basic limit. The cost to a specific layer (L excess of D) is derived by taking the difference between the ILF at the upper limit (D+L) and the ILF at the lower limit (D), scaled by the basic limits loss cost. The formula provided is `Layer loss cost = Basic limits loss cost * (ILF(L+D) - ILF(D))`. If starting from an original limit `l`, the formula becomes `Layer loss cost = Original limit loss cost * (ILF(L+D) - ILF(D)) / ILF(l)`.  
* **Treatment of ALAE:** The treatment of ALAE is a "much more important consideration for casualty business than for property business" because it can represent a very significant proportion of the claims cost. ILFs can be derived to include the ALAE component.  
* **Split Limits:** It's common in the US for "split limits" (e.g., per-claimant and per-occurrence) to be offered, and ILF tables are constructed to account for these.  
* **Cessions-Based Treaties:** In some markets, particularly for casualty, treaties are structured on a "cessions basis" where the premium ceded depends directly on the limit for each original risk, and the premium is determined from ILF tables set out in the treaty. Here, the ILFs "must make full allowance for the treatment of ALAE, and for the reinsurer’s expenses and risk / profit".

#### **4\. Practical Considerations and Assumptions**

The practical application of OLCs/ILFs is nuanced and requires careful consideration of several factors:

* **Data Quality and Quantity:** While OLCs/ILFs are designed for sparse data scenarios, the quality of the available data remains paramount. Actuaries need "individual loss information gross of reinsurance and ideally ‘from the ground up’". Even with large datasets, "credibility is a significant problem for high value losses". Inadequate data can lead to "unprofitable or uncompetitive rates, or anti-selection".  
* **Trending (Inflation) and Time-Related Influences:**  
  * Historical loss data must be adjusted for past and future inflation and other trends to be relevant for the future policy period. This process is known as 'trending'.  
  * A critical aspect is the "leveraged effect of inflation" on excess layers. Inflation tends to affect higher layers more significantly than lower layers. If claims inflation is assumed to be uniform across all loss sizes and sums insured are adjusted, exposure curves might not require adjustment. However, this is often not the case for liability losses.  
  * ILFs must be "adjusted appropriately for trend" between their derivation date and the prospective treaty period.  
* **Developing Losses to Ultimate:**  
  * Unless a very crude approach is taken, historical claims must be developed to their ultimate values to account for reported but not fully settled claims and IBNR (Incurred But Not Reported) claims.  
  * While aggregate loss development is common for burning cost, frequency-severity approaches (and by extension OLC/ILF construction) often focus on developing individual losses to ultimate. This involves estimating the ultimate settlement value for each open claim, potentially using "case estimate development factors".  
  * Challenges arise with "open claims" where the ultimate cost is unknown, potentially "underestimat\[ing\] the loss cost at higher layers (and overestimate the cost at lower layers)" if not properly handled.  
  * Development patterns for "larger claims may show different development patterns to claims in general," for instance, taking longer to report and settle.  
* **Treatment of Large (Non-Catastrophe) Losses:** Excessively large individual losses ("shock losses") can distort historical data. They are often "exclude\[d\] in their entirety or, more typically, may just exclude the portion above some predetermined threshold," with a separate provision for expected shock losses.  
* **Deductibles and Their Leveraged Effect:** Deductibles also have a "leveraging effect on severity trend," analogous to excess limits. While direct methods can be used to determine deductible relativities, the Loss Elimination Ratio (LER) approach is similar to ILFs.  
* **Behavioral Differences/Anti-selection:** A crucial practical consideration is that LER/ILF approaches may "assume claiming behavior will be the same for each deductible" or limit. However, insureds might choose not to report small claims to avoid surcharges, a "difference in behavior" that is often ignored. This highlights a limitation; multivariate techniques (like GLMs) are better at capturing such behavioral differences inherent in historical data.  
* **Selecting Appropriate Curves:** A "major problem with using benchmarks such as exposure curves is simply their lack of availability" at a suitable level of detail. This necessitates "considerable judgement to select the best curves and groupings possible," which in turn "leads to greater uncertainty in the estimated loss cost".  
* **Consistency:** It's important to ensure data is consistent and that curves are derived on a consistent basis (e.g., if risk profiles use MPLs, curves should be derived consistently).  
* **Actuarial Judgement:** Given the complexities and data limitations, "considerable judgement must be used in selecting the ‘right’ curve". Monitoring emerging results is key to validating these judgments.

#### **5\. Constructing Original Loss Curves from Claims Data**

While many actuaries use existing market curves, knowing the methodology for constructing them from scratch is valuable:

* **General Methodology (Exposure Curves):**  
  1. Collect claims data and express each claim "as a percentage of the risk size" (relative loss severity).  
  2. Divide data into "homogenous groups".  
  3. Construct a table of "accumulated loss cost by percentage of risk size".  
  4. Construct an "empirical exposure curve by dividing accumulated loss cost by total value of losses" and combine groups with similar curves.  
  5. "Smooth the curve" (e.g., using interpolation or parametric curve fits).  
  6. Account for open claims, underlying deductibles/limits, and inflation.  
* **ISO Methodology for ILFs (Casualty):** A methodology developed by ISO (Insurance Services Office) in the US, outlined by Joseph Palmer, addresses the challenges of constructing ILFs, particularly with sparse data and policy limits.  
  1. "Trend (ie adjust for inflation) the individual losses" to the target period.  
  2. Focus on "closed claims" (from several accident years) and group them "by payment lag".  
  3. For each lag, construct an "empirical survival function" for claim size. This involves estimating "conditional survival probability" for discrete loss-size intervals, using occurrences observed within policies that can potentially observe losses at both the bottom and top of the interval.  
  4. Derive "limited average severities (and hence ILFs) from the fitted loss distribution". This approach helps to address the problems of "volume and credibility of data" and the loss of information due to policy limits in casualty business.

#### **6\. Types of Curves Used in Practice**

Actuaries employ various approaches:

* **Curve Fitting:** Fitting "statistical curves to data" such as log-normal, Pareto, truncated Pareto, or mixed exponential distributions. Parametric fits ensure the desired properties (increasing at decreasing rate) are maintained.  
* **Riebesell Curves:** These curves "are not derived from underlying data, but are based on an assumption regarding the original loss cost" – specifically, that "each time the sum insured doubles, the loss cost increases by a constant factor". A key advantage is that they are "scale invariant," meaning they do not need adjustment for inflation or currency changes. However, they are "often not appropriate to use Riebesell curves to adjust for original deductibles" if the deductible is too low.  
* **Market Curves:** Actuaries often rely on "a set of curves from different sources (both internal and external) that they consider appropriate for different types of business". Examples include Swiss Re / Gasser curves, Lloyd's curves, and ISO-derived curves. However, strong caution is advised against using curves in "completely inappropriate contexts".

#### **7\. Advantages and Disadvantages/Limitations**

It's vital for your exam to be able to articulate the trade-offs:

* **Advantages:**  
  * **Simplicity and Explainability:** They are "relatively simple to implement" and "relatively easy to explain to non-technical colleagues".  
  * **Consistency:** "The loss costs obtained should be internally consistent" across different layers.  
  * **Data Scarcity Solution:** Crucially, they "can be used where little or no credible loss data is available".  
* **Disadvantages/Limitations:**  
  * **High Sensitivity:** The "modelled loss cost to layers (particularly high ones) can be extremely sensitive to the selected curve".  
  * **Lack of Data/Benchmarks:** A significant practical difficulty is the "lack of relevant data and a lack of appropriate benchmarks" for constructing or selecting the curves.  
  * **Heavy Judgment Reliance:** This method often requires "considerable judgement" in selecting or estimating the appropriate curves.  
  * **Assumptions on Behavior:** Approaches like LER and ILFs often assume consistent claiming behavior across different deductibles/limits, which may not hold true in reality due to factors like policyholder self-selection or the impact of surcharges on small claims.  
  * **Complexity of Adjustments:** Adjusting for inflation, especially the leveraged effect of limits, can be complex. Similarly, developing individual losses to ultimate and accounting for open claims can be challenging.  
  * **Understating Volatility:** Using current reported claim amounts for open claims might "understate the volatility of the loss distribution" and "underestimate the loss cost at higher layers".  
  * **Difficulty in Capturing T\&C Changes:** Rate indices and OLCs often "struggle to allow for changes to terms and conditions adequately," especially in changing market conditions.

#### **8\. Integration with Other Rating Methodologies**

OLCs/ILFs are not used in isolation but integrate with other methods:

* **Cost Plus Approach:** They form a part of the "cost plus" approach to pricing, where the risk premium (expected cost of claims) is calculated, and then loadings for expenses, profit, investment income, etc., are added to arrive at the "office premium".  
* **Credibility Theory:** Premiums derived using OLCs/ILFs are frequently "credibility weighted with experience rates," especially when the historical data for the specific layer is sparse.  
* **Multivariate Analysis (GLMs):** While OLCs/ILFs simplify the process, actuaries may supplement their analysis with "multivariate analysis (e.g., GLMs)". GLMs can "cope more effectively with sparse data" and can capture behavioral differences (e.g., how insureds with different deductibles actually claim) that LER/ILF approaches might miss.

In essence, OLCs and ILFs are invaluable tools for pricing in challenging data environments, particularly for high layers of insurance or reinsurance. However, their practical application requires astute actuarial judgment, a deep understanding of their underlying assumptions, and a willingness to supplement them with other techniques to manage their inherent limitations. This holistic view is what the SP8 exam demands.

