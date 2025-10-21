# PRGB Benchmark

## 📊 Benchmark Details

**Name**: PRGB Benchmark

**Overview**: A multi-level fine-grained benchmark for evaluating the information utilization capabilities of large language models (LLMs) within Retrieval-Augmented Generation (RAG) systems.

**Data Type**: text

**Domains**:
- Natural Language Processing

**Languages**:
- English
- Chinese

**Similar Benchmarks**:
- HIRAG
- RGB
- RAGBench

**Resources**:
- [GitHub Repository](https://github.com/Alipay-Med/PRGB)

## 🎯 Purpose and Intended Users

**Goal**: To provide a nuanced understanding of LLMs’ roles in RAG systems and assess their document utilization capabilities.

**Target Audience**:
- ML Researchers
- Industry Practitioners
- Model Developers

**Tasks**:
- Multi-Level Filtering
- Combination
- Reference Reasoning

**Limitations**: N/A

## 💾 Data

**Source**: Constructed using triplets from Wikipedia with manual verification and synthesis using GPT-4 for diverse entity types and scenarios.

**Size**: 3,887 English samples, 3,387 Chinese samples

**Format**: N/A

**Annotation**: Manual verification and synthesis.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Accuracy
- Exact Match

**Calculation**: Based on whether keywords appear in the document, using logical operators for accuracy enhancements.

**Interpretation**: High scores indicate better LLM performance in generating accurate answers based on given contexts.

**Baseline Results**: N/A

**Validation**: N/A

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Safety
- Accuracy

**Atlas Risks**:
- **Fairness**: Data bias
- **Accuracy**: Poor model accuracy

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
