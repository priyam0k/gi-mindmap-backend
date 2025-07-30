Alright team, let's build out some comprehensive notes on Experience Rating, placing it firmly within the larger context of General Insurance Pricing Methodologies. This is a core concept for SP8, and we need to ensure we understand its nuances and interconnections with other techniques.

---

### **Chapter 15: Commercial Lines Rating Mechanisms – Experience Rating**

**1\. Introduction to Manual Rate Modification Techniques** Most of our discussions in pricing thus far have centered on *manual ratemaking*, which involves determining rates for average members of homogeneous groups based on similar risk characteristics. However, for many commercial insurance products, creating truly homogeneous groups isn't always feasible, or individual risk experience can vary significantly around the average group rate. This is where *special techniques* come into play, particularly for commercial lines, to address the heterogeneity and credibility of commercial risks.

*Manual rate modification techniques* are one category of these special methods. They rely on past experience and/or risk characteristics that are not adequately reflected in the standard manual rate or prior experience. Experience rating is a prime example within this category.

**2\. Defining Experience Rating** *Experience rating* is a system where an individual insured's premium depends, at least partially, on their actual claims experience from the past. The underlying principle is that past loss experience for an individual insured, when appropriately adjusted, can be predictive of their future experience. This aligns with the idea that high-risk policyholders tend to remain high-risk, and low-risk policyholders remain low-risk. Therefore, it makes sense to charge higher premiums to those with frequent past claims and lower premiums to those who have been claim-free. Failure to do so can lead to *anti-selection*, where low-risk policyholders are attracted away by competitors, leaving the insurer with inadequate premiums for high-risk cases.

Historically, manual rates are averages reflecting the usual conditions within each class. Experience rating is specifically designed to reflect the differences that exist among risks *within* the same class.

**3\. Eligibility and Application** Experience rating typically applies only to *larger policies*. This is because larger policies inherently have more stable loss experience, providing more *credible* data for individual risk assessment. For instance, the National Council on Compensation Insurance (NCCI) designates minimum aggregate manual premiums for a company to be eligible for experience rating. Regulators may also mandate the use of experience rating if the employer meets industry eligibility requirements. Conversely, for very small companies, experience rating might not be applicable or its effect limited by credibility considerations.

**4\. Mechanism and Calculation of Experience Modification** When experience rating is applied, the insurer compares the policy's prior loss experience (the "experience component") to the expected statewide average for the same classes (the "expected component"). The manual premium is then adjusted upward if actual losses were higher than expected, and downward if lower. This adjustment is known as the *experience modification* or "experience mod".

The experience rating adjustment for the future policy period's manual premium is determined by a *credibility weighting* of these two components. This is consistent with the core concept of credibility theory, which blends observed experience with other related experience to improve an estimate.

Key components of the experience rating formula and necessary adjustments include:

* **Comparison Basis:** The comparison between the actual (experience) and expected components can be performed in various ways, such as comparing:  
  * Actual paid losses (and ALAE) to expected paid losses (and ALAE) as of a specific date.  
  * Actual reported losses (and ALAE) to expected reported losses (and ALAE) as of a specific date.  
  * Projected ultimate losses (and ALAE) to expected ultimate losses (and ALAE).  
  * Projected ultimate losses (and ALAE) adjusted to current exposure and dollar levels, compared to expected ultimate losses (and ALAE) based on current exposure and dollar levels.  
* **Experience Component (Actual Experience Ratio \- AER):**  
  * **Experience Period:** The historical period typically ranges from two to five policy years, ending with the last complete year. A shorter period is more responsive but more volatile, while a longer period is less responsive but more stable.  
  * **Loss Adjustments:** If the basis is projected ultimate losses at current exposure and dollar levels, historical losses need adjustments for economic and social inflation (e.g., judicial decisions, litigiousness), changes in risk characteristics (e.g., size, type of entity), and changes in policy limits. This involves developing historical losses to ultimate, trending them to current cost levels, and summing them.  
* **Expected Component (Expected Experience Ratio \- EER):**  
  * This component should be consistent with the experience component, including ALAE and consideration of past or current exposure.  
  * Expected losses are usually estimated as the product of an expected loss rate (reflecting manual rates) and an exposure measure. The loss rate can be based on prior or current period manual rates, potentially de-trended to appropriate dollar levels.  
* **Formula Example:** A common formula for computing the experience rating debit/credit is:  
  * Credit/Debit percentage \= Z \* \[(AER \- EER) / EER\].  
  * A credit reduces premium, while a debit increases it.  
* **Other Considerations:** The experience modification factor may be subject to maximum or minimum changes. An "off-balance correction" may also be needed if the total premium under the experience rating plan doesn't equal the total expected premium.

**5\. Credibility in Experience Rating** Credibility is fundamental to experience rating because it determines the weight given to the individual insured's past experience versus broader, more stable data. The goal is to blend the subject experience with related experience to improve the estimate of expected values.

