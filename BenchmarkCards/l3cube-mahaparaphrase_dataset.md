# L3Cube-MahaParaphrase Dataset

## 📊 Benchmark Details

**Name**: L3Cube-MahaParaphrase Dataset

**Overview**: The L3Cube-MahaParaphrase Dataset is a robust Marathi paraphrase corpus consisting of 8,000 labeled pairs of sentences classified as either Paraphrase (P) or Non-paraphrase (NP), divided into five buckets based on varying degrees of paraphrastic and non-paraphrastic relationships.

**Data Type**: sentence pairs

**Domains**:
- Natural Language Processing

**Languages**:
- Marathi

**Similar Benchmarks**:
- IndicParaphrase
- Amritha corpus
- BanglaParaphrase

**Resources**:
- [GitHub Repository](https://github.com/l3cube-pune/MarathiNLP)
- [Resource](https://huggingface.co/datasets/l3cube-pune/MahaParaphrase)

## 🎯 Purpose and Intended Users

**Goal**: The primary objective of the L3Cube-MahaParaphrase Dataset is to provide a valuable resource for researchers and practitioners to advance further research in Marathi NLP.

**Target Audience**:
- ML Researchers
- NLP Practitioners

**Tasks**:
- Paraphrase Detection

**Limitations**: Compared to paraphrase datasets for high-resource languages, this dataset is relatively small (8K pairs).

## 💾 Data

**Source**: The dataset was created from the MahaCorpus dataset, incorporating data through manual verification and annotation processes.

**Size**: 8,000 sentence pairs

**Format**: N/A

**Annotation**: Annotated by human experts as either Paraphrase (P) or Non-paraphrase (NP), with verification by native Marathi speakers.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Cosine similarity
- Back translation

**Metrics**:
- Accuracy
- F1 Score

**Calculation**: Metrics such as accuracy and F1 score are calculated based on the model evaluation on the dataset.

**Interpretation**: An F1 score of 88.7% indicates a high level of accuracy in paraphrase detection.

**Baseline Results**: MahaBERT achieved an F1 score of 88.7%, the highest among evaluated models.

**Validation**: The dataset was validated through manual corrections by native annotators.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Accuracy

**Atlas Risks**:
- **Accuracy**: Data contamination, Unrepresentative data

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
