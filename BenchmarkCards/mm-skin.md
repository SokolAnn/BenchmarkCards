# MM-Skin

## 📊 Benchmark Details

**Name**: MM-Skin

**Overview**: MM-Skin is the first large-scale multimodal dermatology dataset that encompasses 3 imaging modalities, including clinical, dermoscopic, and pathological, and nearly 10k high-quality image-text pairs collected from professional textbooks. It also generates over 27k diverse, instruction-following vision question answering samples.

**Data Type**: image-text pairs, question-answering pairs

**Domains**:
- Healthcare

**Languages**:
- English

**Resources**:
- [Resource](https://arxiv.org/abs/2505.06152)

## 🎯 Purpose and Intended Users

**Goal**: To develop a specialized dermatology vision-language model and to provide a rich dataset that enhances visual understanding of skin diseases.

**Target Audience**:
- ML Researchers
- Domain Experts

**Tasks**:
- Visual Question Answering
- Supervised Fine-tuning
- Zero-shot Classification

**Limitations**: N/A

## 💾 Data

**Source**: Images and textual descriptions collected from 15 dermatology textbooks.

**Size**: 10,000 image-text pairs, 27,000 QA pairs

**Format**: Image-Text pairs

**Annotation**: Expert-written image descriptions and question-answer pairs generated using LLMs.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- BLEU Score
- ROUGE-L
- Accuracy
- Precision

**Calculation**: Metrics are calculated based on model responses and ground truth comparisons on various tasks.

**Interpretation**: Higher BLEU and ROUGE scores indicate better linguistic accuracy and relevance of responses.

**Baseline Results**: MM-Skin achieves high performance on various VQA and classification tasks.

**Validation**: Evaluated on multiple existing medical datasets and through qualitative assessments.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Accuracy
- Privacy

**Atlas Risks**:
- **Accuracy**: Unrepresentative data
- **Privacy**: Personal information in data

**Demographic Analysis**: The dataset includes demographic attributes like age and gender to evaluate model performance across different groups.

**Potential Harm**: The dataset aims to prevent misdiagnosis in skin disease evaluation.

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: All images are sourced from textbooks, ensuring no personal patient data is included.

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
