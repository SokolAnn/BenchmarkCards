# OAG-Bench: A Human-Curated Benchmark for Academic Graph Mining

## 📊 Benchmark Details

**Name**: OAG-Bench: A Human-Curated Benchmark for Academic Graph Mining

**Overview**: OAG-Bench is a comprehensive, multi-aspect, and fine-grained human-curated benchmark based on the Open Academic Graph (OAG), covering 10 tasks, 20 datasets, 70+ baselines, and 120+ experimental results to aid in academic graph mining.

**Data Type**: text, tabular

**Domains**:
- Natural Language Processing
- Data Mining

**Languages**:
- English

**Similar Benchmarks**:
- MAG (Microsoft Academic Graph)
- S2ORC

**Resources**:
- [Resource](https://www.aminer.cn/data/)

## 🎯 Purpose and Intended Users

**Goal**: To evaluate and compare algorithms in academic graph mining, thereby accelerating algorithm development in the field.

**Target Audience**:
- ML Researchers
- Industry Practitioners
- Domain Experts

**Tasks**:
- Entity Alignment
- Author Name Disambiguation
- Scholar Profiling
- Entity Tagging
- Concept Taxonomy Completion
- Paper Recommendation
- Reviewer Recommendation
- Academic Question Answering
- Paper Source Tracing
- Academic Influence Prediction

**Limitations**: N/A

## 💾 Data

**Source**: Open Academic Graph (OAG)

**Size**: 1M+ papers across 20 datasets

**Format**: Various formats including CSV and JSON

**Annotation**: Human-annotated datasets for diverse tasks

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics
- Model-based evaluation

**Metrics**:
- Precision
- Recall
- F1 Score
- Mean Average Precision (MAP)

**Calculation**: Metrics calculated based on standard evaluation methods discussed in the paper.

**Interpretation**: Higher scores indicate better performance in the respective tasks.

**Baseline Results**: Various baseline methods across tasks including traditional classifiers and large language models.

**Validation**: Extensive experiments and community evaluations via the OAG-Challenge.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness

**Atlas Risks**:
- **Accuracy**: Unrepresentative data
- **Fairness**: Data bias

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Sensitive attributes were excluded and attributes provided are publicly accessible.

**Data Licensing**: Not Applicable

**Consent Procedures**: All annotators gave informed consent for their inclusion.

**Compliance With Regulations**: Not Applicable
