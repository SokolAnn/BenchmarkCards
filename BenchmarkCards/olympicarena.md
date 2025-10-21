# OlympicArena

## 📊 Benchmark Details

**Name**: OlympicArena

**Overview**: OlympicArena is a comprehensive, highly-challenging, and rigorously curated benchmark designed to assess cognitive reasoning abilities of LLMs and LMMs using 11,163 bilingual problems from 62 distinct Olympic competitions across seven disciplines.

**Data Type**: question-answering pairs

**Domains**:
- Natural Language Processing
- Computer Science
- Mathematics
- Physics
- Chemistry
- Biology
- Geography
- Astronomy

**Languages**:
- English
- Chinese

**Similar Benchmarks**:
- MMLU
- C-Eval
- AGIEval

**Resources**:
- [GitHub Repository](https://github.com/GAIR-NLP/OlympicArena)

## 🎯 Purpose and Intended Users

**Goal**: To rigorously assess the cognitive reasoning abilities of AI models across multidisciplinary Olympic-level challenges.

**Target Audience**:
- ML Researchers
- AI Practitioners
- Educational Institutions

**Tasks**:
- Cognitive Reasoning Evaluation

**Limitations**: Our benchmark inevitably introduces some noisy problems and is currently limited to evaluating models’ abilities to solve complex problems.

## 💾 Data

**Source**: Collection of problems from 62 distinct Olympic competitions and publicly available URLs.

**Size**: 11,163 problems

**Format**: JSON

**Annotation**: Manual annotation by approximately 30 students with backgrounds in science and engineering.

## 🔬 Methodology

**Methods**:
- Automated metrics
- Human evaluation
- Process-based evaluation

**Metrics**:
- Accuracy
- F1 Score

**Calculation**: Metrics are calculated based on correctness of answers and correctness of reasoning steps.

**Interpretation**: Performance is evaluated not just on final accuracy but also on the correctness of the reasoning processes.

**Baseline Results**: Even advanced models like GPT-4o only achieve a 39.97% overall accuracy on the benchmark.

**Validation**: The benchmark incorporates data leakage detection experiments to ensure its effectiveness.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Accuracy
- Fairness

**Atlas Risks**:
- **Fairness**: Data bias, Decision bias
- **Accuracy**: Unrepresentative data

**Demographic Analysis**: The benchmark includes bilingual problems and aims to support diverse participants.

**Potential Harm**: The benchmark aims to evaluate and improve cognitive reasoning in AI systems while considering ethical implications.

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
