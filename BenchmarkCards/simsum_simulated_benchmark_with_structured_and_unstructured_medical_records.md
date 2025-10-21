# SimSUM (Simulated Benchmark with Structured and Unstructured Medical Records)

## 📊 Benchmark Details

**Name**: SimSUM (Simulated Benchmark with Structured and Unstructured Medical Records)

**Overview**: SimSUM is a benchmark dataset of 10,000 simulated patient records that link unstructured clinical notes with structured background variables. It supports research on clinical information extraction in the presence of tabular background variables.

**Data Type**: simulated patient records (text and tabular data)

**Domains**:
- Healthcare

**Languages**:
- English

**Similar Benchmarks**:
- MIMIC-III
- MIMIC-IV
- BioDEX

**Resources**:
- [GitHub Repository](https://github.com/prabaey/SimSUM)

## 🎯 Purpose and Intended Users

**Goal**: To support research on clinical information extraction, enabling incorporation of structured features into the extraction of clinical concepts from unstructured text.

**Target Audience**:
- ML Researchers
- Healthcare Practitioners

**Tasks**:
- Clinical Information Extraction

**Limitations**: SimSUM is synthetic and does not capture the full complexity or variability of real electronic health records, and should not be used to evaluate clinical model performance.

## 💾 Data

**Source**: Simulated data generated via a Bayesian network and a large language model (GPT-4o).

**Size**: 10,000 simulated patient records

**Format**: JSON

**Annotation**: Automatically annotated with span-level symptom mentions.

## 🔬 Methodology

**Methods**:
- Expert evaluation
- Baseline predictive models

**Metrics**:
- F1 Score

**Calculation**: Metrics calculated as described in the baseline evaluation section.

**Interpretation**: High scores indicate successful integration of structured and unstructured data for clinical information extraction.

**Baseline Results**: The performance of baseline models using SimSUM showed improved accuracy in symptom extraction.

**Validation**: The dataset was validated through expert evaluations and model performance analysis.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Fairness

**Atlas Risks**:
No specific atlas risks defined

**Demographic Analysis**: Not applicable as the dataset is synthetic.

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
