# BLE ND (A Benchmark for LLMs on Everyday Knowledge in Diverse Cultures and Languages)

## 📊 Benchmark Details

**Name**: BLE ND (A Benchmark for LLMs on Everyday Knowledge in Diverse Cultures and Languages)

**Overview**: BLE ND is a hand-crafted benchmark designed to evaluate LLMs’ everyday knowledge across diverse cultures and languages. It comprises 52.6k question-answer pairs from 16 countries/regions in 13 different languages, including low-resource ones.

**Data Type**: question-answer pairs

**Domains**:
- Natural Language Processing

**Languages**:
- English
- Chinese
- Spanish
- Indonesian
- Arabic
- Persian
- Korean
- Azerbaijani
- Hausa
- Amharic
- Assamese
- Sundanese
- Greek

**Similar Benchmarks**:
- CultureAtlas
- CLIcK
- COPAL-ID

**Resources**:
- [GitHub Repository](https://github.com/nlee0212/BLEnD)
- [Resource](https://huggingface.co/datasets/nayeon212/BLEnD)

## 🎯 Purpose and Intended Users

**Goal**: The primary goal of BLE ND is to evaluate the cultural commonsense knowledge of LLMs across different languages and regions.

**Target Audience**:
- ML Researchers
- Model Developers
- Cultural Researchers

**Tasks**:
- Cultural Knowledge Assessment
- Question Answering

**Limitations**: The dataset may not fully represent the cultural knowledge of every individual in the listed countries and regions.

**Out of Scope Uses**:
- Using the benchmark for tasks unrelated to cultural knowledge evaluation.

## 💾 Data

**Source**: Constructed from native speakers providing culturally relevant question-answer pairs across various categories.

**Size**: 52,600 question-answer pairs

**Format**: JSON

**Annotation**: Manual annotation by native speakers from each target country/region.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Model-based evaluation

**Metrics**:
- Accuracy
- F1 Score

**Calculation**: The accuracy is computed based on the percentage of questions to which an LLM's answer matches those provided by human annotators.

**Interpretation**: A higher score indicates better cultural knowledge by the LLMs in regard to everyday life questions within the given cultures.

**Baseline Results**: Various state-of-the-art LLMs were evaluated, including GPT-4 and Claude, with significant performance gaps noted for underrepresented cultures.

**Validation**: The performance of LLMs was validated through extensive human evaluation and automated metrics.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Accuracy
- Fairness

**Atlas Risks**:
- **Fairness**: Data bias
- **Accuracy**: Unrepresentative data

**Demographic Analysis**: The benchmark covers multiple demographic factors to understand cultural knowledge across various groups.

**Potential Harm**: The benchmark aims to address inaccuracies and biases in cultural representation by LLMs.

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: CC BY-SA 4.0

**Consent Procedures**: Informed consent was obtained from all annotators participating in the study.

**Compliance With Regulations**: Not Applicable
