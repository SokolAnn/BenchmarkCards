# MulCogBench (Multi-modal Cognitive Benchmark Dataset)

## 📊 Benchmark Details

**Name**: MulCogBench (Multi-modal Cognitive Benchmark Dataset)

**Overview**: MulCogBench is a multi-modal cognitive benchmark dataset collected from native Chinese and English participants, which encompasses a variety of cognitive data including subjective semantic ratings, eye-tracking, functional magnetic resonance imaging (fMRI), and magnetoencephalography (MEG). The dataset is used to evaluate the relationship between computational language models and cognitive data.

**Data Type**: text

**Domains**:
- Natural Language Processing

**Languages**:
- Chinese
- English

**Resources**:
- [Resource](N/A)

## 🎯 Purpose and Intended Users

**Goal**: To provide a dataset for evaluating the cognitive processing capabilities of computational language models in relation to human cognitive data.

**Target Audience**:
- ML Researchers
- Cognitive Scientists

**Tasks**:
- Language Modeling
- Cognitive Evaluation

**Limitations**: Cognitive data contains noise and may represent multiple cognitive functions, making direct correlation difficult.

## 💾 Data

**Source**: Collected from native Chinese and English participants across various experiments.

**Size**: 170,331 eye-tracking samples, 672 words in word semantic ratings for Chinese and 535 for English.

**Format**: N/A

**Annotation**: Manual annotation by experts and collected via experiments with human participants.

## 🔬 Methodology

**Methods**:
- Similarity-Encoding Analysis (SEA)

**Metrics**:
- Pearson correlation coefficient

**Calculation**: Computed similarity between cognitive data and embeddings of computational language models.

**Interpretation**: Higher Pearson correlation indicates better encoding of linguistic information by the computational model.

**Baseline Results**: Results show significant correlations between language models and human cognitive data.

**Validation**: Validation through various cognitive modalities and linguistic units.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness

**Atlas Risks**:
- **Accuracy**: Unrepresentative data
- **Fairness**: Data bias

**Demographic Analysis**: Analysis across languages includes both Chinese and English participants.

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: All cognitive data collected under the approval of the Institutional Review Board.

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
