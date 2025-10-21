# MathFish

## 📊 Benchmark Details

**Name**: MathFish

**Overview**: MathFish is a dataset that consists of 9.9K human-written math problems labeled with 385 K-12 U.S. curriculum standards, allowing for the evaluation of language models' abilities to assess math problem standards alignment.

**Data Type**: math problems

**Domains**:
- Education

**Languages**:
- English

**Similar Benchmarks**:
- GSM8k

**Resources**:
- [GitHub Repository](https://github.com/allenai/mathfish)
- [Resource](https://huggingface.co/datasets/allenai/mathfish)

## 🎯 Purpose and Intended Users

**Goal**: The goal is to evaluate language models' mathematical reasoning abilities based on their ability to align math problems with educational standards.

**Target Audience**:
- ML Researchers
- Educators
- Curriculum Developers

**Tasks**:
- Verification of problem alignment with standards
- Tagging problems with relevant standards

**Limitations**: N/A

## 💾 Data

**Source**: Curated from open educational resources such as Illustrative Mathematics and Fishtank Learning.

**Size**: 9,923 labeled examples

**Format**: JSON

**Annotation**: Manually annotated by experienced teachers.

## 🔬 Methodology

**Methods**:
- Human evaluation

**Metrics**:
- Accuracy

**Calculation**: Accuracy rates are computed based on the correct identification of alignment between math problems and designated standards.

**Interpretation**: Higher accuracy indicates better alignment of identified standards to the educational goals.

**Validation**: Validated through teacher assessments of generated problems.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Fairness
- Accuracy

**Atlas Risks**:
- **Fairness**: Output bias
- **Accuracy**: Unrepresentative data

**Demographic Analysis**: Demographic factors of teachers involved in validation and annotation are analyzed to understand diversity and representation.

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Data collection methods maintain anonymity of contributors and participants.

**Data Licensing**: The dataset is released under various licenses including Creative Commons Public Domain Dedication License and CC BY 4.0 for specific components.

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
