Let's delve into the Average Cost per Claim (ACPC) method within the larger context of triangulation methods, highlighting its characteristics, suitable applications, and most importantly, its disadvantages as revealed by the sources.

### **1\. Introduction to the Average Cost per Claim (ACPC) Method**

The Average Cost per Claim (ACPC) method is not a single, rigid formula but rather a "family of methods". Its core principle involves estimating future claims by separating the projection into two distinct components:

* **Claim Frequency**: The expected number of claims.  
* **Claim Severity**: The average cost per claim.

These two components are then combined to derive the estimated ultimate claims. The method can be applied to various data types, including incurred, reported, or settled claims, and the average claim size can be defined based on origin, development, or calendar years. Fundamentally, it requires data on **claim numbers in addition to claim amounts**.

### **2\. Advantages of the ACPC Method (When to Use)**

The ACPC method offers several benefits, particularly in situations where other aggregate methods might fall short:

* **Granular Insight**: A primary advantage is its ability to provide information on how both claim numbers (frequency) and claim amounts (severity) are expected to develop separately. This granular detail allows for a deeper understanding of underlying trends that aggregate models might mask. For instance, it can distinguish whether claims inflation is driven by an escalation of settlement amounts or an increase in claim frequency.  
* **Versatility with Data Characteristics**: It can be useful when dealing with data exhibiting features that aggregate modelling methods might not properly detect or model. This includes situations where "claims reserving protocols have changed over the development history," making other methods invalid.  
* **New Lines of Business / Latent Claims**: For new lines of business, or more complex claims like latent claims (e.g., asbestos, pollution, and health hazards – APH), ACPC can be particularly useful. This is because it allows for explicit assumptions regarding average claim size, the long-term effect of inflation, and the expected number of claims, which are crucial given the highly uncertain and long-tailed nature of such liabilities.  
* **Complementary to Other Methods**: ACPC can be used effectively in conjunction with other projection techniques, such as the Chain Ladder and Bornhuetter-Ferguson methods. For example, Chain Ladder or BF might be used to estimate the ultimate number of claims for the most recent origin years, which then feeds into the ACPC calculation. Conversely, an ultimate estimate from ACPC can serve as a prior for the Bornhuetter-Ferguson method.  
* **Clarity and Simplicity**: It is generally "easy to understand and communicate" to non-technical stakeholders, as it aligns with an intuitive breakdown of claims experience.  
* **Data Availability**: For "direct business in particular, the data required is generally available".  
* **Handling Volatility**: It can help "explain volatile data and results when the data contains only a small number of claims," such as for very small lines of business or reinsurance losses.  
* **Targeted Adjustments**: The separation of frequency and severity enables "more accurate adjustments to be made (where these only affect the frequency or the severity of claims) which would not be possible with other (aggregate) methods".

### **3\. Disadvantages and Issues Arising with ACPC**

Despite its strengths, the ACPC method is not without its challenges and limitations:

* **Higher Data Requirements**: It "needs more detailed information" compared to some other methods like the Chain Ladder, specifically requiring "information on claim numbers in addition to claim amounts information," which may not always be readily available or complete.  
* **Sensitivity to Data Definition and Quality**:  
  * **Distortion by Anomalies**: The method "can be distorted by reopened claims, nil claims or partial payments" if not handled carefully and consistently. Careful definition and consistent treatment of these aspects (e.g., whether nil claims are included or excluded, how multiple partial payments are aggregated, or how reopened claims are allocated) are crucial as they "affect the selected average claim sizes" and claim frequency.  
  * **Correspondence between Data**: It's "of utmost importance to ensure that the claim frequency and claim severity are consistent" and that "the aggregate claim amounts used in the numerator, as far as possible, correspond to the claim numbers used in the denominator". Lack of direct correspondence may necessitate adjustments.  
* **Assumption of Claim Distribution Stability**: The method "assumes that the distribution of claims is the same for each origin year or settlement year". If, for example, an increase in claim frequency is caused by a "new type of claim which has a different average claim size to the past data," this underlying assumption would be violated, potentially leading to inaccurate projections.  
* **Meaningfulness of Averages**: The method "should not be used where the claim count or an average claim size is not meaningful". An example cited is a "subscription market where insurers write different shares on each of the policies that they underwrite (unless an adjustment can be made to allow for this)".  
* **Volatility with Small Samples**: While it can help *explain* volatile data, "small data samples may lead to volatile results" themselves, a common issue with other projection techniques as well.  
* **Complexity of Adjustments (Technical Considerations)**:  
  * **Large Claims**: As with other projection techniques, "we should allow for large claims that may or may not have been notified or recognised as being large". This often involves "adjust\[ing\] the data for the large losses by either excluding them or capping the triangles with a large loss threshold to derive an attritional claims triangle". Separate models may then be needed for these excluded large losses.  
  * **Inflation**: While it allows for explicit inflation assumptions, the "choice of index is key to the success" and it requires careful revaluation of historical data and projection of future amounts.  
  * **Mix of Business/Policy Terms**: "We may need to allow for changes in the mix of business or policy terms and conditions as these changes will distort patterns and trends observed in the data".  
  * **Environmental Changes**: The model may need modification to account for "changes in the legal, economic, social environment, or company operation," whether past or expected.  
  * **Payment Speed**: It can be influenced by "acceleration or slowing in claims payments or settlements," requiring adjustments similar to those for the Berquist-Sherman method.  
  * **Cross-Subsidies**: If a trended average claim amount is used, the method "can introduce cross-subsidies between origin years".

### **4\. ACPC in the Context of Triangulation Methods**

The ACPC method is a recognized member of the triangulation techniques, which include the Chain Ladder and Bornhuetter-Ferguson methods. These methods rely on assumptions about the stability of claim development and that past patterns will continue into the future.

While the Chain Ladder method often projects an ultimate value based on historical development, it can produce extreme results (very high or very low) when data is immature or for years with unusual experience. In contrast, the Bornhuetter-Ferguson method offers a credibility-weighted approach, combining actual experience with a prior estimate, thus being less susceptible to extreme results in early development stages.

The ACPC method provides an alternative perspective, particularly beneficial when aggregate models might not sufficiently capture underlying trends. Its ability to separate frequency and severity is a key differentiator, allowing actuaries to apply more precise adjustments or understand the drivers of change more clearly than purely aggregate methods. As an SP7 actuary, it's essential to recognize that "it is generally advisable, if data permits, to use more than one method to project reserves," possibly combining paid and incurred methods, Chain Ladder, Bornhuetter-Ferguson, and ACPC, and then carefully comparing and understanding the divergences in results. This comprehensive approach allows for a more robust and insightful reserving exercise.

