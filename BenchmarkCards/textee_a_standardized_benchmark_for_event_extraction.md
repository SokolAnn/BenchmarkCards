# TEXTEE (A Standardized Benchmark for Event Extraction)

## 📊 Benchmark Details

**Name**: TEXTEE (A Standardized Benchmark for Event Extraction)

**Overview**: TEXTEE is a standardized, fair, and reproducible benchmark for event extraction, comprising standardized data preprocessing scripts and splits for 16 datasets spanning eight diverse domains. It includes 14 methodologies for comprehensive reevaluation and evaluation of events.

**Data Type**: text

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Resources**:
- [GitHub Repository](https://github.com/ej0cl6/TextEE)

## 🎯 Purpose and Intended Users

**Goal**: To standardize and improve the evaluation of event extraction methodologies and facilitate further research in this area.

**Target Audience**:
- ML Researchers
- Domain Experts

**Tasks**:
- Event Extraction

**Limitations**: Limited to the annotated datasets and methodologies discussed in the paper, may overlook certain datasets and models.

## 💾 Data

**Source**: Variety of standard datasets for event extraction including ACE05, RichERE, MLEE, Genia2001, Genia2013, M2E2, CASIE, PHEE, MA VEN, FewEvent, SPEED, RAMS, WikiEvents, MUC-4, and GENEV A.

**Size**: Various sizes depending on the dataset, e.g., 10,000 instances, 1,000 documents.

**Format**: Standardized formats depending on the respective datasets.

**Annotation**: Annotation details vary; rely on previously established datasets for event extraction.

## 🔬 Methodology

**Methods**:
- Standardized evaluation setups
- Data preprocessing scripts
- Event extraction model implementations

**Metrics**:
- Trigger F1 Score
- Argument F1 Score
- AI Score (Argument Identification)
- AC Score (Argument Classification)

**Calculation**: Calculated based on varying methodologies and event extraction models as indicated in the paper.

**Interpretation**: Guided by aggregated results across multiple datasets indicating model usability and performance standards.

**Validation**: Validation achieved through comprehensive reevaluation of multiple datasets and models.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Fairness
- Accuracy

**Atlas Risks**:
- **Fairness**: Data bias
- **Accuracy**: Poor model accuracy

**Demographic Analysis**: 1. Performance may vary across different demographics due to data bias in the event extraction datasets. 2. No specific demographic analysis performed. 

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
