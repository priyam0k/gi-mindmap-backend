Alright, let's delve into the crucial concept of the "Complement of Credibility" within the broader framework of Credibility Theory, a fundamental aspect of general insurance pricing for our SP8 journey.

### **Chapter 12: Credibility – A Deep Dive into Enhancing Actuarial Estimates**

As Specialist Actuarial Note Builders and Exam Coaches for SP8, we understand that robust pricing relies on accurate future loss experience estimates. While historical data is invaluable, it often falls short in providing fully reliable predictions due to limited volume or instability. This is precisely where the science of credibility in ratemaking steps in. It's about intelligently blending the actuarial estimate derived from observed experience with additional, related information to enhance the overall estimate of expected values.

The core of credibility is captured by the fundamental formula for a credibility-weighted actuarial estimate:

**Estimate \= Z × Observed Experience \+ (1 \- Z) × Related Experience**

Here, 'Z' represents the credibility assigned to the observed data, a measure of its predictive value in a given application. It must always be between 0 and 1, inclusive, increasing as the size of the underlying risk increases, but at a decreasing rate. If your observed data is sufficiently large and stable, Z can reach 1.00, implying full credibility.

### **The Indispensable "Complement of Credibility" (1 \- Z)**

Now, let's turn our attention to the unsung hero of this formula: **(1 \- Z)**, commonly referred to as the "complement of credibility". This term represents the weight given to the *related experience* or *ancillary statistic*. When your observed data (the 'subject experience' or 'base statistic') is not fully credible (i.e., Z is less than 1.00), you must rely on this complement.

Think of it this way: if your observed data for a specific risk segment is sparse or volatile, Z will be low. Consequently, the majority of your rate (or expected loss estimate) will be driven by this complement of credibility. This highlights its critical role: the complement of credibility can often be *more important* than the observed data itself, especially for low-credibility situations.

When classical credibility methods are employed, actuaries choose a selected complement. In the context of Bühlmann credibility, the complement of credibility theoretically should be the prior mean, although in practice, other related experience might also be used.

### **Desirable Qualities of a Robust Complement of Credibility**

Selecting the right related experience for the complement of credibility is paramount. Actuarial Standard of Practice (ASOP) Number 25 emphasizes careful selection, stating that the related experience should possess characteristics (frequency, severity, etc.) that can reasonably be expected to be similar to the subject experience. If it cannot be adjusted to meet such criteria, it should not be used.

Joseph A. Boor outlines six desirable qualities for an effective complement of credibility, which are essential considerations for any SP8 candidate:

1. **Accurate:** The complement should help achieve the lowest possible error variance around the future expected losses being estimated. An accurate complement contributes to the overall accuracy of the credibility-weighted estimate.  
2. **Unbiased:** The complement should not consistently overestimate or underestimate the observed experience. In the long run, the differences between the complement and the observed experience should average to zero. If bias is present, the actuary must assess its materiality.  
3. **Statistically Independent from the Base Statistic:** This is a subtle yet crucial quality. Independence means the complement is not related to the base statistic. The benefits of independence are most pronounced for intermediate credibility levels (Z between 10% and 90%), as it significantly enhances the accuracy of the credibility-weighted estimate in these ranges. Ideally, a negative correlation between errors of the two statistics would be best, as errors would offset, but this is rare in practice; positive correlation is more common.  
4. **Available:** Practicality dictates that the chosen statistic for the complement should be readily accessible. Some statistics may require more complex programming or expensive processing, making them less practical for common use.  
5. **Easy to Compute:** Simplicity in calculation is a desirable trait, reducing computational time and complexity.  
6. **Logical Relationship to Base Statistic:** The complement should have an explainable and understandable relationship to the observed experience. This logical connection makes it easier to justify its use to stakeholders or regulators.

Other practical considerations include the ease of explanation to managers and customers, the time taken for calculation (balancing against accuracy needs), and the potential sources of error within the complement itself.

### **Methods for Developing Complements of Credibility**

Complements of credibility are developed differently depending on whether you're performing first dollar ratemaking or excess ratemaking.

#### **I. First Dollar Ratemaking**

First dollar products cover claims from the first dollar of loss (or after a small deductible) up to a limit, such as personal automobile or homeowners insurance. Boor identifies six commonly used methods for developing complements in this context:

