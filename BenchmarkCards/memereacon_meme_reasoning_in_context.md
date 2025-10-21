# MemeReaCon (Meme Reasoning in Context)

## 📊 Benchmark Details

**Name**: MemeReaCon (Meme Reasoning in Context)

**Overview**: MemeReaCon is a novel benchmark specifically designed to evaluate how Large Vision Language Models (LVLMs) understand memes within their original contexts. It focuses on the interplay between meme images, post text, and community comments, and assesses models on their ability to interpret memes as they function in online environments.

**Data Type**: meme-post-comment pairs

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- HatefulMemes
- MemeCap

**Resources**:
- [Resource](https://arxiv.org/abs/2505.17433)

## 🎯 Purpose and Intended Users

**Goal**: To provide a robust resource for evaluating the contextual reasoning capabilities of LVLMs when interpreting memes.

**Target Audience**:
- ML Researchers
- Model Developers

**Tasks**:
- Context-Meme Interplay Classification
- Comment Stance and Affective Consistent Classification
- Post Connection Generation
- Post Intent Generation

**Limitations**: Annotations are subject to challenges in achieving mutual agreement on connection meaning, and interpretation may vary based on annotator background knowledge.

## 💾 Data

**Source**: Collected from Reddit across five diverse subreddits.

**Size**: 1,565 examples

**Format**: JSON

**Annotation**: Annotated by trained English-speaking experts familiar with internet culture.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Model-based evaluation

**Metrics**:
- Accuracy
- Macro F1 Score
- ROUGE-L

**Calculation**: Metrics calculated based on model performance on classification and generation tasks.

**Interpretation**: Higher scores indicate better model understanding of meme-context relationships.

**Baseline Results**: Performance scores reported for various state-of-the-art LVLMs, with contextual understanding assessed.

**Validation**: Inter-annotator agreement calculated using Fleiss' Kappa.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Safety
- Fairness
- Accuracy

**Atlas Risks**:
- **Fairness**: Data bias
- **Accuracy**: Poor model accuracy

**Demographic Analysis**: Analysis of demographic factors and meme interpretation across different communities.

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Usernames and personal identifiers were anonymized to protect user privacy.

**Data Licensing**: Not Applicable

**Consent Procedures**: Data collected from publicly available Reddit posts, compliant with Reddit's API terms.

**Compliance With Regulations**: Not Applicable
