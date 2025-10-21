# DesignProbe: A Graphic Design Benchmark for Multimodal Large Language Models

## 📊 Benchmark Details

**Name**: DesignProbe: A Graphic Design Benchmark for Multimodal Large Language Models

**Overview**: DesignProbe is a benchmark designed to explore the performance of Multimodal Large Language Models (MLLMs) in the field of graphic design, assessing their capabilities across eight tasks focused on both fine-grained design elements and overall design understanding.

**Data Type**: image and text inputs

**Domains**:
- Computer Vision
- Natural Language Processing

**Languages**:
- English

**Resources**:
- [Resource](N/A)

## 🎯 Purpose and Intended Users

**Goal**: To assess the design capabilities of Multimodal Large Language Models and set a new standard for evaluating their understanding of graphic design.

**Target Audience**:
- ML Researchers
- Design Practitioners

**Tasks**:
- Color Theme Recognition
- Font Extraction
- Negative Space Detection
- Color Meaning Understanding
- Font Style Understanding
- Visual Importance Detection
- Style Classification
- Visual Metaphor Interpretation

**Limitations**: N/A

## 💾 Data

**Source**: Curated and re-annotated datasets including elements from existing datasets like Crello, CTXFont, and others.

**Size**: 200 tasks across eight categories

**Format**: N/A

**Annotation**: Manually annotated by designers and evaluated using models like GPT-4.

## 🔬 Methodology

**Methods**:
- Automatic evaluation with GPT-4
- Manual evaluation by experts

**Metrics**:
- Accuracy

**Calculation**: Performance of MLLMs is measured against human-generated ground truth using GPT-4 as an evaluator.

**Interpretation**: An accuracy score indicating how well the model's output matches the expected answers.

**Baseline Results**: N/A

**Validation**: Evaluation of model performance on a set of tasks with varying difficulty levels.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness
- Robustness

**Atlas Risks**:
- **Accuracy**: Unrepresentative data
- **Fairness**: Data bias
- **Robustness**: Evasion attack

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
