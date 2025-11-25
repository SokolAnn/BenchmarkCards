# FINTAGGING

## 📊 Benchmark Details

**Name**: FINTAGGING

**Overview**: FINTAGGING is the first full-scope, table-aware XBRL benchmark designed to evaluate the structured information extraction and semantic alignment capabilities of large language models (LLMs) in the context of XBRL-based financial reporting.

**Data Type**: table-aware information extraction

**Domains**:
- Finance

**Languages**:
- English

**Similar Benchmarks**:
- FiNER
- FNXL

**Resources**:
- [GitHub Repository](https://github.com/The-FinAI/FinTagging)
- [Resource](https://huggingface.co/collections/TheFinAI/fintagging-68270132372c6608ac069bef)

## 🎯 Purpose and Intended Users

**Goal**: To evaluate LLMs on their ability to perform full-scope XBRL tagging, including fact extraction and concept alignment.

**Target Audience**:
- ML Researchers
- Industry Practitioners
- Financial Analysts

**Tasks**:
- Structured Information Extraction
- Concept Linking

**Limitations**: The benchmark focuses primarily on US-GAAP financial reports and does not cover all global accounting standards.

## 💾 Data

**Source**: Collected annual 10-K reports from publicly listed companies filed with the SEC.

**Size**: 81,325 facts

**Format**: Tabular and textual

**Annotation**: Gold-standard annotations of numerical entity types and associated US-GAAP concepts.

## 🔬 Methodology

**Methods**:
- Zero-shot evaluation

**Metrics**:
- Macro F1 Score
- Micro F1 Score
- Accuracy

**Calculation**: Computed using pair-level metrics for FinNI and accuracy for FinCL.

**Interpretation**: Performance threshold varies based on specific subtask; higher scores indicate better extraction and alignment.

**Baseline Results**: Preliminary evaluation results show significant variance in performance across different models.

**Validation**: Joint evaluation framework for structured triplet {Fact, Type, Tag} assessment.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness
- Privacy

**Atlas Risks**:
- **Accuracy**: Poor model accuracy
- **Fairness**: Data bias
- **Privacy**: Exposing personal information

**Demographic Analysis**: N/A

**Potential Harm**: ['Misuse and Misinterpretation', 'Coverage Bias', 'Overreliance on Automation']

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
