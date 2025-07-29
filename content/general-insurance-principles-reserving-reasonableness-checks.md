Alright, aspiring SP7 Actuaries\! Let's delve into the crucial area of *Reasonableness Checks* in the broader context of *Reserving*. This isn't just a theoretical exercise; it's a fundamental aspect of professional actuarial practice that ensures our reserve estimates are robust, reliable, and fit for purpose. Remember, a "best estimate" is not a single, immutable figure, but rather a point within a range of possibilities, and our ability to justify it is paramount.

We'll structure this discussion to provide you with a clear, sequential understanding, just like you'd build a solid actuarial report.

---

### **Section 1: The Importance of Assessing Reserving Results**

As actuaries in General Insurance, *reserving* is a core activity. Our primary goal in a reserving exercise is to determine a point estimate of the best estimate reserves. However, the reality is that the actual reserve required will almost certainly differ from this estimate due to inherent uncertainties. Therefore, assessing the reasonableness of our reserving calculations is one of the most critical stages in the entire reserving process.

The actuary must ensure that:

* The figures are *justifiable*.  
* The *methodology and assumptions adopted are appropriate* for the specific purpose of the reserving exercise.

It's no longer sufficient to merely describe reserves using single point estimates without also gauging the size of the prediction errors. This is why we need robust checks.

---

### **Section 2: Approaches to Analysing Reserving Results**

To achieve the objective of assessing reasonableness, actuaries employ two primary types of analysis, ensuring a balance between the understanding gained and the time/cost involved:

1. **Applying Diagnostic Tests:** These are measures used to help interpret data or results, primarily providing a high-level "reasonableness" check or indicating areas for closer examination.  
2. **Carrying out an Analysis of Emerging Experience:** This involves comparing actual experience to what was expected, allowing for the updating of assumptions to reflect recent trends.

Our final selection of results will always involve judgement, informed by these analyses and our experience.

---

### **Section 3: Diagnostic Tests in Reserving**

Diagnostics are invaluable tools to test and verify the underlying methodology and assumptions used in reserving.

#### **3.1 Common Diagnostics and Their Insights**

A review of various metrics, often presented as triangles, can highlight key trends and potential issues.

* **Loss Ratios (Paid, Outstanding, IBNR, Incurred, Ultimate):** Reviewing changes in these ratios can highlight:  
  * Changes in premium rating strength, potentially influenced by the underwriting cycle. Adjustments using a rate index may be needed, but beware of rating increases solely reflecting increased risk.  
  * Changes in the stringency of claims underwriting.  
  * Improvements or worsening of claims experience.  
  * Changes to the rating basis.  
  * Errors or inconsistencies in the reserving process.  
* **Average Outstanding Case Estimate:** Reviewing the triangle of average outstanding case estimates can reveal changes in the strength or prudence of case reserves over time.  
* **Ratio of IBNR to Case Estimates:** This diagnostic is particularly helpful for more mature cohorts, especially when IBNR is expected to primarily reflect IBNER (Incurred But Not Enough Reported) rather than "pure" IBNR claims.  
* **Open Nil Claim Counts:** For classes where these are recorded, monitoring them can provide an early warning of anticipated increases in claims costs or processing problems.  
* **Reinsurance to Gross Ratios:** Applying diagnostics both gross and net of reinsurance is essential. Reviewing the ratios between gross, reinsurance, and net estimates (e.g., net to gross ratios) is valuable. While simpler for proportional reinsurance, understanding these ratios is crucial for non-proportional business too, noting the impact of fixed limits and deductibles diminishing with inflation.  
* **Incremental Development Triangles:** These diagnostics help consider the level of IBNR or reserves for a cohort compared to movements seen in prior cohorts as they develop to ultimate. While not a precise technique, they provide a good sense check for judgemental selections or when reviewing at a less granular level.  
* **Comparison of Assumed Future Development Patterns with Past Development Patterns:** This is one of the most important sets of diagnostics. It involves comparing cumulative paid or incurred claims development as a proportion of estimated ultimate claims for a given origin cohort across different origin years.  
  * **Stability of Development Pattern:** If the development pattern is volatile, actuaries must consider the reliability of estimates. The distribution of final outcomes is often positively skewed (adverse development exceeding favourable), necessitating allowance for a sufficient tail beyond historical experience.  
  * **Relative Speeds:** Consider if the relative speeds of suggested development patterns for different classes are appropriate.  
  * **Claim Development vs. Premium Development:** Investigate the reasons for changing premium development patterns and their potential impact on claim development patterns.  
  * **Comparison to Benchmarks:** Benchmarks from industry, market sources, related classes (e.g., household contents for household buildings), or similar portfolios can be used to compare development patterns.  
