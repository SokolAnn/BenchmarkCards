# MultiDoc2Dial and FaithDial

## 📊 Benchmark Details

**Name**: MultiDoc2Dial and FaithDial

**Overview**: This work investigates how to improve faithfulness and accuracy in knowledge-grounded dialogue generation tasks by leveraging reinforcement learning with a novel reward function based on accuracy and faithfulness metrics.

**Data Type**: text

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- MultiDoc2Dial
- FaithDial

**Resources**:
- [GitHub Repository](https://github.com/IBM/multidoc2dial/blob/main/scripts/run_data_preprocessing.sh)

## 🎯 Purpose and Intended Users

**Goal**: To improve the faithfulness and accuracy of knowledge-grounded dialogue generation.

**Target Audience**:
- ML Researchers
- Industry Practitioners

**Tasks**:
- Dialogue Generation

**Limitations**: The pretraining of better language models is always helpful for this method.

## 💾 Data

**Source**: Datasets include MultiDoc2Dial and FaithDial.

**Size**: 21,453 training examples for MultiDoc2Dial, 18,357 for FaithDial.

**Format**: N/A

**Annotation**: N/A

## 🔬 Methodology

**Methods**:
- Reinforcement Learning
- Proximal Policy Optimization

**Metrics**:
- SacreBLEU
- ROUGE-L
- BERTScore
- Token-F1

**Calculation**: Metrics are calculated based on how well the generated responses match ground-truth references and relevant knowledge texts.

**Interpretation**: Higher scores in metrics indicate better accuracy and faithfulness of the generated responses.

**Baseline Results**: T5-PPO-Ours achieved the best performance across the evaluated benchmarks.

**Validation**: Models were evaluated using empirical experiments on MultiDoc2Dial and FaithDial.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness

**Atlas Risks**:
- **Accuracy**: Poor model accuracy
- **Fairness**: Data bias

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
