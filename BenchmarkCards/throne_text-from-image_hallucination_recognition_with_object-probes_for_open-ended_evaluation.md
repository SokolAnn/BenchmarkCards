# THRONE (Text-from-image Hallucination Recognition with Object-probes for open-ended Evaluation)

## 📊 Benchmark Details

**Name**: THRONE (Text-from-image Hallucination Recognition with Object-probes for open-ended Evaluation)

**Overview**: THRONE establishes an accurate and accessible benchmark to quantitatively evaluate object hallucinations in free-form responses, leveraging language models to judge the existence of Type I hallucinations.

**Data Type**: text

**Domains**:
- Natural Language Processing
- Computer Vision

**Languages**:
- English

**Similar Benchmarks**:
- POPE
- CHAIR

**Resources**:
- [GitHub Repository](https://github.com/amazon-science/THRONE)

## 🎯 Purpose and Intended Users

**Goal**: To provide a framework for evaluating Type I hallucinations in large vision-language models by employing multiple language models and a voting mechanism.

**Target Audience**:
- ML Researchers
- Industry Practitioners
- Model Developers

**Tasks**:
- Image Captioning
- Object Detection

**Limitations**: N/A

## 💾 Data

**Source**: COCO dataset (Common Objects in Context)

**Size**: 5,000 images

**Format**: JSON

**Annotation**: Annotations are derived from COCO with object categories established for evaluation.

## 🔬 Methodology

**Methods**:
- Automated metrics
- Ensemble voting

**Metrics**:
- F0.5 Score
- Precision
- Recall

**Calculation**: Metrics are calculated based on the performance of large vision-language models in detecting object hallucinations. F0.5 Score favors precision over recall.

**Interpretation**: Higher F0.5 scores indicate better performance in minimizing hallucinations in model responses.

**Validation**: THRONE uses a unanimous voting mechanism across multiple language models to ensure robust evaluation.

## ⚠️ Targeted Risks

**Risk Categories**:
- Safety
- Accuracy

**Atlas Risks**:
- **Accuracy**: Poor model accuracy
- **Societal Impact**: Impact on cultural diversity

**Demographic Analysis**: N/A

**Potential Harm**: ['Potential for misinterpretation of generated responses leading to misinformation.']

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
