# SynthBio

## 📊 Benchmark Details

**Name**: SynthBio

**Overview**: SynthBio is a new evaluation set for the WikiBio dataset, composed of structured attribute lists describing fictional individuals, mapped to natural language biographies. This dataset addresses noise and bias issues found in WikiBio by ensuring better balance with respect to gender and nationality.

**Data Type**: structured attribute lists and natural language biographies

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- WikiBio

**Resources**:
- [Resource](https://storage.googleapis.com/gem-benchmark/SynthBio.json)

## 🎯 Purpose and Intended Users

**Goal**: To provide a high-quality labeled text dataset for evaluating models trained on the WikiBio dataset without the issues of memorization and noise present in real-world data.

**Target Audience**:
- ML Researchers
- Model Developers

**Tasks**:
- Structure-to-Text Generation

**Limitations**: N/A

## 💾 Data

**Source**: The dataset consists of synthesized infoboxes and corresponding biographies generated with the aid of large language models and refined by human raters.

**Size**: 2,249 infoboxes and 4,692 biographies

**Format**: JSON

**Annotation**: Human raters modified the generated attribute lists and biographies for factual plausibility, fluency, and formatting.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Model-based evaluation

**Metrics**:
- Coverage
- Faithfulness
- Fluency

**Calculation**: Metrics were calculated based on human evaluations comparing synthesized biographies to their corresponding infoboxes.

**Interpretation**: Higher coverage indicates more attributes from the infobox are mentioned in the biography; higher faithfulness indicates the biography contains only information from the infobox.

**Baseline Results**: N/A

**Validation**: Human raters conducted an evaluation of selected samples from the SynthBio dataset against WikiBio.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Accuracy

**Atlas Risks**:
- **Fairness**: Data bias
- **Accuracy**: Unrepresentative data

**Demographic Analysis**: The dataset is designed to offer equal representation among male, female, and non-binary individuals.

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Apache 2.0

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
