# RoleTriviaQA

## 📊 Benchmark Details

**Name**: RoleTriviaQA

**Overview**: RoleTriviaQA is a large-scale role-playing knowledge QA benchmark with diverse speaker identities, aimed to evaluate the understanding and generation capabilities of speech-language models.

**Data Type**: question-answering pairs

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Resources**:
- [GitHub Repository](https://github.com/cnxupupup/SLM-Decoupled-MTP)
- [Resource](https://cnxupupup.github.io/SLM-Decoupled-MTP-Demo)

## 🎯 Purpose and Intended Users

**Goal**: To benchmark speech-language models on role embodiment and knowledge-intensive spoken responses across various tasks.

**Target Audience**:
- ML Researchers
- Speech Generation Practitioners

**Tasks**:
- Question Answering

**Limitations**: N/A

## 💾 Data

**Source**: Constructed from TriviaQA and synthesised using CosyVoice2 for diverse speaker roles.

**Size**: 138,384 examples

**Format**: JSON

**Annotation**: Data generated through pretrained text-to-speech synthesis systems.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Exact Match (EM)
- F1 Score
- Speaker Similarity (SIM)

**Calculation**: Metrics calculated as described in the experiments section based on model responses compared to ground truth.

**Interpretation**: Higher EM and F1 scores indicate better model's ability to generate correct and contextually appropriate responses.

**Baseline Results**: Best baseline models showed significant performance improvements, with an EM of 12.0 and F1 of 23.8 on RoleTriviaQA.

**Validation**: Models validated by comparing their predictions against a benchmark set, tracking performance on both in-domain and out-of-domain queries.

## ⚠️ Targeted Risks

**Risk Categories**:
- Fairness
- Robustness

**Atlas Risks**:
- **Fairness**: Data bias
- **Robustness**: Evasion attack

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
