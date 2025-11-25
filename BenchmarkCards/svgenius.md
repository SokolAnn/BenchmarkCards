# SVGenius

## 📊 Benchmark Details

**Name**: SVGenius

**Overview**: SVGenius is a comprehensive benchmark comprising 2,377 queries across three progressive dimensions: understanding, editing, and generation, designed to evaluate models' capabilities in SVG processing. It is built on real-world data from 24 application domains with systematic complexity stratification.

**Data Type**: question-answering pairs

**Domains**:
- Computer Vision

**Languages**:
- English

**Similar Benchmarks**:
- SVGEditBench
- MMSVG-2M
- VGBench
- SVGBench
- ColorSVG-100K

**Resources**:
- [Resource](https://zju-real.github.io/SVGenius)

## 🎯 Purpose and Intended Users

**Goal**: The primary objective of SVGenius is to establish a systematic evaluation framework for SVG processing capabilities and provide crucial insights for developing more capable vector graphics models.

**Target Audience**:
- ML Researchers
- Model Developers
- Industry Practitioners

**Tasks**:
- Understanding
- Editing
- Generation

**Limitations**: N/A

## 💾 Data

**Source**: Real-world SVG data from IconFont spanning 24 application domains.

**Size**: 927 high-quality SVGs

**Format**: SVG

**Annotation**: Manually reviewed and filtered for semantic clarity.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Accuracy
- Compression Code Ratio (CCR)
- Mean Squared Error (MSE)
- Relative Levenshtein Distance (RLD)

**Calculation**: Metrics are computed based on strict equivalence checks against ground-truth SVGs, comparing model outputs to expected results across numerous editing tasks.

**Interpretation**: High accuracy denotes successful error correction while lower error rates and higher CCR indicate effective optimization and visual fidelity.

**Baseline Results**: Detailed leaderboard results presented in tables forming comparative performance analysis across different model architectures and sizes.

**Validation**: Each task is validated through systematic testing with a diverse range of models.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Safety
- Privacy
- Robustness
- Fairness
- Accuracy

**Atlas Risks**:
- **Fairness**: Data bias
- **Robustness**: Evasion attack
- **Accuracy**: Unrepresentative data

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
