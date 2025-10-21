# CoverBench

## 📊 Benchmark Details

**Name**: CoverBench

**Overview**: CoverBench is a challenging benchmark focused on verifying language model outputs in complex reasoning settings, providing a diversified evaluation for complex claim verification in various domains with a consistent schema.

**Data Type**: complex claim verification pairs

**Domains**:
- Natural Language Processing
- Finance
- Wikipedia
- Biomedical
- Legal
- Statistics

**Languages**:
- English

**Resources**:
- [Resource](https://huggingface.co/datasets/google/coverbench)

## 🎯 Purpose and Intended Users

**Goal**: To develop models capable of verifying the correctness of complex claims made by large language models.

**Target Audience**:
- ML Researchers
- Model Developers

**Tasks**:
- Claim Verification

**Limitations**: N/A

## 💾 Data

**Source**: Based on a combination of nine diverse datasets designed for complex reasoning tasks.

**Size**: 733 examples

**Format**: JSON, HTML, Markdown

**Annotation**: Manual vetting and model-assisted transformation and validation.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Macro-F1 Score

**Calculation**: Macro-F1 score is calculated based on the binary classification of claims against their grounding contexts.

**Interpretation**: Scores closer to 70 indicate better performance, with performance below 50 indicating a random baseline.

**Baseline Results**: Best models achieve below a 70 Macro-F1 score.

**Validation**: Manual inspection of example solvability and label correctness.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Accuracy

**Atlas Risks**:
No specific atlas risks defined

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
