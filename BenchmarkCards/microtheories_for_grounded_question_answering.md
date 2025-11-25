# Microtheories for Grounded Question Answering

## 📊 Benchmark Details

**Name**: Microtheories for Grounded Question Answering

**Overview**: This paper presents a methodology for distilling a model's topic-relevant knowledge into microtheories that can augment corpora and improve the performance of language models on grounded question answering tasks.

**Data Type**: text

**Domains**:
- Natural Language Processing
- Healthcare
- Education

**Languages**:
- English

**Similar Benchmarks**:
- WorldTree
- ARC
- MedQA

**Resources**:
- [GitHub Repository](https://github.com/nweir127/microtheories/)

## 🎯 Purpose and Intended Users

**Goal**: To provide a method for distilling a language model's overall understanding of a topic into a concise and inspectable microtheory, enhancing trust and accuracy in question answering.

**Target Audience**:
- ML Researchers
- Domain Experts
- Model Developers

**Tasks**:
- Question Answering

**Limitations**: N/A

## 💾 Data

**Source**: Datasets used include the ARC (AI2 Reasoning Challenge) and MedQA for training and evaluation.

**Size**: 854 training examples for ARC, 641 training examples for MedQA

**Format**: N/A

**Annotation**: Model-generated sentences from a language model were used to create microtheories.

## 🔬 Methodology

**Methods**:
- Textual entailment for reasoning
- Human evaluation for relevance
- Automated metrics for performance evaluation

**Metrics**:
- Accuracy
- F1 Score
- Grounding rate

**Calculation**: Metrics are calculated based on the model's ability to ground answers using the distilled microtheories.

**Interpretation**: Higher grounding rates suggest improved model performance in question answering.

**Baseline Results**: Compared against the performance of using Wikipedia and previous benchmarks like WorldTree.

**Validation**: The performance of microtheories was validated through comparisons with existing evaluation datasets.

## ⚠️ Targeted Risks

**Risk Categories**:
- Trust
- Model Understanding
- Performance

**Atlas Risks**:
- **Accuracy**: Poor model accuracy
- **Fairness**: Data bias

**Demographic Analysis**: N/A

**Potential Harm**: ['Misleading information due to incomplete microtheories.']

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
