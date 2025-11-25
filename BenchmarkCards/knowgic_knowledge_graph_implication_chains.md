# KnowGIC (Knowledge Graph Implication Chains)

## 📊 Benchmark Details

**Name**: KnowGIC (Knowledge Graph Implication Chains)

**Overview**: KnowGIC is a benchmark dataset developed to evaluate model-editing techniques under the deep editing setting. It consists of multi-step reasoning paths designed to assess the extent to which original facts remain deducible after editing, while testing the indirect knowledge leakage and ripple effects caused by the edits.

**Data Type**: multi-step reasoning paths

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- MQuAKE

**Resources**:
- [Resource](https://anonymous.4open.science/r/KnowGIC)

## 🎯 Purpose and Intended Users

**Goal**: The primary objective of the KnowGIC benchmark is to provide a systematic evaluation of model-editing techniques in LLMs, focusing on understanding how edits affect knowledge retention and inferential understanding post-edit.

**Target Audience**:
- ML Researchers
- Model Developers
- Industry Practitioners

**Tasks**:
- Knowledge Recovery Evaluation

**Limitations**: N/A

## 💾 Data

**Source**: Constructed using ThinkEval framework from samples in the MQuAKE dataset and additional complex relational connections.

**Size**: 1,406 samples

**Format**: N/A

**Annotation**: Manually reviewed and pruned by human experts to remove inaccuracies and irrelevant triplets.

## 🔬 Methodology

**Methods**:
- Sequential prompting
- Automated triplet generation
- Human validation

**Metrics**:
- Indirect Fact Recovery (IFR)
- Preservation

**Calculation**: IFR is calculated to measure the deducibility of original facts through reasoning paths after editing, while Preservation assesses retention of related factual knowledge.

**Interpretation**: A high IFR indicates significant original fact deducibility, suggesting incomplete deep editing, whereas a high Preservation score indicates successful retention of broader contextual integrity.

**Baseline Results**: N/A

**Validation**: Data was manually validated and refined through human oversight, focusing on high accuracy and completeness of extracted knowledge.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Bias

**Atlas Risks**:
- **Accuracy**: Unrepresentative data
- **Fairness**: Output bias

**Demographic Analysis**: N/A

**Potential Harm**: The framework emphasizes evaluating indirect knowledge leakage that can affect model reliability and propagate misinformation.

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
