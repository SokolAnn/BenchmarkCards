# M4GT-Bench (Multi-generator, Multi-domain, and Multi-lingual Black-box Machine-Generated Text Detection)

## 📊 Benchmark Details

**Name**: M4GT-Bench (Multi-generator, Multi-domain, and Multi-lingual Black-box Machine-Generated Text Detection)

**Overview**: M4GT-Bench is a benchmark designed for evaluating the detection of machine-generated text (MGT) across diverse languages, domains, and generator models. It includes tasks for binary MGT detection, generator identification, and human-machine text boundary detection.

**Data Type**: text

**Domains**:
- Natural Language Processing

**Languages**:
- English
- Arabic
- Chinese
- German
- Italian
- Russian
- Ukrainian
- Spanish
- Urdu

**Similar Benchmarks**:
- M4 (Multi-generator, Multi-domain, and Multi-lingual Black-box Machine-Generated Text Detection)

**Resources**:
- [GitHub Repository](https://github.com/mbzuai-nlp/M4GT-Bench)

## 🎯 Purpose and Intended Users

**Goal**: Provide a comprehensive benchmark for black-box machine-generated text detection methods, enabling researchers and developers to evaluate and improve the effectiveness of these detection systems.

**Target Audience**:
- ML Researchers
- Industry Practitioners
- Model Developers
- Domain Experts

**Tasks**:
- Binary Human-Written vs. Machine-Generated Text Classification
- Multi-Way Machine-Generated Text’s Generator Detection
- Human-Written to Machine-Generated Text Change Point Detection

**Limitations**: The current benchmark struggles to generalize across unseen domains and generators, indicative of an issue with the current methodology's adaptability.

## 💾 Data

**Source**: Combination of multilingual, multi-domain datasets specifically curated for machine-generated text detection.

**Size**: Over 73,000 examples across 9 languages and multiple generators.

**Format**: JSON

**Annotation**: Annotations were conducted through crowd-sourcing and expert review to ensure quality and reliability.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics
- Model-based evaluation

**Metrics**:
- Accuracy
- Precision
- Recall
- F1 Score

**Calculation**: Metrics are calculated based on the performance of detection models on the benchmark tasks, compared against human-level performance where applicable.

**Interpretation**: Higher scores in metrics indicate better performance of models in distinguishing between human-generated and machine-generated texts.

**Baseline Results**: Models such as RoBERTa and XLM-R serve as baseline classifiers, demonstrating state-of-the-art performance on the benchmark tasks.

**Validation**: The tasks and metrics were validated against standard detection benchmarks and through human assessments to ensure reliability.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Safety
- Privacy
- Robustness
- Fairness
- Accuracy

**Atlas Risks**:
- **Accuracy**: Unrepresentative data
- **Fairness**: Data bias
- **Robustness**: Evasion attack
- **Privacy**: Personal information in data

**Demographic Analysis**: The benchmark includes demographic factors in its evaluation metrics, focusing on representation across different languages and regions.

**Potential Harm**: ['Potential misuse leading to misinformation spread due to false negative rates in detection.']

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: All datasets used are publicly available and sourced from licensed datasets.

**Data Licensing**: Datasets adhere to their respective licenses, ensuring compliance with data usage regulations.

**Consent Procedures**: Data collected through existing, publicly available datasets with no personal identifiable information.

**Compliance With Regulations**: Not Applicable
