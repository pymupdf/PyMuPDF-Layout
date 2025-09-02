

# Risk Management

## Basic Approach

As risks in the financial services increase in diversity and complexity, risk management—identifying, measuring, and controlling risk—has never been more important in the management of a financial holding company.

SMFG has encapsulated the basic principles to be employed in risk management in the manual entitled Regulations on Risk Management. In the manual, we have specified the basic policies for risk management: 1) Set forth SMFG's Groupwide basic policies for risk management after specifying the categories of risk to which these policies apply; 2) Provide all necessary guidance to Group companies to enable them to follow the basic risk management policies set forth by SMFG and set up their own appropriate risk management systems; and 3) Monitor the implementation of risk management by all Group companies to ensure that their practices meet the relevant standards.

### (1) Types of Risk to Be Managed

At SMFG, we classify risk into the following categories: (1) credit risk, (2) market risk, (3) liquidity risk and (4) operational risk (including processing risk and system risk). In addition, we provide individually tailored guidance to help Group companies identify categories of risk that need to be addressed. Risk categories are constantly reviewed, and new categories may be added in response to changes in the operating environment. The Corporate Risk Management Department works with the Corporate Planning Department to comprehensively and systematically manage all these categories of risk across the entire Group.

### (2) Fundamental Principles and Basic Policies for Risk Management

SMFG's Groupwide basic policies for risk management stipulate the fundamental principles for risk management that must be followed, and spell out risk management procedures from various perspectives. These include managing risk on a consolidated accounting basis, managing risk using quantification methods, ensuring consistency with business strategies, setting up a system of checks and balances, contingency planning for emergencies and serious situations, and verifying preparedness to handle all conceivable risk situations. In addition, there are specific operational policies for implementing appropriate management of risk by all Group companies.

Under SMFG's Groupwide basic policies for risk management, all Group companies periodically carry out reviews of the basic management policies for each risk category, or whenever deemed necessary, thus ensuring that the policies followed at any time are the most appropriate. The management of SMFG constantly monitors the conduct of risk management at Group companies, providing guidance when necessary.

## Risk Management System

Top management plays an active role in determining SMFG's Groupwide basic policies for risk management. The system works as follows: The basic policies for risk management are determined by the Management Committee before being authorized by the Board. The Management Committee, the designated board members, and the relevant risk management departments perform risk management according to the basic policies.

### ■SMFG's Risk Management System

```mermaid
flowchart TD
    subgraph SMFG_Group ["SMFG"]
        BOD1["Board of Directors"]
        CA1["Corporate Auditors"]
        MC1["Management Committee"]
        EA1["External Audit"]
        DBM1["Designated Board Members"]
        AD1["Audit Dept."]
        
        subgraph CRMD1["Corporate Risk Management Dept."]
            CR1["Credit Risk"]
            MR1["Market Risk"]
            LR1["Liquidity Risk"]
            OR1["Operational Risk"]
        end
        
        subgraph Other_Depts1 ["Other Departments"]
            GAD1["General Affairs Dept."]
            IPD1["IT Planning Dept."]
            PR1["Processing Risk"]
            SR1["System Risk"]
        end
        
        CWRM1["Corporate-wide Risk Management Corporate Planning Dept./ Corporate Risk Management Dept."]
    end
    
    subgraph Subsidiaries ["Group Companies"]
        subgraph SMBC_Group ["SMBC"]
            BOD2["Board of Directors"]
            CA2["Corporate Auditors"]
            MC2["Management Committee"]
            CRMC2["Credit Risk Management Committee"]
            MRMC2["Market Risk Management Committee"]
            EA2["External Audit"]
            DBM2["Designated Board Members"]
            BMCRMU2["Board Member in Charge of Risk Management Unit"]
            IAU2["Internal Audit Unit"]
            
            subgraph RMU2["Risk Management Unit"]
                CIPD2["Credit & Investment Planning Dept."]
                CRMD2["Corporate Risk Management Dept."]
            end
            
            subgraph BWRM2["Bank-wide Risk Management"]
                CR2["Credit Risk"]
                MR2["Market Risk"]
                LR2["Liquidity Risk"]
                OR2["Operational Risk"]
                PR2["Processing Risk"]
                SR2["System Risk"]
                STR2["Settlement Risk"]
            end
            
            subgraph Other_Depts2["Other Departments"]
                CPD2["Corporate Planning Dept./Corporate Risk Management Dept."]
                OPD2["Operations Planning Dept."]
                IPD2["IT Planning Dept."]
                OD2["Other Departments"]
                OTR2["Other Risks"]
            end
        end
        
        SMBC_NS["SMBC Nikko Securities"]
        SMFG_CC["SMFG Card & Credit"]
        SMC["Sumitomo Mitsui Card"]
        CF["Cedyna Financial"]
        SMFL["Sumitomo Mitsui Finance & Leasing"]
        JRI["Japan Research Institute"]
        SMBC_FS["SMBC Friend Securities"]
    end
    
    BOD1 --> MC1
    MC1 --> DBM1
    DBM1 --> AD1
    MC1 --> CRMD1
    CRMD1 --> CWRM1
    
    SMFG_Group -->|"Guidance for drafting of basic policies Monitoring"| Subsidiaries
    CWRM1 -->|"Report"| Subsidiaries
    
    BOD2 --> MC2
    MC2 --> CRMC2
    MC2 --> MRMC2
    MC2 --> DBM2
    DBM2 --> BMCRMU2
    BMCRMU2 --> RMU2
    RMU2 --> BWRM2
    BWRM2 --> Other_Depts2
```

32 SMFG 2011
