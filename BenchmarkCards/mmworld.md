# MMWorld

## 📊 Benchmark Details

**Name**: MMWorld

**Overview**: MMWorld is a multi-discipline, multi-faceted multimodal video understanding benchmark designed to evaluate Multimodal Large Language Models (MLLMs) in world modeling through video content. It contains a variety of questions that require different types of reasoning including explanation, counterfactual thinking, and future prediction.

**Data Type**: video question-answering pairs

**Domains**:
- Natural Language Processing
- Computer Vision
- Healthcare
- Science
- Business
- Tech & Engineering
- Gaming
- Sports & Arts

**Languages**:
- English

**Similar Benchmarks**:
- ActivityNet-QA
- MovieQA
- TVQA

**Resources**:
- [GitHub Repository](https://github.com/eric-ai-lab/MMWorld)
- [Resource](https://mmworld-bench.github.io/)

## 🎯 Purpose and Intended Users

**Goal**: To evaluate MLLMs' capabilities in reasoning and interpreting real-world dynamics through multimodal video understanding.

**Target Audience**:
- ML Researchers
- Industry Practitioners

**Tasks**:
- Video Question Answering
- Video Captioning

**Limitations**: N/A

## 💾 Data

**Source**: Videos collected from YouTube and other platforms under Creative Commons licenses.

**Size**: 1,910 videos, 6,627 question-answer pairs

**Format**: JSON

**Annotation**: Human-annotated and synthetic question-answer pairs generated through an automated pipeline.

## 🔬 Methodology

**Methods**:
- Automated metrics
- Human evaluation

**Metrics**:
- Accuracy

**Calculation**: Metrics are calculated based on model performance in answering video-related questions from the dataset.

**Interpretation**: Performance is interpreted based on accuracy percentages of models when answering questions.

**Baseline Results**: GPT-4V achieved a maximum accuracy of 52.3%

**Validation**: The dataset was validated with human evaluation to ensure the quality of the generated questions and answers.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Safety
- Privacy
- Robustness

**Atlas Risks**:
- **Fairness**: Data bias
- **Privacy**: Personal information in data
- **Robustness**: Data poisoning

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: CC BY 4.0

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
