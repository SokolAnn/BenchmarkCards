# StyleEval

## 📊 Benchmark Details

**Name**: StyleEval

**Overview**: StyleEval is a large-scale dataset for stylized dialogue generation, comprising 38 styles and 24,728 dialogues, constructed to enable more engaging and personalized dialogue agents utilizing large language models.

**Data Type**: stylized dialogue examples

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Resources**:
- [Resource](https://arxiv.org/abs/2403.11439)

## 🎯 Purpose and Intended Users

**Goal**: To facilitate the training and evaluation of LLMs in generating stylized dialogues across various stylistic dimensions.

**Target Audience**:
- ML Researchers
- Industry Practitioners
- Model Developers

**Tasks**:
- Stylized Dialogue Generation
- Text Style Transfer

**Limitations**: N/A

## 💾 Data

**Source**: Generated using the GPT-4 model and human quality control.

**Size**: 24,728 dialogues

**Format**: N/A

**Annotation**: Quality checked through rigorous human-led verification.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- BLEU Score
- ROUGE-L
- Relevance
- Coherence
- Style

**Calculation**: Metrics computed based on overlap between generated and reference dialogues.

**Interpretation**: Higher scores indicate better alignment with stylistic and contextual nuances.

**Baseline Results**: Compared against various models including LLaMA and ChatGPT.

**Validation**: The dataset was tested on in-domain and out-of-domain scenarios to validate generalization capabilities.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Fairness
- Accuracy

**Atlas Risks**:
No specific atlas risks defined

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Data sampled from DailyDialog and verified to not contain harmful information.

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
