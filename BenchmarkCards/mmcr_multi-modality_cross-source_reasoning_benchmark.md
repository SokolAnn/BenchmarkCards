# MMCR (Multi-Modality Cross-source Reasoning benchmark)

## 📊 Benchmark Details

**Name**: MMCR (Multi-Modality Cross-source Reasoning benchmark)

**Overview**: MMCR is a high-difficulty benchmark designed to evaluate Vision-Language Models' capacity for reasoning with cross-source information from scientific papers.

**Data Type**: question-answering pairs

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- DocVQA
- ChartQA
- MMLongBench-Doc

**Resources**:
- [GitHub Repository](https://github.com/yangtian6781/MMCR)

## 🎯 Purpose and Intended Users

**Goal**: To evaluate the cross-source reasoning ability of VLMs using information from multiple sources within scientific papers.

**Target Audience**:
- ML Researchers
- Domain Experts

**Tasks**:
- Figure Comprehension
- Multi-figure Comprehension
- Figure-Table Comprehension
- Figure-Text Comprehension
- Figure-Formula Comprehension
- Table Comprehension
- Multi-table Comprehension
- Text Comprehension
- Formula Comprehension
- Pseudocode Comprehension

**Limitations**: N/A

## 💾 Data

**Source**: Collected from scientific papers on Arxiv and high-quality publications on the OpenReview platform.

**Size**: 31 papers with an average of 19 pages, totaling 276 questions

**Format**: JPEG images and associated question-answer data

**Annotation**: Annotated by expert annotators with rigorous quality control procedures

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Accuracy

**Calculation**: Accuracy is calculated based on model responses to the multiple-choice questions.

**Interpretation**: Performance is interpreted in context to the overall accuracy across various question types.

**Baseline Results**: Best model achieved an accuracy of 48.55%, while lower-performing models generally scored below 10%.

**Validation**: Validated through extensive testing of 18 different VLMs.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness

**Atlas Risks**:
- **Accuracy**: Poor model accuracy
- **Fairness**: Data bias

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
