# WikiTableEdit

## 📊 Benchmark Details

**Name**: WikiTableEdit

**Overview**: WikiTableEdit is a benchmark for both regular and irregular table editing by natural language instruction, encompassing six different types of editing operations and includes 194,996 training data instances and 28,706 testing data instances.

**Data Type**: table editing instructions

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Resources**:
- [Resource](https://anonymous.4open.science/r/WikiTableEdit-ECEC)

## 🎯 Purpose and Intended Users

**Goal**: To introduce the task of table editing and construct a high-quality dataset to support this endeavor.

**Target Audience**:
- ML Researchers
- Industry Practitioners
- Model Developers

**Tasks**:
- Table Editing

**Limitations**: The dataset is a programmatically generated dataset with a relatively uniform instruction format, where each editing operation has only one form of instruction.

## 💾 Data

**Source**: WikiSQL dataset with 26,531 tables used to generate the WikiTableEdit dataset.

**Size**: 194,996 training instances, 28,706 testing instances

**Format**: HTML

**Annotation**: Automatically generated natural language instructions for table editing operations.

## 🔬 Methodology

**Methods**:
- Automated metrics
- Human evaluation

**Metrics**:
- Exact Match (EM)
- SARI
- BLEU
- ROUGE
- Table Edit Distance (TED)

**Calculation**: Table Edit Distance (TED) combines both the minimum edit distance of table structures and content.

**Interpretation**: Higher scores indicate better model performance in editing tables correctly.

**Validation**: Manually sampled results were verified for correctness.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy

**Atlas Risks**:
No specific atlas risks defined

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
