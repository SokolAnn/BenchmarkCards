# WebMMU (Multimodal Multilingual Website Understanding)

## 📊 Benchmark Details

**Name**: WebMMU (Multimodal Multilingual Website Understanding)

**Overview**: WebMMU is a comprehensive benchmark designed to evaluate multimodal large language models (MLLMs) on three core tasks: website visual question answering, code editing involving HTML/CSS/JavaScript, and mockup-to-code generation, across four languages.

**Data Type**: multimodal

**Domains**:
- Natural Language Processing
- Web Development

**Languages**:
- English
- Spanish
- German
- French

**Resources**:
- [Resource](https://webmmu-paper.github.io)

## 🎯 Purpose and Intended Users

**Goal**: To provide a unified evaluation framework for assessing MLLMs in real-world web understanding and task automation.

**Target Audience**:
- ML Researchers
- Web Developers
- Industry Practitioners

**Tasks**:
- Website Visual Question Answering
- Mockup2Code Generation
- Web Code Editing

**Limitations**: N/A

## 💾 Data

**Source**: Diverse webpages curated from the FineWeb dataset and expert annotations.

**Size**: 2059 webpage images, 6102 WebQA samples, 436 Mockup2Code instances, 1602 Web Code Editing cases

**Format**: N/A

**Annotation**: Human-annotated by 127 professionals across multiple continents.

## 🔬 Methodology

**Methods**:
- Human evaluation
- LLM-as-Judge
- Automated metrics

**Metrics**:
- Accuracy
- BLEU
- TreeBLEU
- Functional accuracy

**Calculation**: Metrics calculated based on predefined criteria for semantic accuracy and reasoning completeness.

**Interpretation**: Higher scores indicate better performance on web understanding tasks.

**Validation**: 100% quality assurance through multiple review stages.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Privacy
- Robustness
- Fairness
- Accuracy

**Atlas Risks**:
No specific atlas risks defined

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: All tasks are created using everyday web content and undergo thorough validation.

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
