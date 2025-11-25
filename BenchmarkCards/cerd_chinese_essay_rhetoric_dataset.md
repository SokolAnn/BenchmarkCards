# CERD (Chinese Essay Rhetoric Dataset)

## 📊 Benchmark Details

**Name**: CERD (Chinese Essay Rhetoric Dataset)

**Overview**: CERD is a manual annotated comprehensive Chinese rhetoric dataset that consists of 4 coarse-grained and 23 fine-grained categories across both form and content levels, aimed at rhetorical understanding and generation in essays.

**Data Type**: text

**Domains**:
- Natural Language Processing

**Languages**:
- Chinese

**Resources**:
- [GitHub Repository](https://github.com/cubenlp/cerd)

## 🎯 Purpose and Intended Users

**Goal**: To improve the understanding and generation of various rhetorical devices in essays, and to provide a benchmark for future research on rhetoric.

**Target Audience**:
- Researcher
- Educators

**Tasks**:
- Rhetoric Classification
- Form Classification
- Content Classification
- Component Extraction
- Rhetoric Generation

**Limitations**: The dataset collected from students may include typographical errors due to limited language proficiency.

## 💾 Data

**Source**: Constructed from essays written by primary and middle school students in real educational settings.

**Size**: 10,349 sentences

**Format**: JSON

**Annotation**: Manual annotation by annotators with backgrounds in Education or Chinese Language and Literature.

## 🔬 Methodology

**Methods**:
- Multi-label classification
- Named Entity Recognition
- Controllable Text Generation

**Metrics**:
- F1 Score
- Precision
- Recall
- Exact Match
- BLEU Score
- ROUGE-L

**Calculation**: Metrics are calculated based on the predictions of the model compared to the ground truth.

**Interpretation**: Higher scores in metrics indicate better performance of the models.

**Validation**: The dataset is validated through inter-annotator agreement and assessments of task performance.

## ⚠️ Targeted Risks

**Risk Categories**:
- Fairness
- Privacy

**Atlas Risks**:
- **Fairness**: Data bias
- **Privacy**: Personal information in data

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Data anonymization procedures were adopted to remove personal information of the authors.

**Data Licensing**: Not Applicable

**Consent Procedures**: All essays in CERD have been authorized for use.

**Compliance With Regulations**: Not Applicable
