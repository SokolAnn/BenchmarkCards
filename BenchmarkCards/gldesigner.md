# GLDesigner

## 📊 Benchmark Details

**Name**: GLDesigner

**Overview**: We propose a Vision-Language Model (VLM)-based framework that generates content-aware text logo layouts by integrating multi-modal inputs with user-defined constraints, enabling more flexible and robust layout generation for real-world applications. We introduce two extensive text logo datasets that are five times larger than existing public datasets.

**Data Type**: text logo layouts

**Domains**:
- Natural Language Processing
- Graphic Design

**Languages**:
- English
- Chinese

**Similar Benchmarks**:
- TextLogo
- LayoutGAN

**Resources**:
- [Resource](https://doi.org/10.1145/3746027.3755289)

## 🎯 Purpose and Intended Users

**Goal**: To provide an advanced framework for generating aesthetically pleasing text logos using Vision-Language Models.

**Target Audience**:
- ML Researchers
- Designers
- Industry Practitioners

**Tasks**:
- Layout Generation

**Limitations**: N/A

## 💾 Data

**Source**: Two large-scale text logo datasets: SynTextLogo (containing synthesized logos) and GenTextLogo (curated collection of real-world logos).

**Size**: 17,000 samples

**Format**: JSON

**Annotation**: Pixel-level annotations, detailed layout descriptions, and user-defined constraints.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Fréchet Inception Distance (FID)
- Inception Score (IS)
- Intersection over Union (IoU)
- Visual Balance
- Glyph Ratio Consistency

**Calculation**: Metrics such as FID and IS assess visual quality, while IoU, Visual Balance, and Ratio measure geometric aesthetics and layout adherence.

**Interpretation**: Lower FID and higher IS indicate better quality; IoU, Visual Balance, and Ratio assess the fidelity of the generated logos to their specifications.

**Baseline Results**: Outperforms existing methods on various benchmarks that assess geometric aesthetics and human preferences.

**Validation**: Validate against user-defined constraints and assess layout accuracy through human studies.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness
- Robustness

**Atlas Risks**:
- **Accuracy**: Unrepresentative data
- **Fairness**: Data bias
- **Robustness**: Data poisoning

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
