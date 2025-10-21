# CAPE (Cognitive Appraisal theory-based Emotional corpus)

## 📊 Benchmark Details

**Name**: CAPE (Cognitive Appraisal theory-based Emotional corpus)

**Overview**: CAPE is a Chinese dataset designed for appraisal-based emotional generation using large language models. It facilitates the generation of dialogues with contextually appropriate emotional responses by accounting for personal and situational factors. The dataset supports two tasks: emotion prediction and next utterance prediction.

**Data Type**: multi-turn dialogues

**Domains**:
- Natural Language Processing

**Languages**:
- Chinese

**Resources**:
- [Resource](https://arxiv.org/abs/2410.14145)

## 🎯 Purpose and Intended Users

**Goal**: The primary objective of the benchmark is to enable LLMs to generate emotionally appropriate responses in dialogues by utilizing Cognitive Appraisal Theory.

**Target Audience**:
- ML Researchers
- Model Developers

**Tasks**:
- Emotion Prediction
- Next Utterance Prediction

**Limitations**: N/A

## 💾 Data

**Source**: Synthetic dialogues generated using GPT-4-turbo based on the Cognitive Appraisal Theory framework.

**Size**: 2,848 dialogues

**Format**: N/A

**Annotation**: Manual refinement and evaluation by native Chinese-speaking workers.

## 🔬 Methodology

**Methods**:
- Automated metrics
- Human evaluation

**Metrics**:
- Accuracy
- F1 Score
- BLEU Score
- ROUGE-L

**Calculation**: Metrics are calculated based on model outputs compared to ground truth labels for emotion prediction and utterance generation tasks.

**Interpretation**: Results are interpreted in the context of how well generated emotions and utterances align with human emotional expressions.

**Baseline Results**: N/A

**Validation**: Manual evaluation by three raters to assess dialogue quality and emotional alignment.

## ⚠️ Targeted Risks

**Risk Categories**:
- Fairness
- Accuracy

**Atlas Risks**:
No specific atlas risks defined

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Data collection ensured that no personal or sensitive information was included in the dataset.

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
