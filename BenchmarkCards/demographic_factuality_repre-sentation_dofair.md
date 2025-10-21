# DemOgraphic FActualIty Repre-sentation (DoFaiR)

## 📊 Benchmark Details

**Name**: DemOgraphic FActualIty Repre-sentation (DoFaiR)

**Overview**: DoFaiR is a benchmark to systematically quantify the trade-off between using diversity interventions and preserving demographic factuality in Text-to-Image (T2I) models. It consists of 756 meticulously fact-checked test instances aimed at revealing the factuality tax of various diversity prompts through an automated evidence-supported evaluation pipeline.

**Data Type**: text

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Resources**:
- [GitHub Repository](https://github.com/uclanlp/diverse-factual.git)

## 🎯 Purpose and Intended Users

**Goal**: The primary objective of the benchmark is to measure the trade-off between demographic diversity and factuality in T2I model generations.

**Target Audience**:
- ML Researchers
- Model Developers

**Tasks**:
- Text Classification

**Limitations**: N/A

## 💾 Data

**Source**: Generated data from T2I models and fact-checked demographic information from Wikipedia.

**Size**: 756 entries

**Format**: JSON

**Annotation**: Automated and systematic data construction with retrieval-based fact labeling.

## 🔬 Methodology

**Methods**:
- Automated metrics
- Model-based evaluation

**Metrics**:
- Dominant Demographic Accuracy (DDA)
- Involved Demographic Accuracy (IDA)
- Involved Demographic F-1 Score (IDF)
- Factual Diversity Divergence (FDD)

**Calculation**: Metrics are calculated based on comparisons between the generated demographic distributions and the ground truth distributions regarding racial and gender traits.

**Interpretation**: Higher scores in DDA, IDA, and IDF indicate better adherence to factual demographic distributions, whereas lower FDD indicates closer alignment to ground truth demographic diversity.

**Validation**: Human verification confirmed high quality of collected data with an overall average factual correctness of 92.92%.

## ⚠️ Targeted Risks

**Risk Categories**:
- Fairness
- Accuracy

**Atlas Risks**:
No specific atlas risks defined

**Demographic Analysis**: The benchmark includes both race-related and gender-related demographic assessments.

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
