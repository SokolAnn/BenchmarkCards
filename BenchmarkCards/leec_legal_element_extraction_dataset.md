# LEEC (Legal Element Extraction Dataset)

## 📊 Benchmark Details

**Name**: LEEC (Legal Element Extraction Dataset)

**Overview**: LEEC is a large-scale criminal element extraction dataset comprising 15,831 judicial documents and 159 labels, constructed to enhance the interpretative and analytical capacities of legal cases for various downstream applications in law.

**Data Type**: text

**Domains**:
- Natural Language Processing
- Legal

**Languages**:
- Chinese

**Resources**:
- [GitHub Repository](https://github.com/THUlawtech/LEEC)

## 🎯 Purpose and Intended Users

**Goal**: To provide a comprehensive dataset for legal element extraction in the context of Chinese criminal law to facilitate various LegalAI applications.

**Target Audience**:
- ML Researchers
- Legal Practitioners
- Academics

**Tasks**:
- Element Extraction
- Document Event Extraction

**Limitations**: The dataset may contain selection bias and should be used cautiously due to the sensitive nature of legal data.

## 💾 Data

**Source**: Annotated from publicly available cases of LEVEN and LeCaRD datasets.

**Size**: 15,831 judicial documents

**Format**: N/A

**Annotation**: Annotated manually by law students and supervised by legal experts using a detailed annotation guideline.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- F1 Score

**Calculation**: Evaluation metrics were calculated by comparing extracted elements with ground truth annotations.

**Interpretation**: Higher F1 scores indicate better performance in accurately extracting legal elements from judicial documents.

**Baseline Results**: Models demonstrated varying performance levels with different baseline methods indicated in the paper.

**Validation**: The dataset was validated using multiple state-of-the-art models for Document Event Extraction.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Privacy
- Safety

**Atlas Risks**:
- **Fairness**: Data bias
- **Privacy**: Reidentification
- **Robustness**: Evasion attack

**Demographic Analysis**: The dataset includes elements that capture demographic factors of defendants and victims.

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: The dataset includes measures to comply with Chinese law regarding personal information.

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: The dataset was created in compliance with applicable laws.
