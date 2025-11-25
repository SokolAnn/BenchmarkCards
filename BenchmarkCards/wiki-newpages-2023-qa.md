# Wiki-Newpages-2023-QA

## 📊 Benchmark Details

**Name**: Wiki-Newpages-2023-QA

**Overview**: The Wiki-Newpages-2023-QA datasets are specifically designed to study the knowledge acquisition capabilities of large language models (LLMs) related to memorization, extraction, and reasoning.

**Data Type**: question-answering pairs

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- N/A

**Resources**:
- [GitHub Repository](https://github.com/zhangxy-2019/Effective-Knowledge-Injection)

## 🎯 Purpose and Intended Users

**Goal**: To explore the knowledge acquisition capabilities of LLMs through self-teaching via newly curated datasets.

**Target Audience**:
- ML Researchers
- Domain Experts

**Tasks**:
- Knowledge Memorization
- Knowledge Extraction
- Natural Language Inference

**Limitations**: N/A

## 💾 Data

**Source**: Collected articles from Wikipedia NewPages published after the pre-training cut-off time of the LLMs.

**Size**: 4,257 articles

**Format**: JSON

**Annotation**: Generated QA pairs using prompts for open-ended generation and natural language inference tasks.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Accuracy
- Exact Match (EM)
- F1 Score
- Recall
- ROUGE-L

**Calculation**: Metrics calculated using the generated responses in comparison to ground truth answers.

**Interpretation**: Higher scores indicate better knowledge acquisition capabilities of LLMs.

**Baseline Results**: SELF-TUNING significantly outperforms baseline methods.

**Validation**: Results validated through extensive experiments on knowledge extraction and retention tasks.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness

**Atlas Risks**:
- **Accuracy**: Unrepresentative data
- **Fairness**: Data bias

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
