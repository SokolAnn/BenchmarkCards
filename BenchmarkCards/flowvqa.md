# FlowVQA

## 📊 Benchmark Details

**Name**: FlowVQA

**Overview**: FlowVQA is a novel benchmark aimed at assessing the capabilities of visual question-answering multimodal language models in reasoning with flowcharts as visual contexts. It consists of 2,272 generated and human-verified flowchart images and 22,413 diverse question-answer pairs.

**Data Type**: question-answering pairs

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- TextVQA
- DocVQA
- MathVista
- ChartQA
- InfoGraphicVQA

**Resources**:
- [Resource](https://flowvqa.github.io/)

## 🎯 Purpose and Intended Users

**Goal**: To evaluate the effectiveness of modern Vision Language Models in reasoning through complex visual and logical tasks using flowcharts.

**Target Audience**:
- ML Researchers
- Domain Experts

**Tasks**:
- Visual Question Answering

**Limitations**: N/A

## 💾 Data

**Source**: Flowcharts generated from WikiHow articles, Instructables DIY blogs, and FloCo code snippets.

**Size**: 2,272 flowchart images, 22,413 question-answer pairs

**Format**: N/A

**Annotation**: Generated with human input and verified by experts to ensure quality.

## 🔬 Methodology

**Methods**:
- Zero-Shot
- Few-Shot
- Fine-Tuning

**Metrics**:
- Accuracy

**Calculation**: Accuracy calculated based on majority voting across multiple evaluator models.

**Interpretation**: Higher accuracy indicates better performance of models in visual reasoning tasks.

**Baseline Results**: The best-performing model achieved 68.42% Majority accuracy across all evaluators.

**Validation**: Extensive evaluation was conducted using both open-source and proprietary VLMs.

## ⚠️ Targeted Risks

**Risk Categories**:
- Fairness
- Accuracy

**Atlas Risks**:
- **Fairness**: Data bias
- **Accuracy**: Unrepresentative data

**Demographic Analysis**: N/A

**Potential Harm**: Potential for biased model evaluations based on visual logic and reasoning capabilities.

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
