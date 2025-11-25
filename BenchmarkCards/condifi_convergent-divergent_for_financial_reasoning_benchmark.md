# ConDiFi (Convergent-Divergent for Financial Reasoning Benchmark)

## 📊 Benchmark Details

**Name**: ConDiFi (Convergent-Divergent for Financial Reasoning Benchmark)

**Overview**: ConDiFi is a benchmark that jointly evaluates divergent and convergent thinking in LLMs for financial tasks, featuring 607 macro-financial prompts for divergent reasoning and 990 multi-hop MCQs for convergent reasoning.

**Data Type**: text

**Domains**:
- Finance

**Languages**:
- English

**Similar Benchmarks**:
- MMLU

**Resources**:
- [Resource](N/A)

## 🎯 Purpose and Intended Users

**Goal**: To provide a more holistic and domain-relevant standard for measuring the cognitive capabilities of LLMs in finance by evaluating both divergent and convergent thinking.

**Target Audience**:
- ML Researchers
- Financial Analysts
- Model Developers

**Tasks**:
- Divergent Thinking Evaluation
- Convergent Thinking Evaluation

**Limitations**: N/A

## 💾 Data

**Source**: Constructed from post-LLM training financial scenarios and macroeconomic data.

**Size**: 1,597 financial prompts

**Format**: JSON

**Annotation**: Automated scoring using a model as a judge, with adjusted metrics based on domain knowledge.

## 🔬 Methodology

**Methods**:
- LLM-As-A-Judge Evaluation
- Direct Comparison of Multiple Models

**Metrics**:
- Plausibility
- Novelty
- Elaboration
- Actionable
- Richness

**Calculation**: Scores are calculated based on a defined rubric for financial scenario reasoning.

**Interpretation**: Higher scores indicate better reasoning capabilities for financial decision-making complexities.

**Baseline Results**: Results showed a performance spectrum among various models, with notable differences in divergent and convergent metrics.

**Validation**: Evaluated across 14 models to ensure robustness and variability in cognitive capabilities.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Accuracy
- Privacy

**Atlas Risks**:
- **Fairness**: Data bias
- **Accuracy**: Poor model accuracy
- **Privacy**: Personal information in data

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Data sourced from public financial reports, avoiding private or sensitive data.

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
