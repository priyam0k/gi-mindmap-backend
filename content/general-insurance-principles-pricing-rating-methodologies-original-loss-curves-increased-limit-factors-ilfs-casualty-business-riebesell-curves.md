Alright, let's dive deep into this SP8 core concept\! As your Specialist Actuarial Note Builder and Exam Coach, I'm here to build a comprehensive understanding of Original Loss Curves (OLCs) and Increased Limit Factors (ILFs), with a specific focus on their application in Casualty business and the intriguing Riebesell Curves. This is a fundamental area in General Insurance Pricing, so let's construct these notes carefully.

### **Building Structured Notes: Original Loss Curves / Increased Limit Factors (ILFs) and Casualty Business (Riebesell Curves)**

#### **1\. Introduction to Original Loss Curves (OLCs) and their Terminology**

Original Loss Curves are indispensable tools in general insurance pricing, particularly when data is sparse for higher layers of cover, making it difficult to derive a credible experience rate \[SP8.pdf 606\]. They allow actuaries to infer prices for these layers by extrapolating from known loss costs at lower layers where sufficient data exists \[SP8.pdf 607\]. This technique is frequently employed for excess of loss pricing, but also for calculating large loss loadings on full-value covers or ensuring consistent prices for different primary limits in direct insurance \[SP8.pdf 606\].

The terminology can vary greatly among practitioners, but the curves are generally related to loss severity distributions. The most common forms include \[SP8.pdf 610, 611, 612, 690\]:

* **First Loss Scales / Exposure Curves:** Primarily seen in property business, these curves indicate the proportion of the full-value premium allocated to primary layers limited at different values. Alternatively, they show the value (as a percentage of full-value premium) of imposing deductibles at various levels. Limits are typically expressed as a fraction of the sum insured (SI), Maximum Probable Loss (MPL), or Estimated Maximum Loss (EML) \[SP8.pdf 610, 690\]. They are also sometimes called loss elimination functions \[SP8.pdf 610, 690\].  
* **Increased Limit Factors (ILFs):** These are multiplicative factors that provide the ratio of the premium for higher limits to a chosen "basic limit" premium. This terminology and format are commonly used in casualty (liability) business \[SP8.pdf 611, 691\].  
* **XL Scales (Excess of Loss Scales):** Similar to first loss scales, but they give the proportion of premium to be allocated to the excess layer rather than the primary layer. They effectively represent the "other end" of the curve compared to first loss scales \[SP8.pdf 612, 619, 690\].

**What's Included in the Curves?** Originally, OLCs describe the ratio of pure loss cost at different levels of deductible or excess. However, they can also be constructed to account for \[SP8.pdf 613, 614, 691\]:

* Allocated Loss Adjustment Expenses (ALAE) and potentially Unallocated Loss Adjustment Expenses (ULAE) at each limit. ALAE are directly attributable to a specific claim (e.g., legal defence costs), while ULAE are general claim handling expenses not directly assigned to one claim (e.g., claims department salaries) \[SP8.pdf 613, 614\].  
* A load for risk at each limit, which would typically be greater for higher limits \[SP8.pdf 614\].

It's crucial that curves are appropriate for the cover granted, whether on a per-claim (individual claimant) or per-occurrence (total for all claimants from one incident) basis \[SP8.pdf 615\].

**Key Properties of the Curves:** Regardless of their specific form, OLCs are closely related to the *limited expected value (LEV) function* \[SP8.pdf 616, 618, 700\]. The LEV function represents the expected value of losses limited to a primary layer of a given size. Its core properties are \[SP8.pdf 618, 675, 700\]:

* **Non-decreasing:** As the limit increases, the expected value of losses limited to that limit will also increase or stay the same \[SP8.pdf 618, 675\].  
* **Concave (Increases at a Decreasing Rate):** The rate at which the expected value increases diminishes as the limit rises. This is because fewer and fewer claims fall above an ever-increasing limit \[SP8.pdf 618, 675\].

These properties are intuitively sensible: as you increase the coverage limit, you collect more in claims, but the additional claims captured become progressively rarer and less impactful on the average \[SP8.pdf 618, 255\]. XL scales, being the "other end" of the curve, exhibit reversed properties (non-increasing and convex) \[SP8.pdf 619\].

#### **2\. Differentiating Application: Property vs. Casualty Business**

While the basic pricing methodology is consistent, the assumptions and considerations for OLCs differ significantly between property and casualty lines \[SP8.pdf 620, 644\]. This is a crucial distinction for your understanding, so pay close attention here\!

**2.1 Property Business (Exposure Curves)** In property insurance, like household policies, there's a clear measure of risk such as the sum insured (SI) or estimated maximum loss (EML) \[SP8.pdf 621\]. The underlying assumption for property exposure curves is that the **relative loss size distribution (Y \= X/M)** – where X is the loss severity and M is the measure of risk – can be considered independent of the individual characteristics and size of the risk \[SP8.pdf 626, 627, 644, 701\]. This implies that if sums insured are adjusted appropriately for trend and the trend's effect is uniform across all loss sizes, no adjustment to the exposure curves is needed \[SP8.pdf 631, 702\].

