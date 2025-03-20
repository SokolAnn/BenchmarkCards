# EUREQA

## 📊 Benchmark Details

**Name**: EUREQA

**Overview**: EUREQA is an entity-searching task where a model finds a missing entity based on described multi-hop relations with other entities. The benchmark probes LLMs' dependency on semantic associations and their ability to follow correct reasoning paths.

**Data Type**: Question Answering

**Domains**:
- Reasoning
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- MATH
- FLAN
- HellaSwag

**Resources**:
- [GitHub Repository](https://github.com/VincentLeebang/eureqa)

## 🎯 Purpose and Intended Users

**Goal**: To evaluate the reasoning capabilities of LLMs and their reliance on semantic shortcuts.

**Target Audience**:
- Researchers
- AI Developers
- Data Scientists

**Tasks**:
- Evaluate reasoning paths
- Assess accuracy in entity identification

**Limitations**: The benchmark may not cover all reasoning mechanisms utilized by LLMs.

**Out of Scope Uses**:
- Non-reasoning tasks
- General question-answering beyond the specified framework

## 💾 Data

**Source**: DBpedia knowledge base

**Size**: 2991 questions

**Format**: JSON

**Annotation**: Questions are generated with a focus on multi-hop reasoning and semantic associations.

## 🔬 Methodology

**Methods**:
- Direct prompting
- In-context learning prompting

**Metrics**:
- Accuracy
- Semantic similarity correlation

**Calculation**: Accuracy is determined based on string-matching with gold references.

**Interpretation**: A model's performance is assessed by its ability to correctly identify entities based on their relational context.

**Baseline Results**: GPT-4 achieved 62% accuracy in identifying entities on EUREQA.

**Validation**: Results are validated through a majority vote from multiple runs, ensuring higher accuracy reliability.

## ⚠️ Targeted Risks

**Risk Categories**:
- Fairness
- Transparency
- Accuracy
- Robustness

**Atlas Risks**:
No specific atlas risks defined

**Demographic Analysis**: N/A

**Potential Harm**: Potential for biased outputs based on training data disparities.

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Care is taken to avoid personal data usage in examples and testing.

**Data Licensing**: Data used is adhered to licensing from DBpedia.

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Efforts are made to ensure alignment with data regulation standards.
