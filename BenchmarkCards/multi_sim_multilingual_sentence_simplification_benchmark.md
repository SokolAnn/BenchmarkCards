# MULTI SIM (Multilingual Sentence Simplification Benchmark)

## 📊 Benchmark Details

**Name**: MULTI SIM (Multilingual Sentence Simplification Benchmark)

**Overview**: The MULTI SIM benchmark is a collection of 27 resources in 12 distinct languages containing over 1.7 million complex-simple sentence pairs aimed at encouraging research in developing effective multilingual text simplification models and evaluation metrics.

**Data Type**: complex-simple sentence pairs

**Domains**:
- Natural Language Processing

**Languages**:
- English
- French
- German
- Italian
- Japanese
- Russian
- Arabic
- Danish
- Basque
- Slovene
- Urdu
- Brazilian Portuguese
- Spanish

**Resources**:
- [GitHub Repository](https://github.com/XenonMolecule/MultiSim)

## 🎯 Purpose and Intended Users

**Goal**: To provide a comprehensive multilingual benchmark for sentence simplification to enable the development and evaluation of multilingual models and metrics.

**Target Audience**:
- ML Researchers
- Model Developers

**Tasks**:
- Text Simplification

**Limitations**: N/A

## 💾 Data

**Source**: A collection of existing multilingual text simplification corpora unified into a single format.

**Size**: 1,749,056 complex-simple sentence pairs

**Format**: N/A

**Annotation**: Data collected from published literature and various methodologies

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics
- Model-based evaluation

**Metrics**:
- SARI
- BLEU

**Calculation**: SARI is the average of the F1 score for adding, keeping, and deleting n-grams. BLEU evaluates the overlap of generated simplifications with reference simplifications.

**Interpretation**: Higher SARI and BLEU scores indicate better performance in text simplification tasks.

**Baseline Results**: Common baselines include Identity and Truncation methods.

**Validation**: Validation through human evaluation and comparison with baseline results.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Accuracy

**Atlas Risks**:
- **Accuracy**: Unrepresentative data

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
