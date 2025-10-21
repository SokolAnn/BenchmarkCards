# HelpSteer2

## 📊 Benchmark Details

**Name**: HelpSteer2

**Overview**: HelpSteer2 is a permissively licensed preference dataset (CC-BY-4.0) designed to train state-of-the-art reward models for aligning large language models (LLMs) with human preferences. It consists of 10,000 response pairs and has been shown to achieve state-of-the-art performance on the Reward-Bench primary dataset.

**Data Type**: response pairs

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- HelpSteer

**Resources**:
- [Resource](https://huggingface.co/datasets/nvidia/HelpSteer2)
- [GitHub Repository](https://github.com/NVIDIA/NeMo-Aligner)

## 🎯 Purpose and Intended Users

**Goal**: To provide a high-quality help dataset for training reward models that effectively align LLMs with human preferences.

**Target Audience**:
- ML Researchers
- Model Developers
- Domain Experts

**Tasks**:
- Reward Modeling
- Preference Learning

**Limitations**: N/A

## 💾 Data

**Source**: The dataset is derived predominantly from ShareGPT, supplemented with proprietary prompts; multi-turn prompts are also included.

**Size**: 10,681 prompts with 21,362 total annotated responses

**Format**: CSV

**Annotation**: Responses are annotated by human annotators using a Likert-5 scale across five attributes.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Cohen's kappa
- Accuracy

**Calculation**: Metrics are calculated based on inter-annotator agreement for rating quality and accuracy of responses.

**Interpretation**: Higher Cohen's kappa indicates stronger agreement among annotators, while accuracy reflects the proportion of instances where the chosen response outperforms the rejected response.

**Baseline Results**: State-of-the-art performance on Reward-Bench primary dataset at 92.0% overall accuracy.

**Validation**: The dataset was validated through inter-annotator agreement assessments and extensive quality assurance procedures.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Safety

**Atlas Risks**:
- **Fairness**: Data bias
- **Privacy**: Personal information in data

**Demographic Analysis**: The dataset primarily consists of annotations by US-based annotators, limiting cultural diversity.

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Annotators are instructed to skip samples containing Personally Identifiable Information (PII) and to report unsafe content.

**Data Licensing**: Licensed under CC-BY-4.0 allowing permissive commercial use.

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
