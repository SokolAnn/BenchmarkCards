# PUMBENCH

## 📊 Benchmark Details

**Name**: PUMBENCH

**Overview**: PUMBENCH is a benchmark covering product understanding tasks designed to evaluate the performance of Large Vision Language Models (LVLMs) specifically focused on e-commerce product understanding.

**Data Type**: question-answering pairs

**Domains**:
- Natural Language Processing
- Computer Vision

**Languages**:
- English

**Resources**:
- [Resource](https://www.aliexpress.com/PUMBENCH)

## 🎯 Purpose and Intended Users

**Goal**: To assess the capabilities of product understanding across different large vision-language models in the context of e-commerce.

**Target Audience**:
- ML Researchers
- E-commerce platform developers
- Product data analysts

**Tasks**:
- Caption Generation
- Product Category Multiple-Choice Question
- Attribute Inference
- Caption Completion
- Attribute Correction

**Limitations**: While PUMGPT demonstrated superior performance, it still has limitations in improving relevance in the CMC task and generalization due to a limited number of tasks.

## 💾 Data

**Source**: Dataset compiled from AliExpress containing product images, captions, categories, and attributes.

**Size**: 663,000 examples

**Format**: N/A

**Annotation**: A universal hallucination detection framework using multi-expert collaboration to clean the dataset.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- ROUGE-L
- CIDEr
- BLEU Score
- Accuracy
- F1 Score
- Precision
- Recall

**Calculation**: Metrics are calculated based on the performance of PUMGPT and compared with other models across defined tasks.

**Interpretation**: Higher scores in ROUGE and CIDEr indicate better performance in generating captions that align with product attributes.

**Baseline Results**: PUMGPT outperforms five open-source LVLMs and GPT-4V.

**Validation**: Experiments conducted to validate PUMGPT's performance across multiple tasks.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Robustness
- Fairness
- Accuracy

**Atlas Risks**:
No specific atlas risks defined

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
