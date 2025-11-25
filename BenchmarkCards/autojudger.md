# AutoJudger

## 📊 Benchmark Details

**Name**: AutoJudger

**Overview**: AutoJudger is an agent-driven framework for efficient benchmarking of multimodal large language models (MLLMs), leveraging Item Response Theory (IRT) for question difficulty estimation and adaptive question selection to reduce evaluation costs while maintaining high accuracy.

**Data Type**: question-answering pairs

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- MMT-Bench
- SEED-Bench
- MMMU

**Resources**:
- [GitHub Repository](https://github.com/IMNearth/AutoJudger)

## 🎯 Purpose and Intended Users

**Goal**: To provide an efficient and reliable method for evaluating multimodal large language models using only a fraction of the full evaluation data.

**Target Audience**:
- ML Researchers
- Model Developers
- Industry Practitioners

**Tasks**:
- Model Evaluation
- Benchmarking

**Limitations**: N/A

## 💾 Data

**Source**: Experimentally evaluated using various multimodal benchmarks including MMT-Bench, SEEDBench, and MMMU.

**Size**: 4 benchmarks

**Format**: N/A

**Annotation**: Question difficulties estimated using Item Response Theory (IRT) based on offline evaluation of models.

## 🔬 Methodology

**Methods**:
- Dynamic Question Selection
- Item Response Theory

**Metrics**:
- Ranking Accuracy

**Calculation**: Ranking accuracy calculated by comparing the predicted model rankings to the ground-truth rankings derived from full benchmark evaluations.

**Interpretation**: Higher ranking accuracy indicates better consistency with full benchmark evaluations.

**Baseline Results**: Tests show AutoJudger achieves 92% ranking consistency using only 4% of benchmark data on MMT-Bench.

**Validation**: Results validated against full benchmark evaluations across multiple experiments.

## ⚠️ Targeted Risks

**Risk Categories**:
- Efficiency
- Accuracy

**Atlas Risks**:
No specific atlas risks defined

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