1. **Loss Costs of a Larger Group that Includes the Group Being Rated:**

   * **Description:** This method utilizes the experience of a broader group that encompasses the subject experience. Examples include using data from all states in a region to supplement a single state's experience, or all primary care physicians for primary care pediatricians. It can also involve using data from a longer historical period to weight shorter-term observed experience.  
   * **Evaluation:** If the complement excludes the subject experience, it's likely independent. If included, ensure it doesn't dominate the larger group. Data is typically available and easy to compute, and a logical connection exists if risks in the larger group share commonalities. However, older data in a longer-term complement might introduce bias if loss costs have changed significantly.  
2. **Loss Costs of a Larger Related Group:**

   * **Description:** Instead of the exact larger group, this method uses loss costs from a separate but similar large group. For instance, a homeowners insurer might use contents loss experience from owner forms to supplement condo forms.  
   * **Evaluation:** This method is generally biased, and the magnitude/direction of bias might be unknown. Adjustments to match exposure to loss can reduce bias. Independence from the subject experience makes it potentially preferable to the first method. Data is usually available, and calculations are straightforward, though explaining adjustments for bias can be challenging. A logical relationship exists if groups are closely related.  
3. **Rate Change from the Larger Group Applied to Present Rates:**

   * **Description:** This approach uses the indicated rate change for a larger group, applied to the subject experience's current loss cost, to mitigate the bias found in direct use of larger group loss costs. The complement (C) is calculated as: $C \= \\text{Current Loss Cost of Subject Experience} \\times (\\frac{\\text{Indicated Loss Cost of Larger Group}}{\\text{Current Average Loss Cost of Larger Group}})$. For example, a current loss cost of $200 with a larger group indicating a change from $300 to $330 would yield a complement of $220 ($200 \* ($330/$300)).  
   * **Evaluation:** This complement is largely unbiased, even if overall loss costs differ, and is likely accurate for small rate changes over the long term. Independence depends on the subject experience's size relative to the larger group. Data is readily available, calculations are simple, and it's logically indicative of rate change for the subject experience.  
