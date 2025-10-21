# Text-Scene Graph (TSG) Bench

## 📊 Benchmark Details

**Name**: Text-Scene Graph (TSG) Bench

**Overview**: TSG Bench is a benchmark designed to systematically assess large language models' ability to understand and generate scene graphs from textual narratives, evaluating their interpretation and reasoning capabilities.

**Data Type**: text, scene graphs

**Domains**:
- Natural Language Processing
- Computer Vision

**Languages**:
- English

**Similar Benchmarks**:
- Ego-centric Action Scene Graphs (EASG)

**Resources**:
- [Resource](https://tsg-bench.netlify.app)
- [GitHub Repository](https://github.com/docworlds/tsg-bench)

## 🎯 Purpose and Intended Users

**Goal**: To evaluate and improve large language models' abilities in understanding and generating scene graphs from narratives.

**Target Audience**:
- ML Researchers
- Industry Practitioners
- Model Developers

**Tasks**:
- Scene Graph Understanding
- Scene Graph Generation

**Limitations**: Current TSG Bench does not include object attributes or multiple actors in the scene graphs, limiting its complexity.

## 💾 Data

**Source**: Derived from the Ego-centric Action Scene Graphs (EASG) dataset using LLMs and human annotation.

**Size**: 4,289 scene graphs

**Format**: Custom format for scene graphs and narratives

**Annotation**: Generated using a combination of LLM prompts and human validation.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics
- Model-based evaluation

**Metrics**:
- Exact Match (EM) for SGQA
- Precision
- Recall
- F1 Score

**Calculation**: Metrics are calculated based on model performance against ground truth answers or scene graphs.

**Interpretation**: Higher values in metrics indicate better performance in understanding and generating scene graphs.

**Baseline Results**: Human performance serves as a baseline, showing significant gaps in model outputs for scene generation tasks.

**Validation**: The benchmark's tasks were validated through a review process involving human annotators.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness

**Atlas Risks**:
- **Accuracy**: Poor model accuracy
- **Fairness**: Data bias

**Demographic Analysis**: N/A

**Potential Harm**: ['Misrepresentation of scene contexts in generated graphs.', 'Potential biases inherent in scene graph representations.']

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: CC BY 4.0 license for datasets used and generated.

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
