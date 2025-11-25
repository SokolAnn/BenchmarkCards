# P-MME VAL (Parallel Multilingual Multitask Benchmark for Consistent Evaluation of LLMs)

## 📊 Benchmark Details

**Name**: P-MME VAL (Parallel Multilingual Multitask Benchmark for Consistent Evaluation of LLMs)

**Overview**: P-MME VAL is a comprehensive multilingual multitask benchmark that incorporates both fundamental and capability-specialized tasks, ensuring consistent language coverage and providing parallel samples across different languages.

**Data Type**: multimodal

**Domains**:
- Natural Language Processing

**Languages**:
- English
- Chinese
- Arabic
- Spanish
- Japanese
- Korean
- Thai
- French
- Portuguese
- Vietnamese

**Similar Benchmarks**:
- XTREME
- XGLUE
- MEGA
- BUFFET

**Resources**:
- [Resource](https://huggingface.co/datasets/Qwen/P-MMEval)

## 🎯 Purpose and Intended Users

**Goal**: To develop a comprehensive evaluation system that unifies diverse NLP and capability-specialized tasks, ensuring consistent language coverage per task and offering parallel samples across languages.

**Target Audience**:
- ML Researchers
- Industry Practitioners
- Model Developers

**Tasks**:
- Text Classification
- Question Answering
- Code Generation
- Mathematical Reasoning
- Logical Reasoning
- Knowledge Acquisition
- Instruction Following

**Limitations**: N/A

## 💾 Data

**Source**: Combinations of datasets such as XNLI, MH ELLA SWAG, HUMAN EVAL-XL, MGSM, ML OGIQA, MMMLU, and others.

**Size**: Data spans across multiple datasets with a combined total of approximately 15,000 examples per language across 10 languages.

**Format**: N/A

**Annotation**: Datasets involve both manual annotation and curated translations with expert reviews.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Accuracy
- BLEU Score

**Calculation**: Metrics calculated based on the performance of models on various tasks across multiple languages, with results aggregated to analyze multilingual capabilities.

**Interpretation**: Higher scores indicate stronger multilingual capabilities of models across the evaluated tasks.

**Baseline Results**: N/A

**Validation**: Validation involves performance comparison using different models across the included multilingual tasks.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Fairness
- Privacy
- Robustness
- Accuracy

**Atlas Risks**:
- **Fairness**: Data bias
- **Accuracy**: Unrepresentative data

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Informed consent was obtained from all individual participants included in the study.

**Data Licensing**: Not Applicable

**Consent Procedures**: Informed consent from participants involved in the studies.

**Compliance With Regulations**: All procedures were in accordance with ethical standards of institutional and/or national research committees.
