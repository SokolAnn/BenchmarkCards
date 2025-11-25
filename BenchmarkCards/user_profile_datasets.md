# User Profile Datasets

## 📊 Benchmark Details

**Name**: User Profile Datasets

**Overview**: This paper presents two high-quality open-source user profile datasets for profile construction and updating, which serve to evaluate user profile modeling techniques in dynamic settings.

**Data Type**: text

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Resources**:
- [Resource](https://huggingface.co/datasets/Nusrat1234/UserProfileConstruction)
- [Resource](https://huggingface.co/datasets/Nusrat1234/UserProfileUpdate)

## 🎯 Purpose and Intended Users

**Goal**: To provide robust resources for evaluating user profiling techniques in dynamic scenarios and to advance personalization systems.

**Target Audience**:
- ML Researchers
- Industry Practitioners

**Tasks**:
- Profile Construction
- Profile Updating

**Limitations**: N/A

## 💾 Data

**Source**: Wiki People dataset and generated user profiles via LLMs.

**Size**: 42,786 profiles

**Format**: N/A

**Annotation**: Profiles generated using a probabilistic framework and validated through human evaluation.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- F1 Score
- Precision
- Recall

**Calculation**: Metrics calculated using precision, recall, and F1 Score at the user level.

**Interpretation**: Higher precision, recall, and F1 scores indicate better model performance in predicting user profiles.

**Validation**: Manual evaluation of 10% of generated profiles using Fleiss’s kappa for agreement among annotators.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Accuracy

**Atlas Risks**:
- **Accuracy**

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
