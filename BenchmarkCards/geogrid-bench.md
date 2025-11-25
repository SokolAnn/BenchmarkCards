# GeoGrid-Bench

## 📊 Benchmark Details

**Name**: GeoGrid-Bench

**Overview**: GeoGrid-Bench is designed to evaluate the ability of foundation models to understand geo-spatial data in a grid structure, featuring large-scale, real-world data covering 16 climate variables across 150 locations and extended time frames with approximately 3,200 question-answer pairs.

**Data Type**: question-answering pairs

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- GeoGPT
- GeoBench
- EarthVQA

**Resources**:
- [GitHub Repository](https://github.com/bowen-upenn/GeoGrid_Bench)
- [Resource](https://huggingface.co/datasets/bowen-upenn/GeoGrid_Bench)

## 🎯 Purpose and Intended Users

**Goal**: To evaluate foundation models on their ability to analyze multimodal geo-spatial data and assist scientific research in climate science.

**Target Audience**:
- ML Researchers
- Domain Scientists

**Tasks**:
- Question Answering

**Limitations**: Limited to the United States due to data availability and focuses on geo-spatial data in gridded formats, intentionally excluding Earth observation data.

## 💾 Data

**Source**: ClimRR dataset from Argonne National Laboratory, sampled to cover 150 unique locations across North America.

**Size**: 3,200 question-answer pairs

**Format**: Tabular and image formats

**Annotation**: Expert-curated templates for generating questions based on domain expertise.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Accuracy

**Calculation**: Models' answers are evaluated against ground-truth generated using oracle code.

**Interpretation**: Performance is interpreted based on models' ability to answer questions across different modalities and formats.

**Baseline Results**: Evaluation compares 5 OpenAI models and 6 open-source models across various tasks, with performance metrics detailed in comparing models.

**Validation**: Validation is based on the consistent generation of question instances from curated templates and their evaluation.

## ⚠️ Targeted Risks

**Risk Categories**:
- Fairness
- Accuracy

**Atlas Risks**:
- **Fairness**: Data bias
- **Accuracy**: Poor model accuracy

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
