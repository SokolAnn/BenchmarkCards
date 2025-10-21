# VisualWebBench

## 📊 Benchmark Details

**Name**: VisualWebBench

**Overview**: VisualWebBench is a comprehensive multimodal benchmark designed to evaluate the capabilities of Multimodal Large Language Models (MLLMs) in web-related tasks, consisting of seven tasks and 1.5K human-curated instances from 139 real websites across 87 sub-domains.

**Data Type**: question-answering pairs

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Resources**:
- [Resource](https://visualwebbench.github.io/)

## 🎯 Purpose and Intended Users

**Goal**: To provide a standardized benchmark for evaluating MLLMs in web understanding, enabling the development of more capable and efficient models specific to web-related applications.

**Target Audience**:
- ML Researchers
- Industry Practitioners

**Tasks**:
- Webpage Captioning
- Webpage Question Answering
- Heading OCR
- Element OCR
- Element Grounding
- Action Prediction
- Action Grounding

**Limitations**: N/A

## 💾 Data

**Source**: 1.5K human-curated instances from 139 real websites, covering 87 sub-domains.

**Size**: 1,500 examples

**Format**: N/A

**Annotation**: Manually curated and verified by human annotators.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- F1 Score
- ROUGE-L
- Accuracy

**Calculation**: Specific tasks use F1 Score for the WebQA task, ROUGE-L for captioning, and Accuracy for multiple-choice tasks.

**Interpretation**: Performance is interpreted based on scores relative to the best-performing models, with an average of scores signaling capabilities.

**Baseline Results**: Average scores for GPT-4V(ision) is 64.6, Claude Sonnet 65.8, and the leading open-source model LLaVA-1.6-34B 50.5.

**Validation**: Comprehensive validation through human curation and ensuring clarity of instruction tasks.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness
- Robustness

**Atlas Risks**:
- **Accuracy**: Unrepresentative data, Poor model accuracy
- **Fairness**: Data bias
- **Robustness**

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
