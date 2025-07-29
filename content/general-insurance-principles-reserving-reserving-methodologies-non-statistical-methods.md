Right, Actuarial Trainees, let's delve into the discussion of **Non-statistical Methods** within the broader context of Reserving Methodologies. As your Specialist Actuarial Note Builder and Exam Coach for SP7, I'll guide you through the various approaches, their applications, advantages, and disadvantages, drawing directly from our source materials.

### **I. Introduction to Reserving Methodologies and Uncertainty**

At its core, general insurance reserving aims to determine a point estimate of the best estimate reserves. However, reserving is not an exact science, and the actual reserve required will almost certainly differ from this estimate. This inherent uncertainty necessitates the use of various methods to quantify the range of possible outcomes around the best estimate.

The sources of reserving uncertainty are broadly categorized into three types:

* **Process Uncertainty:** Arises from the inherent randomness of future claims events, such as the amount and timing of individual claims.  
* **Parameter Uncertainty:** Stems from the imprecision in estimating model parameters due to imperfect, inconsistent, incomplete, or non-existent historical data.  
* **Model Uncertainty (or Model Error):** Occurs because actuarial models are simplified representations of complex underlying processes and may not fully reflect all features of the underlying system, leading to uncertainty in the estimates produced.

To address this uncertainty, actuaries employ different approaches, including stochastic models, scenario tests, and the use of alternative sets of assumptions. While stochastic models aim to produce a full distribution of outcomes, there are many circumstances where non-statistical methods are employed due to data limitations, the nature of the risk, or practical considerations.

### **II. Non-Statistical Methods in Reserving**

Non-statistical methods for reserving are those that do not primarily rely on fitting statistical distributions to historical data or extrapolating past statistical patterns. Instead, they often lean heavily on actuarial judgement, expert opinion, or simplified approaches when data is sparse, unreliable, or when dealing with unique or extreme events.

The sources highlight several non-statistical methods or approaches:

#### **A. Case Estimates**

Case estimates refer to the amounts set aside for individual reported claims that have not yet been fully settled.

* **Definition and Application:** An insurer's claims department often sets case estimates for individual claims, which are amounts recorded for known outstanding claims. These can be subjective and vary based on the company's philosophy, e.g., realistic or prudent. Some insurers rely on a total estimated value for a risk group based on statistical methods rather than individual case estimates, though this is rare.  
* **Advantages:**  
  * It is the only approach that can make use of all the known data on individual outstanding claims.  
  * Experienced and skilled assessors can weigh qualitative factors that influence the claim amount.  
  * Case-by-case methods may still be applicable when statistical models are not reliable.  
  * They give greater management control over total claims reserves.  
  * They can pick up new trends more quickly than statistical methods.  
* **Disadvantages:**  
  * Case estimates cannot produce estimates for claims that have not been reported (IBNR). A separate allowance for IBNR must be made if case estimates are used for the main reserving process.  
  * Assessors may not use consistent rates of inflation, and it is hard to produce estimates on a range of possible bases.  
  * Individual case-by-case estimates are not possible for outsiders who do not have access to all individual claim data.  
  * They can be expensive, particularly for classes with many small claims.  
  * Case estimates can be influenced by changes in reserving philosophy.

#### **B. Exposure-Based Methods**

These methods relate reserves or premiums to a measure of exposure rather than relying solely on past claims development patterns. They are particularly useful when historical claims data is limited or non-existent.

* **Application:**  
  * **New Books of Business:** For a new line of business with little or no historical data, an insurer may apply market benchmarks or benchmarks from similar books of business to estimate reserves based on premiums or claims information.  
  * **Latent Claims:** Exposure-based methods are usually used for claims like asbestos, pollution, and health hazards (APH), where development patterns are unpredictable and it's difficult to allocate claims to a single origin year. This is because their long-term development is inherently unknown.  
  * **One-off Events or Risks:** For specific large, one-off events or non-standard risks (e.g., satellite launch), where statistical methods are not suitable due to the unique characteristics of the event.  