However, this assumption holds primarily for reasonably homogeneous data (e.g., residential buildings fire losses). Problems arise with less homogeneous data or wider ranges in risk size, where the distribution of Y can become dependent on the peril or even show that smaller risks have a higher proportion of severe losses relative to their sum insured \[SP8.pdf 628\]. Heterogeneity due to jurisdiction, claims environment, sub-classes, or different coverages necessitates deriving separate exposure curves, though data scarcity often leads to judgmental adjustments \[SP8.pdf 629, 630, 692\].

**2.2 Casualty Business (Increased Limit Factors \- ILFs)** In contrast, casualty (liability) business presents a different challenge \[SP8.pdf 643\]. There's typically **no easily definable upper limit on the possible severity of loss** to the original insured; court awards can lead to effectively unlimited claims \[SP8.pdf 645, 702\]. The policy limit purchased by an insured in casualty lines often doesn't provide significant information about the potential ground-up loss severity, as it can be influenced by factors like the insured's budget, cost of cover, or market practice, rather than the true maximum potential loss \[SP8.pdf 645\].

Therefore, for casualty business, the assumption that the *relative* loss size (Y) is independent of the risk size *does not hold* \[SP8.pdf 646, 702\]. Instead, the approach for casualty ILFs makes the following assumptions within selected risk groups \[SP8.pdf 646, 703\]:

* The **ground-up loss frequency** is independent of the limit purchased.  
* The **ground-up severity** is independent of both the number of losses and the limit purchased.

Casualty ILFs are expressed in **absolute monetary values** rather than as proportions of a sum insured \[SP8.pdf 648, 703\]. The treatment of Allocated Loss Adjustment Expenses (ALAE) is particularly critical for casualty business, as they can represent a substantial portion of the claims cost, and ILFs may need to be derived to include them \[SP8.pdf 649, 704\].

Furthermore, the effect of claims inflation (or "trend") is often *not uniform* across all loss sizes in casualty business \[SP8.pdf 654\]. Large liability losses, for instance, may be subject to higher inflation than smaller ones, leading to a "leveraged effect of inflation" on excess of loss rating. This means inflation dampens the effect on lower layers but significantly impacts higher layers \[SP8.pdf 655, 38, 39, 40, 41, 665, 705\]. Legal reforms can also affect different parts of the loss distribution disproportionately \[SP8.pdf 655\].

#### **3\. Riebesell Curves in Casualty Business**

Now, let's focus specifically on Riebesell Curves, a notable application of OLC principles within casualty business.

**3.1 Purpose and Origin:** Riebesell curves are a family of curves frequently used in **European casualty treaty business** \[SP8.pdf 677\]. They are popular in Germany, where they originated from the work of mathematician Paul Riebesell \[SP8.pdf 678\].

**3.2 Key Assumptions and Consistency:** Unlike some curves derived directly from empirical data, Riebesell curves are **not derived from underlying data directly** \[SP8.pdf 679\]. Instead, they are based on a fundamental assumption regarding the original loss cost:

* **The assumption is that each time the sum insured doubles, the loss cost increases by a constant factor (x%)** \[SP8.pdf 679\].

This specific assumption is mathematically consistent with an original loss distribution having a **Pareto tail** with a shape parameter less than 1 (alpha \< 1\) \[SP8.pdf 679, 680\]. This means if you believe your casualty claims exhibit such a Pareto tail, Riebesell curves are a suitable choice for ILF purposes \[SP8.pdf 680\].

Furthermore, Thomas Mack and Michael Fackler demonstrated that this assumption can also be consistent with the **collective risk model**, provided it is applied only for sufficiently high loss thresholds. A common threshold suggested is approximately five times the expected loss (5 \* E\[X\]) \[SP8.pdf 680, 681\]. For many international casualty markets with high limits of liability, this condition is easily met, making Riebesell curves practical for reinsurers \[SP8.pdf 681\].

**3.3 Why Riebesell for Casualty?** Riebesell curves are more commonly used for casualty (liability) business than property because they successfully address the complexity unique to casualty lines: the limit purchased by the policyholder does not serve as a reliable indicator of the maximum potential claim amount, unlike the sum insured in property business \[SP8.pdf 678\].

**3.4 Practical Properties and Limitations:** A significant practical advantage of Riebesell curves is their **scale invariance** \[SP8.pdf 682\]. This means they, and the ILFs derived from them, generally *do not need to be adjusted for inflation or changes in currency*, assuming the attachment points remain sufficiently high for their underlying assumptions to be valid \[SP8.pdf 682\]. This stems directly from their foundational assumption about the constant factor increase in loss cost when the sum insured doubles \[SP8.pdf 682\].

