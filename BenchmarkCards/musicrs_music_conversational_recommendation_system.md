# MusiCRS (Music Conversational Recommendation System)

## 📊 Benchmark Details

**Name**: MusiCRS (Music Conversational Recommendation System)

**Overview**: MusiCRS is the first benchmark for audio-centric conversational recommendation that links authentic user conversations from Reddit with corresponding audio tracks. It contains 477 high-quality conversations across diverse genres, enabling evaluation across three input modality configurations: audio-only, query-only, and audio+query (multimodal).

**Data Type**: text

**Domains**:
- Natural Language Processing
- Music Information Retrieval

**Languages**:
- English

**Resources**:
- [Resource](https://huggingface.co/datasets/rohan2810/MusiCRS)
- [GitHub Repository](https://github.com/rohan2810/musiCRS)

## 🎯 Purpose and Intended Users

**Goal**: To advance research in multimodal music recommendation by providing a structured dataset that integrates conversational context with audio content.

**Target Audience**:
- ML Researchers
- Model Developers
- Data Scientists

**Tasks**:
- Conversational Recommendation

**Limitations**: N/A

## 💾 Data

**Source**: Collected from 2.7 million Reddit submissions and 28.5 million comments from various music-oriented subreddits.

**Size**: 477 conversations

**Format**: JSON

**Annotation**: Manually validated by human annotators to ensure relevance and quality.

## 🔬 Methodology

**Methods**:
- Automated metrics

**Metrics**:
- Recall
- nDCG
- MRR

**Calculation**: Metrics are calculated based on ranking tasks across three modalities: audio-only, query-only, and audio+query.

**Interpretation**: Higher metrics indicate better performance in recommending music based on the given conversational context and audio content.

**Baseline Results**: N/A

**Validation**: Validated through a manual filtering and annotation process.

## ⚠️ Targeted Risks

**Risk Categories**:
- Fairness
- Accuracy

**Atlas Risks**:
No specific atlas risks defined

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