* **Types of Exposure-Based Methods:**  
  * **Bottom-up Approach:** Involves examining policies individually to determine the likelihood of exposure to a loss event, with claims experts assessing the extent of any potential claim.  
  * **Top-down Approach:** Less detailed, often applying factors to aggregated exposures.  
* **Data Requirements:** Requires information for each policy to establish potential liability, such as policy limits, start/end dates, insured perils, and exclusions.

#### **C. Simple Ratio Methods / Benchmarks**

These involve applying pre-determined ratios or comparing results against external or internal benchmarks when detailed data or sophisticated models are not feasible.

* **Application:**  
  * **IBNR Estimation:** For simple cases, IBNR might be estimated as a fixed percentage of earned premiums or reported claims, derived from past knowledge of the business.  
  * **Comparison and Cross-Checks:** Benchmarks (from industry, market, or other related classes) are valuable for comparing reserving strength between insurers, or as an alternative approach to compare against results derived from the insurer's own data.  
  * **When Data is Sparse:** Useful when data is insufficient to produce reasonable development patterns for complex techniques.  
* **Considerations:** It is crucial to assess whether the benchmark source has characteristics appropriate to the business being analysed, including similar reserving philosophies, underlying business nature, terms and conditions, and inflation allowances.

#### **D. Policy Limits**

Policy limits can provide a simple upper bound for reserves in certain circumstances.

* **Application:** Used where materiality is not an issue, or when time pressure prevents significant analysis.  
* **Approach:** A more reasonable approach than simply using the maximum limit might be a proportion of the policy limits, determined by benchmarking or intuition.

#### **E. Intuition / Professional Judgement**

Actuarial judgement is a pervasive non-statistical element throughout all reserving work.

* **Application:**  
  * **Cross-Checking:** It serves as a useful cross-check for any actuary, using personal insight, views, beliefs, and knowledge to produce an initial estimate for comparison with other methods and actual experience.  
  * **Model Selection and Adjustment:** Judgement is vital in selecting models, adjusting parameters for one-off events, and determining the reasonableness of results.  
  * **Parameterization of Dependencies:** It can be difficult to parameterize dependencies from data, making judgement important, especially for correlations in stochastic models.  
* **Importance:** It helps to bridge the gap where quantitative data is incomplete, inaccurate, or sparse.

#### **F. Scenario Tests**

While they can involve quantitative elements, scenario tests often focus on plausible future conditions or extreme events that may not be directly extrapolable from historical data, making them less purely "statistical" in their design compared to, say, a full stochastic model.

* **Definition and Purpose:** Scenario testing involves examining the likely impact of catastrophic events or specific plausible future conditions on an insurer's outstanding liabilities. The key aspect is understanding the interdependency of various uncertainties under extreme conditions, which is difficult to model parametrically.  
* **Examples of Scenarios:** Can include poor attritional claims experience, latent claims, reinsurance bad debt, interest rate changes, inflation levels, expense levels, and exchange rate movements.  
* **Advantages:**  
  * Allows a more detailed analysis of the tail end of the reserve distribution compared to a full stochastic model, by specifically focusing on the coincidence of adverse factors.  
  * More focused and quicker to produce results than a full stochastic model, as it targets specific questions and extreme outcomes.  
  * Model uncertainty is less of a problem, as it's not trying to perfectly model the underlying process but rather test specific 'what-if' situations.  
  * Easier to communicate to a non-technical audience.  
* **Disadvantages:**  
  * Typically provides information only on the extremes of the distribution, not a full distribution of outcomes.  
  * More subjective than other methods, as the actuary must decide which extreme scenarios to investigate.

#### **G. Use of Alternative Sets of Assumptions**

This approach involves estimating reserves using parameter values that differ from those chosen for the best estimate. When applied to deterministic models, it is inherently non-statistical in its output of uncertainty, as it doesn't generate a probability distribution.

