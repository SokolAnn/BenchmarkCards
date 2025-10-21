# Com2 (A Causal-Guided Benchmark for Exploring Complex Commonsense Reasoning in Large Language Models)

## 📊 Benchmark Details

**Name**: Com2 (A Causal-Guided Benchmark for Exploring Complex Commonsense Reasoning in Large Language Models)

**Overview**: Com2 focuses on complex commonsense reasoning by utilizing causal event graphs to create structured reasoning tasks that mimic real-world concerns.

**Data Type**: question-answering pairs

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Resources**:
- [Resource](https://arxiv.org/abs/2506.07064)

## 🎯 Purpose and Intended Users

**Goal**: To assess the complex commonsense reasoning abilities of large language models.

**Target Audience**:
- ML Researchers
- Model Developers

**Tasks**:
- Complex Commonsense Reasoning
- Counterfactual Reasoning
- Intervention Reasoning
- Decision Making
- Transition Reasoning

**Limitations**: The dataset synthesis process could benefit from finer-grained guidance of causal event graphs and could be refined with deeper analyses of causal relationships.

## 💾 Data

**Source**: Causal event graphs incorporated with various task types generated through automated synthesis.

**Size**: 2,500 examples for Com2-main; 1,254 examples for Com2-hard

**Format**: JSONL

**Annotation**: Generated with guidance from causal event graphs and human evaluation.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Accuracy

**Calculation**: Metrics calculated based on the correctness of the model's responses to the generated common sense reasoning tasks.

**Interpretation**: Higher scores reflect better performance in commonsense reasoning tasks.

**Validation**: Human evaluators assessed the quality of generated tasks for Com2.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness

**Atlas Risks**:
- **Accuracy**: Unrepresentative data
- **Fairness**: Data bias

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
