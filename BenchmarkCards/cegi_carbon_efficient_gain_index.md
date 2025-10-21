# CEGI (Carbon Efficient Gain Index)

## 📊 Benchmark Details

**Name**: CEGI (Carbon Efficient Gain Index)

**Overview**: CEGI measures the trade-off between model performance and carbon emissions for Small Language Models (SLMs) and Vision Language Models (VLMs) across tasks such as Image Captioning, Visual Question Answering, Dialogue Summarization, and Text-to-SQL conversion.

**Data Type**: text

**Domains**:
- Natural Language Processing
- Computer Vision

**Languages**:
- English

**Resources**:
- [Resource](N/A)

## 🎯 Purpose and Intended Users

**Goal**: To quantify and optimize carbon emissions of AI model training while maintaining high task performance.

**Target Audience**:
- ML Researchers
- AI Practitioners
- Sustainability Advocates

**Tasks**:
- Image Captioning
- Visual Question Answering
- Dialogue Summarization
- Text-to-SQL

**Limitations**: N/A

## 💾 Data

**Source**: Datasets for Image Captioning (artbench-pd-256x256), Visual Question Answering (PathVQA), Dialogue Summarization (SAMSum), Text-to-SQL (synthetic_text_to_sql)

**Size**: 2,200 examples for Image Captioning, 30,000 examples for VQA, 14,000 examples for Dialogue Summarization, 50,000 examples for Text-to-SQL

**Format**: JSON

**Annotation**: Annotated through manual and automated processes.

## 🔬 Methodology

**Methods**:
- Fine-tuning with Low-Rank Adaptation (LoRA)
- Quantization (4-bit, 8-bit)
- Performance evaluation using specific metrics (SPICE, BLEU, ROUGE, Execution Accuracy, Valid Efficiency Score)

**Metrics**:
- SPICE
- BLEU
- ROUGE
- Execution Accuracy (EA)
- Valid Efficiency Score (VES)

**Calculation**: Metrics calculated based on performance comparison of fine-tuned versus base models.

**Interpretation**: Higher scores indicate better performance on defined tasks.

**Baseline Results**: Comparison to GPT-4o used as a baseline for performance across tasks.

**Validation**: Experiments conducted with control measures and multiple runs for reliability.

## ⚠️ Targeted Risks

**Risk Categories**:
- Environmental Impact
- Model Efficiency

**Atlas Risks**:
No specific atlas risks defined

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
