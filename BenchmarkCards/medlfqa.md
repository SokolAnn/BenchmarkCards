# MedLFQA

## 📊 Benchmark Details

**Name**: MedLFQA

**Overview**: MedLFQA is a benchmark dataset reconstructed using long-form question-answering datasets related to the biomedical domain, facilitating automatic evaluation of factuality for LLM responses.

**Data Type**: question-answering pairs

**Domains**:
- Healthcare

**Languages**:
- English

**Resources**:
- [Resource](https://huggingface.co/datasets/dmis-lab/MedLFQA)
- [GitHub Repository](https://github.com/dmis-lab/OLAPH)

## 🎯 Purpose and Intended Users

**Goal**: To evaluate the long-form generation ability of large language models (LLMs) in the medical domain and improve their factuality.

**Target Audience**:
- ML Researchers
- Healthcare Professionals

**Tasks**:
- Long-form Question Answering

**Limitations**: The dataset consists only of test datasets, making it difficult to assess the efficacy of the O LAPH framework on training datasets.

## 💾 Data

**Source**: Reconstructed from current biomedical LFQA datasets including LiveQA, MedicationQA, HealthSearchQA, and K-QA.

**Size**: 4,000 QA pairs

**Format**: JSON

**Annotation**: Curated by medical experts with additional statements evaluated through automated methods.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Factuality
- Semantic Similarity
- Word Composition

**Calculation**: Metrics were calculated based on automatic evaluations comparing model-generated responses to expert-curated content.

**Interpretation**: An increase in scores indicates improved factuality and coherence of the generated text.

**Validation**: Models were validated through pairwise evaluations by medical experts.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Bias
- Privacy

**Atlas Risks**:
- **Accuracy**
- **Fairness**: Data bias
- **Transparency**: Lack of training data transparency

**Demographic Analysis**: N/A

**Potential Harm**: Potential for misinformation could affect patient health decisions.

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Anonymization procedures were followed in the creation of the dataset.

**Data Licensing**: Data usage rights depend on the licenses of the original datasets used for reconstruction.

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
