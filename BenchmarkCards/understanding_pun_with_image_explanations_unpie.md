# Understanding Pun with Image Explanations (UNPIE)

## 📊 Benchmark Details

**Name**: Understanding Pun with Image Explanations (UNPIE)

**Overview**: UNPIE is a novel benchmark designed to assess the impact of multimodal inputs in resolving lexical ambiguities, specifically using text-based puns paired with illustrative images. It includes three multimodal challenges: Pun Grounding, Pun Disambiguation, and Pun Reconstruction.

**Data Type**: text-image pairs

**Domains**:
- Natural Language Processing

**Languages**:
- English
- German
- French
- Korean

**Resources**:
- [Resource](https://huggingface.co/datasets/jiwan-chung/VisualPun_UNPIE)
- [GitHub Repository](https://github.com/JiwanChung/VisualPun_UNPIE)

## 🎯 Purpose and Intended Users

**Goal**: To assess machines’ capacity to actively integrate information from visual sources to resolve ambiguity in text, using puns as a testing ground.

**Target Audience**:
- ML Researchers
- Model Developers

**Tasks**:
- Pun Grounding
- Pun Disambiguation
- Pun Reconstruction

**Limitations**: The dataset primarily models lexical ambiguities unique to English and may inadvertently perpetuate cultural biases present in the humor.

## 💾 Data

**Source**: The data is derived from the SemEval 2017 English pun corpus, enhanced with visual annotations and multilingual translations.

**Size**: 1,000 puns

**Format**: JSON

**Annotation**: The pun explanations were generated using a text-to-image model and curated by human annotators.

## 🔬 Methodology

**Methods**:
- Automated metrics
- Human evaluation

**Metrics**:
- Accuracy
- BLEU Score
- BERTScore

**Calculation**: Metrics are calculated based on exact matches with the ground-truth outputs and semantic similarity using BERTScore.

**Interpretation**: A higher accuracy indicates better performance in identifying puns and translating them accurately, while BERTScore correlates with human judgments on semantic alignment.

**Validation**: Evaluations were conducted through a combination of machine-based and human assessments.

## ⚠️ Targeted Risks

**Risk Categories**:
- Fairness
- Accuracy
- Robustness

**Atlas Risks**:
- **Fairness**: Data bias
- **Accuracy**: Unrepresentative data
- **Robustness**: Evasion attack

**Demographic Analysis**: UNPIE includes multilingual aspects aimed at diverse linguistic contexts, but specifics on demographic breakdowns are not provided.

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
