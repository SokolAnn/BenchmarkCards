# WixQA

## 📊 Benchmark Details

**Name**: WixQA

**Overview**: WixQA is a benchmark suite featuring QA datasets precisely grounded in the released knowledge base corpus, enabling holistic evaluation of retrieval and generation components in enterprise environments.

**Data Type**: question-answering pairs

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- SQuAD
- TechQA
- Natural Questions

**Resources**:
- [Resource](https://huggingface.co/datasets/Wix/WixQA)

## 🎯 Purpose and Intended Users

**Goal**: To provide a robust foundation for future research in procedural, multi-document Question Answering (QA) in enterprise contexts.

**Target Audience**:
- ML Researchers
- Industry Practitioners
- Model Developers

**Tasks**:
- Question Answering

**Limitations**: N/A

## 💾 Data

**Source**: Three datasets derived from Wix.com customer support interactions.

**Size**: 6,221 question-answering pairs

**Format**: N/A

**Annotation**: Expert-authored, expert-validated, and LLM-generated QA pairs.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- F1 Score
- BLEU Score
- ROUGE-1
- ROUGE-2

**Calculation**: Metrics are calculated based on evaluation against ground truth answers.

**Interpretation**: Higher scores in metrics indicate better generation that aligns closely with expert-authored answers.

**Baseline Results**: N/A

**Validation**: Extensive experiments across all datasets provide in-depth analyses.

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

**Data Licensing**: MIT license

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
