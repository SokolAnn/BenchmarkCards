# Emotion Reasoning as a Theory of Mind Benchmark for Large Language Models

## 📊 Benchmark Details

**Name**: Emotion Reasoning as a Theory of Mind Benchmark for Large Language Models

**Overview**: This study advances beyond surface-level perceptual features to investigate how large language models (LLMs) reason about others’ emotional states using contextual information, within a Theory-of-Mind (ToM) framework, by curating a specialized ToM evaluation dataset to assess both forward reasoning—from context to emotion—and backward reasoning—from emotion to inferred context.

**Data Type**: vignettes for emotion reasoning tasks

**Domains**:
- Psychology
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- Fantom

**Resources**:
- [GitHub Repository](https://github.com/GerardYeo/ToMEmoReason.git)

## 🎯 Purpose and Intended Users

**Goal**: To evaluate how well LLMs can engage in both forward and backward emotion reasoning.

**Target Audience**:
- ML Researchers
- Psychologists
- Cognitive Scientists

**Tasks**:
- Emotion Reasoning
- Cognitive Appraisal Evaluation

**Limitations**: This study investigates emotion reasoning within a constrained context —the Prisoner’s Dilemma game.

## 💾 Data

**Source**: Curated vignettes derived from psychological decision-making frameworks.

**Size**: 582 vignettes total (432 for forward reasoning, 150 for backward reasoning)

**Format**: Text

**Annotation**: Manual annotation with theoretical grounding in cognitive appraisal theory.

## 🔬 Methodology

**Methods**:
- Evaluation against Theory of Mind tasks
- Statistical analysis of reasoning patterns

**Metrics**:
- Accuracy

**Calculation**: Accuracy calculated based on how well LLMs predict the correct emotional states or appraisals.

**Interpretation**: Higher accuracy reflects better reasoned emotional inference by LLMs.

**Baseline Results**: Gemma 7B achieved an accuracy score of 57.9% on the forward reasoning task.

**Validation**: Training validations were based on systematic manipulation of emotional appraisals in provided vignettes.

## ⚠️ Targeted Risks

**Risk Categories**:
- Fairness
- Bias

**Atlas Risks**:
- **Fairness**: Data bias
- **Accuracy**: Poor model accuracy

**Demographic Analysis**: N/A

**Potential Harm**: Potential misinference of emotional states leading to misunderstandings in applications.

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
