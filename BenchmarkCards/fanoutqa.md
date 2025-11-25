# FanOutQA

## 📊 Benchmark Details

**Name**: FanOutQA

**Overview**: FanOutQA is a high-quality dataset of fan-out question-answer pairs and human-annotated decompositions with English Wikipedia as the knowledge base, designed to evaluate complex multi-hop, multi-document reasoning capabilities of large language models.

**Data Type**: question-answering pairs

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- HotpotQA
- LongBench
- Zero-SCROLLS

**Resources**:
- [Resource](https://fanoutqa.com)
- [GitHub Repository](https://github.com/zhudotexe/fanoutqa)

## 🎯 Purpose and Intended Users

**Goal**: To evaluate the performance of large language models on complex multi-hop, multi-document reasoning tasks.

**Target Audience**:
- ML Researchers
- Model Developers
- Industry Practitioners

**Tasks**:
- Question Answering

**Limitations**: N/A

## 💾 Data

**Source**: Crowdsourced from undergraduate and graduate students at a university, utilizing English Wikipedia as the knowledge base.

**Size**: 1,034 questions, 7,305 sub-questions

**Format**: N/A

**Annotation**: Human-written questions and decompositions

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Loose Accuracy
- Strict Accuracy
- ROUGE-1
- ROUGE-2
- ROUGE-L
- BLEURT

**Calculation**: Metrics are calculated based on the normalized reference answer strings and models' generated responses.

**Interpretation**: Higher accuracy indicates better performance in answering fan-out questions.

**Baseline Results**: Human performance achieved a loose accuracy of 68.5%.

**Validation**: Performance validations were conducted through benchmarking seven large language models against the dataset.

## ⚠️ Targeted Risks

**Risk Categories**:
- Fairness
- Accuracy

**Atlas Risks**:
- **Accuracy**: Poor model accuracy, Unrepresentative data
- **Fairness**: Data bias

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: No personal identifying information was collected from human participants.

**Data Licensing**: The dataset is released under the Creative Commons Attribution-ShareAlike 4.0 International License (CC BY-SA).

**Consent Procedures**: Participants gave informed consent before accepting the tasks.

**Compliance With Regulations**: Data collected from human annotators is IRB exempt under 45 CFR 46.104, category 2.
