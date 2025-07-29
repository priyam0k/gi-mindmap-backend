Right, Actuarial Trainees, let's turn our focus to another crucial aspect of assessing reserving uncertainty: the **Use of Alternative Sets of Assumptions**. As your Specialist Actuarial Note Builder and Exam Coach for SP7, I'll guide you through its definition, purpose, application, and its place within the broader context of reserving methodologies.

### **I. Introduction to Reserving Methodologies and Uncertainty**

At the core of general insurance actuarial practice lies the estimation of reserves – the amounts an insurer sets aside to cover future claim payments arising from past and present policies. While traditional reserving methods, such as the chain ladder, often yield a single "best estimate" of these liabilities, the reality is that the actual amount ultimately paid will almost certainly diverge from this estimate. This inherent variability necessitates sophisticated approaches to quantify the uncertainty surrounding our best estimates.

This growing emphasis on quantifying uncertainty stems from various factors, including the potential for bankruptcies due to catastrophic events, increased awareness of latent claim issues, adverse economic conditions, and evolving regulatory and professional guidance.

The sources of reserving uncertainty can be broadly categorised into three types:

* **Process Uncertainty:** Arises from the inherent randomness of future claims events (e.g., frequency, severity, timing of payments).  
* **Parameter Uncertainty:** Stems from the imprecision in estimating model parameters due to imperfect, inconsistent, incomplete, or non-existent historical data.  
* **Model Uncertainty (or Model Error):** Occurs because actuarial models are simplified representations of complex underlying processes and may not fully capture all features of the real-world system, leading to uncertainty in the estimates produced.

To address these uncertainties, actuaries employ various methods to estimate ranges of reserves, rather than just a single point estimate. These approaches include stochastic models, scenario tests, and critically, the **use of alternative sets of assumptions**.

### **II. Alternative Sets of Assumptions: A Detailed Examination**

#### **A. Definition and Purpose**

The **use of alternative sets of assumptions** is an approach to quantifying uncertainty in reserves by estimating reserves using parameter values that differ from those chosen for the best estimate. Instead of providing just one calculation based on the single best estimate, this method involves performing multiple calculations, each time varying a selection of underlying assumptions.

The primary purpose of this approach is to assess the **sensitivity of the reserving results to changes in key assumptions**. It helps an insurer understand the potential impact on outstanding liabilities if certain factors develop differently than expected under the "best estimate" basis. This is particularly valuable for:

* **Internal Management Information:** To provide a realistic view of the business and to show management how sensitive results are to various assumptions, helping them understand potential deviations from the best estimate.  
* **Due Diligence for Mergers and Acquisitions (M\&A):** A purchaser will often make a range of estimates based on different assumptions to understand the impact of potentially selecting alternative assumptions, forming a view on the adequacy of booked reserves.

#### **B. Application and Characteristics**

This method can be applied to both **deterministic and stochastic models**. When using alternative sets of assumptions, it is crucial to consider the interdependencies between different assumptions. For instance, inflation assumptions and discount rate assumptions are typically correlated and should be varied consistently across alternative scenarios.

The selection of alternative assumptions often involves actuarial judgment, especially when exploring "worst-case scenarios" to provide management with a sense of the downside risk. This can involve systematically increasing or decreasing a few data values by a certain percentage, or removing specific data points, to understand their impact.

#### **C. Types of Uncertainty Addressed**

This approach primarily addresses **parameter uncertainty**. By varying parameters like inflation rates, claims development factors, or expense levels, actuaries can quantify the uncertainty arising from the selection of these parameters.

While it can be used with stochastic models to explore how the *distribution* of outcomes changes under different parameter sets, if alternative assumptions are applied to a **deterministic model**, this method generally **does not allow for process uncertainty**. Furthermore, it inherently **ignores model uncertainty**, as it assumes the chosen model structure is correct and only varies the inputs to that model.

#### **D. Advantages of Using Alternative Sets of Assumptions**

1. **Simplicity and Ease of Implementation:** This method is relatively straightforward to perform, whether applied to deterministic or stochastic models. It doesn't necessarily require complex statistical modelling to generate multiple outputs.  
2. **Facilitates Actuarial Judgment:** It provides a flexible framework for actuaries to explicitly apply their professional judgment in selecting which assumptions to vary and by how much. This allows for a targeted analysis of specific concerns or sensitivities.  
3. **Targeted Scenario Analysis:** Unlike a full stochastic model that produces a complete distribution of outcomes (including very unlikely ones), this method allows actuaries to explicitly *exclude* scenarios that are not expected to be repeated in the future. This enables a more focused analysis on plausible adverse or favourable outcomes that are of direct interest to management.  
4. **Improved Comprehensibility:** By presenting a limited number of distinct scenarios or assumption sets, the results can be more easily explained and understood by a non-technical audience compared to complex statistical distributions from stochastic models.  
5. **Supports 'What-if' Analysis:** It is highly effective for 'what-if' analysis and scenario planning, allowing management to explore the financial implications of different strategic decisions or external events.

#### **E. Disadvantages of Using Alternative Sets of Assumptions**

1. **Limited Distributional Information:** A key drawback is that this method, on its own, generally **cannot estimate the full distribution of future outcomes** unless probabilities are explicitly assigned to each alternative set of assumptions. Without assigned probabilities, it provides a range of point estimates rather than a complete probability distribution of reserves.  
2. **Ignores Model Uncertainty:** As discussed, this method assumes the underlying model is correct and only varies its inputs. It does not account for the uncertainty inherent in the choice or specification of the model itself.  
3. **Limited Process Uncertainty Capture (for Deterministic Models):** If applied to a deterministic model, it does not inherently capture process uncertainty, which is the inherent randomness of future claims. While it can be used with a stochastic model to incorporate process risk, its standalone application to deterministic models overlooks this crucial source of variability.  
4. **Subjectivity in Assumption Selection:** The selection of which assumptions to vary, and the range over which they are varied, can be subjective. This might lead to an incomplete picture of uncertainty if critical but unconsidered correlations or extreme movements are overlooked.

### **III. Context within Reserving Methodologies and Communication**

The use of alternative sets of assumptions is one of three primary approaches for estimating ranges of reserves, alongside stochastic models and scenario tests. While scenario tests often involve varying *combinations* of stresses or plausible future conditions to examine *interdependencies* under extreme conditions, the "alternative sets of assumptions" method focuses more broadly on varying individual or correlated parameters to assess overall sensitivity.

When communicating the results derived from alternative sets of assumptions, it is paramount to ensure clarity and avoid misunderstandings. Actuaries must:

* Clearly define what is meant by the "best estimate" and acknowledge that it is just one point estimate among many possibilities.  
* Highlight the key assumptions made and explain their rationale.  
* Emphasise the critical assumptions to which the reserve estimate is most sensitive.  
* State clearly the extent to which the calculated range is intended to reflect various sources of uncertainty (e.g., parameter uncertainty, but often not full model or process uncertainty with deterministic models).  
* Comment on any restrictions or shortcomings in the analysis, such as incomplete data or limitations in the scope of work.

By effectively employing and communicating the results from alternative sets of assumptions, actuaries can provide stakeholders with a more comprehensive understanding of reserving uncertainty, supporting better-informed decision-making for internal management, capital assessment, and strategic planning.

