# Modeling Motivated Reasoning in Law: Evaluating Strategic Role Conditioning in LLM Summarization

## 📊 Benchmark Details

**Name**: Modeling Motivated Reasoning in Law: Evaluating Strategic Role Conditioning in LLM Summarization

**Overview**: This paper introduces a systematic framework for detecting motivated reasoning in legal AI, evaluating how LLMs adapt summaries based on the roles of legal actors and presenting an evaluation pipeline grounded in legal fact and reasoning.

**Data Type**: text

**Domains**:
- Natural Language Processing
- Legal

**Languages**:
- German

**Similar Benchmarks**:
- Swissblawg

**Resources**:
- [Resource](https://arxiv.org/abs/2509.00529)

## 🎯 Purpose and Intended Users

**Goal**: To systematically evaluate role-conditioned legal summarization and assess motivated reasoning in LLM outputs.

**Target Audience**:
- Legal Researchers
- AI Developers
- Legal Practitioners

**Tasks**:
- Text Summarization
- Evaluation of AI outputs

**Limitations**: N/A

## 💾 Data

**Source**: 200 German-language decisions from the Swiss Federal Supreme Court and human-written summaries from Swissblawg.

**Size**: 200 cases

**Format**: N/A

**Annotation**: Summaries evaluated using LLM assessments and human evaluations based on inclusion of key facts and reasoning.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Fact inclusion rate
- Favorability bias score

**Calculation**: Metrics computed based on the proportion of extracted facts included in each summary and bias assessed via omission analysis.

**Interpretation**: Higher favorability bias scores indicate selective inclusion patterns that align with stakeholder perspectives.

**Baseline Results**: Human-written summaries from Swissblawg serve as the baseline for comparison.

**Validation**: Evaluation of summaries against key legal points and reasoning by experts.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Accuracy

**Atlas Risks**:
- **Fairness**: Output bias
- **Accuracy**: Poor model accuracy

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
