# FineDialFact

## 📊 Benchmark Details

**Name**: FineDialFact

**Overview**: FineDialFact is a benchmark for fine-grained dialogue fact verification, which involves verifying atomic facts extracted from dialogue responses.

**Data Type**: text

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- DiaHalu
- DialFact

**Resources**:
- [GitHub Repository](https://github.com/XiangyanChen/FineDialFact)

## 🎯 Purpose and Intended Users

**Goal**: To provide a benchmark for fine-grained dialogue fact verification in dialogue systems.

**Target Audience**:
- ML Researchers
- Industry Practitioners
- Model Developers

**Tasks**:
- Fine-Grained Dialogue Fact Verification

**Limitations**: N/A

## 💾 Data

**Source**: Constructed from public dialogue datasets OpenDialKG and HybriDialogue.

**Size**: 1,000 samples

**Format**: N/A

**Annotation**: Manual annotation by multiple annotators.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Accuracy
- Precision
- Recall
- F1 Score
- Cohen's Kappa

**Calculation**: Metrics are calculated based on classifier performance on the annotated dataset.

**Interpretation**: Higher scores indicate better performance in verifying facts within dialogues.

**Baseline Results**: Highest F1-score achieved is 0.75 on the HybriDialogue dataset.

**Validation**: Inter-annotator agreement measured by Cohen's Kappa with results showing substantial agreement.

## ⚠️ Targeted Risks

**Risk Categories**:
- Fairness
- Accuracy

**Atlas Risks**:
No specific atlas risks defined

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: The OpenDialKG dataset is under CC BY-NC 4.0 and HybriDialogue under the MIT license.

**Consent Procedures**: Participants provided consent for the use of annotated data in research.

**Compliance With Regulations**: Not Applicable
