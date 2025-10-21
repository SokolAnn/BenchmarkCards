# CANTTALKABOUT THIS

## 📊 Benchmark Details

**Name**: CANTTALKABOUT THIS

**Overview**: The CANTTALKABOUT THIS dataset enables language models to maintain topic relevance in dialogues by including synthetic conversations interspersed with distractor turns designed to divert chatbots from predefined topics.

**Data Type**: synthetic dialogues with distractors

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- MT-Bench

**Resources**:
- [Resource](N/A)

## 🎯 Purpose and Intended Users

**Goal**: To improve the ability of language models to maintain topical coherence in conversations.

**Target Audience**:
- ML Researchers
- Industry Practitioners
- Model Developers

**Tasks**:
- Dialogue Management
- Topic Following

**Limitations**: The dataset is relatively small with a total of 1080 dialogues.

## 💾 Data

**Source**: Synthetic generation using dialogue inpainting techniques.

**Size**: 1080 dialogues

**Format**: N/A

**Annotation**: N/A

## 🔬 Methodology

**Methods**:
- Data generation using LLMs
- Manual evaluation of dialogue quality

**Metrics**:
- Precision
- Recall
- F1 Score

**Calculation**: Metrics are calculated based on model responses to distractors and on-topic turns in the dataset.

**Interpretation**: Higher scores indicate better performance in maintaining focus and handling complex instructions.

**Baseline Results**: Fine-tuned models demonstrated significant improvements over general-purpose models.

**Validation**: N/A

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Bias

**Atlas Risks**:
- **Accuracy**: Poor model accuracy
- **Fairness**: Data bias

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
