# SPhyR: Spatial-Physical Reasoning Benchmark on Material Distribution

## 📊 Benchmark Details

**Name**: SPhyR: Spatial-Physical Reasoning Benchmark on Material Distribution

**Overview**: SPhyR introduces a novel dataset designed to benchmark the physical and spatial reasoning capabilities of Large Language Models (LLM) based on topology optimization, requiring models to reason about optimal material distribution under specific constraints in 2D settings.

**Data Type**: structured grid of material distributions

**Domains**:
- Natural Language Processing
- Engineering

**Languages**:
- English

**Similar Benchmarks**:
- CLEVR
- IntPhys
- Physion
- PIQA

**Resources**:
- [Resource](https://huggingface.co/datasets/philippds/SPhyR)
- [GitHub Repository](https://github.com/philippds/SPhyR)

## 🎯 Purpose and Intended Users

**Goal**: To evaluate the spatial and physical reasoning abilities of large language models based on topology optimization tasks.

**Target Audience**:
- ML Researchers
- Model Developers
- Engineers

**Tasks**:
- Material Distribution Prediction
- Structural Stability Assessment

**Limitations**: N/A

## 💾 Data

**Source**: Generated using McNeel Rhinoceros 8 and the Grasshopper programming environment with the Millipede plugin for topology optimization.

**Size**: 1,296 scenarios

**Format**: Structured grids and task-specific subsets

**Annotation**: Automatically generated through topology optimization simulations.

## 🔬 Methodology

**Methods**:
- Exact Match
- Score
- Normalized Score

**Metrics**:
- Exact Match
- Score
- Normalized Score

**Calculation**: Exact Match is binary based on whether the predicted output matches the ground truth. Score is the ratio of corrected errors. Normalized Score is a capped version of the Score.

**Interpretation**: Higher scores indicate better model performance in predicting material distributions.

**Baseline Results**: N/A

**Validation**: Evaluated state-of-the-art LLMs in a zero-shot setting.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Robustness

**Atlas Risks**:
- **Accuracy**: Poor model accuracy, Unrepresentative data
- **Robustness**: Evasion attack, Data poisoning

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
