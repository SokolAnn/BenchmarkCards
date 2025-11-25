# CVALUES

## 📊 Benchmark Details

**Name**: CVALUES

**Overview**: CVALUES is the first Chinese human values evaluation benchmark to measure the alignment ability of LLMs in terms of both safety and responsibility criteria.

**Data Type**: adversarial and induced prompts

**Domains**:
- Environmental Science
- Psychology
- Law
- Social Science
- Data Science
- Intimate Relationship
- Barrier-free
- Lesser-known Major

**Languages**:
- Chinese

**Similar Benchmarks**:
- C-EVAL
- M3KE
- GAOKAO-Bench
- HEL
- MMLU

**Resources**:
- [Resource](https://www.modelscope.cn/datasets/damo/CValues-Comparison/summary)
- [GitHub Repository](https://github.com/X-PLUG/CValues)

## 🎯 Purpose and Intended Users

**Goal**: To provide a comprehensive evaluation of Chinese LLMs' human values alignment, enhancing responsible AI development.

**Target Audience**:
- Researchers
- Developers

**Tasks**:
- Assessing safety
- Assessing responsibility

**Limitations**: N/A

**Out of Scope Uses**:
- N/A

## 💾 Data

**Source**: Manually collected adversarial safety prompts and induced responsibility prompts

**Size**: 2100 safety prompts, 4312 multi-choice prompts

**Format**: N/A

**Annotation**: Prompts were manually labeled by specialized annotators and professional experts.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automatic evaluation

**Metrics**:
- Safety score
- Responsibility score
- Multi-choice accuracy

**Calculation**: Scores calculated based on the proportion of safe responses and average points by experts.

**Interpretation**: Higher scores indicate better alignment with human values.

**Baseline Results**: Various LLM performance results compared to ChatGPT.

**Validation**: Human evaluators and automated multi-choice tests.

## ⚠️ Targeted Risks

**Risk Categories**:
- Safety
- Responsibility

**Atlas Risks**:
- **Accuracy**: Poor model accuracy
- **Fairness**: Data bias
- **Value Alignment**: Improper data curation
- **Misuse**: Nonconsensual use

**Demographic Analysis**: N/A

**Potential Harm**: ['Potential for harmful outputs based on misalignment with human values']

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Data collection minimized risks regarding personal data.

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
