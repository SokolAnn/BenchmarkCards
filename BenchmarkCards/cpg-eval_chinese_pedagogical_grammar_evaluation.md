# CPG-EVAL (Chinese Pedagogical Grammar Evaluation)

## 📊 Benchmark Details

**Name**: CPG-EVAL (Chinese Pedagogical Grammar Evaluation)

**Overview**: CPG-EVAL is the first dedicated benchmark specifically designed to evaluate LLMs’ knowledge of pedagogical grammar within the context of foreign language instruction. It comprises five tasks designed to assess grammar recognition, fine-grained grammatical distinction, categorical discrimination, and resistance to linguistic interference.

**Data Type**: grammar recognition tasks

**Domains**:
- Natural Language Processing
- Education

**Languages**:
- Chinese

**Similar Benchmarks**:
- GLUE
- SuperGLUE
- CLUE
- SuperCLUE

**Resources**:
- [GitHub Repository](https://github.com/wd-github-2017/CPG-EVAL)

## 🎯 Purpose and Intended Users

**Goal**: To systematically evaluate LLMs' pedagogical grammar competence in teaching Chinese as a second language.

**Target Audience**:
- Educators
- Policymakers
- Model Developers
- Researchers

**Tasks**:
- Grammar Recognition
- Grammatical Distinction
- Categorical Discrimination
- Resistance to Linguistic Interference

**Limitations**: N/A

## 💾 Data

**Source**: Constructed from the Chinese Grammar Learning Manual (CGLM) and synthetic data generated based on expert guidelines.

**Size**: 6,651 synthetic sentences

**Format**: N/A

**Annotation**: Synthetic data reviewed and revised by expert linguists.

## 🔬 Methodology

**Methods**:
- Automated metrics
- Model-based evaluation

**Metrics**:
- Accuracy

**Calculation**: Scores calculated by comparing model outputs against the correct answers using regular expressions.

**Interpretation**: Higher accuracy indicates better understanding and application of pedagogical grammar by LLMs.

**Baseline Results**: N/A

**Validation**: Benchmarked against multiple open-source and proprietary LLMs under a zero-shot setting.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness
- Robustness

**Atlas Risks**:
- **Accuracy**: Poor model accuracy
- **Fairness**: Output bias
- **Robustness**: Data poisoning

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
