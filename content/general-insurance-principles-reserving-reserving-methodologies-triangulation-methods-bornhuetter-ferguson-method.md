### **📗 Chapter 15: Triangulation Methods – The Bornhuetter-Ferguson Approach**

As a Specialist Actuarial Note Builder and Exam Coach, I'll guide you through the intricacies of the Bornhuetter-Ferguson (BF) method, a cornerstone of general insurance reserving. We'll explore its definition, application, advantages, disadvantages, and its interplay with other triangulation techniques, always keeping the SP7 syllabus objectives firmly in sight.

#### **0.0 Introduction to Triangulation Methods**

Before we dive into the specifics of Bornhuetter-Ferguson, it's vital to appreciate the broader context. Triangulation methods are fundamental to claims reserving in general insurance, providing structured ways to project future claims based on historical patterns. The main methods covered in SP7 include the chain ladder, Bornhuetter-Ferguson (BF), and Average Cost Per Claim (ACPC) methods.

These methods, while powerful, operate under specific assumptions about the underlying data. Your role as an actuary is not merely to apply these mechanically, but to understand their underlying principles, strengths, weaknesses, and how distortions in data can impact their results.

#### **4.0 The Bornhuetter-Ferguson (BF) Method: A Hybrid Approach**

The Bornhuetter-Ferguson method stands out as a sophisticated "credibility estimate". It strategically combines two distinct philosophies of claims reserving:

1. **An expected level of claims (Exposure-based):** Often derived from an *a priori* estimate or a loss ratio method, providing stability and an external viewpoint.  
2. **A projection based on experience to date (Development-based):** Typically derived from a chain ladder method, incorporating the actual claims development observed in the data.

This makes BF a powerful hybrid, leveraging the strengths of both approaches. It's applicable to both paid and incurred claims data.

##### **4.1 Application of the Bornhuetter-Ferguson Method: Step-by-Step**

Applying the BF method involves a structured sequence of calculations:

1. **Determine an Initial Expected Ultimate Claim Amount (LR):** This is your *a priori* estimate for the relevant origin period. This initial loss ratio might typically come from the previous year's best estimate results, adjusted for factors like claims inflation, rate changes, or large claims.  
2. **Estimate the Proportion of Claims Currently Incurred or Paid (p):** This is based on the observed development of the claims data up to the valuation date. For an incurred BF method, you use incurred claims; for a paid BF method, you use paid claims.  
3. **Derive the Proportion of Claims Yet to Be Incurred or Paid (1-p):** This is simply the complement of the proportion already developed.  
4. **Determine the Value of Undeveloped or Unpaid Claims:** Multiply the initial expected ultimate claims (LR) by the proportion of claims currently undeveloped or unpaid (1-p). This effectively estimates the future IBNR or future paid claims based on the *a priori* expectation.  
   * *Formula:* `Undeveloped/Unpaid Claims = LR × (1 - p)`  
5. **Calculate the Final Expected Ultimate Claims:** This is the sum of the claims incurred or paid to date (C, from your data) and the estimated value of the undeveloped or unpaid claims from Step 4\.  
   * *Formula:* `Final Ultimate Claims = C + LR × (1 - p)`

Beyond calculating ultimate claim amounts, the BF method can also be adapted to derive estimated ultimate loss ratios, ultimate numbers of claims, or even ultimate premiums.

##### **4.2 When to Use the Bornhuetter-Ferguson Method (Use Cases)**

The BF method truly shines in specific scenarios where other methods might fall short:

* **Sparse or Immature Data:** It is particularly useful when the available data for a specific cohort is sparse, such as for recent cohorts or very long-tailed portfolios like liability excess of loss reinsurance. In such cases, purely projection-based methods (like chain ladder) can produce highly volatile or unreliable results.  
* **Volatile Claim Activity:** For business lines where claims activity is expected to be extremely volatile due to small premium volumes, BF provides a more stable estimate by incorporating an *a priori* expectation.  
* **Blending Experience and Exposure:** When a combination of actual claims experience to date and an

