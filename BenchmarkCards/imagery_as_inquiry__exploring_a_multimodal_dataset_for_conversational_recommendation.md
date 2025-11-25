# Imagery as Inquiry: Exploring a Multimodal Dataset for Conversational Recommendation

## 📊 Benchmark Details

**Name**: Imagery as Inquiry: Exploring a Multimodal Dataset for Conversational Recommendation

**Overview**: This paper introduces a multimodal dataset where users express preferences through images to request recommendations for books or music that evoke similar feelings to those images. It supports two recommendation tasks: title generation and multiple-choice selection.

**Data Type**: multimodal

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Resources**:
- [GitHub Repository](https://github.com/granelle/24-multimodal-crs)

## 🎯 Purpose and Intended Users

**Goal**: To evaluate how well AI models understand and provide appropriate recommendations based on multimodal expressions involving images.

**Target Audience**:
- ML Researchers
- Model Developers

**Tasks**:
- Title Generation
- Multiple-Choice Selection

**Limitations**: N/A

## 💾 Data

**Source**: Reddit posts from specific communities requesting recommendations based on images.

**Size**: 1,470 requests and 12,208 items for books; 796 requests and 38,204 items for music.

**Format**: N/A

**Annotation**: Manual inspection to ensure posts are recommendation requests, with item extraction from comments.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Accuracy
- Hit@k

**Calculation**: Metrics were calculated based on model performance on the recommendation tasks.

**Interpretation**: Performance is evaluated using accuracy and how often the generated recommendations include ground truth items.

**Baseline Results**: The overall best model achieved 67% accuracy on a music selection task.

**Validation**: N/A

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness

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
