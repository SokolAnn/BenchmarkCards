# CHiSafetyBench (Chinese Hierarchical Safety Benchmark)

## 📊 Benchmark Details

**Name**: CHiSafetyBench (Chinese Hierarchical Safety Benchmark)

**Overview**: CHiSafetyBench is a dedicated safety benchmark for evaluating large language models’ capabilities in identifying risky content and refusing to answer risky questions in Chinese contexts. It incorporates a hierarchical Chinese safety taxonomy consisting of 5 risk areas and 31 categories, covering multiple-choice questions and question-answering tasks.

**Data Type**: multiple-choice questions and question-answering

**Domains**:
- Natural Language Processing

**Languages**:
- Chinese

**Resources**:
- [GitHub Repository](https://github.com/UnicomAI/UnicomBenchmark/tree/main/CHiSafetyBench)

## 🎯 Purpose and Intended Users

**Goal**: To provide a comprehensive evaluation of the safety capabilities of Chinese LLMs.

**Target Audience**:
- LLM Developers
- Researchers

**Tasks**:
- Risk Content Identification
- Refusal to Answer

**Limitations**: N/A

## 💾 Data

**Source**: Combination of open resources and manual data writing.

**Size**: 2,130 questions (1,567 multiple-choice and 563 risky questions)

**Format**: N/A

**Annotation**: Manual writing and aligned with predefined safety taxonomy.

## 🔬 Methodology

**Methods**:
- Automatic evaluation
- Human evaluation

**Metrics**:
- Accuracy
- Rejection Rate
- Responsibility Rate
- Harmfulness Rate

**Calculation**: Metrics calculated based on model responses to multiple-choice questions and question-answering tasks.

**Interpretation**: Higher accuracy and rejection rates signify better safety capabilities.

**Validation**: The effectiveness of automatic evaluation was validated against human assessment results.

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