4. **Harwayne’s Method:**

   * **Description:** Used when subject and related experiences have significantly different distributions, requiring adjustment before blending. A common application is adjusting countrywide data to remove overall differences before using it as a complement for a specific state. This involves calculating average pure premiums for both the subject area and the complementary areas (re-weighted to the subject area's exposure distribution by class), then deriving adjustment factors to apply to the complementary data.  
   * **Evaluation:** This method is unbiased as it accounts for distributional differences. Using multi-state data generally makes it accurate, assuming sufficient data to minimize process variance. It is considered mostly independent as data comes from different states. While data is usually available, computations can be complex and time-consuming, making it harder to explain despite its logical relationship.  
5. **Trended Present Rates:**

   * **Description:** When a larger group complement isn't available, current rates can be used as a proxy. This involves two adjustments: trending the current rates forward to the effective date of the new rates and accounting for differences between the last indicated rate change and the implemented rate change. The formula is: $C \= \\text{Present Rate} \\times \\text{Loss Trend Factor} \\times (\\frac{\\text{Prior Indicated Loss Cost}}{\\text{Prior Implemented Loss Cost}})$. An example calculation shows trending $200 present average rate by 5% over two years and adjusting for prior indication/implementation.  
   * **Evaluation:** Accuracy depends on the process variance of historical loss costs, making it suitable for voluminous data. It is unbiased, as pure trended loss costs are unbiased. Independence varies; if subject and complement data share historical periods, they are not independent. Data is readily available, calculations are straightforward, and the approach is easily explainable. This method is featured in Appendix A of the sources, where the complement is the residual indication based on the latest rate change and indication.  
6. **Competitor’s Rates:**

   * **Description:** For new or small companies with unreliable internal data, competitors' rates can serve as a complement. The rationale is that competitors, especially larger ones, have more exposures and thus less process error.  
   * **Evaluation:** Competitors' manual rates reflect not only loss costs but also marketing, judgment, and regulatory effects, which can introduce inaccuracy. Differences in underwriting and claims practices can also create hard-to-quantify bias. However, competitors' rates are independent of the subject company's data. Obtaining this data can be difficult and time-consuming. Despite potential differences, the rates of similar competitors have a logical relationship and are generally accepted by regulators, often considered the only viable alternative.

#### **II. Excess Ratemaking**

Excess insurance products cover claims exceeding a high attachment point, such as personal umbrella policies or large deductible commercial policies. Boor outlines four methods for developing complements in this area:

1. **Increased Limits Analysis (ILFs):**

   * **Description:** Used when ground-up loss data through the attachment point is available. Increased Limits Factors (ILFs) adjust losses capped at the attachment point to estimate losses in a specific excess layer. The complement formula is: $C \= \\text{Losses capped at A} \\times (\\frac{\\text{ILF}\_{A+L} \- \\text{ILF}\_A}{\\text{ILF}\_A})$.  
   * **Evaluation:** Results can be biased if the subject experience's size of loss distribution differs from that used for ILFs, especially if ILFs are industry-based. Despite accuracy issues, it's often the best available estimate. The error is parameter error, not process error, and tends to be independent of the base statistic. It requires ILFs and ground-up losses, making it practical if information is available. However, its logical relationship to data *below* the attachment point (used for projection) rather than the layer itself can be controversial.  
2. **Lower Limits Analysis:**

   * **Description:** This method uses losses capped at a *lower* limit (d) to estimate the excess layer. The complement formula is: $C \= \\text{Losses capped at d} \\times (\\frac{\\text{ILF}\_{A+L} \- \\text{ILF}\_A}{\\text{ILF}\_d})$.  
   * **Evaluation:** It's difficult to determine if this is more or less accurate than increased limits analysis. Intuitively, it might be more biased due to exacerbated differences in loss distributions, but it could increase estimate stability. Error is generally independent of the base statistic. Data might be less available if a non-standard lower limit is chosen. Calculations are similar to the previous method but still face criticism for being logically related to lower limit losses rather than the layer being priced.  
3. **Limits Analysis:**

   * **Description:** Used when losses capped at a single point are unavailable. This approach analyzes policies at each limit of coverage separately, calculating estimated losses in a given layer using premium volume and expected loss ratio, then performing an ILF analysis on each first dollar limit's loss costs.  
   * **Evaluation:** This complement is biased and inaccurate, similar to the prior two methods. It adds the assumption that the expected loss ratio does not vary by limit. It might be the only available method for reinsurers lacking full loss distribution access. It's more time-consuming but straightforward computationally. It also suffers the criticism of not being based on actual data from the layer being priced.  
4. **Fitted Curves:**

   * **Description:** This method relies on historical data to fit curves (e.g., probability distributions for claim severity or loss costs) and then derives the complement from the distribution.  
   * **Evaluation:** The curve-fitting process is heavily dependent on underlying data, especially large claims, leading to less independence of error than other approaches. It's computationally complex and requires readily available data. While potentially the most logically related to losses in the layer, its complexity can hinder communication.

### **Credibility When Using Statistical Methods (e.g., GLMs)**

It's important to note a key distinction regarding credibility when employing statistical methods like Generalized Linear Models (GLMs) for multivariate classification analysis. Unlike the traditional credibility approaches discussed, the results of a multivariate classification analysis are **typically not credibility-weighted with univariate actuarial estimates**.

Instead, GLMs provide their *own* statistical diagnostics, such as standard errors of parameter estimates and standardized deviance tests (e.g., Chi-Square or F-test), along with practical tests like consistency of results over time. These diagnostics inform the actuary about the meaningfulness and appropriateness of the model results, aiding in the selection of the final model structure and rate differentials. While some research explores integrating Bayesian analysis into statistical modeling (e.g., hierarchical models), this is generally beyond the scope of common practice covered in these texts.

### **Conclusion: The Art and Science of Credibility**

In essence, Credibility Theory provides actuaries with a structured methodology to navigate data limitations and enhance the stability and accuracy of rate estimates. The "complement of credibility" is not merely the inverse of 'Z'; it's a strategically chosen, well-justified ancillary statistic that plays a vital role in refining our predictions, especially when our primary data lacks full credibility.

Whether employing classical methods or more advanced statistical models, the underlying principle remains: effectively leveraging all available, relevant information – both direct and supplementary – to arrive at the most reasonable and justifiable rate for the future policy period. This continuous refinement, supported by careful selection and evaluation of the complement of credibility, is a cornerstone of professional actuarial practice in general insurance pricing.

