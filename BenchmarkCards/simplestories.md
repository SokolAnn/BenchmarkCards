# SimpleStories

## 📊 Benchmark Details

**Name**: SimpleStories

**Overview**: SimpleStories is a large synthetic story dataset in simple language, consisting of 2 million samples each in English and Japanese, designed for pretraining and interpretability research.

**Data Type**: text

**Domains**:
- Natural Language Processing

**Languages**:
- English
- Japanese

**Similar Benchmarks**:
- TinyStories

**Resources**:
- [Resource](https://huggingface.co/SimpleStories)
- [GitHub Repository](https://github.com/lennart-finke/simple_stories_generate)
- [Resource](https://fi-le.net/simplestories)
- [GitHub Repository](https://github.com/danbraunai/simple_stories_train)

## 🎯 Purpose and Intended Users

**Goal**: To create a dataset suitable for training interpretable language models with diverse grammatical and syntactic patterns while remaining within the realm of simple language and fiction.

**Target Audience**:
- ML Researchers
- Model Developers
- Domain Experts

**Tasks**:
- Text Generation

**Limitations**: N/A

## 💾 Data

**Source**: Synthetic generation using commercial LLMs with template prompts.

**Size**: 2,000,000 samples per language

**Format**: JSON

**Annotation**: Automatically generated based on prompt specifications.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Diversity metrics
- Flesch-Kincaid readability scores

**Calculation**: Metrics are calculated based on the analysis of n-grams and their frequencies from a random sample of the dataset.

**Interpretation**: Higher diversity scores indicate less repetitiveness and more unique content.

**Baseline Results**: SimpleStories models consistently outperform TinyStories across multiple evaluation metrics.

**Validation**: N/A

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Safety

**Atlas Risks**:
No specific atlas risks defined

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
