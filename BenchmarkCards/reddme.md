# REDDME

## 📊 Benchmark Details

**Name**: REDDME

**Overview**: REDDME is a new dataset comprising 4,760 posts from mental health subreddits, annotated for the presence and intensity of three support attributes: event, effect, and requirement. It aims to enhance engagement in Online Mental Health Communities by prompting users to share comprehensive support-seeking posts.

**Data Type**: text

**Domains**:
- Healthcare

**Languages**:
- English

**Resources**:
- [Resource](https://huggingface.co/datasets/Shadowking912/REDDME)
- [GitHub Repository](https://github.com/flamenlp/MH-COPILOT)

## 🎯 Purpose and Intended Users

**Goal**: To systematically improve the engagement of users in Online Mental Health Communities by enhancing the quality of their support-seeking posts.

**Target Audience**:
- ML Researchers
- Mental Health Professionals
- AI Developers

**Tasks**:
- Text Classification
- Question Answering

**Limitations**: N/A

## 💾 Data

**Source**: Manually curated posts from mental health subreddits, extended from the BeCOPE dataset.

**Size**: 4,760 posts

**Format**: JSON

**Annotation**: Manual annotation by experts for the spans and intensity of support attributes.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- ROUGE-L
- BLEU Score
- BERTScore
- METEOR

**Calculation**: Metrics are calculated based on the generated questions from the model compared against the benchmark.

**Interpretation**: Higher scores indicate better alignment of questions with the context of the posts, improving engagement.

**Baseline Results**: Results demonstrate significant improvements over various language models, with specific improvements indicated in the paper.

**Validation**: Evaluation conducted through human assessment and quantitative metrics.

## ⚠️ Targeted Risks

**Risk Categories**:
- Fairness
- Privacy
- Accuracy

**Atlas Risks**:
- **Fairness**: Data bias, Output bias
- **Privacy**: Personal information in data
- **Accuracy**: Unrepresentative data

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Focus on ensuring users' posts do not divulge personal identifiable information.

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
