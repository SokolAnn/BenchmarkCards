# MMR-V: What’s Left Unsaid? A Benchmark for Multimodal Deep Reasoning in Videos

## 📊 Benchmark Details

**Name**: MMR-V: What’s Left Unsaid? A Benchmark for Multimodal Deep Reasoning in Videos

**Overview**: MMR-V is a benchmark designed to evaluate multimodal reasoning capabilities in videos, requiring models to analyze long-range evidence frames and perform deep reasoning beyond surface-level understanding.

**Data Type**: question-answering pairs

**Domains**:
- Natural Language Processing
- Computer Vision

**Languages**:
- English

**Resources**:
- [Resource](https://mmr-v.github.io/)

## 🎯 Purpose and Intended Users

**Goal**: To evaluate the multimodal reasoning capabilities of large language models in the context of video understanding.

**Target Audience**:
- ML Researchers
- Model Developers

**Tasks**:
- Multimodal Reasoning
- Question Answering

**Limitations**: Some categories and themes may be underrepresented, and the dataset primarily includes English videos.

## 💾 Data

**Source**: 317 videos curated from multiple sources, including popular YouTube content.

**Size**: 1,257 tasks

**Format**: Multiple-choice questions

**Annotation**: Manually annotated by experts referencing extensive user understanding.

## 🔬 Methodology

**Methods**:
- Manual evaluation
- Automated metrics

**Metrics**:
- Accuracy

**Calculation**: Average accuracy calculated based on the number of correct responses from evaluated models.

**Interpretation**: The results indicate the percentage of correct answers among the tasks.

**Baseline Results**: Current best accuracy achieved is 52.5% by o4-mini.

**Validation**: Evaluated against various models using both zero-shot and chain-of-thought reasoning.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Safety
- Accuracy

**Atlas Risks**:
No specific atlas risks defined

**Demographic Analysis**: The benchmark does not have extensive demographic breakdowns of content.

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
