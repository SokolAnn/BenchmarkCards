# Fine-tuning Language Models for Recipe Generation: A Comparative Analysis and Benchmark Study

## 📊 Benchmark Details

**Name**: Fine-tuning Language Models for Recipe Generation: A Comparative Analysis and Benchmark Study

**Overview**: This research presents an exploration and study of the recipe generation task by fine-tuning various very small language models, focusing on developing robust evaluation metrics and comparing across different language models for recipe generation.

**Data Type**: text

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Resources**:
- [Resource](N/A)

## 🎯 Purpose and Intended Users

**Goal**: To address challenges in recipe generation and allergen substitution through controlled fine-tuning and comprehensive evaluation metrics.

**Target Audience**:
- ML Researchers
- Domain Experts

**Tasks**:
- Recipe Generation

**Limitations**: N/A

## 💾 Data

**Source**: Food.com dataset containing over 180,000 recipes and 700,000 recipe reviews.

**Size**: 231,637 recipes

**Format**: Raw text files

**Annotation**: Standardization of ingredient formats and measurements

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- BLEU
- ROUGE
- Ingredient Coverage
- Step Complexity
- Recipe Coherence

**Calculation**: Metrics calculated based on traditional and domain-specific evaluation methods.

**Interpretation**: Scores range from 0 to 1; higher scores indicate better quality in generated recipes.

**Baseline Results**: SmolLM and Phi-2 models were evaluated with traditional NLP metrics.

**Validation**: Evaluation performed on 500 generated recipes from the test set.

## ⚠️ Targeted Risks

**Risk Categories**:
- Fairness
- Accuracy

**Atlas Risks**:
No specific atlas risks defined

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
