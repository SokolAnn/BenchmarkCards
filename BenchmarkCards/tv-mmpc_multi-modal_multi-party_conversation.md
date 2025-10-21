# TV-MMPC (Multi-modal Multi-Party Conversation)

## 📊 Benchmark Details

**Name**: TV-MMPC (Multi-modal Multi-Party Conversation)

**Overview**: TV-MMPC is a human-annotated dataset focused on multimodal conversation structure understanding, featuring annotations for speakers, addressees, and side-participants across various video clips, enabling evaluation of conversational role attribution and conversation disentanglement tasks.

**Data Type**: text

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- TVQA

**Resources**:
- [Resource](https://doi.org/10.7910/DVN/4KUKUL)

## 🎯 Purpose and Intended Users

**Goal**: To evaluate and facilitate understanding of multimodal conversation structure in multi-party settings through task-based benchmarks, specifically in conversational role attribution and conversation disentanglement.

**Target Audience**:
- ML Researchers
- Industry Practitioners
- Model Developers

**Tasks**:
- Conversational Role Attribution
- Conversation Disentanglement

**Limitations**: N/A

## 💾 Data

**Source**: The TV-MMPC dataset is constructed from clips of popular TV shows annotated for conversational dynamics, derived from the TVQA dataset.

**Size**: 4,378 annotations for speakers and reply-to relationships, 5,599 addressees, 3,412 side-participants

**Format**: N/A

**Annotation**: Human-annotated, based on defined guidelines for role attribution and conversation threading.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Accuracy
- Set-Based F1

**Calculation**: Metrics are calculated by comparing predicted annotations against the true labels for speakers, addressees, and side-participants using standard classification metrics.

**Interpretation**: High scores indicate better model performance in correctly identifying conversational roles and relationships among utterances.

**Baseline Results**: N/A

**Validation**: The performance of models was validated through comparison against established baselines using precision and recall within the context of conversation structure.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Privacy
- Fairness

**Atlas Risks**:
- **Fairness**: Data bias
- **Privacy**: Personal information in data
- **Accuracy**: Poor model accuracy

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Annotated data is based on publicly available TV shows and does not contain personal information from identifiable individuals.

**Data Licensing**: Data licensing information is not specified beyond its availability via DOIs and open-access repositories.

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