* **Purpose:** To assess the sensitivity of the reserving results to changes in key assumptions. It helps understand the potential impact if factors develop differently from the "best estimate" basis.  
* **Advantages:**  
  * Simple to perform on both deterministic and stochastic models.  
  * Allows for the exercise of judgement in selecting parameters, enabling the exclusion of atypical historical volatility that is not expected to be repeated.  
  * Useful for providing information to management about the sensitivity of results.  
* **Disadvantages:**  
  * Unless explicit probabilities are assigned, it cannot estimate the full distribution of future outcomes.  
  * It ignores model uncertainty.  
  * If used with a deterministic model, it does not allow for process uncertainty, only parameter uncertainty.

### **III. Context within Reserving Methodologies**

Non-statistical methods are crucial complements to statistical and stochastic reserving techniques, especially when the limitations of the latter become apparent.

* **When Statistical Methods are Not Suitable:**

  * **Sparse or Inadequate Data:** Statistical methods may not be appropriate when data is incomplete, inconsistent, non-existent, or of poor quality. This is common for new lines of business or high-layer reinsurance.  
  * **Unusual or One-off Events:** Statistical methods, particularly triangulation techniques, are often unsuitable for unique, large, or catastrophic claims, as their development profiles may differ significantly from attritional claims.  
  * **Latent Claims:** The unpredictable and long-tailed nature of latent claims (e.g., asbestos, pollution) makes standard statistical methods unreliable.  
  * **Changes in Business or Procedures:** Significant changes in the mix of business, policy conditions, underwriting, claim settlement practices, or data storage protocols can distort historical patterns, making statistical projections problematic.  
  * **Extreme Tails of Distribution:** Statistical methods, especially those based on historical data, tend to underestimate true variability and may not accurately represent the extreme tails of the distribution due to limited historical experience of rare events.  
* **Relationship with Deterministic and Stochastic Models:**

  * Non-statistical approaches often form the basis of **deterministic models**, which produce a single point estimate without a full probability distribution of outcomes. When used with deterministic models, alternative sets of assumptions and scenario tests primarily address parameter uncertainty, but not process uncertainty.  
  * Even when stochastic models are used, non-statistical insights are vital. For instance, the Mack and bootstrapping methods, while stochastic, are limited by historical data and will underestimate variability not reflected in the past. Actuarial judgement is crucial to supplement these models, especially when estimating parameters for the tail of a claims distribution.  
  * A blend of approaches, including stochastic models for some risks and stress/scenario tests (often non-statistical in nature) for others, is common in capital modelling.

### **IV. Communication of Results and Professional Issues**

Regardless of the methods used, effective communication of the reserving results and associated uncertainties is paramount.

* **Clarity on "Best Estimate":** The actuary must clearly define what is meant by a "best estimate" reserve and acknowledge it as a single point estimate among many possibilities.  
* **Transparency of Assumptions and Limitations:** It is essential to highlight key assumptions, their rationale, and emphasize the critical assumptions to which the reserve estimate is most sensitive. Any restrictions or shortcomings in the analysis, such as incomplete data or scope limitations, must be stated clearly.  
* **Extent of Uncertainty Capture:** Actuaries must specify the extent to which the calculated range reflects various sources of uncertainty (e.g., parameter uncertainty from alternative assumptions, but often not full model or process uncertainty with deterministic models).  
* **Audience Appropriateness:** Communication must be tailored to the audience, explaining technical terms and concepts clearly to non-technical stakeholders, ensuring they understand the implications for decision-making.  
* **Professional Judgement in Resolving Differences:** When alternative results arise (e.g., from different actuaries or management), it is important to compare them, identify areas of difference, and communicate these to stakeholders, recognizing that financial interests can influence preferred figures.

By judiciously applying and communicating the results from non-statistical methods, actuaries can provide a more robust and realistic understanding of reserving uncertainty, which is vital for internal management, regulatory compliance, and strategic decision-making.

