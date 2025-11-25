# TactfulToM

## 📊 Benchmark Details

**Name**: TactfulToM

**Overview**: TactfulToM is a novel English benchmark designed to evaluate LLMs’ ability to understand white lies within real-life conversations and reason about prosocial motivations behind them.

**Data Type**: conversation sets with question-answering pairs

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- ToMBench

**Resources**:
- [GitHub Repository](https://github.com/nii-cl/tactful-tom)

## 🎯 Purpose and Intended Users

**Goal**: To evaluate LLMs' understanding of white lies in social contexts, filling a research gap in Theory of Mind evaluation.

**Target Audience**:
- ML Researchers
- Model Developers

**Tasks**:
- Theory of Mind Evaluation
- Natural Language Understanding

**Limitations**: Limited to White Lies; lacks extensive exploration of other second-order ToM abilities.

## 💾 Data

**Source**: Generated through a multi-stage human-in-the-loop process, maintaining information asymmetry necessary for white lies.

**Size**: 100 conversations with 6,700 questions

**Format**: JSON

**Annotation**: Reviewed by graduate students and independent annotators for coherence and white lie authenticity.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Accuracy
- Comprehension accuracy
- Justification accuracy

**Calculation**: Metrics calculated based on comparison of responses from LLMs and human participants.

**Interpretation**: Performance reflects understanding of complex social reasoning regarding white lies.

**Baseline Results**: Human performance achieved 85% accuracy, while state-of-the-art LLMs significantly underperformed.

**Validation**: Consisted of multiple iterated reviews and evaluations by trained annotators.

## ⚠️ Targeted Risks

**Risk Categories**:
- Fairness
- Accuracy

**Atlas Risks**:
- **Fairness**: Data bias, Decision bias
- **Accuracy**: Poor model accuracy

**Demographic Analysis**: N/A

**Potential Harm**: ['Misrepresenting human social behaviors', 'Potential unethical applications in sensitive contexts']

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: All annotator data was anonymized and secured.

**Data Licensing**: Not Applicable

**Consent Procedures**: Informed consent obtained from all annotators.

**Compliance With Regulations**: Not Applicable
