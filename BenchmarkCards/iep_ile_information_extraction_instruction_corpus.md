# IEP ILE (Information Extraction Instruction Corpus)

## 📊 Benchmark Details

**Name**: IEP ILE (Information Extraction Instruction Corpus)

**Overview**: IEP ILE is a comprehensive bilingual (English and Chinese) information extraction instruction corpus, constructed through the collection and cleaning of 33 existing datasets, containing approximately 0.32B tokens. It aims to improve the performance of large language models in information extraction tasks.

**Data Type**: instruction-output pairs

**Domains**:
- Natural Language Processing

**Languages**:
- English
- Chinese

**Resources**:
- [GitHub Repository](https://github.com/zjunlp/IEPile)

## 🎯 Purpose and Intended Users

**Goal**: To provide a large-scale, high-quality instruction dataset to enhance the adaptability and performance of large language models in information extraction tasks.

**Target Audience**:
- ML Researchers
- Model Developers
- Domain Experts

**Tasks**:
- Named Entity Recognition
- Relation Extraction
- Event Extraction

**Limitations**: N/A

## 💾 Data

**Source**: The corpus was created by collecting and cleaning 33 existing datasets focused on information extraction tasks.

**Size**: 0.32B tokens

**Format**: JSON

**Annotation**: Data was cleaned and standardized from various existing information extraction datasets.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Micro-F1

**Calculation**: Micro-F1 score is computed based on the extraction accuracy of identified entities and relationships in the output.

**Interpretation**: Higher Micro-F1 scores indicate better performance in extraction tasks, with improvements noted in zero-shot scenarios.

**Baseline Results**: The performance of models fine-tuned on the IEP ILE dataset demonstrated significant improvements over baseline models.

**Validation**: Models were validated against a range of unseen datasets to assess zero-shot generalization abilities.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Safety
- Accuracy

**Atlas Risks**:
- **Fairness**: Data bias
- **Accuracy**: Unrepresentative data

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: All data collected are sourced from publicly available materials, ensuring no personal data is used.

**Data Licensing**: IEP ILE adheres to the CC BY-NC-SA 4.0 license except for ACE2005, which adheres to the LDC User Agreement.

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: The study complies with legal standards concerning data usage and privacy.
