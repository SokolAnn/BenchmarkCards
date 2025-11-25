# USDC (User Stance and Dogmatism in Long Conversations)

## 📊 Benchmark Details

**Name**: USDC (User Stance and Dogmatism in Long Conversations)

**Overview**: USDC is a dataset curated from 764 long multi-user Reddit conversation threads for studying user opinion fluctuations, annotated for stance and dogmatism classification tasks.

**Data Type**: text

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- SPINOS

**Resources**:
- [GitHub Repository](https://github.com/mounikamarreddy/USDC)

## 🎯 Purpose and Intended Users

**Goal**: Analyze Reddit conversations to identify user stances on sociopolitical topics and determine their level of dogmatism.

**Target Audience**:
- Natural Language Processing Researchers
- Social Media Analysts
- Market Researchers

**Tasks**:
- User Stance Classification
- User Dogmatism Classification

**Limitations**: None discussed explicitly.

## 💾 Data

**Source**: Reddit conversation threads in English from 22 different subreddits.

**Size**: 764 conversations

**Format**: JSON

**Annotation**: Annotated using majority voting based on LLM outputs from models like GPT-4 and Mistral Large.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated annotations using LLMs
- Majority voting

**Metrics**:
- F1 Score
- Accuracy

**Calculation**: F1 scores are calculated based on predicted stance and dogmatism labels compared to true labels.

**Interpretation**: Higher F1 scores indicate improved model performance in correctly classifying user stances and dogmatism.

**Baseline Results**: Un-fine-tuned models demonstrated an F1 score of ~0.3; fine-tuned models achieved scores improving significantly, e.g., 56.2 for stance.

**Validation**: Inter-annotator agreement evaluated using Cohen's kappa score.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Accuracy
- Privacy

**Atlas Risks**:
- **Fairness**: Data bias
- **Accuracy**: Unrepresentative data
- **Privacy**: Personal information in data

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: User identities are anonymized by not including personal demographic details, focusing on post IDs only.

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
