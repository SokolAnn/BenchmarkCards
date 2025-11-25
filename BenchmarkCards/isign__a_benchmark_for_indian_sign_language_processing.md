# iSign: A Benchmark for Indian Sign Language Processing

## 📊 Benchmark Details

**Name**: iSign: A Benchmark for Indian Sign Language Processing

**Overview**: iSign proposes a benchmark for Indian Sign Language (ISL) processing by releasing one of the largest ISL-English datasets with more than 118k video-sentence/phrase pairs and introducing multiple NLP-specific tasks.

**Data Type**: video-sentence/phrase pairs

**Domains**:
- Natural Language Processing

**Languages**:
- English
- Indian Sign Language

**Similar Benchmarks**:
- ISLTranslate
- CISLR

**Resources**:
- [Resource](https://exploration-lab.github.io/iSign/)

## 🎯 Purpose and Intended Users

**Goal**: To bridge the gap in resources and benchmark methodologies for Indian Sign Language processing.

**Target Audience**:
- ML Researchers
- Domain Experts

**Tasks**:
- ISL-to-English Translation
- English-to-ISL Pose Generation
- Word/Gloss Recognition
- Word Presence Prediction
- Semantic Similarity Prediction

**Limitations**: The large number of ISL-English sentence pairs makes validation challenging.

## 💾 Data

**Source**: Publicly available YouTube resources: ISLRTC, ISH News, and DEF.

**Size**: 118,228 video-sentence/phrase pairs

**Format**: N/A

**Annotation**: Validated by certified ISL signers on a pro-bono basis.

## 🔬 Methodology

**Methods**:
- Neural Machine Translation
- Dynamic Time Warping
- One-shot Learning

**Metrics**:
- BLEU Score
- ROUGE-L
- Top-1 Accuracy
- Top-5 Accuracy

**Calculation**: Standard translation metrics (e.g., BLEU, ROUGE) were used to evaluate translation tasks.

**Interpretation**: Higher BLEU and ROUGE scores indicate better performance in ISL translation accuracy.

**Baseline Results**: BLEU-4 score is 69.3 for ISL-to-English Translation.

**Validation**: Performed via a small sample validated by certified ISL instructors.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness
- Privacy

**Atlas Risks**:
- **Accuracy**: Data contamination, Unrepresentative data
- **Fairness**: Data bias
- **Privacy**: Personal information in data

**Demographic Analysis**: The dataset focuses on the Indian demographic for the Deaf and Hard of Hearing community.

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: The dataset was created from publicly available resources without violating copyright.

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