* **Residuals of Fitted Link Ratios:** Analysing the size and pattern of residuals on individually fitted link ratios from run-off patterns can provide useful insights.

#### **3.2 Interpreting Diagnostics – Key Considerations**

Simply producing these diagnostics isn't enough; interpretation is key.

* **Understanding Reasons for Change:** We must ensure we understand *why* diagnostics change over time or show unusual features.  
* **Investigation and Action:** If unusual features are identified, investigate the reason, understand the implications for the reserving process, and take appropriate action (e.g., change methodology or assumptions).  
* **Materiality:** Consider materiality when addressing features. An actuary may choose *not* to update methodology or assumptions if the resulting change in reserves is immaterial, especially if it aligns with the purpose of the exercise.  
* **Actuarial Control Cycle Link:** This process is analogous to the feedback stage of the actuarial control cycle: identifying deviations, understanding their reasons, and making appropriate adjustments.  
* **Exclusion of Special Features:** Where possible, exclude exceptional items like large losses to avoid distorting the overall picture, but *ensure the final reserve still accounts for these items*.  
* **Granularity:** Consider the appropriate level of granularity for reviewing diagnostics and making assumptions, sometimes reviewing at a higher level.

---

### **Section 4: Analysis of Emerging Experience**

This involves a direct comparison of actual experience against previously expected outcomes.

#### **4.1 Actual Versus Expected (A vs E) Analysis**

Actuaries often perform an 'Actual versus Expected' exercise, comparing the actual experience in the period since the last review to the expected experience for that period. This analysis informs updates to selected assumptions to reflect the most recent trends.

#### **4.2 Avoiding Anchoring and Overreaction**

A significant pitfall is *anchoring*, the tendency to rely too heavily on prior information. There's a danger of anchoring on past experience and not adjusting assumptions quickly enough to unexpected developments. Conversely, there's also a risk of *overreacting* to short-term fluctuations. Finding the right balance is crucial. Periodically reviewing the accuracy of past estimates and methods helps learn what works well in different situations.

#### **4.3 Consistency and Inflation**

When providing discounted estimates, it's vital to ensure *consistency* between economic inflation assumptions and the discount rate, as well as any assumptions used for yields and asset returns in a corresponding solvency assessment. The *difference* between these two assumptions is often more critical than their absolute values.

---

### **Section 5: Factors Influencing Reasonableness and Potential Divergence**

Several factors can lead to differences in reserving results and warrant careful consideration during reasonableness checks.

#### **5.1 Underwriting and Reserving Cycles**

The *underwriting cycle* (periods of hard/soft premium rates) and the *reserving cycle* (over- or under-estimation of booked reserves) can significantly influence results.

* **Underwriting Cycle:** Rates may soften due to competition, potentially leading to future adverse claims experience.  
* **Reserving Cycle:** This can cause development patterns to appear longer in a soft market.  
* **Allowance:** Use of a *rate index* when deriving initial expected loss ratios in methods like Bornhuetter-Ferguson can help allow for the underwriting cycle. The initial expected loss ratio should also account for changes in the reserving cycle.

#### **5.2 Actuarial Judgement and Alternative Estimates**

Reserving is not an exact science, and actuarial judgement plays a significant role.

