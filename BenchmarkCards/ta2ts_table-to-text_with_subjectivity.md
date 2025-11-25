# Ta2TS (Table-to-Text with Subjectivity)

## 📊 Benchmark Details

**Name**: Ta2TS (Table-to-Text with Subjectivity)

**Overview**: The Ta2TS dataset introduces a novel dataset for table-to-text generation tasks, including subjectivity in the generated text. It comprises 3849 table instances from various genres such as sports, financial statements, and weather forecasts, aimed at improving the generation of text from tabular data.

**Data Type**: table-to-text pairs

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Resources**:
- [Resource](https://arxiv.org/abs/2406.10560)

## 🎯 Purpose and Intended Users

**Goal**: To introduce a dataset that captures both objectivity and subjectivity in the context of table-to-text generation, allowing for nuanced interpretations of tabular data.

**Target Audience**:
- ML Researchers
- Industry Practitioners
- Model Developers

**Tasks**:
- Text Generation

**Limitations**: The dataset is restricted to three genres (sports, finance, weather), which may limit the generalizability of findings to other contexts.

## 💾 Data

**Source**: Collected from various sites including Groww, Indian Meteorological Dept., ESPN Cric Info, IPL, and Goal.

**Size**: 3849 instances

**Format**: Raw tables

**Annotation**: Annotated by three trained annotators following detailed guidelines.

## 🔬 Methodology

**Methods**:
- Fine-tuning of T5 models
- Prompting on large language models

**Metrics**:
- BLEU Score
- BERTScore
- Meteor Score
- ROUGE-L
- Parent-FScore

**Calculation**: Metrics are calculated based on the generated texts compared to reference texts according to established NLP evaluation standards.

**Interpretation**: Higher scores indicate better text generation with factual consistency, coherence, and appropriateness of subjectivity capture.

**Baseline Results**: T5-base achieved a BERTScore of 85.15; GPT3.5-turbo reached a Parent-FScore of 0.54.

**Validation**: Five-fold cross-validation was used during the training and evaluation process.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Accuracy

**Atlas Risks**:
- **Accuracy**: Unrepresentative data

**Demographic Analysis**: N/A

**Potential Harm**: ['Potential biases due to limited contextual representation in the dataset.']

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: All collected data were sourced from open-access platforms and contained no personally identifiable information.

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
