# Footstep-set and Impact-set

## 📊 Benchmark Details

**Name**: Footstep-set and Impact-set

**Overview**: Two sound effect datasets designed to evaluate both controllability and sound quality in sound synthesis.

**Data Type**: audio

**Domains**:
- Computer Vision

**Languages**:
- N/A

**Resources**:
- [Resource](https://zenodo.org/records/14286414)

## 🎯 Purpose and Intended Users

**Goal**: To benchmark a similarity-based conditioning method for controllable sound effect synthesis.

**Target Audience**:
- ML Researchers
- Sound Designers
- Audio Engineers

**Tasks**:
- Sound Effect Generation

**Limitations**: The effective range of control is densely concentrated around similarity scores of 0.8 to 1.0.

## 💾 Data

**Source**: Collected from Freesound, categorized into detailed sound effect categories.

**Size**: 2,127 footstep sounds and 1,666 impact sounds

**Format**: N/A

**Annotation**: Categorized based on the material of the contacting surface.

## 🔬 Methodology

**Methods**:
- Regression analysis
- Statistical evaluation metrics

**Metrics**:
- Frechet Audio Distance (FAD)
- Log Spectral Distance (LSD)

**Calculation**: FAD measures the overall similarity between two distributions: the reference dataset and the reconstructed dataset.

**Interpretation**: Lower FAD values indicate better synthesis quality.

**Validation**: Evaluated using objective metrics (FAD, LSD) against existing models.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness

**Atlas Risks**:
No specific atlas risks defined

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
