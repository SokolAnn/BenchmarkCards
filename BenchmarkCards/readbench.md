# ReadBench

## 📊 Benchmark Details

**Name**: ReadBench

**Overview**: ReadBench is a multimodal benchmark specifically designed to evaluate the reading comprehension capabilities of Vision-Language Models (VLMs) by adapting contexts from established text-only benchmarks into images of text while keeping textual prompts and questions intact.

**Data Type**: text-image pairs

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- MMLU (Massive Multitask Language Understanding)
- DocVQA
- TextVQA

**Resources**:
- [Resource](https://huggingface.co/learn/cookbook/en/multimodal_rag_using_document_retrieval_and_reranker_and_vlms)

## 🎯 Purpose and Intended Users

**Goal**: To evaluate VLMs' ability to effectively answer questions based on text presented visually.

**Target Audience**:
- ML Researchers
- Model Developers

**Tasks**:
- Question Answering

**Limitations**: ReadBench primarily focuses on the English language, limiting its applicability to other languages.

## 💾 Data

**Source**: Adapted from established text-only benchmarks

**Size**: N/A

**Format**: Image with embedded text

**Annotation**: N/A

## 🔬 Methodology

**Methods**:
- Automated metrics
- Human evaluation

**Metrics**:
- Accuracy

**Calculation**: Performance is measured based on the average scores of the evaluated VLMs across multiple runs to reduce variance.

**Interpretation**: Performance degradation is analyzed based on the input length and task difficulty.

**Baseline Results**: Evaluated models included Pixtral 12B, GPT-4o, Qwen2.5-VL.

**Validation**: N/A

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
