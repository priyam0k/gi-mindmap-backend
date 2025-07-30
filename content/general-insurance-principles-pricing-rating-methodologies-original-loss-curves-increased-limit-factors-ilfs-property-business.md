Right, team, let's build some solid notes on Property Business within the larger context of Original Loss Curves (OLCs) and Increased Limit Factors (ILFs) for your SP8 exam. This is a core concept for understanding how we price risks, especially when direct experience is a bit thin.

### **SP8: General Insurance Pricing \- Actuarial Note Builder**

#### **Chapter: Original Loss Curves / Increased Limit Factors (ILFs) and Property Business**

##### **1\. Introduction to Original Loss Curves (OLCs) and Increased Limit Factors (ILFs)**

At a fundamental level, Original Loss Curves (OLCs) and Increased Limit Factors (ILFs) are indispensable tools in general insurance pricing. They come into play when the historical claims data for a particular layer or limit of coverage is too sparse or volatile to derive a credible price using traditional methods. Essentially, they allow us to infer prices for higher layers or different limits based on more credible data from lower layers, or on broader distributional assumptions. This is particularly critical in contexts like excess of loss (XL) reinsurance pricing, or for direct insurance policies with varying limits.

##### **2\. Application to Property Business: Exposure Curves**

For property business, OLCs are typically referred to as **first loss scales**, **exposure curves**, or **loss elimination functions**. When they specifically show the proportion to be allocated to the *excess* layer rather than the primary layer, they might be called **excess of loss scales**.

**2.1 Purpose and Use Cases for Property Business**

These curves are highly valuable in property insurance because they help us price policies with different limits and attachment points, especially for large or complex commercial risks where a single event could lead to substantial losses. For instance, a property policy's premium might be determined by reference to the Estimated Maximum Loss (EML) or Probable Maximum Loss (PML), rather than the full sum insured, particularly for properties with multiple locations or where complete destruction is remote. Exposure curves aid in translating this risk measure into appropriate premiums for specific layers of coverage.

**2.2 Outline Theory of Property Exposure Curves**

Let's break down the mechanics, keeping in mind the foundational assumptions:

* **Measure of Risk (M)**: For a single property risk, we often use a measure of its size, such as the Sum Insured (SI), Maximum Probable Loss (MPL), or Estimated Maximum Loss (EML).  
* **Relative Loss Severity (Y)**: A crucial concept is the 'relative loss severity', denoted as *Y*, which represents the actual loss (*X*) as a proportion of the measure of risk (*M*) (i.e., *Y \= X/M*).  
* **Exposure Curve Function (G(x))**: The exposure curve, *G(x)*, is formally defined as the Limited Expected Value (LEV) of *Y* at a given limit *x*, divided by the Expected Value of *Y*. It effectively represents the expected value of losses limited to a primary layer of size *x*.  
  * *G(x) \= E\[Y ⋀ x\] / E\[Y\]*  
* **Loss Cost to a Layer**: To estimate the loss cost to a specific layer (say, between attachment point *D* and limit *L+D*), we use the full value loss cost (*C*) multiplied by the difference in the exposure curve values at the upper and lower limits of the layer, expressed as proportions of *M*:  
  * *Layer Loss Cost \= C × \[G((L+D)/M) \- G(D/M)\]*

**Crucially, the underlying assumption for property exposure curves is that the relative loss size distribution (*Y*) is independent of the absolute size of the risk (*M*)**. This is based on the belief that the sum insured provides genuine information about the ground-up, unlimited loss severity distribution. Research, such as Salzmann's 1960s study on US homeowners' fire losses, has indicated that this is a reasonable approximation for homogeneous data within certain construction types.

**2.3 Selecting Exposure Curves**

