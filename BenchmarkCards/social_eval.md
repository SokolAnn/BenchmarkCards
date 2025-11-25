# SOCIAL EVAL

## 📊 Benchmark Details

**Name**: SOCIAL EVAL

**Overview**: SOCIAL EVAL is a script-based bilingual benchmark designed to evaluate and inspect large language models' social intelligence (SI) through outcome-oriented goal achievement evaluation and process-oriented interpersonal ability evaluation.

**Data Type**: text

**Domains**:
- Natural Language Processing

**Languages**:
- English
- Chinese

**Similar Benchmarks**:
- N/A

**Resources**:
- [GitHub Repository](https://github.com/thu-coai/SocialEval)

## 🎯 Purpose and Intended Users

**Goal**: To thoroughly evaluate and inspect LLMs’ social intelligence via a comprehensive social world construction and to identify discrepancies between LLMs and humans in social interactions.

**Target Audience**:
- ML Researchers
- Social Scientists
- Model Developers

**Tasks**:
- Social Intelligence Evaluation
- Outcome-oriented Goal Achievement
- Process-oriented Interpersonal Ability Evaluation

**Limitations**: The scale of SOCIAL EVAL is currently limited due to the manual construction process, involving 153 world trees for evaluation, which might not provide a comprehensive analysis of all interpersonal abilities.

## 💾 Data

**Source**: Manually crafted narrative scripts incorporating social interactions and outcomes tailored toward evaluating social intelligence.

**Size**: 153 world trees, 2,493 test samples

**Format**: N/A

**Annotation**: Manually crafted by experts in social psychology and narrative structure.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Accuracy
- F1 Score

**Calculation**: Metrics measure LLMs’ ability to achieve social goals and use appropriate interpersonal abilities in scripted scenarios.

**Interpretation**: Results provide comparative insights between human and LLM performance in navigating social interactions.

**Baseline Results**: Human baselines established using graduate-level participants for evaluating performance on SI tasks.

**Validation**: Through rigorous script crafting and iterative quality checks among multiple annotators.

## ⚠️ Targeted Risks

**Risk Categories**:
- Fairness
- Privacy
- Safety

**Atlas Risks**:
- **Fairness**: Data bias
- **Privacy**: Personal information in data
- **Robustness**: Prompt injection attack

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Data collected does not contain any personally identifiable information, and all contributors are compensated fairly.

**Data Licensing**: Not Applicable

**Consent Procedures**: A consent form was obtained from all human participants involved in the creation of the benchmark and evaluations.

**Compliance With Regulations**: Not Applicable