* **Classical Credibility:** This approach, commonly called limited fluctuation credibility, is frequently used in insurance ratemaking. It calculates a credibility measure (Z) to assign weights to the observed (subject) experience and related experience. If the individual policy's data is sufficiently large and stable ("fully credible"), Z will be 1.00, meaning the estimate relies entirely on its own experience. If the data is sparse, partial credibility is assigned, blending the individual experience with a broader complement. Experience rating plans are designed to give due consideration to what the insured perceives as fair, often through features like swing limits (maximum premium change) or self-rating for very large insureds.  
* **Bühlmann Credibility:** Also known as least squares credibility, it aims to minimize the error between the estimate and the true expected value. While less common than classical credibility, it's used within the industry.  
* **Bayesian Analysis:** This probabilistic method adjusts a prior estimate to reflect new information, without explicitly calculating a Z parameter. It's noted as more complex and less commonly used in practice than Bühlmann. However, it is fundamentally linked to credibility, as the Bornhuetter-Ferguson method (a credibility approach) can be seen as a Bayesian approach.

The choice of the "complement of credibility" – the related experience blended with the subject experience – is crucial. It should have characteristics similar to the subject experience and be reasonably independent. For experience rating, common complements could include the overall book rate or industry benchmarks.

**6\. Relationship with Other Rating Methodologies**

* **Manual Rating:** Experience rating directly *modifies* the manual rate. Manual rates are averages, and experience rating refines these for individual risks based on their own history.  
* **Schedule Rating:** Both experience rating and *schedule rating* are manual rate modification techniques. However, schedule rating adjusts the manual rate based on specific objective criteria or underwriter judgment, for characteristics *not adequately reflected* in the manual rate or past experience (if experience rating applies). An underwriter credits (reduces) for loss-reducing characteristics and debits (increases) for loss-increasing ones. It's crucial to avoid *double-counting* the effect of a risk characteristic in both experience and schedule rating.  
* **Loss-Rated Composite Risks:** For very large commercial risks, premium may be calculated based *entirely* on the individual risk's historical loss experience, without using standard rating algorithms. This is called *loss-rated composite rating*. In such cases, the composite rate is *not adjusted* by a separate experience rating plan because the insured's own experience has already been reflected directly in the rate. Schedule rating, however, may still apply.  
* **Classification Ratemaking (Univariate/Multivariate):** Experience rating complements classification ratemaking. While classification ratemaking groups risks with similar loss potential to set manual rates, experience rating then takes into account the individual risk's historical performance to *further differentiate* their premium within that class. This addresses residual heterogeneity within rating cells.  
* **Burning Cost and Frequency/Severity Approaches:** The sources describe the burning cost approach as an "experience rating approach" where the "burning cost" is the actual cost of claims during a past period, expressed as an annual rate per unit of exposure, often used with a simple regression model based solely on historical data. Similarly, the frequency/severity approach, by projecting frequency and severity separately and then combining them, can be applied to individual risks, often requiring simulation techniques due to its complexity. These are fundamental methods for calculating the "risk premium".

**7\. Advantages and Disadvantages/Considerations**

* **Advantages:**  
  * **Equity and Anti-selection:** It allows for more equitable rates by recognizing individual risk differences, thereby reducing the likelihood of adverse selection.  
  * **Predictive Value:** An individual insured's past experience can be highly predictive of future experience, especially for larger policies.  
  * **Customer Perception:** When transparent, it can be perceived as fair by insureds.  
* **Disadvantages/Considerations:**  
  * **Data Requirements:** Requires reliable and sufficient historical loss data for the individual risk to be credible. Data quality, consistency, and volume are paramount.  
  * **Volatility:** Experience of any single insured can vary significantly year to year, especially for small risks. This volatility needs to be managed through credibility.  
  * **Adjustments Needed:** Historical losses often require significant adjustments for development to ultimate, trend, changes in policy limits, and other factors before they are relevant for future pricing.  
  * **Simplicity vs. Accuracy:** While simplicity is valued for frequent calculations, achieving accuracy requires complex adjustments and modeling, which can be time-consuming and require high expertise.  
  * **"Soft Factors":** Experience rating primarily focuses on quantifiable loss experience. Other "soft factors" (e.g., quality of management, safety programs) are usually addressed by schedule rating.  
  * **Moral Hazard:** The system can create moral hazard, for example, if the sale of good players by a sports club affects their demotion risk.  
  * **Regulatory Scrutiny:** Regulations may prescribe or limit its use, or require documentation of its application and supporting judgment.  
  * **Off-Balance:** The total premium derived from experience rating might not align with the desired total expected premium for the entire book, requiring off-balance corrections.  
  * **Double-Counting:** Care must be taken to avoid double-counting effects already captured by other rating mechanisms, such as schedule rating.

**8\. Examples in Practice** Experience rating plans are commonly used for commercial general liability (CGL) and workers compensation insurance. For workers compensation, the NCCI Experience Rating Plan, with its unique features of dividing losses into primary and excess components, is widely designated by state insurance departments in the U.S..

---

This detailed breakdown should give you a robust understanding of Experience Rating for your SP8 studies. Remember, the goal is not just to define it, but to truly grasp how it fits into the actuarial control cycle and the broader pricing landscape\!

