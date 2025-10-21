# Document Haystack: A Long Context Multimodal Image/Document Understanding Vision LLM Benchmark

## 📊 Benchmark Details

**Name**: Document Haystack: A Long Context Multimodal Image/Document Understanding Vision LLM Benchmark

**Overview**: Document Haystack is a comprehensive benchmark designed to evaluate the performance of Vision Language Models (VLMs) on long, visually complex documents, featuring 400 document variants and a total of 8,250 questions.

**Data Type**: text and image retrieval tasks

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- Needle in a Haystack
- LongBench
- VQA
- NLVR
- MileBench
- DUDE
- Loong
- SlideVQA
- MMLongBench-Doc

**Resources**:
- [Resource](https://huggingface.co/datasets/AmazonScience/document-haystack)
- [GitHub Repository](https://github.com/amazon-science/document-haystack)

## 🎯 Purpose and Intended Users

**Goal**: To provide a comprehensive and challenging benchmark for evaluating the long context capabilities of multimodal Language Models, focusing on VLMs' ability to accurately retrieve key multimodal information from lengthy documents.

**Target Audience**:
- ML Researchers
- Model Developers

**Tasks**:
- Text Retrieval
- Image Retrieval
- Multimodal Retrieval

**Limitations**: N/A

## 💾 Data

**Source**: Comprises 400 document variants sourced from publicly available financial 10-K reports.

**Size**: 8250 questions

**Format**: PDF, Image, Text

**Annotation**: Automated evaluation framework

## 🔬 Methodology

**Methods**:
- Automated metrics

**Metrics**:
- Accuracy

**Calculation**: Responses are lowercased and searched for the VALUE associated with the KEY to determine success.

**Interpretation**: Accuracy in retrieving the correct value in response to the provided key.

**Baseline Results**: Results from prominent VLMs such as Nova Lite, Gemini Flash-2.0, and GPT-4o-mini.

**Validation**: Evaluation against automated, objective standards.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness
- Privacy

**Atlas Risks**:
- **Accuracy**: Unrepresentative data

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
