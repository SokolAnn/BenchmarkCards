# GLIMPSE

## 📊 Benchmark Details

**Name**: GLIMPSE

**Overview**: GLIMPSE is a benchmark specifically designed to evaluate whether large vision-language models (LVLMs) can genuinely think with videos, emphasizing comprehensive video understanding beyond static image cues.

**Data Type**: video and question-answering pairs

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Resources**:
- [GitHub Repository](https://github.com/aiming-lab/GLIMPSE)

## 🎯 Purpose and Intended Users

**Goal**: To evaluate the video understanding capabilities of large vision-language models, focusing on deep reasoning content through visual-centric questions.

**Target Audience**:
- ML Researchers
- Industry Practitioners
- Model Developers

**Tasks**:
- Video Question Answering

**Limitations**: The dataset’s focus on pre-selected video categories may underrepresent niche scenarios, and the multiple-choice format simplifies real-world reasoning.

## 💾 Data

**Source**: 3,269 videos curated from various sources, along with 4,342 high-quality question pairs manually annotated.

**Size**: 3,269 videos

**Format**: Video

**Annotation**: Manually created by researchers proficient in English and converted to multiple-choice format using GPT-4o API.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Accuracy

**Calculation**: Accuracy is calculated based on the proportion of correctly answered questions across various categories.

**Interpretation**: A higher accuracy indicates better performance in understanding and reasoning with video content.

**Validation**: The benchmark was validated through comparison against human performance results.

## ⚠️ Targeted Risks

**Risk Categories**:
- Fairness
- Accuracy
- Robustness

**Atlas Risks**:
No specific atlas risks defined

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
