Excellent, let's build a detailed, structured note focusing on the specific data quality issue of **Wrong Numbers** (for policies and claims). This is a foundational topic for SP8, as the integrity of the entire pricing dataset relies on the correct linking of policy, premium, and loss information. An error in an identifier can corrupt multiple records and fundamentally undermine actuarial analysis.

### **📗 Data Quality Issues: Wrong Policy and Claim Numbers**

Data is the most significant underpinning of the ratemaking process. The actuary’s responsibility with respect to data quality is a recurring theme and is even formalised in professional standards like "Actuarial Standard of Practice No. 23, Data Quality". Within the spectrum of data quality issues, the use of incorrect policy or claim numbers is a fundamental error that can have severe consequences.

#### **🔹 1\. The Critical Role of Identifiers in Data Systems**

An insurer's internal risk information is typically stored in two separate but linked databases: a **policy database** and a **claim database**.

* **Policy Database**: Contains records for individual policies or their subdivisions, capturing premium, exposure, and risk characteristics. It must store a unique **policy identifier** and, for products insuring multiple risks (eg, different vehicles on one auto policy), unique **risk identifiers**.  
* **Claims Database**: Captures all transactional information about claims, such as payments and reserve changes. To be useful for pricing, it must store the corresponding **policy and risk identifiers** to create a reliable link back to the policy data. It also contains a unique **claim identifier** for all transactions related to a single claim and often a **claimant identifier** for liability cases.

This system of identifiers is the essential mechanism that allows an actuary to accurately match losses with the corresponding premium, exposure, and risk characteristics that generated them.

#### **🔹 2\. Causes and Consequences of Wrong Numbers**

Data errors can arise at any stage of the data lifecycle, but entering an incorrect policy or claim number is a particularly damaging error that happens at the point of data capture.

##### **🔸 2.1 Causes**

The primary cause is data entry or transcription error. When details of a claim or a policy amendment are being entered into the system, an employee might inadvertently type the wrong number. This is a fundamental operational failure.

##### **🔸 2.2 Consequences**

The sources highlight that allocating details to the wrong record corrupts the data for both the correct and the incorrect policy/claim.

* **For the Incorrect Policy:** It will be assigned claims that it did not generate. This will make its loss experience appear worse than it is, potentially leading to incorrect pricing signals for that risk segment.  
* **For the Correct Policy:** It will appear to have generated no claims (when it did), making its loss experience look artificially favourable. This could lead an actuary to believe the rates for that segment are too high when they may be inadequate.

If these errors are systemic, they can severely distort the entire dataset, leading to flawed actuarial analysis. This undermines the reliability of:

* **Overall Rate Level Reviews**: If losses are misallocated, aggregate loss ratios will be incorrect.  
* **Classification Ratemaking**: The relationship between risk characteristics and losses will be obscured, leading to an inequitable and uncompetitive rating structure. This can expose the insurer to **adverse selection**.  
* **Experience Rating**: For commercial lines, experience rating relies on accurately tracking an individual insured's past experience. Wrong numbers make this impossible.

#### **🔹 3\. Prevention and Mitigation Strategies**

Given the severe impact of wrong numbers, establishing a good information system with robust integrity checks is paramount. The sources identify several key prevention strategies:

* **System Integrity Checks**: The information system must have built-in checks to prevent errors at the point of entry.  
* **Use of Check Digits**: A primary defence mechanism is the use of **check digits** in file numbers, such as policy numbers. A check digit is typically the last digit of an identifier, derived from a mathematical formula based on the preceding digits. If a number is entered incorrectly, it is highly likely that the formula will fail, causing the system to reject the transaction rather than process it to the wrong policy. The check digit can be alphabetic to further reduce the probability of a wrong but valid number being entered.  
* **Staff Training and Culture**: Even the best system is ineffective without well-trained staff who understand the importance of accurate data entry. Management must foster a culture that values data quality to minimize human error.  
* **Automatic Linking**: A well-designed system should automatically link databases. For example, when a claim form is processed, the system should refer to the corresponding policy record to verify coverage, reducing the chance of misallocation.

In conclusion, ensuring the accuracy of policy and claim numbers is a fundamental aspect of data quality management. A single incorrect digit can corrupt the experience of multiple policies, leading to flawed pricing conclusions. Robust information systems, particularly those using check digits, combined with diligent staff training, are essential safeguards to maintain the integrity of the data that underpins all actuarial pricing work.

