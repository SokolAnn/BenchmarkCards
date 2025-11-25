# TEXT2WORLD

## 📊 Benchmark Details

**Name**: TEXT2WORLD

**Overview**: TEXT2WORLD is a novel benchmark based on Planning Domain Definition Language (PDDL), featuring hundreds of diverse domains for evaluating the symbolic world modeling capabilities of large language models (LLMs). It employs multi-criteria, execution-based metrics for robust evaluation.

**Data Type**: PDDL domain specifications

**Domains**:
- Artificial Intelligence

**Languages**:
- English

**Resources**:
- [Resource](https://text-to-world.github.io)

## 🎯 Purpose and Intended Users

**Goal**: To provide a comprehensive evaluation framework for symbolic world modeling capabilities of LLMs.

**Target Audience**:
- ML Researchers
- Model Developers

**Tasks**:
- World Modeling

**Limitations**: N/A

## 💾 Data

**Source**: A collection of 1,801 raw PDDL files from public repositories and planning competitions, filtered to 264 high-quality PDDL domain specifications.

**Size**: 103 domains

**Format**: PDDL (Planning Domain Definition Language)

**Annotation**: Manually annotated natural language descriptions by recruited computer science graduates.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Executability
- Structural Similarity
- Component-wise F1 Scores

**Calculation**: Based on parsing generated PDDL and comparing it to ground truth PDDL.

**Interpretation**: Higher values in metrics indicate better performance in world modeling.

**Baseline Results**: The best-performing LLM, DeepSeek-R1, achieves F1 scores below 60% for both preconditions and effects without error correction.

**Validation**: Multiple validation stages to ensure accuracy and quality of annotations.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Safety
- Accuracy

**Atlas Risks**:
- **Fairness**: Data bias
- **Accuracy**: Poor model accuracy

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: All annotators provided informed consent.

**Compliance With Regulations**: Adheres to ethical guidelines for data collection.
