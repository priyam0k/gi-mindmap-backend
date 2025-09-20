As your Specialist Actuarial Note Builder and Exam Coach for SP8, let's construct a detailed note on **Rating Factors** within the broader context of **Key Product Features**. Understanding rating factors is a cornerstone of general insurance pricing. It's the mechanism by which insurers differentiate risk and move from a single community price to a more equitable and commercially sound pricing structure that reflects the risk characteristics of individual policyholders.

### **Key Product Features: Rating Factors**

In general insurance, the premium charged to a policyholder must reflect the amount of risk they bring to the insurer. While a basic premium can be calculated using a simple *measure of exposure* (e.g., vehicle-year for motor insurance or sum-insured-year for property insurance), this is rarely sufficient on its own. Risks are not homogeneous, and insurers must refine their pricing using rating factors to ensure fairness, remain competitive, and avoid adverse selection.

---

#### **1\. Differentiating Key Terminology**

It's crucial to distinguish between three related concepts:

* **Risk Factors**: These are any characteristics that have a genuine bearing on the amount of risk, affecting either the expected frequency or severity of claims. Examples include a driver's skill, the number of miles driven, or how carefully a business is managed.  
* **Rating Factors**: These are the specific, measurable factors actually used in the premium calculation process. A good rating factor is either a directly measurable risk factor or a reliable proxy for an underlying risk factor that is difficult to measure objectively. For example, "number of years no-claim discount" is used as a proxy for "driving skill".  
* **Underwriting Factors**: This term encompasses all rating factors plus any subjective judgements that an underwriter might apply when assessing a risk and setting the final premium or policy conditions.

---

#### **2\. The Purpose and Importance of Rating Factors**

The primary function of a rating structure is to categorize policyholders into homogeneous risk groups, ensuring that the premium charged is appropriate for the relative risk of each group. A fair and accurate structure is vital for several reasons:

* **Equity**: It ensures fairness between policyholders, with higher-risk individuals paying more than lower-risk ones.  
* **Avoiding Adverse Selection**: If an insurer's rating structure is inaccurate, it risks charging too much for low risks (who will go to competitors) and too little for high risks (who will be attracted to the insurer), leading to an unprofitable portfolio.  
* **Commercial Viability**: A robust rating structure allows an insurer to compete effectively, manage its risk appetite, and achieve its profitability targets.

---

#### **3\. Desirable Properties of a Rating Factor**

For a characteristic to be an effective rating factor, it should ideally meet several criteria:

* **Defines the Risk Clearly**: It must have a demonstrable correlation with the expected claims cost.  
* **Practicality**: The information must be easy for the policyholder to provide and for the insurer to obtain and record.  
* **Objectivity and Verifiability**: It should be a factual quantity that is not open to subjective interpretation, helping to prevent fraud and disputes. For example, `date of birth` is better than `age`.  
* **Non-Manipulable**: The policyholder should not be able to easily manipulate the factor to obtain a cheaper quote.  
* **Low Correlation with Other Factors**: An ideal rating factor adds new information and does not simply replicate what another factor is already measuring.  
* **Market and Customer Acceptability**: The factor must be acceptable to policyholders, brokers, and the wider market. For instance, requiring genetic test results would likely be unacceptable to customers.  
* **Legal and Regulatory Compliance**: The use of the factor must be permitted by law. For example, the EU Gender Directive prohibits the use of gender as a rating factor in insurance pricing.

---

#### **4\. Rating Factors by Line of Business**

The specific rating factors used vary significantly by the type of insurance product.

##### **🔸 4.1 Private Motor Insurance**

Motor insurance is a prime example of a class that uses a large number of rating factors to proxy for underlying risks like driving ability, vehicle usage, and theft risk. Common rating factors include:

* **Driver-related**: Age, gender (where permitted), driving convictions, no-claim discount (NCD) level, occupation, and marital status.  
* **Vehicle-related**: Make and model (often via an ABI vehicle group in the UK), vehicle age, value, engine size, security features, and modifications.  
* **Usage and Location**: Stated use of the vehicle (e.g., social vs. business), estimated annual mileage, and where the vehicle is kept overnight (e.g., garage, street). The policyholder's postcode is a crucial factor, acting as a proxy for traffic density and theft risk.  
* **Policy-related**: Type of cover (comprehensive vs. third party), and the level of voluntary excess.

##### **🔸 4.2 Household Insurance**

For household property (both buildings and contents), the key risk factors are the scale of the risk and its location, as perils like theft, subsidence, and flooding are highly location-dependent. Key rating factors include:

* **Property Characteristics**: Sum insured (or number of rooms as a proxy), type of property (house, flat), age, and construction type (e.g., brick vs. thatched roof).  
* **Location**: Postcode is a critical factor.  
* **Security and Safety**: Presence of approved locks, burglar alarms, and smoke detectors.  
* **Occupancy**: Whether the property is occupied during the day, as this affects the risk of burglary and the severity of events like fires or burst pipes.  
* **Policyholder**: Age, smoking status, and claims history are also used.

##### **🔸 4.3 Commercial Liability (e.g., Employers' and Public Liability)**

For commercial liability, the primary factor influencing risk is the nature of the insured's business. Specific underwriting factors include:

* Type of industry or occupation.  
* The company's past claims experience.  
* Turnover and payroll (which is also the main exposure measure for Employers' Liability).  
* Specific processes and materials handled.  
* The quality of risk management and safety precautions in place.

##### **🔸 4.4 Professional Indemnity and Directors' & Officers' (D\&O) Liability**

For these specialized lines, each policy is typically underwritten individually. The primary risk factor is the nature of the profession or the company being insured. The insured's past experience is also a key factor.

---

#### **5\. External Data and Advanced Modelling**

In highly competitive markets like UK personal lines, insurers increasingly supplement data gathered from the proposal form with external data to refine their pricing. This data is linked to the policy via keys like the policyholder's identity, location (postcode), or insured asset (vehicle registration number). Examples of external data sources include:

* Credit scores or customer insurance scores.  
* Geodemographic data from census or electoral rolls.  
* Specialist data on perils like flood or subsidence risk.  
* Shared industry claims databases (e.g., CUE in the UK).

These additional data points enable the use of sophisticated multivariate modelling techniques like **Generalised Linear Models (GLMs)**. GLMs are superior to simple one-way analyses because they can simultaneously assess the impact of multiple rating factors and account for correlations between them, thereby avoiding the distortions that can arise from correlated factors. This allows for a more accurate and robust pricing structure.

