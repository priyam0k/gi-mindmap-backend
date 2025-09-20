As your Specialist Actuarial Note Builder and Exam Coach, let's construct a comprehensive set of notes on **Technical Reserves** (also called Technical Provisions), placing this core concept within the broader context of the **Balance Sheet**. Understanding this component is absolutely fundamental for both SP7 and SP8 students, as it is the largest liability on an insurer's balance sheet and directly connects reserving, pricing, and capital management.

### **The Balance Sheet Context**

First, let's situate Technical Reserves on a general insurer's balance sheet. The balance sheet provides a snapshot of an insurer's financial position, summarising what it owns (**Assets**) and what it owes (**Liabilities**). Technical Reserves form the principal liability.

A simplified structure is as follows:

| LIABILITIES | ASSETS |
| ----- | ----- |
| **Technical Reserves** | Investments |
| Provision for other risks & Creditor items | Fixed Assets |
| **Free Reserves** (Balancing Item) | Net Current Assets |

Here, Technical Reserves represent the amounts set aside to meet expected claim payments and related expenses for policies already written. They are distinct from Free Reserves (capital), which act as a buffer for *unexpected* adverse outcomes.

### **Defining Technical Reserves**

The sources describe Technical Reserves as the liabilities relating to policies that the insurer has already written. They can be broken down into two main categories based on when the claim-causing event occurs:

1. **Reserves for Past Events (Claims Provision)**: These are provisions for accidents or losses from events that occurred *before* the balance sheet date. This is the largest and most uncertain liability for a general insurer.  
2. **Reserves for Future Events (Premium Provision)**: These cover liabilities for future insurance cover on policies for which premiums have already been received. In essence, they relate to the unexpired portion of existing policies.

Different accounting and regulatory regimes define the structure of Technical Reserves in different ways.

### **Components of Technical Reserves**

#### **1\. Claims Provision (Reserves for Past Events)**

This covers liabilities for claim events that have already occurred, whether the insurer knows about them or not. The key challenge here is dealing with the delays between an event occurring and the claim being fully settled. This provision is typically broken down into several components:

* **Reserve for Outstanding Reported Claims**: An estimate to settle claims that have been reported to the insurer but are not yet paid as of the accounting date. These are typically estimated on a case-by-case basis.  
* **Reserve for Incurred But Not Reported (IBNR) Claims**: A provision for claims that have occurred but have not yet been reported to the company. Individual case estimates cannot be used for IBNR as the insurer is unaware of the specific claims.  
* **Reserve for Incurred But Not Enough Reported (IBNER)**: A provision to cover expected future development (increases or decreases) on claims that have already been reported.  
* **Reserve for Re-opened Claims**: An additional reserve for claims that were considered settled but may require further payments in the future.  
* **Reserve for Claims Handling Expenses (CHE)**: A provision for the future costs of settling all of the above claims, such as legal fees.

#### **2\. Premium Provision (Reserves for Future Events)**

This provision covers liabilities for future claim events on the unexpired portion of policies already written. There are two main ways to assess this:

* **Unearned Premium Reserve (UPR)**: This is a *retrospective* assessment. It represents the portion of premiums received that corresponds to the unexpired period of cover. It can be calculated gross of acquisition costs, or net of Deferred Acquisition Costs (DAC).  
* **Unexpired Risk Reserve (URR) / Additional Unexpired Risk Reserve (AURR)**: This is a *prospective* assessment of the amount needed to cover future claims and expenses from unexpired policies. If the URR is greater than the UPR (net of DAC), it implies an expected loss on the unexpired business, and an AURR must be established to cover this shortfall. **AURR \= URR \- UPR (minimum of zero)**.

### **The Solvency II Approach to Technical Provisions**

The Solvency II regime, which applies to all insurers in the European Economic Area (EEA), takes a market-consistent, prospective approach to valuing Technical Provisions (TPs).

**TPs \= Best Estimate \+ Risk Margin**.

* **Best Estimate (BE)**: This is the probability-weighted average of all future cashflows (premiums, claims, expenses, reinsurance), discounted to allow for the time value of money using a prescribed risk-free interest rate term structure. It is calculated without prudent margins. The BE covers both the claims provision and the premium provision elements described previously.  
* **Risk Margin (RM)**: This is an additional amount calculated to ensure the total TP value is equivalent to what another insurer would require to take over the obligations. It is calculated by determining the cost of holding the Solvency Capital Requirement (SCR) needed to support the liabilities over their lifetime, using a prescribed cost-of-capital rate (currently 6%).

### **Key Considerations for Technical Reserves**

* **Gross vs. Net**: Technical provisions can be calculated gross of reinsurance recoveries or net of them. Under Solvency II, reinsurance recoverables are shown as an asset on the balance sheet, adjusted for the probability of reinsurer default, rather than being deducted directly from the gross liabilities.  
* **Data Quality**: High-quality data is crucial for the reliable calculation of technical provisions. Inadequate data leads to greater uncertainty and potentially inaccurate reserving.  
* **Discounting**: Whether and how to discount future claim payments for investment income is a key consideration that varies by regulatory regime. Solvency II mandates discounting using specified risk-free rates.  
* **Uncertainty**: A primary challenge for actuaries is the great uncertainty surrounding the ultimate cost of claims, especially for long-tail classes of business. This uncertainty is what necessitates the holding of Free Reserves (capital) in addition to the Technical Reserves.

