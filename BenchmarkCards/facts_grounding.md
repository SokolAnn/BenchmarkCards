# FACTS Grounding

## 📊 Benchmark Details

**Name**: FACTS Grounding

**Overview**: An online leaderboard and associated benchmark that evaluates language models’ ability to generate text that is factually accurate with respect to given context in the user prompt. The benchmark involves long-form responses based on user requests and context documents, assessing factual accuracy against provided prompts.

**Data Type**: question-answering pairs

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Resources**:
- [Resource](https://www.kaggle.com/facts-leaderboard)

## 🎯 Purpose and Intended Users

**Goal**: To rigorously challenge language models’ ability to maintain factual accuracy when generating long-form responses grounded in a document provided within the prompt and in accordance with a user’s specific request.

**Target Audience**:
- ML Researchers
- Model Developers

**Tasks**:
- Question Answering
- Summarization

**Limitations**: N/A

## 💾 Data

**Source**: A curated collection of documents and associated user requests written by human raters, validated and filtered to form the evaluation set.

**Size**: 1,719 examples

**Format**: N/A

**Annotation**: Prompts requiring processing of long-form input and writing of long-form output designed by third-party human raters.

## 🔬 Methodology

**Methods**:
- Automated metrics

**Metrics**:
- Factuality Score

**Calculation**: The factuality score is an aggregate of multiple judge models' evaluations after disqualifying ineligible responses that do not sufficiently fulfill the user request.

**Interpretation**: A model response is marked 'accurate' if all claims are grounded in the prompt, otherwise 'not accurate'.

**Baseline Results**: N/A

**Validation**: The performance of automated judge models was evaluated against a held-out test set to determine the best prompt template.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness
- Robustness

**Atlas Risks**:
- **Accuracy**: Poor model accuracy

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
