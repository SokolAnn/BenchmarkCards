# MapIQ

## 📊 Benchmark Details

**Name**: MapIQ

**Overview**: MapIQ is a benchmark dataset comprising 14,706 question-answer pairs designed to gauge the map-reading capabilities of state-of-the-art multimodal large language models (MLLMs) across three map types—choropleth maps, cartograms, and proportional symbol maps—spanning six distinct themes.

**Data Type**: question-answering pairs

**Domains**:
- Natural Language Processing
- Geographical Information Systems

**Languages**:
- English

**Similar Benchmarks**:
- MapQA
- MapWise

**Resources**:
- [Resource](https://osf.io/kp6j4/?view_only=fa2847a270094fd98512127bebd8de87)

## 🎯 Purpose and Intended Users

**Goal**: To provide a diverse and thematically rich benchmark dataset for evaluating the low-level map-reading capabilities of state-of-the-art MLLMs and understanding the influences of thematic content on model performance.

**Target Audience**:
- ML Researchers
- Geospatial Data Analysts
- Data Visualization Experts

**Tasks**:
- Visual Question Answering
- Map Reading

**Limitations**: N/A

## 💾 Data

**Source**: Data sourced from the U.S. Census Bureau, Environmental Protection Agency, FBI Crime Data Explorer, and Centers for Disease Control and Prevention.

**Size**: 14,706 question-answer pairs

**Format**: JSON

**Annotation**: Manually validated questions and answers with ground truth extraction programmatically verified against geospatial metadata.

## 🔬 Methodology

**Methods**:
- Zero-shot prompting
- Human evaluation
- Automated metrics

**Metrics**:
- Accuracy
- F1 Score

**Calculation**: Accuracy for binary questions scored as 100 (correct) or 0 (incorrect), while F1 Score used for MCQ and list-type questions.

**Interpretation**: Higher scores indicate better model performance in accurately answering map-related questions.

**Baseline Results**: Humans outperformed MLLMs by an average margin of 50.35% across all four experimental variables.

**Validation**: Responses validated for consistency and accuracy, ensuring model responses were formatted correctly for evaluation.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Accuracy

**Atlas Risks**:
- **Accuracy**: Unrepresentative data

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
