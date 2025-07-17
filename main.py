from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# 1. Initialize your FastAPI app
app = FastAPI()

# 2. IMPORTANT: Add CORS Middleware
# This allows your website (priyamalok.me) to request data from this API.
# Without this, the browser will block the request for security reasons.
origins = [
    "https://priyamalok.me",
    "http://127.0.0.1:5500", # For local testing
    "http://localhost:5500", # For local testing
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 3. Move your mindmapData from JavaScript into this Python dictionary
mindmap_data = {
    "General Insurance Principles": {
        "Financial Management": {
            "Profit Calculation": {
                "Net Earned Premium Formula": {},
                "Net Incurred Claims Formula": {},
                "Insurance Profit": {},
                "Operating Profit": {},
                "Post-Tax Profit": {},
                "Retained Profit": {}
            },
            "Financial Plan": {
                "Aim: Short-term & Long-term Targets": {},
                "Detail Level": {}
            },
            "Capital Management": {
                "Capital Costs in Premiums": {},
                "Aggregate Capital Requirements": {},
                "Efficient Capital Use": {},
                "Capital Load in Premiums": {},
                "Opportunity Cost": {},
                "Return of Capital for Acquisition/Expansions": {}
            },
            "Balance Sheet Components": {
                "Free Reserves": {},
                "Technical Reserves": {},
                "Investments": {},
                "Fixed Assets": {},
                "Net Current Assets": {},
                "Judgement in Valuation": {},
                "Different Purposes": {}
            },
            "Taxation": {
                "Technical Provisions Deductible": {},
                "Lloyd’s Members Tax Deferral": {},
                "Overseas Profits Taxed": {}
            }
        },
        "Reserving": {
            "Purpose of Reserves": {
                "Published Accounts": {},
                "Supervision of Solvency": {},
                "Internal Management Accounts": {},
                "Purchase/Sale Valuation": {},
                "Adequacy of Previous Estimates": {},
                "Tax Purposes": {},
                "Information for Management": {}
            },
            "Types of Reserves": {
                "Outstanding Reported Claims": {},
                "Incurred But Not Reported (IBNR)": {},
                "Incurred But Not Enough Reported (IBNER)": {},
                "Re-opened Claims": {},
                "Claims Handling Expenses": {},
                "Unearned Premium Reserve (UPR)": {
                    "Definition": {},
                    "Calculation Issues": {},
                    "Net vs Gross UPR": {}
                },
                "Unexpired Risk Reserve (URR)": {
                    "Definition": {},
                    "Additional Unexpired Risk Reserves (AURR)": {}
                },
                "Catastrophe Reserve": {},
                "Claims Equalisation Reserve": {}
            },
            "Reserving Methodologies": {
                "Case Estimates": {},
                "Triangulation Methods": {
                    "Chain Ladder Method": { "Basic": {}, "Inflation Adjusted": {}, "Assumption": {}, "Uses": {} },
                    "Bornhuetter-Ferguson Method": { "Principle": {}, "Advantages": {}, "Disadvantages": {} },
                    "Average Cost per Claim Method (ACPC)": {}
                },
                "Stochastic Models": {
                    "Purpose: Confidence Intervals": {},
                    "Prediction Variance Components": {},
                    "Testing the Model": {},
                    "Mack Model": {},
                    "Bootstrapping": { "Definition": {}, "Over-dispersed Poisson (ODP) Model": {} },
                    "Merz-Wuthrich Model": {},
                    "Copulas for Dependecies": {},
                    "Limitations": {},
                    "Bayesian Credibility": {}
                },
                "Scenario Tests": {},
                "Alternative Sets for Assumptions": {},
                "Non-statistical Methods": {}
            },
            "Data for Reserving": {
                "Quality & Detail Importance": {},
                "Triangulated Data": {},
                "Large Losses": {},
                "Asbestos Claim": {}
            },
            "Reasonableness Checks": {
                "Diagnostic Tests": {},
                "Analysis of Emerging Experience": {},
                "Underwriting Cycle Impact": {},
                "Reserving Cycle": {}
            },
            "Communication of Uncertainty": {
                "Stakeholder Understanding": {},
                "Consistent Vocabulary": {},
                "Quantifying Divergence Likelihood": {}
            }
        },
        "General Insurance Products": {
            "Core Principles": {
                "Risk Aversion": {},
                "Profit Seeking": {},
                "Risk Transfer": {}
            },
            "Types of Cover": {
                "Liability to Third Parties": {},
                "Property Damage": {},
                "Financial Loss": {},
                "Fixed Benefits": {}
            },
            "Key Product Features": {
                "Indemnity Principle": {},
                "Multiple Claims": {},
                "Nil Claims": {},
                "Policy Document Importance": {},
                "Exclusions": { "Common Examples": {}, "Reasons for Use": {} },
                "Basis for Cover": { "Losses-Occurring Basis": {}, "Claims-Made Basis": {} },
                "Selection/Anti-selection": { "Definition": {}, "Dangers": {} },
                "Exposures Measures": { "Definition": {}, "Examples": {} },
                "Claim Characteristics": { "Origin": {}, "Notification": {}, "Settlement & Payment": {}, "Reopened Claims": {}, "Frequency": {}, "Delays (Short vs Long-tail)": {}, "Amount": {} },
                "Rating Factors": {},
                "Risk Factors": {},
                "Rating Factors (Proxies)": {},
                "Underwriting Factors": {}
            },
            "Specific Product Lines": {
                "Liability Insurance": {
                    "Employer’s Liability/ Worker’s Compensation": {},
                    "Motor Third Party Liability": {},
                    "Public Liability": {},
                    "Product Liability": {},
                    "Professional Indemnity": {},
                    "Director’s and Officer’s Liability": {},
                    "Environmental Liability": {},
                    "Employment Practices Liability (EPL)": {}
                },
                "Property Insurance": {
                    "Household Building & Contents": {},
                    "Commercial Property": {},
                    "Motor Property Damage": {},
                    "Marine and Aviation Property": {
                        "Goods in Transit": {},
                        "Construction and Engineering": {},
                        "Extended Warranty": {}
                    }
                },
                "Financial Loss Insurance": {
                    "Credit Insurance": {},
                    "Fidelity Guarantee": {},
                    "Mortgage Indemnity": {},
                    "Business Interruption Cover": {},
                    "Legal Expenses Cover": {},
                    "Suretyship": {}
                },
                "Fixed Benefits Insurance": {
                    "Personal Accident Cover": {}
                }
            },
            "Emerging Risks": {
                "Cyber Risk": {},
                "Nanotechnology": {},
                "Climate Change Transition Risk": {}
            }
        },
        "Reinsurance": {
            "Definition": {},
            "Retrocession": {},
            "Reason for Purchase": {
                "Exposure Limitation/ Risk Spreading": {},
                "Avoidance of Large Single Losses": {},
                "Smoothing of Results": {},
                "Increased Profitability": {},
                "Improves Solvency Margin": {},
                "Increasing Capacity": {},
                "Financial Assistance": {},
                "Expertise Availability": {}
            },
            "Ways of Writing Business": {
                "Facultative Reinsurance": {},
                "Treaty Reinsurance": { "Advantages": {}, "Treaty Terms": {} }
            },
            "Types of Reinsurance Products": {
                "Proportional Reinsurance": {
                    "Quota Share": { "Operation": {}, "Commission": {} },
                    "Surplus": { "Operation": {}, "Estimated Maximum Loss (EML)": {}, "Advantages": {}, "Disadvantages": {} }
                },
                "Non-Proportional Reinsurance": {
                    "Excess of Loss (XL)": { "Operation": {}, "Layers": {}, "Working Layer": {}, "Indexed Limits (Stability Clause)": {}, "Reinstatement": {}, "Rate on Line": {}, "Claims Handling Incentives": {}, "Aggregate XL": {}, "Catastrophe XL": {}, "Pricing Challenges": {} },
                    "Stop Loss": { "Purpose": {}, "Losses Incurred Basis": {}, "Conditions Imposed": {} }
                },
                "Finite Risk (Financial) Reinsurance": {
                    "Purpose": {},
                    "Typical Features": {},
                    "Types (Pre-funded, Time & Distance Deals, Spread Loss, Financial Quota Share)": {},
                    "Risk Transfer Requirement": {}
                }
            },
            "Alternatives to Reinsurance (Capital Markets)": {
                "Committed (Contingent) Capital": { "Mechanism": {}, "Advantages": {} },
                "Securitisation": { "General Principle": {}, "Insurance-Linked Securities (ILS)/ Cat Bonds": {}, "Special Purpose Vehicle (SPV)": {}, "Credit Securitisation": {}, "Motor Securitisation": {}, "Advantages": {} },
                "Weather Derivatives": {}
            }
        },
        "General Business Environment": {
            "Insurance Market Structure": {
                "Direct Insurers (Composite, Pure GI, Specialist)": {},
                "Captive Insurance Companies": {},
                "Lloyd’s of London": {},
                "P&I Clubs": {},
                "Pooling Arrangements": {}
            },
            "Marketing Strategies": {
                "Non-London Market Business": { "Intermediaries (Brokers, Tied Agents)": {}, "Direct Sales (Staff, Internet, Telesales, Off-the-page)": {} },
                "London Market Business (Specialist Brokers, Slip System)": {}
            },
            "Regulation": {
                "Aims of Regulation": {},
                "Regulatory Requirements (Licensing, Reporting, Solvency, Pricing Limits)": {},
                "Solvency II Framework": {},
                "FCA UK Review (Pricing Practices)": {},
                "Disadvantages of Regulation": {},
                "IAIS Insurance Core Principles (ICPs)": {}
            },
            "Economic Factors": {
                "Claim Inflation": { "Price Inflation": {}, "Earnings Inflation": {}, "Medical Cost Inflation": {}, "Court Award Inflation (Ogden Tables)": {}, "Factors Affecting Accuracy": {} },
                "Underwriting Cycle": { "Description (Hard/Soft Markets)": {}, "Causes (Delayed Understanding, Low Entry Barriers, Simplistic Capital Regimes)": {}, "Impact on Loss Ratios & Premiums Volumes": {} },
                "Investment Conditions": { "Asset-Liability Matching": {}, "Significance for GI": {}, "Cashflow Underwriting": {} },
                "Currency Movements": { "Impact on Premiums/Claims": {}, "Currency Hedging": {}, "Lloyd’s Multi-currency Accounting": {} },
                "Economic Conditions Affecting Claims (Recession, Growth)": {},
                "Expense Inflation": {}
            },
            "Legal, Political & Social Factors": {
                "Court Awards": { "Negligence Principle": {}, "Jurisdiction Shopping": {}, "Compensation Determination (Principle of Indemnity, Head of Damage)": {}, "Trends in Awards": {}, "Out-of-court Settlements": {} },
                "Legislation": { "Impact on Claims Experience (Frequency/Severity)": {}, "Retrospective Changes": {}, "Examples (No-win-no fee, Alcohol Limits)": {} },
                "Social Attitudes and Behaviour (Propensity to Claim, Fraud, Drink Driving)": {}
            },
            "Climate & Environmental Factors": {
                "Weather Impact (Seasonal, Local Variation)": {},
                "Global Warming/Climate Change Implications": {},
                "Subsidence and Heave": {},
                "Flood Re (UK)": {}
            },
            "Technical Change": {
                "Increased Computer Power": {},
                "Reduced Data Storage Costs": {},
                "Online Claims Handlings": {},
                "Cyber Risk": {},
                "Data Protection Regulations (GDPR)": {},
                "Telematics": {}
            }
        },
        "Pricing": {
            "Premium Components": {
                "Pure Risk Premium": {},
                "Office Premium (Loadings)": {},
                "Investment Income Allowance": {},
                "Capital Charge/ Profit Loading": {}
            },
            "Rating Methodologies": {
                "Frequency/Severity Approach": { "Description": {}, "Assumption": {}, "Practical Considerations": {}, "Distribution Fitting": {}, "Simulation Use": {} },
                "Burning Cost Approach": { "Description": {}, "Assumption": {}, "Practical Considerations": {} },
                "Original Loss Curves/ Increased Limit Factors (ILFs)": { "Property Business": {}, "Casualty Business (Riebesell Curves)": {} },
                "Generalised Linear Models (GLMs)": { "Applications (Personal Lines, Small Commercial)": {}, "Mathematical Foundations": {}, "Model Specification": {}, "Link Functions": {}, "Error Structures": {}, "Parameter Estimation": {}, "Model Refinement (Interactions, Offsets)": {}, "Diagnostics (Deviance, Residuals, Leverage, Cook’s Distance)": {}, "Aliasing": {}, "Time Consistency Check": {}, "Validation": {} },
                "Credibility Theory": { "Purpose (Sparse Data)": {}, "Full Credibility Standards (Poisson, General Frequency, Severity, Aggregate)": {}, "Partial Credibility (Square Root Rule, Classical, Bayesian)": {}, "Complements of Credibility": {}, "Buhlmann-Straub Model": {} },
                "Experience Rating": {}
            },
            "Data for pricing": {
                "Reliability & Relevance": {},
                "Policy Data": {},
                "Claims Data (Peril, Reference, Loss Date, Amount)": {},
                "Internal Data (Policy, Premium, Claim info)": {},
                "External Data (Industry Schemes, Published Accounts)": {},
                "Data Grouping/Risk Classification": {},
                "Information System Requirements": { "User’s Requirement": {}, "Proposal & Claim form Design": {}, "Staff Training": {}, "Data Storage": {} },
                "Data Quality Issues": { "Errors, Omissions, Distortions": {}, "Wrong Numbers (Claim, Policy)": {}, "Wrong Risk Details": {}, "Wrong Dates (Event, Payment, Reported)": {}, "Claims Inflation": {}, "Changes in Procedures": {}, "Case Estimates (Inconsistent Updates)": {}, "Delays": {} }
            },
            "Large Claims": {},
            "Return Premiums": {},
            "Reopened Claims": {},
            "Actuarial Investigations": {
                "Monitoring Written Business (Growth, Premiums, Claims, Expenses)": {},
                "Analysis of Claims Experience (Trends, Diagnostics)": {},
                "Expense Analysis & Allocation": {},
                "Policyholder Behaviour (Lapse, New Business, Cancellation Rates)": {},
                "Reinsurance Performance": {},
                "Investment Performance": {}
            }
        }
    }
}


# 4. Create your API endpoint
@app.get("/api/mindmap")
def get_mindmap_data():
    """This endpoint returns the entire mind map data structure."""
    return mindmap_data
