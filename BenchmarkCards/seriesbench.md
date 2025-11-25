# SeriesBench

## 📊 Benchmark Details

**Name**: SeriesBench

**Overview**: SeriesBench is a novel benchmark designed to evaluate Multi-modal Large Language Models' (MLLMs) understanding of narrative-driven drama series through 105 curated series and 28 specialized tasks that require deep narrative comprehension.

**Data Type**: video, subtitles, annotation data

**Domains**:
- Natural Language Processing
- Computer Vision

**Languages**:
- Chinese

**Similar Benchmarks**:
- Video-Bench
- VLM-Eval
- MVBench

**Resources**:
- [GitHub Repository](https://github.com/username/repository)

## 🎯 Purpose and Intended Users

**Goal**: To comprehensively evaluate MLLMs' narrative understanding capabilities across interconnected series.

**Target Audience**:
- ML Researchers
- Model Developers
- Film and Media Studies Scholars

**Tasks**:
- Narrative Understanding
- Character Analysis
- Event Comprehension

**Limitations**: N/A

## 💾 Data

**Source**: 105 selected narrative-driven series from Kuaishou platform containing 1,072 videos.

**Size**: 1,072 videos

**Format**: video, JSON

**Annotation**: Annotations by over 30 professional annotators with rigorous quality checks.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics
- Model-based evaluation

**Metrics**:
- Accuracy
- BLEU Score
- METEOR
- BERTScore F1

**Calculation**: Metrics are derived based on the predicted versus actual outcomes for various question types.

**Interpretation**: Higher accuracy and scores indicate better model performance on the narrative understanding tasks.

**Baseline Results**: Human performance reported at approximately 95.8% accuracy.

**Validation**: Stratified random sampling for training, validation, and test splits.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness
- Robustness

**Atlas Risks**:
- **Accuracy**: Unrepresentative data
- **Fairness**: Data bias
- **Robustness**: Evasion attack

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
