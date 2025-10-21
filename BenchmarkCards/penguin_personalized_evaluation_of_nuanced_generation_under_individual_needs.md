# PENGUIN (Personalized Evaluation of Nuanced Generation Under Individual Needs)

## 📊 Benchmark Details

**Name**: PENGUIN (Personalized Evaluation of Nuanced Generation Under Individual Needs)

**Overview**: PENGUIN is a benchmark that includes 14,000 scenarios across seven sensitive domains, designed to evaluate personalized safety in large language models (LLMs) by taking into account individual user contexts and emotional states.

**Data Type**: user scenarios with structured attributes

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- MMLU
- HellaSwag
- TruthfulQA

**Resources**:
- [Resource](https://huggingface.co/datasets/wick1d/Personalized_Safety_Data)

## 🎯 Purpose and Intended Users

**Goal**: To benchmark personalized safety in LLMs by evaluating how well these models handle user-specific contexts that may affect response safety.

**Target Audience**:
- ML Researchers
- Safety Researchers
- AI Model Developers

**Tasks**:
- Text Classification
- Sentiment Analysis

**Limitations**: N/A

## 💾 Data

**Source**: Combination of real-world Reddit posts and synthetic examples generated to ensure realism and data variety.

**Size**: 14,000 scenarios

**Format**: N/A

**Annotation**: Structured user profile attributes extracted through a combination of real user submissions and model-guided generation.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Risk Sensitivity
- Emotional Empathy
- User-specific Alignment

**Calculation**: The final Personalized Safety Score is computed as the unweighted average of the three evaluation dimensions.

**Interpretation**: Scores range from 1 (highly unsafe) to 5 (strongly safe) across three dimensions.

**Baseline Results**: N/A

**Validation**: Details regarding validation were drawn from a large-scale reliability analysis indicating strong alignment with human evaluations.

## ⚠️ Targeted Risks

**Risk Categories**:
- Safety
- Fairness
- Accuracy

**Atlas Risks**:
- **Fairness**: Data bias, Output bias
- **Accuracy**: Poor model accuracy

**Demographic Analysis**: N/A

**Potential Harm**: ['Potential for emotional distress among users if safety is not properly addressed.']

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
