# ES-KT-24 (Multimodal Knowledge Tracing Benchmark Dataset)

## 📊 Benchmark Details

**Name**: ES-KT-24 (Multimodal Knowledge Tracing Benchmark Dataset)

**Overview**: ES-KT-24 is a novel multimodal Knowledge Tracing dataset for intelligent tutoring systems in educational game contexts, incorporating game-playing videos, synthetically generated question text, and detailed game logs.

**Data Type**: multimodal

**Domains**:
- Natural Language Processing
- Education

**Languages**:
- English
- Indonesian
- Malay

**Resources**:
- [Resource](N/A)

## 🎯 Purpose and Intended Users

**Goal**: To support KT research and broader studies in Learning Analytics by providing a benchmark for knowledge tracing using game data.

**Target Audience**:
- ML Researchers
- Educators
- Learning Analysts

**Tasks**:
- Knowledge Tracing

**Limitations**: The dataset relies solely on duration time as the indicator of answer correctness, which may oversimplify interactions.

## 💾 Data

**Source**: Game logs collected from educational gameplay sessions and synthetic text generated using GPT-4o.

**Size**: 15,032 users and 7,783,466 interactions

**Format**: N/A

**Annotation**: Synthetic question text generated through language models and manual curation.

## 🔬 Methodology

**Methods**:
- 5-fold cross-validation

**Metrics**:
- Area Under the Curve (AUC)
- Accuracy (ACC)

**Calculation**: Performance was evaluated using AUC and Accuracy scores based on KT model predictions.

**Interpretation**: Models are assessed based on their ability to predict student performance on unseen questions.

**Baseline Results**: SimpleKT demonstrated the best performance with an AUC of 0.7366 and ACC of 0.6709.

**Validation**: Results reported as mean values and standard deviations from multiple runs.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Privacy

**Atlas Risks**:
- **Privacy**: Personal information in data
- **Fairness**: Data bias

**Demographic Analysis**: The dataset includes users from various backgrounds and languages.

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Data processed to ensure anonymity of students and prevent personal identification.

**Data Licensing**: Released under the CC BY-NC 4.0 license.

**Consent Procedures**: Gameplay videos were recorded by researchers to protect privacy.

**Compliance With Regulations**: Not Applicable
