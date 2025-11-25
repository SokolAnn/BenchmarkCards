# CRAFT (Corpus Retrieval and Augmentation for Fine-Tuning)

## 📊 Benchmark Details

**Name**: CRAFT (Corpus Retrieval and Augmentation for Fine-Tuning)

**Overview**: CRAFT is a framework for generating task-specific synthetic datasets grounded in text corpora, requiring only a small set of human-curated few-shot examples to initiate. It retrieves relevant documents and uses instruction-tuned large language models to augment them into task-specific samples for fine-tuning models across various domains.

**Data Type**: text

**Domains**:
- Natural Language Processing
- Healthcare
- Education

**Languages**:
- English

**Similar Benchmarks**:
- Self-Instruct
- Evol-Instruct

**Resources**:
- [GitHub Repository](https://github.com/ziegler-ingo/CRAFT)

## 🎯 Purpose and Intended Users

**Goal**: To efficiently generate high-quality task-specific training datasets for various applications, enabling effective fine-tuning of language models.

**Target Audience**:
- ML Researchers
- Domain Experts
- Industry Practitioners

**Tasks**:
- Question Answering
- Summarization
- Recipe Generation

**Limitations**: Scaling performance for recipe generation noted to be suboptimal.

## 💾 Data

**Source**: Synthetic datasets generated from large-scale web-crawled corpora through corpus retrieval and similarity-based augmentation.

**Size**: 383 million documents

**Format**: JSON

**Annotation**: No manual annotation; relies on few-shot examples for task definition.

## 🔬 Methodology

**Methods**:
- Automated metrics
- Human evaluation
- In-context learning

**Metrics**:
- Accuracy
- Win Rate

**Calculation**: Metrics calculated based on performance evaluations against human-annotated baselines for various tasks.

**Interpretation**: Higher metrics indicate better model performance on specific tasks; win rates represent preference scores for generative outputs.

**Baseline Results**: CRAFT models consistently match or exceed the performance of instruction-tuned baselines in most tasks except for recipe generation.

**Validation**: CRAFT demonstrates robustness to variations in initial few-shot quality during synthetic dataset generation.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Accuracy
- Transparency

**Atlas Risks**:
- **Accuracy**: Unrepresentative data
- **Transparency**: Uncertain data provenance

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: CRAFT utilizes web-crawled corpora with no personally identifiable information; human involvement is minimal.

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
