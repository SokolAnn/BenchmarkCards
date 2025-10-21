# TemplateCSR (Template Filling for Controllable Commonsense Reasoning)

## 📊 Benchmark Details

**Name**: TemplateCSR (Template Filling for Controllable Commonsense Reasoning)

**Overview**: We propose a dataset of commonsense reasoning template-expansion pairs and introduce POTTER, a pretrained sequence-to-sequence model to perform commonsense reasoning across concepts via template filling.

**Data Type**: template-expansion pairs

**Domains**:
- Natural Language Processing
- Healthcare

**Languages**:
- English

**Similar Benchmarks**:
- commonsenseqa

**Resources**:
- [Resource](https://www.mturk.com)
- [Resource](https://www.cdc.gov)
- [Resource](https://www.webmd.com)
- [Resource](https://www.healthline.com)
- [Resource](https://www.mayoclinic.org)

## 🎯 Purpose and Intended Users

**Goal**: To enhance commonsense reasoning capabilities of NLP systems through controllable reasoning via templates.

**Target Audience**:
- ML Researchers
- Domain Experts
- Industry Practitioners

**Tasks**:
- Commonsense Reasoning

**Limitations**: N/A

## 💾 Data

**Source**: Crowdsourced via Amazon Mechanical Turk, based on commonsense reasoning related to lifestyle and health.

**Size**: 3,600 unique template-expansion pairs

**Format**: N/A

**Annotation**: Collected with a filtering step for quality and correctness, ensuring factual information and no identifying details.

## 🔬 Methodology

**Methods**:
- Automated metrics
- Human evaluation

**Metrics**:
- ROUGE
- BERTSCORE
- FACTCC

**Calculation**: Standard evaluation metrics were computed comparing generated expansions against gold annotations.

**Interpretation**: Higher ROUGE and BERTSCORE indicate better generation quality, while FACTCC measures factual consistency.

**Baseline Results**: BART-LARGE POTTER achieved a ROUGE-1 score of 20.58.

**Validation**: 70/10/20 train/val/test split was used for model evaluation.

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