Selecting the right exposure curve is paramount. The distribution of *Y*, and thus the exposure curve, is highly dependent on the peril involved. Problems arise when the data is less homogeneous, including wider ranges in risk size or different sub-classes (e.g., retail vs. manufacturing). Smaller risks, for example, have shown a higher proportion of severe losses relative to their sum insured compared to larger risks. Other heterogeneities like differences in jurisdiction, claims environment, or coverages (e.g., buildings-only vs. contents and business interruption) can also significantly alter the distribution of *Y*.

Ideally, we should derive separate exposure curves for each peril, risk size band, and other significant differentiators. However, the sheer volume of quality data required often makes this impractical. In practice, actuaries frequently apply judgment to group data or adjust existing curves. Published exposure curves can be used, but always with caution and potential adjustment, especially if your specific business is highly unique.

**2.4 Effect of Claims Inflation (Trending)**

Claims inflation, often termed 'trend,' plays a vital role. If we can assume that the effect of claims trend is uniform across all loss sizes and that sums insured are appropriately adjusted for inflation, then no specific adjustment to the exposure curves themselves is needed, as *Y* (X/M) remains unchanged. However, this is often *not* the case, especially for losses in higher layers, which are often subject to greater inflationary pressure than lower layers. Ignoring this 'leveraging effect of limits on severity trend' can introduce bias. When inflation affects the loss distribution non-uniformly, we must adjust the curves or rework the entire analysis.

**2.5 Using Exposure Curves in Property Risk XL Treaty Rating**

When pricing property per-risk excess of loss (XL) treaties, exposure rating is a common method. This requires detailed information from the cedant on the sizes of risks written, such as sums insured (SI) or probable maximum losses (PMLs), and premium income, often presented as a table of original premiums by sum insured band.

Key practical considerations include:

* **Limit Profile Interpretation**: Understanding whether provided limits are the insurer's share or 100% of the limit for the risk.  
* **Original Deductibles**: Accounting for underlying deductibles (or excesses) in the original business. Exposure curves derived from 'ground-up' data need adjustment to reflect these deductibles.  
* **Inuring Reinsurance**: Recognizing any other (facultative or proportional) reinsurances that apply *before* the risk XL treaty. These reduce the gross claims by a fixed percentage before the XL treaty is applied.  
* **Stacked Limits**: For large commercial business, especially multi-location risks, details on the distribution of insured values are needed to properly account for how losses to different layers from a single event might be summed for treaty limits.  
* **Catastrophe Element**: It's common practice to model the "natural catastrophe" (nat-cat) element of the loss cost separately, often using **catastrophe models**, and then add this to the cost of other perils modeled with exposure curves. These models are crucial for low-frequency, high-severity risks that traditional methods struggle with.

##### **3\. Brief Contrast with Casualty (Liability) Business and ILFs**

While the underlying principle is similar, ILFs for casualty (liability) business differ significantly due to the nature of liability claims.

* **No Definable Upper Limit**: For casualty business, there's no easily definable upper limit on the possible severity of loss (unlike a property's sum insured), as it often depends on court awards and societal factors.  
* **Independence Assumption Invalid**: The crucial assumption that the relative loss size distribution (*Y*) is independent of the risk size *M* does *not* hold for casualty business. Factors influencing the limit purchased (e.g., budget, risk aversion) may not correlate with potential loss severity. Therefore, for casualty business, ILFs are usually functions of a monetary amount (e.g., *ILF(x)*) rather than relative proportions.  
* **ALAE Treatment**: Allocated Loss Adjustment Expenses (ALAE) are a much more significant component of claims cost in casualty business than in property. ILFs can be derived to include ALAE, but understanding its treatment in the policy and treaty is essential.  
* **Leveraged Effect of Inflation**: The leveraged effect of inflation is particularly pronounced and important for casualty excess layers. Higher layers can experience substantially higher inflation than lower layers.

##### **4\. Constructing Original Loss Curves from Claims Data**

Constructing OLCs (whether exposure curves or ILFs) from internal claims data presents considerable challenges due to data scarcity and credibility issues, particularly for high-value losses.

