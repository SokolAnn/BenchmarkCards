# MIMIC-IV-BHC (MIMIC-IV Brief Hospital Course)

## 📊 Benchmark Details

**Name**: MIMIC-IV-BHC (MIMIC-IV Brief Hospital Course)

**Overview**: We introduce a novel pre-processed dataset, the MIMIC-IV-BHC, encapsulating clinical note and brief hospital course (BHC) pairs to adapt LLMs for BHC synthesis. Furthermore, we introduce a benchmark of the summarization performance of two general-purpose LLMs and three healthcare-adapted LLMs.

**Data Type**: clinical note and brief hospital course pairs

**Domains**:
- Natural Language Processing
- Healthcare

**Languages**:
- English

**Resources**:
- [Resource](https://doi.org/10.13026/fh2q-4148)
- [Resource](https://www.physionet.org/content/mimic-iv-note/2.2/)
- [Resource](https://physionet.org/content/clinical-t5/1.0.0/)
- [GitHub Repository](https://github.com/StanfordMIMI/clin-bhc-summ)

## 🎯 Purpose and Intended Users

**Goal**: To facilitate the development of more efficient and accurate models for brief hospital course summarization.

**Target Audience**:
- ML Researchers
- Healthcare practitioners

**Tasks**:
- Text Summarization

**Limitations**: N/A

## 💾 Data

**Source**: MIMIC-IV-Note dataset, a compilation of 331,794 de-identified discharge summaries.

**Size**: 270,033 pairs

**Format**: N/A

**Annotation**: Pre-processed using whitespace removal, section identification, tokenization, and manual review.

## 🔬 Methodology

**Methods**:
- Prompting-based adaptation
- Fine-tuning-based adaptation

**Metrics**:
- BLEU Score
- BERT-Score
- ROUGE-L

**Calculation**: Evaluated across multiple context-length inputs using natural language similarity metrics.

**Interpretation**: Quantitative metrics used to evaluate the performance of summarization.

**Baseline Results**: N/A

**Validation**: Conducted a clinical study with five clinicians comparing clinician-written and LLM-generated BHCs.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Privacy
- Accuracy

**Atlas Risks**:
- **Accuracy**: Unrepresentative data
- **Privacy**: Personal information in data

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
