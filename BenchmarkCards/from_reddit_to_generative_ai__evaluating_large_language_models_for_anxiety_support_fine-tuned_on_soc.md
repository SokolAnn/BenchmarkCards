# From Reddit to Generative AI: Evaluating Large Language Models for Anxiety Support Fine-tuned on Social Media Data

## 📊 Benchmark Details

**Name**: From Reddit to Generative AI: Evaluating Large Language Models for Anxiety Support Fine-tuned on Social Media Data

**Overview**: This study presents a systematic evaluation of LLMs (GPT and Llama) for their potential utility in anxiety support using real user-generated posts from the r/Anxiety subreddit for prompting and fine-tuning.

**Data Type**: question-answering pairs

**Domains**:
- Natural Language Processing
- Healthcare

**Languages**:
- English

**Similar Benchmarks**:
- CounselingBench

**Resources**:
- [Resource](https://arxiv.org/abs/2505.18464)

## 🎯 Purpose and Intended Users

**Goal**: To evaluate Large Language Models for their performance in anxiety support using a domain-specific evaluation framework.

**Target Audience**:
- ML Researchers
- Mental Health Practitioners
- AI Developers

**Tasks**:
- Text Classification
- Sentiment Analysis
- Emotion Recognition

**Limitations**: Fine-tuning can improve linguistic quality but may also increase toxicity and bias.

## 💾 Data

**Source**: User-generated posts from the r/Anxiety subreddit.

**Size**: 26,450 posts

**Format**: JSON

**Annotation**: Manual annotation by licensed mental health professionals.

## 🔬 Methodology

**Methods**:
- Quantitative evaluation
- Qualitative human evaluation
- Statistical analysis

**Metrics**:
- Flesch-Kincaid Grade
- RoUGE
- BLEU Score
- Toxicity
- Empathy Reflection Scores

**Calculation**: Evaluated using a domain-specific framework based on linguistic quality, safety and trustworthiness, and supportiveness using various metrics.

**Interpretation**: Model performance is assessed across linguistic quality, safety, and supportiveness metrics, interpreting higher scores for better performance except for bias and toxicity measures, where lower scores indicate better performance.

**Validation**: Statistical tests like Welch’s ANOVA and Games-Howell post-hoc tests are used to compare model performance.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Safety
- Privacy

**Atlas Risks**:
- **Fairness**: Data bias
- **Accuracy**: Poor model accuracy
- **Robustness**: Data poisoning
- **Privacy**: Exposing personal information

**Demographic Analysis**: Analysis across various demographics including gender and race was conducted.

**Potential Harm**: ['Increased toxicity', 'Bias in responses']

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: The data was anonymized and complies with ethical standards concerning sensitive information.

**Data Licensing**: Not Applicable

**Consent Procedures**: Informed consent from users on r/Anxiety was obtained through publicly available posts.

**Compliance With Regulations**: Not Applicable
