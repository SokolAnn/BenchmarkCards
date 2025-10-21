# DICE-B ENCH (Dialogue-based Interactive Calling Evaluation Benchmark)

## 📊 Benchmark Details

**Name**: DICE-B ENCH (Dialogue-based Interactive Calling Evaluation Benchmark)

**Overview**: DICE-B ENCH is a framework designed to evaluate function-calling performance in realistic multi-party, multi-round dialogues, addressing the complexity of real-world scenarios.

**Data Type**: dialogue instances

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Resources**:
- [GitHub Repository](https://github.com/snuhcc/DICE-Bench)
- [Resource](https://huggingface.co/datasets/OfficerChul/DICE-BENCH)

## 🎯 Purpose and Intended Users

**Goal**: To provide a benchmark for evaluating tool-calling capabilities in large language models within complex multi-party dialogue contexts.

**Target Audience**:
- ML Researchers
- Model Developers
- Industry Practitioners

**Tasks**:
- Function Calling

**Limitations**: The benchmark has limited coverage of specialized domains and advanced tools, restricting its applicability in professional contexts.

## 💾 Data

**Source**: Synthetically generated from dialogues reflecting real-world conversation scenarios.

**Size**: 1,607 instances

**Format**: N/A

**Annotation**: Human validation and automated filtering based on established criteria.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Exact Match (EM) Score

**Calculation**: Mean accuracy across function-calling tasks based on the dataset's dialogue structure.

**Interpretation**: Higher EM scores indicate better performance in accurately identifying function names and parameters from the dialogue.

**Baseline Results**: Evaluated performance of 19 LLMs, with varied results across different models.

**Validation**: Three-stage filtering process to ensure realism, coherence, and functional correctness of dialogues.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness

**Atlas Risks**:
No specific atlas risks defined

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
