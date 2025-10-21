# CCI4.0 (A Bilingual Pretraining Dataset for Enhancing Reasoning in Large Language Models)

## 📊 Benchmark Details

**Name**: CCI4.0 (A Bilingual Pretraining Dataset for Enhancing Reasoning in Large Language Models)

**Overview**: CCI4.0 is a large-scale bilingual pre-training dataset designed to enhance reasoning capabilities in large language models through superior data quality and diverse reasoning trajectories.

**Data Type**: text

**Domains**:
- Natural Language Processing

**Languages**:
- Chinese
- English

**Resources**:
- [Resource](https://data.commoncrawl.org/contr/Nemotron/Nemotron-CC/index.html)
- [Resource](https://huggingface.co/datasets/BAAI/CCI2-Data)
- [Resource](https://huggingface.co/datasets/BAAI/CCI-Data)
- [Resource](https://huggingface.co/datasets/BAAI/CCI3.0-Data)
- [Resource](https://huggingface.co/datasets/allenai/dolma/blob/main/urls/v1_6.txt)
- [Resource](https://huggingface.co/datasets/OpenCoder-LLM/opc-fineweb-code-corpus)
- [Resource](https://huggingface.co/datasets/OpenCoder-LLM/opc-fineweb-math-corpus)
- [Resource](https://huggingface.co/datasets/allenai/dolma/blob/main/urls/v1_7.txt)

## 🎯 Purpose and Intended Users

**Goal**: To provide high-quality and diverse corpora for large language model training, specifically focused on enhancing logical and commonsense reasoning capacities.

**Target Audience**:
- ML Researchers
- Model Developers

**Limitations**: Supports only Chinese and English languages; may not be suitable for researchers with limited computational resources.

## 💾 Data

**Source**: Multiple sources including Nemotron-CC and various open-source datasets

**Size**: 35TB

**Format**: N/A

**Annotation**: Human curation, multi-classifier quality scoring, various filtering methods

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Accuracy
- F1 Score

**Calculation**: Empirical evaluations based on performance across various benchmarks.

**Interpretation**: Demonstrates significant performance improvements on reasoning-intensive benchmarks.

**Baseline Results**: Various benchmarks like MMLU and ARC-Challenge used for comparison.

**Validation**: Results validated through empirical evaluations against existing benchmarks.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Safety

**Atlas Risks**:
No specific atlas risks defined

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Applied privacy-preserving techniques and multiple toxicity filtering strategies.

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
