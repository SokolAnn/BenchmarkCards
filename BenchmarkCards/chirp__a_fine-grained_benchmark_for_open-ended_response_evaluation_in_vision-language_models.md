# CHIRP: A Fine-Grained Benchmark for Open-Ended Response Evaluation in Vision-Language Models

## 📊 Benchmark Details

**Name**: CHIRP: A Fine-Grained Benchmark for Open-Ended Response Evaluation in Vision-Language Models

**Overview**: CHIRP is a hybrid evaluation benchmark developed for assessing Vision-Language Models (VLMs), featuring 104 open-ended questions that require complex and creative responses. It combines human evaluations and automated metrics for more robust assessments.

**Data Type**: open-ended question-response pairs

**Domains**:
- Natural Language Processing
- Computer Vision

**Languages**:
- English

**Similar Benchmarks**:
- VQA (Visual Question Answering)
- GQA
- TextVQA
- MM-Vet

**Resources**:
- [Resource](https://huggingface.co/datasets/Anonymous1234565/CHIRP)

## 🎯 Purpose and Intended Users

**Goal**: To provide a comprehensive evaluation framework that captures nuanced differences in model performance by focusing on open-ended responses.

**Target Audience**:
- Researchers in AI
- Model Developers
- Practitioners in VLM evaluations

**Tasks**:
- Open-Ended Response Evaluation

**Limitations**: The benchmark is limited to 104 questions, which may restrict comprehensive evaluations across a wider model variety.

## 💾 Data

**Source**: Generated dataset using GPT-4 for question formulation and DALL-E 3 for image generation.

**Size**: 104 questions

**Format**: N/A

**Annotation**: Manual refinement of questions and image descriptions combined with AI-generated content.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics
- Model-based evaluation

**Metrics**:
- Elo Scores

**Calculation**: Elo scores based on pairwise comparisons of model responses.

**Interpretation**: Higher Elo scores indicate better perceived performance based on evaluators' judgments.

**Baseline Results**: Evaluation against existing benchmarks like VQA, GQA, TextVQA.

**Validation**: Human evaluations across various criteria were utilized to validate model rankings.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Accuracy

**Atlas Risks**:
- **Accuracy**: Unrepresentative data, Poor model accuracy
- **Fairness**: Data bias

**Demographic Analysis**: Evaluation data includes diverse participant demographics.

**Potential Harm**: Potential for evaluative bias based on user preferences.

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Evaluators’ privacy ensured through anonymous participation.

**Data Licensing**: Not Applicable

**Consent Procedures**: Informed consent obtained from all human evaluators before participation.

**Compliance With Regulations**: Not Applicable
