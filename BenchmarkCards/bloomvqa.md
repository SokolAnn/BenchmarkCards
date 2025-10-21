# BloomVQA

## 📊 Benchmark Details

**Name**: BloomVQA

**Overview**: BloomVQA is a novel Visual Question Answering dataset designed to assess multi-modal comprehension using tasks that reflect different levels of comprehension outlined in Bloom’s Taxonomy. The dataset facilitates systematic evaluation of large vision-language models by categorizing questions based on cognitive skills required as per the taxonomy.

**Data Type**: multiple-choice VQA samples

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Resources**:
- [Resource](https://huggingface.co/datasets/ygong/BloomVQA)

## 🎯 Purpose and Intended Users

**Goal**: The primary objective of BloomVQA is to systematically evaluate multi-modal comprehension capabilities of models on tasks categorized by cognitive complexity following Bloom's Taxonomy.

**Target Audience**:
- ML Researchers
- Model Developers

**Tasks**:
- Visual Question Answering

**Limitations**: N/A

## 💾 Data

**Source**: Collected from Creative Commons resources including StoryWeaver and Book Dash, focusing on picture stories suitable for teaching young children.

**Size**: 1200 examples

**Format**: N/A

**Annotation**: Data samples were annotated through a web-based UI with input gathered from multiple annotators using templates derived from Bloom's Taxonomy.

## 🔬 Methodology

**Methods**:
- Zero-shot experiments
- Model evaluation based on conditional accuracy

**Metrics**:
- Accuracy
- Conditional performance based on task difficulty

**Calculation**: Metrics were calculated based on model performance evaluations through graded tasks categorized by Bloom’s levels.

**Interpretation**: Models demonstrating high consistency in accuracy across Bloom's levels would suggest a comprehension pattern aligned with human behaviors.

**Baseline Results**: GPT-4V achieved an average accuracy of 75.3% on the BloomVQA dataset.

**Validation**: Results were validated through comparisons with human annotator performances and other state-of-the-art models.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness

**Atlas Risks**:
- **Accuracy**: Unrepresentative data
- **Fairness**: Data bias

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Data is collected under Creative Commons (CC BY 4.0) license.

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
