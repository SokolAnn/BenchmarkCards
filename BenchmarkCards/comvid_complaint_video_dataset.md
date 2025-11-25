# ComVID (Complaint Video Dataset)

## 📊 Benchmark Details

**Name**: ComVID (Complaint Video Dataset)

**Overview**: ComVID is a video complaint dataset containing 1,175 complaint videos and the corresponding descriptions, annotated with the emotional state of the complainer, aimed at generating expressive complaints from videos.

**Data Type**: video-text pairs

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Resources**:
- [GitHub Repository](https://github.com/sarmistha-D/CoD-V)

## 🎯 Purpose and Intended Users

**Goal**: To provide a platform for users to articulate complaints through video, improving engagement with e-commerce platforms.

**Target Audience**:
- Researchers
- Industry Practitioners

**Tasks**:
- Complaint Generation

**Limitations**: N/A

## 💾 Data

**Source**: Collected from Amazon review videos focusing on electronic and non-electronic products.

**Size**: 1,175 videos

**Format**: mp4

**Annotation**: Manual annotation by a team of linguists for complaint descriptions and emotional states.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Vader Score
- Complaint Retention Score (CR)
- BLEU Score
- ROUGE

**Calculation**: CR score is calculated as the average of sentiment score, emotion detection, and aspect identification.

**Interpretation**: A higher CR score indicates better retention of complaint nature in the generated complaints.

**Validation**: Validated through multiple phases of expert annotation and human evaluation.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness

**Atlas Risks**:
- **Accuracy**: Unrepresentative data
- **Fairness**: Data bias

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 International License

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
