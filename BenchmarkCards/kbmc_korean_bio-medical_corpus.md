# KBMC (Korean Bio-Medical Corpus)

## 📊 Benchmark Details

**Name**: KBMC (Korean Bio-Medical Corpus)

**Overview**: KBMC is the first open-source medical NER dataset for Korean, aimed at improving named entity recognition in the medical domain.

**Data Type**: sentence-entity pairs

**Domains**:
- Natural Language Processing
- Healthcare

**Languages**:
- Korean

**Similar Benchmarks**:
- NCBI-disease
- BC5CDR

**Resources**:
- [GitHub Repository](https://github.com/naver/nlp-challenge)
- [Resource](https://chat.openai.com)

## 🎯 Purpose and Intended Users

**Goal**: To address data scarcity in medical NER for the Korean language and enhance the performance of models in recognizing medical entities.

**Target Audience**:
- ML Researchers
- Healthcare Practitioners
- NLP Developers

**Tasks**:
- Named Entity Recognition

**Limitations**: The primary challenge arises from the limited availability of Korean medical data, restricting the development of a comprehensive corpus.

## 💾 Data

**Source**: The dataset consists of sentences constructed with assistance from ChatGPT, annotated by human reviewers according to the BIO format.

**Size**: 6,150 sentences, 153,971 tokens

**Format**: N/A

**Annotation**: Manual annotation by experts with initial pre-annotations supported by an algorithm.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Model-based evaluation

**Metrics**:
- F1 Score
- Precision
- Recall

**Calculation**: Metrics calculated based on the performance of models trained using the KBMC dataset in comparison to those trained on general datasets.

**Interpretation**: An increase in F1 score signifies improved performance in recognizing medical entities.

**Baseline Results**: F1 scores for models trained on general datasets averaged below 80%, while models using KBMC achieved scores over 98% for specific categories.

**Validation**: Validated through comparisons of performance metrics on various language models.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Privacy
- Accuracy

**Atlas Risks**:
- **Accuracy**: Unrepresentative data
- **Privacy**: Data privacy rights alignment

**Demographic Analysis**: Includes demographic breakdowns for medical entities but lacks comprehensive analysis across distinct population groups.

**Potential Harm**: Aims to prevent misclassification of medical terms and promote accurate recognition to enhance patient data privacy.

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Dataset annotations focus on medical terms, aiding in the anonymization of sensitive patient information.

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
