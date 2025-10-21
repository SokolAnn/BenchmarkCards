# CNNSum

## 📊 Benchmark Details

**Name**: CNNSum

**Overview**: CNNSum is a multi-scale long-context summarization benchmark based on Chinese novels, featuring human-driven annotations across four subsets totaling 695 samples, with lengths ranging from 16k to 128k tokens. It is designed to facilitate the evaluation of long-context summarization abilities of large language models (LLMs).

**Data Type**: text

**Domains**:
- Natural Language Processing

**Languages**:
- Chinese

**Similar Benchmarks**:
- CLongEval-LStSum

**Resources**:
- [GitHub Repository](https://github.com/CxsGhost/CNNSum)

## 🎯 Purpose and Intended Users

**Goal**: To advance research in long-context summarization by providing a reliable evaluation benchmark for large language models.

**Target Audience**:
- ML Researchers
- Domain Experts

**Tasks**:
- Text Summarization

**Limitations**: N/A

## 💾 Data

**Source**: A newly collected corpus of 103 books from Chinese Internet open-source data, featuring 695 samples in total.

**Size**: 695 samples

**Format**: N/A

**Annotation**: Annotations were completed by human experts with assistance from LLMs.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- ROUGE-L

**Calculation**: ROUGE-L is calculated based on the output of the models against reference summaries, measuring the overlap of tokens between them.

**Interpretation**: Higher ROUGE-L scores indicate better summarization performance and alignment with human preferences.

**Baseline Results**: Performance gaps were noted across different model versions, highlighting challenges in long-context summarization.

**Validation**: Tested for reliability with diverse prompts and human assessments.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Safety
- Accuracy

**Atlas Risks**:
- **Accuracy**: Unrepresentative data

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
