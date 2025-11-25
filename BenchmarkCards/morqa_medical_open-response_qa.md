# MORQA (Medical Open-Response QA)

## 📊 Benchmark Details

**Name**: MORQA (Medical Open-Response QA)

**Overview**: MORQA is a new multilingual benchmark designed to assess the effectiveness of NLG evaluation metrics across three medical visual and text-based QA datasets in English and Chinese, featuring 2-4+ gold-standard answers authored by medical professionals, along with expert human ratings.

**Data Type**: question-answering pairs

**Domains**:
- Healthcare

**Languages**:
- English
- Chinese

**Resources**:
- [Resource](http://example.com/morqa_dataset_details)

## 🎯 Purpose and Intended Users

**Goal**: To provide a comprehensive evaluation benchmark for assessing NLG methods in medical contexts and highlight the effectiveness of LLMs as evaluators.

**Target Audience**:
- ML Researchers
- Domain Experts
- Model Developers

**Tasks**:
- Open-Ended Question Answering
- Visual Question Answering

**Limitations**: Sample size is limited, and evaluations may not fully represent all expert judgments.

## 💾 Data

**Source**: DermaVQA, WoundcareVQA, LiveQA, and MedDialog datasets.

**Size**: 16,041 expert judgments

**Format**: N/A

**Annotation**: Expert-annotated by certified medical professionals.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics
- LLM-based evaluation

**Metrics**:
- BLEU
- ROUGE
- BERTScore
- GPTScore

**Calculation**: Metrics calculated comparing responses against expert judgments.

**Interpretation**: Scores indicate correlation with expert judgments and assessment of output quality.

**Baseline Results**: Traditional metrics tend to underperform compared to LLM-based evaluations.

**Validation**: Cross-validation across multiple datasets and human expert evaluations.

## ⚠️ Targeted Risks

**Risk Categories**:
- Fairness
- Accuracy

**Atlas Risks**:
No specific atlas risks defined

**Demographic Analysis**: Diverse expert evaluations included.

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: All newly created data has been approved for public release and research use.

**Consent Procedures**: Expert annotators provided informed consent prior to task initiation.

**Compliance With Regulations**: Not Applicable
