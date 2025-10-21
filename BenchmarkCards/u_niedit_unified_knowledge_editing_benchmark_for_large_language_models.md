# U NIEDIT (Unified Knowledge Editing Benchmark for Large Language Models)

## 📊 Benchmark Details

**Name**: U NIEDIT (Unified Knowledge Editing Benchmark for Large Language Models)

**Overview**: U NIEDIT is a unified benchmark for knowledge editing in large language models (LLMs), providing comprehensive coverage of knowledge domains and diverse editing evaluation by integrating various criteria.

**Data Type**: editing samples, generality samples, locality samples

**Domains**:
- Natural Sciences
- Humanities
- Social Sciences
- Applied Sciences
- Interdisciplinary Studies

**Languages**:
- English

**Similar Benchmarks**:
- ZSRE
- CounterFact
- MQuAKE
- RippleEdit

**Resources**:
- [GitHub Repository](https://github.com/qizhou000/UniEdit)
- [Resource](https://huggingface.co/datasets/qizhou/UniEdit)

## 🎯 Purpose and Intended Users

**Goal**: To evaluate and enhance the editing capabilities and generalization robustness of LLM editors in open-domain knowledge.

**Target Audience**:
- ML Researchers
- Industry Practitioners
- Model Developers

**Tasks**:
- Knowledge Editing

**Limitations**: N/A

## 💾 Data

**Source**: Wikidata, the largest open-source knowledge graph.

**Size**: 311,142 instances

**Format**: N/A

**Annotation**: Automatically generated from knowledge graphs.

## 🔬 Methodology

**Methods**:
- Automated metrics
- Human evaluation

**Metrics**:
- Reliability
- Generality
- Locality

**Calculation**: Performance scores are calculated based on the ability of the edited LLM to correctly recall the edited knowledge in different contexts.

**Interpretation**: Higher scores indicate better reliability, generality, and locality in LLM performance after editing.

**Validation**: Comprehensive experiments testing various LLMs' performance on the benchmark.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Accuracy
- Robustness

**Atlas Risks**:
No specific atlas risks defined

**Demographic Analysis**: N/A

**Potential Harm**: Exploration of issues relevant to open-domain knowledge editing and potential for misuse in sensitive applications.

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
