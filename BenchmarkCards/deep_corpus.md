# DEEP corpus

## 📊 Benchmark Details

**Name**: DEEP corpus

**Overview**: The DEEP corpus is designed for modeling the social display of the emotion shame, with annotations for different emotion regulation strategies classified during shame-inducing situations.

**Data Type**: video frames with behavior annotations

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Resources**:
- [Resource](https://git.opendfki.de/philipp.mueller/acii24_emotionregulationllm)

## 🎯 Purpose and Intended Users

**Goal**: To investigate how instruction-tuned large language models can classify emotion regulation strategies during shame-eliciting interactions.

**Target Audience**:
- Researchers in Affective Computing
- Psychology students
- Developers of emotion recognition systems

**Tasks**:
- Emotion Regulation Classification

**Limitations**: Due to the complexity of annotations, the corpus is limited in size and variability, focusing specifically on shame regulation.

## 💾 Data

**Source**: The DEEP corpus consisting of recordings from shame-eliciting job interviews.

**Size**: 11535 video frames from 20 expert-annotated videos

**Format**: Video

**Annotation**: Annotations conducted by three trained raters based on participant behavior, verbalized introspection, and context.

## 🔬 Methodology

**Methods**:
- Fine-tuning instruction-tuned Large Language Models
- A/B testing

**Metrics**:
- Accuracy
- F1 Score

**Calculation**: Metrics calculated based on model predictions compared to ground truth labels from the DEEP corpus.

**Interpretation**: Accuracy rates indicate the percentage of correctly classified emotion regulation strategies among all predictions.

**Baseline Results**: The compared models include Bayesian Networks and instruction-tuned Llama2-7B with reported accuracy of 0.84.

**Validation**: Leave-one-subject-out evaluation for assessing generalizability.

## ⚠️ Targeted Risks

**Risk Categories**:
- Privacy
- Fairness
- Accuracy

**Atlas Risks**:
- **Privacy**: Personal information in data
- **Fairness**: Data bias
- **Accuracy**: Poor model accuracy

**Demographic Analysis**: Limited to a small, culturally homogeneous group of participants.

**Potential Harm**: ['Potential exposure of participants to negative emotional states during data collection.']

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Informed consent obtained from participants with measures in place to protect sensitive data.

**Data Licensing**: Received corpus upon request from the authors, ethical review board approved data collection.

**Consent Procedures**: Informed consent acquired prior to participation in the study.

**Compliance With Regulations**: Ethical approval for data processing outlined in the study.
