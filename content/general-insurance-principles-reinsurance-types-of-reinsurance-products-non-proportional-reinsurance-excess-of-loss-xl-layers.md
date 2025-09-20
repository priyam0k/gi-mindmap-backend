As your Specialist Actuarial Note Builder and Exam Coach for SP8, let's construct a detailed note on the concept of **Layers** as it applies to **Excess of Loss (XL) Reinsurance**. Understanding how XL programmes are structured into layers is a fundamental concept in pricing reinsurance (SP8), as well as in reserving and capital modelling (SP7), as it defines the precise scope of risk transfer between the cedant and reinsurer \[SP8.pdf, SP7.pdf, 11, 12\].

### **Types of Reinsurance Products**

#### **🔹 Non-Proportional Reinsurance (Excess of Loss \- XL)**

##### **🔸 Operation: The Layer of Cover**

The core mechanism of Excess of Loss (XL) reinsurance is the creation of a **layer of cover** \[SP7.pdf\]. Unlike proportional reinsurance which shares risk from the first pound, the reinsurer's liability under an XL contract is triggered only when the cedant's loss exceeds a pre-agreed monetary amount \[SP7.pdf, SP8.pdf, Reinsurance.pdf\]. The layer defines the specific slice of a loss for which the reinsurer is responsible \[SP7.pdf\].

---

###### **1\. Defining a Layer**

A layer of cover is defined by two key monetary values:

* **Retention / Excess Point / Attachment Point**: This is the pre-agreed amount that the ceding insurer (cedant) must bear in full from a qualifying loss before the reinsurer becomes liable. It represents the reinsurer's lower limit of liability \[Reinsurance.pdf, SP7.pdf, SP8.pdf\]. This amount is sometimes also referred to as the "priority" \[Reinsurance.pdf\].  
* **Upper Limit**: This is the maximum amount the reinsurer will pay for any single qualifying loss. The reinsurer's liability is capped at this upper limit minus the retention \[Reinsurance.pdf, SP7.pdf, 323\].

A contract is typically described as providing cover of "Amount of layer *excess of* lower limit" \[323, SP7.pdf, SP8.pdf\].

* **Example**: A treaty described as "**£4.5m excess of £0.5m**" (or £4.5m xs £0.5m) creates a layer of cover for losses between £0.5m and £5m. It operates as follows \[323, SP7.pdf\]:  
  * **Cedant's Retention**: The cedant pays the first £0.5m of any qualifying loss.  
  * **Reinsurer's Layer**: The reinsurer pays the amount of the loss above £0.5m, up to a maximum recovery of £4.5m.  
  * **Cedant's Upper Retention**: The cedant remains liable for any portion of the loss that exceeds the sum of the retention and the layer, i.e., any amount over £5m (£0.5m \+ £4.5m) \[323, SP7.pdf\].

---

###### **2\. Stacking Layers in a Reinsurance Programme**

An insurer will typically purchase multiple layers of XL cover from different reinsurers, which are "stacked" on top of each other to create a comprehensive reinsurance programme \[Reinsurance.pdf\].

* **Structure**: The layers should be arranged so that there are no gaps in cover. This means the lower limit (attachment point) of a higher layer of reinsurance should be set at the upper limit of the layer immediately below it \[Reinsurance.pdf\].

* **Purpose**: This layered structure allows an insurer to cede different parts of its risk profile to different reinsurers, who may have varying appetites for risk at different levels \[SP8.pdf\]. It also allows an insurer to build up a large amount of total cover that might not be available from a single reinsurer \[SP8.pdf\].

* **Example of a Stacked Programme**: An insurer with the following programme has cover up to £700,000 for a single loss, but it is split between three reinsurers \[Reinsurance.pdf\]:

  * Layer 1: £140,000 excess of £60,000  
  * Layer 2: £300,000 excess of £200,000  
  * Layer 3: £200,000 excess of £500,000 *Note: The example in the source material \[Reinsurance.pdf\] incorrectly cites Layer 3 as £2m excess of £700,000, which would create a gap. The figures above are adjusted for consistency to illustrate the principle of stacked layers without gaps.*

---

###### **3\. Types of Layers**

The terminology for layers can vary depending on their position in the reinsurance tower and the frequency with which they are expected to be hit by claims:

* **Working Layers**: These are the lower layers of cover, sitting just above the cedant’s retention, where moderate to heavy loss activity is expected \[SP8.pdf, Reinsurance.pdf\]. Because these layers are expected to be used relatively frequently, they often include adjustable features, such as premiums that increase with adverse claims experience, or unlimited free reinstatements \[SP8.pdf, Reinsurance.pdf\].  
* **Higher Layers**: As layers move up the reinsurance tower, they are exposed to less frequent but more severe losses. These higher layers will typically have limited, paid reinstatements \[SP8.pdf, Reinsurance.pdf\].

---

###### **4\. Pricing Considerations for Layers**

The pricing of a layer depends critically on its characteristics.

* **Data Sparsity**: For higher layers, there will be limited or no historical claims experience, making it difficult to price using traditional methods. The pricing for these layers is often driven by minimum rate requirements, expenses, and the cost of the capital required to support such volatile business, rather than by the expected loss cost which may be close to zero \[SP8.pdf\].  
* **Original Loss Curves / ILFs**: When data is sparse, pricing actuaries use tools like Original Loss Curves or Increased Limit Factors (ILFs) to estimate the proportion of total ground-up losses that will fall into a specific layer \[SP8.pdf, 323\]. This allows the reinsurer to infer a price for a high, data-poor layer based on the more credible experience of a lower layer or the underlying primary business \[SP8.pdf, 323\].

*Exam Coach Tip: In your SP8 exam, questions about XL reinsurance will almost always involve the concept of layers. You must be able to describe how a layer is defined by its **retention (attachment point)** and its **limit**. Be prepared to calculate the recovery for a given loss amount through a stacked programme of multiple layers, identifying any gaps in cover. For higher-order marks, you should be able to discuss the different characteristics of a **"working layer"** versus a **"higher layer"**, linking this to features like reinstatement terms and the challenges of pricing data-sparse layers using tools like ILFs.*

