# Tri-HE

## 📊 Benchmark Details

**Name**: Tri-HE

**Overview**: Tri-HE is a novel Triplet-level Hallucination Evaluation benchmark designed for Large Vision-Language Models to simultaneously measure both object and relation hallucination. It provides a unified framework that evaluates LVLMs by analyzing (object, relation, object) triplets extracted from the models' responses.

**Data Type**: Image and text pairs

**Domains**:
- Vision-Language
- Commonsense reasoning

**Similar Benchmarks**:
- Reefknot

**Resources**:
- [GitHub Repository](https://github.com/wujunjie1998/Tri-HE)

## 🎯 Purpose and Intended Users

**Goal**: To evaluate and analyze hallucinations in Large Vision-Language Models using a unified triplet-level framework.

**Target Audience**:
- Researchers
- Practitioners in AI and machine learning

**Tasks**:
- Evaluating hallucination in LVLMs
- Analyzing the prevalence of relation versus object hallucination

**Limitations**: The dataset construction requires significant resources and time for manual verification.

## 💾 Data

**Source**: GQA dataset

**Size**: 300 images, 1226 questions

**Format**: Triplet-based representation

**Annotation**: Triplets represent relationships and entities derived from the questions and images

## 🔬 Methodology

**Methods**:
- Hallu Q and Hallu I metrics for grading hallucination rates
- Knowledge graph extraction
- GPT-4 based judging for hallucination validation

**Metrics**:
- Hallucination rate at question-level (Hallu Q)
- Hallucination rate at image-level (Hallu I)

**Calculation**: Calculating the proportion of hallucinated triplets in the total triplets extracted from LVLM responses.

**Interpretation**: Lower hallucination rates indicate better alignment between model responses and the actual scene represented in images.

**Validation**: Validation performed using both human judgments and automated methods via GPT-4

## ⚠️ Targeted Risks

**Risk Categories**:
- Misuse of LVLM outputs
- Data quality issues
- Inspection of ethical implications in model outputs

**Atlas Risks**:
- **Accuracy**: Poor model accuracy
- **Fairness**: Data bias
- **Transparency**: Lack of training data transparency
- **Robustness**: Hallucination

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Dataset is based on GQA which is publicly available.

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
