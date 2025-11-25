# InfiniBench

## 📊 Benchmark Details

**Name**: InfiniBench

**Overview**: InfiniBench is a comprehensive benchmark designed to evaluate large multi-modal models in long video understanding, featuring over 1,000 hours of content and 87.7K question-answer pairs that assess grounding-based and reasoning-based skills necessary for understanding long-form videos such as movies and TV shows.

**Data Type**: question-answering pairs

**Domains**:
- Natural Language Processing
- Computer Vision

**Languages**:
- English

**Similar Benchmarks**:
- TVQA
- MovieChat
- LongVU

**Resources**:
- [Resource](https://arxiv.org/abs/2406.19875)

## 🎯 Purpose and Intended Users

**Goal**: To rigorously evaluate the abilities of multi-modal large language models (MLLMs) in comprehending long-form videos.

**Target Audience**:
- ML Researchers
- Model Developers
- Industry Practitioners

**Tasks**:
- Grounding-based skills
- Reasoning-based skills

**Limitations**: N/A

## 💾 Data

**Source**: Over 1,000 hours of video content sourced from movies and TV shows.

**Size**: 87,700 questions

**Format**: JSON

**Annotation**: Manually curated and verified questions targeting multiple cognitive skills.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Accuracy
- F1 Score

**Calculation**: Metrics are calculated based on accuracy for grounding tasks and a scoring system for reasoning tasks.

**Interpretation**: Models are ranked based on their accuracy in answering questions correctly and the quality of their responses.

**Baseline Results**: GPT-4o achieved 47.1% accuracy on grounding skills.

**Validation**: Validated through manual checks to ensure clarity and correctness of Q/A pairs.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Accuracy
- Privacy

**Atlas Risks**:
- **Fairness**: Data bias
- **Accuracy**: Poor model accuracy
- **Privacy**: Personal information in data

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Privacy measures include careful curation of video content and question-answer pairs to avoid personal data inclusion.

**Data Licensing**: Data used from publicly available datasets with compliance for academic research.

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
