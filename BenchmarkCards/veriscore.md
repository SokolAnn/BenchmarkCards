# VERISCORE

## 📊 Benchmark Details

**Name**: VERISCORE

**Overview**: VERISCORE is a metric developed to evaluate the factuality of verifiable claims in long-form text generation, addressing limitations in existing metrics by focusing on both verifiable and unverifiable content.

**Data Type**: text

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- FACTSCORE
- SAFE

**Resources**:
- [GitHub Repository](https://github.com/Yixiao-Song/VeriScore)

## 🎯 Purpose and Intended Users

**Goal**: To provide an automatic metric for evaluating the factuality of language models' long-form text outputs.

**Target Audience**:
- ML Researchers
- Natural Language Processing Practitioners

**Tasks**:
- Long-Form Question Answering
- Text Generation

**Limitations**: The system struggles with verifying complex claims that require extensive reasoning.

## 💾 Data

**Source**: Various long-form text datasets including biographies, FAQs, and other fact-seeking prompts.

**Size**: N/A

**Format**: N/A

**Annotation**: Claims were annotated through human evaluation for verification against Google Search results.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- F1 Score

**Calculation**: VERISCORE is calculated using F1@K metric considering both precision and recall of verifiable claims.

**Interpretation**: Higher VERISCORE indicates better factual support of generated text.

**Baseline Results**: Various models such as GPT-4o, Claude 3, and Mixtral were evaluated using VERISCORE indicating their factual accuracy.

**Validation**: Human evaluation and performance analysis across various tasks.

## ⚠️ Targeted Risks

**Risk Categories**:
- Fairness
- Accuracy
- Robustness

**Atlas Risks**:
- **Fairness**: Output bias
- **Accuracy**: Poor model accuracy
- **Robustness**: Prompt leaking

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
