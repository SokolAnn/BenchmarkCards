# Russian-Language Multimodal Dataset for Automatic Summarization of Scientific Papers

## 📊 Benchmark Details

**Name**: Russian-Language Multimodal Dataset for Automatic Summarization of Scientific Papers

**Overview**: The paper discusses the creation of a multimodal dataset of Russian-language scientific papers and testing of existing language models for the task of automatic text summarization.

**Data Type**: multimodal

**Domains**:
- Natural Language Processing

**Languages**:
- Russian

**Resources**:
- [GitHub Repository](https://github.com/iis-research-team/summarization-dataset)

## 🎯 Purpose and Intended Users

**Goal**: To create a dataset for the scientific papers summarization for Russian, covering different domains including technical, humanitarian, and natural sciences.

**Target Audience**:
- ML Researchers
- Domain Experts

**Tasks**:
- Automatic Text Summarization

**Limitations**: Current version of the dataset covers only 7 scientific domains, but it should be increased to include more diverse areas.

## 💾 Data

**Source**: Collected from three scientific journals covering Economics, History, Information Technologies, Journalism, Law, Linguistics, and Medicine.

**Size**: 420 texts

**Format**: N/A

**Annotation**: N/A

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- BERTScore
- BLEURT
- ROUGE-1
- ROUGE-2
- ROUGE-L
- BLEU

**Calculation**: Metrics like BERTScore and BLEURT calculate the similarity based on pre-trained embeddings, while ROUGE metrics calculate overlapping n-grams.

**Interpretation**: Values near 1 for metrics indicate better matches.

**Baseline Results**: The models were evaluated against the reference abstracts from the dataset.

**Validation**: The quality of generated abstracts was compared with the reference summaries.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness

**Atlas Risks**:
No specific atlas risks defined

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
