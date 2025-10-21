# MovieStory101

## 📊 Benchmark Details

**Name**: MovieStory101

**Overview**: MovieStory101 is a new dataset focused on generating dense descriptions for three-minute movie clips, annotated with detailed storyline descriptions, subtitles, and character identity labels for dialogue lines.

**Data Type**: video clips with storyline descriptions and annotations

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- Movie101
- Movie101v2

**Resources**:
- [GitHub Repository](https://github.com/hyc2026/StoryTeller)

## 🎯 Purpose and Intended Users

**Goal**: To provide a comprehensive dataset for evaluating long video descriptions through dense annotations and automated question answering.

**Target Audience**:
- ML Researchers
- Industry Practitioners
- Model Developers

**Tasks**:
- Video Captioning
- Question Answering

**Limitations**: N/A

## 💾 Data

**Source**: Derived from movies in Movie101 and Movie101v2, with curated three-minute clips annotated for storyline and character identification.

**Size**: 5,982 video clips

**Format**: N/A

**Annotation**: Manual annotation by data experts, including storyline descriptions and character identity labels.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Accuracy

**Calculation**: QA accuracy based on responses generated relative to automated questions.

**Interpretation**: Higher accuracy indicates better performance in generating coherent and detailed video descriptions.

**Baseline Results**: Outperformed Gemini-1.5-pro with 9.5% higher accuracy on StoryQA.

**Validation**: Evaluated via StoryQA, focusing on multiple-choice questions related to video content.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Accuracy

**Atlas Risks**:
No specific atlas risks defined

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
