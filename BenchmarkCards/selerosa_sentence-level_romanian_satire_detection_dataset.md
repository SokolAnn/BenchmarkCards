# SeLeRoSa (Sentence-Level Romanian Satire Detection Dataset)

## 📊 Benchmark Details

**Name**: SeLeRoSa (Sentence-Level Romanian Satire Detection Dataset)

**Overview**: The first sentence-level dataset for Romanian satire detection for news articles, comprising 13,873 manually annotated sentences spanning various domains, including social issues, IT, science, and movies.

**Data Type**: text

**Domains**:
- Natural Language Processing

**Languages**:
- Romanian

**Resources**:
- [Resource](https://huggingface.co/datasets/unstpb-nlp/SeLeRoSa)

## 🎯 Purpose and Intended Users

**Goal**: To provide a dataset for sentence-level satire detection in Romanian, facilitating research in this area.

**Target Audience**:
- ML Researchers
- Domain Experts

**Tasks**:
- Sentence-Level Classification

**Limitations**: N/A

## 💾 Data

**Source**: Collected from satirical and non-satirical Romanian news outlets using web scraping.

**Size**: 13,873 sentences

**Format**: N/A

**Annotation**: Manually annotated by native Romanian speakers using majority voting.

## 🔬 Methodology

**Methods**:
- Fine-tuning pre-trained language models
- Human evaluation

**Metrics**:
- Accuracy
- F1 Score

**Calculation**: Metrics computed on the test set samples.

**Interpretation**: Accuracy and F1 score indicate the model's performance in detecting satire.

**Baseline Results**: RoGemma 2 9B FT achieved 76.88% accuracy and 80.72% F1 score.

**Validation**: N/A

## ⚠️ Targeted Risks

**Risk Categories**:
- Fairness
- Accuracy

**Atlas Risks**:
No specific atlas risks defined

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Entities in the dataset were anonymized to minimize bias.

**Data Licensing**: CC BY-NC-SA 4.0 license.

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
