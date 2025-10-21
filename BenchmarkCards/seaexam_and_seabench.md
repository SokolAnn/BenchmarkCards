# SeaExam and SeaBench

## 📊 Benchmark Details

**Name**: SeaExam and SeaBench

**Overview**: This study introduces two novel benchmarks, SeaExam and SeaBench, designed to evaluate the capabilities of Large Language Models (LLMs) in Southeast Asian (SEA) application scenarios.

**Data Type**: question-answering pairs

**Domains**:
- Natural Language Processing

**Languages**:
- Indonesian
- Thai
- Vietnamese

**Similar Benchmarks**:
- MMLU (Massive Multitask Language Understanding)
- MT-bench

**Resources**:
- [GitHub Repository](https://github.com/DAMO-NLP-SG/SeaExam)
- [GitHub Repository](https://github.com/DAMO-NLP-SG/SeaBench)

## 🎯 Purpose and Intended Users

**Goal**: The primary objective of the benchmark is to evaluate the multilingual capabilities of LLMs in Southeast Asian contexts using real scenarios.

**Target Audience**:
- ML Researchers
- Industry Practitioners

**Tasks**:
- Question Answering
- Instruction Following

**Limitations**: N/A

## 💾 Data

**Source**: Manually collected exam questions and user queries from Southeast Asian regions.

**Size**: 5,451 examples for SeaExam; 300 examples for SeaBench

**Format**: N/A

**Annotation**: Questions were reviewed and corrected by native linguists.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Accuracy

**Calculation**: Metrics are calculated based on model responses to the benchmark questions.

**Interpretation**: Accuracy is determined based on the percentage of correct answers relative to total questions.

**Baseline Results**: N/A

**Validation**: The benchmarks were tested with various LLMs to assess their effectiveness.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Safety
- Privacy

**Atlas Risks**:
- **Fairness**: Data bias
- **Robustness**: Prompt injection attack
- **Misuse**: Non-disclosure

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