**4.1 Deriving Exposure Curves (Property)**

In principle, deriving property exposure curves is straightforward:

1. **Collect Data**: Gather claims data and express each claim as a percentage of the risk size (*Y*).  
2. **Group Data**: Divide data into homogeneous groups.  
3. **Accumulated Loss Cost**: Construct a table of accumulated loss cost by percentage of risk size.  
4. **Empirical Curve**: Construct an empirical exposure curve by dividing the accumulated loss cost by the total value of losses, combining groups where the curve is similar.  
5. **Smooth Curve**: Smooth the curve using interpolation or parametric fits, ensuring it retains the mathematical properties of an LEV function (increasing at a decreasing rate). **Problem of Open Claims**: A significant hurdle is dealing with open claims, as their ultimate cost is unknown and their development pattern may differ by size. Standard reserving methods for aggregate claims may not fully capture the growth of a *distribution* of losses, which is what's needed for OLCs.

**4.2 Deriving ILFs (Casualty)**

Deriving ILFs for casualty business introduces additional complexities:

* **Information Loss from Policy Limits**: Policy limits can obscure information about true large losses, especially since the limit purchased may not reflect the maximum possible loss.  
* **Long-Tailed Nature**: Casualty business is often long-tailed, making trending (adjusting for inflation) and developing losses to ultimate more significant and challenging. Larger claims often take longer to settle.  
* **Problematic Naïve Approaches**: Simply ignoring open claims or using current reported amounts (paid \+ case reserve) for open claims is inappropriate, as it can skew the curve and underestimate volatility, particularly at higher layers.  
* **ISO Methodology**: The Insurance Services Office (ISO) in the US developed a methodology that addresses these issues by applying survival functions to *closed* claims, grouped by payment lag. This involves trending individual losses, grouping closed claims by payment lag, constructing empirical survival functions for claim size at each lag, and then deriving ILFs from the fitted loss distribution.

##### **5\. Curves Used in Practice**

Practitioners rely on several approaches when original loss data is insufficient:

* **Fitting Statistical Curves**: Fitting parametric distributions (e.g., MBBEFD curves, log-normal, Pareto, truncated Pareto, mixed exponential) to available data.  
* **Riebesell Curves**: These are popular in Germany, especially for casualty business, and are not derived from underlying data. Instead, they assume that for a given group of risks, each time the sum insured doubles, the loss cost increases by a constant factor.  
* **Published Market Curves**: Using curves developed by organizations like ISO (for US property and casualty), Swiss Re, or even historical "Lloyd's curves".

It is absolutely vital to test the goodness of fit of any selected curve to your data and to be cautious about using curves developed in potentially inappropriate contexts.

##### **6\. Advantages and Disadvantages of OLCs/ILFs**

**Advantages**:

* **Consistency**: They produce internally consistent loss costs across different layers.  
* **Ease of Explanation**: The methodology can be relatively easy to explain to non-technical colleagues.  
* **Sparse Data**: Crucially, they can be used effectively when there is little or no credible direct loss data for specific layers.

**Disadvantages/Limitations**:

* **Construction Difficulty**: In practice, constructing these curves is difficult, primarily due to uncertainties in estimating or selecting appropriate curves.  
* **Sensitivity**: The modelled loss cost, especially for high layers, can be extremely sensitive to the chosen curve.  
* **Homogeneity Assumptions**: The validity of the underlying assumptions (e.g., independence of relative loss severity for property, or independence of frequency/severity for casualty) is critical and often challenging to maintain with heterogeneous data.  
* **Data Quality**: Access to sufficient high-quality data remains a significant hurdle for many practitioners.

Overall, OLCs and ILFs are powerful tools, but they demand careful application, sound actuarial judgment, and a keen awareness of their underlying assumptions and limitations. Always remember your professional guidance when venturing into these complex areas.