* **Different Actuaries, Different Results:** Two actuaries, even with the same data and purpose, may estimate different reserve values due to differences in judgement.  
* **Alternative Estimates:** Estimates from other actuaries, management (claims and underwriting teams), or market benchmarks should be compared.  
  * **Underwriting and Claims Staff Insights:** These teams have greater familiarity with the portfolio and can provide valuable qualitative information (e.g., changes in claims processes, specific claim issues) that can influence the actuary's selections. However, evidence of such changes should be sought in data, not solely taken as fact.  
  * **Materiality and Purpose:** When deciding whether to adjust a reserve based on alternative estimates, consider overall materiality, the purpose of the exercise, and whether the current estimate lies at the extreme ends of a reasonable range.  
  * **Professional Issues:** Be aware that alternative estimates may be influenced by financial interests (e.g., management pressure to reduce figures). Challenges should not solely be aimed at reducing figures.

---

### **Section 6: Reasonableness Checks for Stochastic Reserving Results**

Stochastic reserving methods produce not just a point estimate but also a distribution of possible outcomes, allowing for the quantification of uncertainty. Validating these results is an essential stage before communicating them.

#### **6.1 Validation Approaches for Stochastic Models**

The assessment depends on the methods used and the exercise's purpose, involving judgement and experience.

* **Reconciliation:** Compare stochastic results with deterministic results.  
* **Graphical Review:** Visually inspect the results.  
* **High-Level Reasonableness Checks:** Apply numerical diagnostics.  
* **Comparison to Benchmarks:** Compare results against external benchmarks.  
* **Back Testing:** Test the model's performance against past actual outcomes.  
* **Stress and Scenario Tests:** Apply these to assess the impact of specific adverse conditions or extreme events, especially for the tail of the distribution. These are crucial where historical data may not represent extreme outcomes.

#### **6.2 Limitations and Judgement**

* **Data Scarcity for Extremes:** Parameterising distributions for the extreme tails of outcomes is difficult due to limited historical data.  
* **Simplifying Assumptions:** Assumptions reasonable for the central distribution may break down at the extremes.  
* **External Factors:** Historical data may not capture all sources of variability, such as future Ogden discount rate changes, one-off court judgments, or prolonged inflation.  
* **Subjectivity of Judgement:** Coping with data peculiarities, such as negative increments in claims data (which can be problematic for log-normal models), requires actuarial judgement.  
* **Higher Percentiles:** Validation is especially important for results used to estimate reserves at higher percentiles (e.g., 99.5th), as these are generally less reliable than estimates at lower percentiles.

---

### **Section 7: Professionalism and Communication**

Effective communication of reserving results and their inherent uncertainties is critical.

#### **7.1 Transparency and Justification**

* **Clarity on Best Estimate:** Clearly define what is meant by a "best estimate" reserve.  
* **Material Assumptions:** Communicate material assumptions and their rationale.  
* **Limitations and Uncertainty:** Explain any significant limitations of models used and their implications. Describe material uncertainty in the data and the approach taken to deal with it.  
* **Judgements:** Communicate key judgements that have a material impact on estimates.  
* **Sources of Uncertainty:** State clearly the extent to which any margin or range reflects the various sources of uncertainty (specification error, selection error, estimation error, process error).  
* **Consistency in Terminology:** Define terms carefully and communicate them appropriately to the audience, especially for concepts like "range of best estimates," "range of possible outcomes," and "range of reasonable/probable/plausible outcomes".

#### **7.2 Regulatory and Accounting Compliance**

* **Local Regulations:** Reserving actuaries *must* understand and comply with local reserving regulations and accounting standards, seeking advice or refusing to act if competence is lacking. This includes regulations that might require or prohibit discounting, or specify risk margins (e.g., Solvency II, IFRS 17).  
* **Audit Trail:** Maintain a clear audit trail justifying selected assumptions, documenting limitations, and explaining methodology choices.

By rigorously applying these reasonableness checks and adhering to professional standards, actuaries can build confidence in their reserving results, support informed decision-making, and uphold the integrity of financial reporting for general insurers. Keep honing these skills; they are indispensable for your SP7 success and your professional career\!

