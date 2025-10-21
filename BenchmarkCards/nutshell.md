# NUTSHELL

## 📊 Benchmark Details

**Name**: NUTSHELL

**Overview**: NUTSHELL is a novel multimodal dataset for Speech-to-Abstract Generation (SAG) from *ACL conference talks, containing recorded presentations paired with their corresponding abstracts to facilitate the generation of abstracts from spoken content.

**Data Type**: multimodal

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- SCISUMMNET

**Resources**:
- [Resource](https://huggingface.co/datasets/maikezu/nutshell)

## 🎯 Purpose and Intended Users

**Goal**: Advance research in Speech-to-Abstract Generation (SAG) and foster the development of improved models and evaluation methods.

**Target Audience**:
- ML Researchers
- Model Developers
- Domain Experts

**Tasks**:
- Summarization

**Limitations**: N/A

## 💾 Data

**Source**: Recorded presentations from *ACL conferences (2017-2022) paired with their abstracts.

**Size**: 6,316 presentations, 1,172 hours of audio

**Format**: N/A

**Annotation**: Human evaluations for quality assessment and model evaluations.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automatic metrics

**Metrics**:
- ROUGE
- BERTScore

**Calculation**: Metrics are calculated based on n-gram overlap and contextualized token embeddings between summaries and references.

**Interpretation**: Higher scores indicate better performance in generating concise and accurate abstracts.

**Baseline Results**: N/A

**Validation**: Models were evaluated based on both automatic metrics and human judgments to ensure reliability.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness

**Atlas Risks**:
- **Accuracy**: Unrepresentative data
- **Fairness**: Output bias

**Demographic Analysis**: N/A

**Potential Harm**: Automatic summaries may misrepresent key findings or lack scientific accuracy.

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: CC-BY 4.0

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
