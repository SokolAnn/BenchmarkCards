# GeoChain

## 📊 Benchmark Details

**Name**: GeoChain

**Overview**: GeoChain is a large-scale benchmark for evaluating step-by-step geographic reasoning in multimodal large language models (MLLMs), utilizing 1.46 million Mapillary street-level images paired with a 21-step chain-of-thought question sequence.

**Data Type**: image-question-answer pairs

**Domains**:
- Natural Language Processing
- Computer Vision

**Languages**:
- English

**Similar Benchmarks**:
- GeoReasoner
- GAEA

**Resources**:
- [GitHub Repository](https://github.com/sahitiy/geochain)
- [Resource](https://huggingface.co/datasets/sahitiy51/geochain)

## 🎯 Purpose and Intended Users

**Goal**: To provide a comprehensive evaluation framework for assessing geographic reasoning capabilities of MLLMs through a structured diagnostic approach.

**Target Audience**:
- ML Researchers
- Model Developers

**Tasks**:
- Geographic Reasoning
- Visual Question Answering

**Limitations**: The benchmark is built on the Mapillary Street-Level Sequences training split, which may affect the novelty of the visual scenes presented to models.

## 💾 Data

**Source**: Mapillary Street-Level Sequences dataset, augmented with semantic segmentation and locatability scores.

**Size**: 1.46 million images, with 30 million question-answer pairs

**Format**: N/A

**Annotation**: Semantic class labeling and human-inspired locatability score for difficulty stratification.

## 🔬 Methodology

**Methods**:
- Automated metrics
- Diagnostic evaluation

**Metrics**:
- Pass Score
- Haversine Distance

**Calculation**: Pass Score is the average fraction of questions correctly answered across the full 21-step reasoning chain for each image. Haversine Distance measures the shortest distance over the Earth’s surface between predicted and ground-truth coordinates.

**Interpretation**: A higher Pass Score indicates better performance in answering the question chain correctly. Lower Haversine Distance indicates better localization accuracy.

**Baseline Results**: Evaluation of leading MLLMs such as GPT-4.1, Claude 3.7, and Gemini 2.5 variants.

**Validation**: Test-Mini subset of 2088 images manually curated for high quality and challenge.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Accuracy
- Robustness

**Atlas Risks**:
- **Accuracy**: Poor model accuracy
- **Robustness**: Evasion attack

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
