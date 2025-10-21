# CompoST (Compositional Systematicity Test)

## 📊 Benchmark Details

**Name**: CompoST (Compositional Systematicity Test)

**Overview**: A benchmark for investigating the abilities of LLMs to interpret questions in a compositional manner, generating datasets of varying difficulty based on graph patterns in DBpedia.

**Data Type**: question-query pairs

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Resources**:
- [Resource](https://doi.org/10.5281/zenodo.16312287)

## 🎯 Purpose and Intended Users

**Goal**: To test the compositional systematicity of language models in the context of question answering over linked data.

**Target Audience**:
- ML Researchers
- Domain Experts

**Tasks**:
- Question Answering

**Limitations**: N/A

## 💾 Data

**Source**: Generated from graph patterns in DBpedia with controlled lexicalization.

**Size**: 2803 question-query pairs per dataset (total of 3 datasets giving 8409 question-query pairs)

**Format**: N/A

**Annotation**: Hand-crafted using Lemon lexical entries for verbalization.

## 🔬 Methodology

**Methods**:
- Zero-Shot Prompting
- Few-Shot Prompting
- Fine-Tuning

**Metrics**:
- Accuracy
- Macro F1 Score

**Calculation**: F1 scores calculated based on true positives, false positives, and false negatives from the confusion matrix.

**Interpretation**: Higher F1 scores indicate better ability to interpret questions compositionally.

**Baseline Results**: Best macro F1 score was 0.94 for fine-tuned models on easier datasets.

**Validation**: N/A

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy

**Atlas Risks**:
- **Accuracy**: Poor model accuracy

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
