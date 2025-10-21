# MFTCXplain (Moral Foundations Twitter Corpus with Explanations)

## 📊 Benchmark Details

**Name**: MFTCXplain (Moral Foundations Twitter Corpus with Explanations)

**Overview**: MFTCXplain is a multilingual benchmark dataset for evaluating the moral reasoning of LLMs via hate speech multi-hop explanations using Moral Foundation Theory (MFT). It comprises 3,000 tweets across Portuguese, Italian, Persian, and English, annotated with hate speech labels, moral categories, and text span-level rationales.

**Data Type**: text

**Domains**:
- Natural Language Processing

**Languages**:
- Portuguese
- Italian
- Persian
- English

**Resources**:
- [GitHub Repository](https://github.com/franciellevargas/MFTCXplain)

## 🎯 Purpose and Intended Users

**Goal**: To evaluate the moral reasoning of large language models through structured hate speech explanations based on expert annotations.

**Target Audience**:
- ML Researchers
- Ethics Researchers
- Sociologists
- NLP Practitioners

**Tasks**:
- Hate Speech Detection
- Moral Sentiment Prediction

**Limitations**: The annotations were produced by a small group of graduate-level annotators, which may limit generalizability.

## 💾 Data

**Source**: Collected tweets from various sources including OLID, datasets on political hate speech, and PHATE for Persian.

**Size**: 3,000 tweets

**Format**: CSV

**Annotation**: Annotated by native speakers with diverse cultural backgrounds regarding hate speech and moral categories.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- F1 Score
- Jaccard Similarity
- BERTScore

**Calculation**: F1 Score is calculated for hate speech classification and moral sentiment prediction, while Jaccard metrics evaluate rationale alignment.

**Interpretation**: F1 score above 0.70 indicates good model performance for hate speech classification, while moral sentiment prediction success is generally considered above 0.35.

**Baseline Results**: GPT-4o and LLaMA-70B were utilized as baseline models for evaluating moral reasoning and hate speech detection.

**Validation**: Empirical evaluation through inter-annotator agreement using Cohen's Kappa and qualitative evaluations during annotation discussions.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Accuracy
- Fairness

**Atlas Risks**:
- **Fairness**: Data bias
- **Accuracy**: Poor model accuracy

**Demographic Analysis**: The dataset reflects socio-political and cultural factors affecting moral judgments, analyzed through annotator profiles.

**Potential Harm**: ['Marginalization of underrepresented languages, potential biases introduced by annotators.']

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: The study involved publicly available social media content and was conducted in accordance with platform policies. Detailed annotator metadata was collected for bias analysis.

**Data Licensing**: Not Applicable

**Consent Procedures**: Annotators provided informed consent and underwent training in best practices for handling sensitive content.

**Compliance With Regulations**: Not Applicable
