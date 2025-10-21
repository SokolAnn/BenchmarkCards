# OntoRock

## 📊 Benchmark Details

**Name**: OntoRock

**Overview**: OntoRock is a benchmark created for evaluating the robustness of Named Entity Recognition (NER) models using natural adversarial examples generated from the OntoNotes dataset.

**Data Type**: text

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Resources**:
- [Resource](https://inklab.usc.edu/rockner)

## 🎯 Purpose and Intended Users

**Goal**: To audit the robustness of named entity recognition (NER) models through adversarial examples.

**Target Audience**:
- ML Researchers
- Model Developers

**Tasks**:
- Named Entity Recognition

**Limitations**: N/A

## 💾 Data

**Source**: Combination of the OntoNotes dataset and adversarial examples generated using the RockNER method.

**Size**: 8,262 test sentences

**Format**: N/A

**Annotation**: Utilizes existing annotated data from OntoNotes for NER tasks.

## 🔬 Methodology

**Methods**:
- Evaluation of NER models using adversarial examples generated via RockNER.
- Comparison of model performance on original vs. OntoRock dataset.

**Metrics**:
- F1 Score
- Precision
- Recall

**Calculation**: F1 score is calculated based on matches between predicted and true entities.

**Interpretation**: Higher scores indicate better robustness against adversarial attacks.

**Baseline Results**: RoBERTa-CRF F1 score drops from 92.4% on OntoNotes to 58.5% on OntoRock.

**Validation**: Evaluation based on performance metrics on both original and adversarial datasets.

## ⚠️ Targeted Risks

**Risk Categories**:
- Robustness
- Accuracy

**Atlas Risks**:
- **Robustness**
- **Accuracy**: Poor model accuracy

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