However, this threshold condition (e.g., 5 \* E\[X\]) also leads to a key limitation: Riebesell curves are often **not appropriate for adjusting for original deductibles** \[SP8.pdf 681\]. This is because the deductible on an original policy is typically *unlikely* to exceed five times the expected losses, thus falling below the threshold where the Pareto tail assumption is consistent with the collective risk model \[SP8.pdf 682\].

#### **4\. Constructing and Applying Original Loss Curves / ILFs**

Constructing OLCs and ILFs from claims data is a complex undertaking, often hampered by data scarcity and quality issues, particularly for high-value losses where credibility is a significant problem \[SP8.pdf 661\].

**4.1 General Methodology for Derivation:** In principle, the derivation involves \[SP8.pdf 662, 663, 694, 695\]:

1. **Collect claims data:** For property, express each claim as a percentage of risk size (e.g., MPL). For casualty, use absolute monetary values \[SP8.pdf 662, 694\].  
2. **Divide into homogeneous groups:** Combine groups with no significant difference in the empirical curve \[SP8.pdf 663, 694\].  
3. **Construct table of accumulated loss cost:** Organize by percentage of risk size (property) or absolute value (casualty) \[SP8.pdf 663, 694\].  
4. **Construct empirical curve:** Divide accumulated loss cost by total value of losses for the group \[SP8.pdf 663, 695\].  
5. **Smooth the empirical curves:** Ensure the smoothed curves display the expected properties (non-decreasing, concave) \[SP8.pdf 663, 675, 695\]. Interpolation methods or parametric curve fits (e.g., log-normal, Pareto, truncated Pareto, mixed exponential, or MBBEFD for exposure curves) can be used, ensuring consistency with the LEV properties \[SP8.pdf 674, 676, 695\].

**4.2 Specific Challenges for Casualty ILFs:** Deriving ILFs for casualty business presents additional acute problems due to its long-tailed nature \[SP8.pdf 666, 667\]:

* **Loss of Information on Large Losses:** Policy limits can obscure information about true large losses, especially since the limit purchased may not reflect the maximum possible loss \[SP8.pdf 666\].  
* **Trend Adjustment:** Losses must be adjusted for inflation/trend, which itself needs careful estimation, and the leveraged effect on higher layers must be considered \[SP8.pdf 667, 654\].  
* **Open Claims:** Many claims remain open for long periods. Naïve approaches (ignoring them or using current case reserves) are problematic because loss size often correlates with settlement delay, and current reserves may underestimate ultimate values for large claims or their volatility \[SP8.pdf 667, 668\].

The ISO (Insurance Services Office) in the US has developed a methodology to address these issues, essentially applying survival functions to closed claims grouped by payment lag to construct empirical survival functions for claim size \[SP8.pdf 669, 670, 671, 672\].

**4.3 Practical Considerations in Application:**

* **Credibility:** The application of OLCs/ILFs is difficult in practice primarily due to uncertainty in estimating or selecting appropriate curves, often stemming from data scarcity, especially for high-value losses \[SP8.pdf 696\]. A larger volume of data generally leads to more reliable loss cost estimates \[SP8.pdf 509\].  
* **Heterogeneity:** The underlying business often isn't perfectly homogeneous, requiring careful segmentation or judgmental adjustments to selected curves \[SP8.pdf 630, 692\].  
* **Data Quality:** Reinsurers must critically question the validity of data provided by cedants or brokers \[SP8.pdf 636\]. Individual loss information should ideally be gross of reinsurance and "from the ground up" \[SP8.pdf 577\].  
* **Inflation/Trend:** Consistent trending of all components is vital. While uniform inflation may simplify adjustments for property exposure curves, non-uniform (leveraged) inflation in casualty requires more complex re-evaluation of ILFs \[SP8.pdf 631, 654, 655, 667, 702, 705\].  
* **Original Deductibles/Limits:** The methodology needs careful adjustment if the original business has underlying deductibles or stacked limits that are affected differently than the curves' underlying assumptions \[SP8.pdf 640, 641, 642, 693\].  
* **Complementary Models:** Often, the "nat-cat" (natural catastrophe) element of loss cost is modeled separately (e.g., using catastrophe models) and then added to the cost from other perils derived using OLCs/ILFs \[SP8.pdf 643, 693\]. This acknowledges that OLCs/ILFs are less appropriate for low-frequency, high-severity events \[SP8.pdf 807\].  
* **Market Curves:** While some published curves exist (e.g., Swiss Re/Gasser, Lloyd's curves), their appropriateness must be seriously considered for any specific pricing exercise, as using them in inappropriate contexts can lead to significant errors \[SP8.pdf 683, 684\].

Despite the challenges, OLCs and ILFs are valuable tools due to their relative simplicity in implementation, ease of explanation to non-technical colleagues, internal consistency of derived loss costs, and their utility when credible historical loss data is limited \[SP8.pdf 689, 696\]. This concludes our deep dive into Original Loss Curves and their crucial role in General Insurance Pricing. Keep reviewing these concepts, as they are central to the SP8 syllabus\!

