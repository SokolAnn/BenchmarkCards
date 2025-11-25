# CataractSurg-80K: Knowledge-Driven Benchmarking for Structured Reasoning in Ophthalmic Surgery Planning

## 📊 Benchmark Details

**Name**: CataractSurg-80K: Knowledge-Driven Benchmarking for Structured Reasoning in Ophthalmic Surgery Planning

**Overview**: CataractSurg-80K is the first large-scale benchmark for cataract surgery planning that incorporates structured clinical reasoning. Each case is annotated with diagnostic questions, expert reasoning chains, and structured surgical recommendations to support fine-grained supervision and evaluation.

**Data Type**: structured clinical reasoning data

**Domains**:
- Healthcare

**Languages**:
- English
- Chinese

**Similar Benchmarks**:
- MedQA
- CMB
- CliMedBench

**Resources**:
- [Resource](https://huggingface.co/datasets/my2000cup/CataractSurg-80K)
- [Resource](https://huggingface.co/my2000cup/Qwen-CSP)
- [Resource](https://anonymous.4open.science/r/CataractCareMAS-A363)

## 🎯 Purpose and Intended Users

**Goal**: To provide a comprehensive AI-driven preoperative decision support framework for cataract surgery that integrates structured reasoning.

**Target Audience**:
- ML Researchers
- Medical Practitioners
- AI Developers in Healthcare

**Tasks**:
- Clinical Decision Support
- Reasoning in Cataract Surgery

**Limitations**: N/A

## 💾 Data

**Source**: Curated from ophthalmology electronic medical records at Peking University Third Hospital.

**Size**: 80,000 cases

**Format**: structured format

**Annotation**: Expert-annotated with diagnostic questions, reasoning chains, and structured surgical recommendations.

## 🔬 Methodology

**Methods**:
- Experiment evaluation using multiple LLMs
- Quantitative evaluations on general LLMs and customized fine-tuned models

**Metrics**:
- BLEU Score
- ROUGE-L
- BERTScore
- Keypoint-level F1/Precision/Recall

**Calculation**: Metrics calculated based on output quality comparisons with human-annotated references.

**Interpretation**: Higher scores on metrics indicate better model performance in generating clinical decision support outputs.

**Baseline Results**: Comparison against general-purpose LLMs like GPT-4 and Claude-3.7.

**Validation**: Cross-validation with the benchmark subset of 777 cases.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness
- Privacy
- Robustness

**Atlas Risks**:
- **Accuracy**: Unrepresentative data
- **Fairness**: Data bias
- **Privacy**: Personal information in data

**Demographic Analysis**: Analysis of the dataset shows an average patient age of 69.4 years.

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: All data was de-identified with ethical approval.

**Data Licensing**: Released under CC BY-NC-SA 4.0 license.

**Consent Procedures**: Ethical compliance ensured during patient data processing.

**Compliance With Regulations**: Not Applicable
