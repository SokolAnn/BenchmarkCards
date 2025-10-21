# IncidentAI dataset

## 📊 Benchmark Details

**Name**: IncidentAI dataset

**Overview**: This paper introduces a new IncidentAI dataset for safety prevention, comprising three tasks: named entity recognition (NER), cause-effect extraction (CE), and information retrieval (IR), annotated by domain experts.

**Data Type**: text

**Domains**:
- Natural Language Processing
- Healthcare

**Languages**:
- Japanese

**Resources**:
- [GitHub Repository](https://github.com/Cinnamon/incident-ai-datasetwork)

## 🎯 Purpose and Intended Users

**Goal**: To provide a high-quality annotated dataset that can assist in the efficient analysis of incident reports using AI models.

**Target Audience**:
- ML Researchers
- Domain Experts

**Tasks**:
- Named Entity Recognition
- Cause-Effect Extraction
- Information Retrieval

**Limitations**: The dataset size is quite small with 970 annotated samples for NER and CE, and 2,159 samples for IR.

## 💾 Data

**Source**: Publicly available reports of high-gas incidents published in 2022 by the High-Pressure Gas Safety Institute of Japan.

**Size**: 970 total annotated samples for NER and CE, 2,159 samples for IR

**Format**: N/A

**Annotation**: Annotated by three Japanese domain experts with at least six years of practical experience in high-pressure gas conservation.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- F1 Score

**Calculation**: Fleiss’ Kappa score was used for inter-annotator agreement assessment.

**Interpretation**: Higher F1 Scores indicate better performance in recognizing entities, causes, and effects.

**Baseline Results**: F1 Scores for NER tasks ranged around 87.53 for best-performing models.

**Validation**: Dataset was validated through expert annotation and cross-checking with high agreement scores.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy

**Atlas Risks**:
- **Accuracy**: Unrepresentative data

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: No confidential or personal information included; the data was obtained from public reports.

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
