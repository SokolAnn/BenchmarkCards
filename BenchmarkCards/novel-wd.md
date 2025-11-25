# NOVEL-WD

## 📊 Benchmark Details

**Name**: NOVEL-WD

**Overview**: NOVEL-WD is a dataset containing sentences with novel facts extracted from recent Wikidata updates, designed for evaluating the capability of Large Language Models (LLMs) in learning and recalling new world knowledge through prefix-tuning.

**Data Type**: text

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- SciQ
- MMLU

**Resources**:
- [Resource](N/A)

## 🎯 Purpose and Intended Users

**Goal**: To explore how pre-trained language models can learn new factual knowledge efficiently, using a dataset derived from Wikidata updates.

**Target Audience**:
- ML Researchers
- Model Developers

**Tasks**:
- Causal Language Modeling
- Question Answering

**Limitations**: N/A

## 💾 Data

**Source**: Wikidata

**Size**: 338 distinct triples

**Format**: N/A

**Annotation**: Manually edited where necessary after generation from prompts.

## 🔬 Methodology

**Methods**:
- Prefix-tuning
- Causal Language Modeling
- Multiple Choice Question Answering

**Metrics**:
- Perplexity
- Accuracy

**Calculation**: Perplexity measured against the training set; accuracy calculated on multiple choice tasks.

**Interpretation**: Higher accuracy and lower perplexity indicate better performance in learning and recalling factual information.

**Baseline Results**: The baseline model shows 3.0% to 6.3% accuracy, while prefix-tuned models reach a peak accuracy of 29.1% for k=3.

**Validation**: N/A

## ⚠️ Targeted Risks

**Risk Categories**:
- Safety
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
