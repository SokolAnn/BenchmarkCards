# LONG SAFETY

## 📊 Benchmark Details

**Name**: LONG SAFETY

**Overview**: LONG SAFETY is the first comprehensive benchmark specifically designed to evaluate LLM safety in open-ended long-context tasks, encompassing 7 categories of safety issues and 6 user-oriented long-context tasks.

**Data Type**: text

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- LongSafetyBench

**Resources**:
- [GitHub Repository](https://github.com/thu-coai/LongSafety)

## 🎯 Purpose and Intended Users

**Goal**: To provide a systematic evaluation of safety vulnerabilities in long-context tasks for large language models.

**Target Audience**:
- ML Researchers
- Industry Practitioners

**Tasks**:
- Question Answering
- Generation
- Brainstorming
- Summarization
- Rewrite
- Role-playing

**Limitations**: While LONG SAFETY provides a comprehensive evaluation, some attack-oriented tasks, such as many-shot jailbreaking, are not included.

## 💾 Data

**Source**: Documents sourced from the Internet related to various safety topics.

**Size**: 1,543 instances

**Format**: N/A

**Annotation**: Annotation by crowd-workers to curate safety instructions relevant to each context.

## 🔬 Methodology

**Methods**:
- Multi-agent evaluation framework

**Metrics**:
- Safety rate

**Calculation**: Safety rate is calculated as the proportion of instances for which both responses to the two concatenation formats are assessed as safe.

**Interpretation**: Higher safety rates indicate better safety performance in long-context scenarios.

**Validation**: Evaluated on 16 representative long-context LLMs.

## ⚠️ Targeted Risks

**Risk Categories**:
- Safety

**Atlas Risks**:
- **Fairness**: Data bias
- **Robustness**: Evasion attack

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Participation of crowd workers was voluntary and they were informed about potential harmful content they may encounter.

**Compliance With Regulations**: Not Applicable
