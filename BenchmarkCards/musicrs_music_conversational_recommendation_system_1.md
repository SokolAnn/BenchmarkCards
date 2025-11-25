# MusiCRS (Music Conversational Recommendation System)

## 📊 Benchmark Details

**Name**: MusiCRS (Music Conversational Recommendation System)

**Overview**: MusiCRS is the first benchmark for audio-centric conversational recommendation that links authentic user conversations from Reddit with corresponding audio tracks. It enables evaluation across three input modality configurations: audio-only, query-only, and audio+query (multimodal).

**Data Type**: conversational audio recommendations

**Domains**:
- Natural Language Processing
- Music Information Retrieval

**Languages**:
- English

**Resources**:
- [Resource](https://huggingface.co/datasets/rohan2810/MusiCRS)
- [GitHub Repository](https://github.com/rohan2810/musiCRS)

## 🎯 Purpose and Intended Users

**Goal**: To advance research in multimodal music recommendation by providing a benchmark that incorporates conversational context and audio.

**Target Audience**:
- ML Researchers
- Music Recommendation Developers

**Tasks**:
- Conversational Recommendation
- Audio Recommendation

**Limitations**: N/A

## 💾 Data

**Source**: Large-scale Reddit discussions focused on music.

**Size**: 477 conversations

**Format**: JSON

**Annotation**: Conversations validated by manual review and audio clips sourced from validated YouTube links.

## 🔬 Methodology

**Methods**:
- Automated metrics
- User evaluation

**Metrics**:
- Recall
- nDCG
- Mean Reciprocal Rank (MRR)

**Calculation**: Metrics calculated by aggregating results across different input modalities and models.

**Interpretation**: Higher Recall and nDCG values indicate better recommendation performance.

**Validation**: Manual validation of Reddit conversations ensuring contextual relevance and audio alignment.

## ⚠️ Targeted Risks

**Atlas Risks**:
No specific atlas risks defined

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
