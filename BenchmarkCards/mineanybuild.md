# MineAnyBuild

## 📊 Benchmark Details

**Name**: MineAnyBuild

**Overview**: MineAnyBuild is a novel benchmark built on the Minecraft game, which aims to evaluate the spatial planning capabilities of open-world AI agents. It consists of 4,000 curated tasks and evaluates dimensions including spatial understanding, spatial reasoning, creativity, and spatial commonsense.

**Data Type**: executable spatial plans and visual question-answer pairs

**Domains**:
- Artificial Intelligence
- Gaming

**Languages**:
- English

**Resources**:
- [Resource](https://mineanybuild.github.io/)
- [Resource](https://huggingface.co/datasets/SaDil/MineAnyBuild)

## 🎯 Purpose and Intended Users

**Goal**: To benchmark the spatial planning evaluation for open-world AI agents in the Minecraft game, enhancing the research in spatial intelligence.

**Target Audience**:
- AI Researchers
- Game Developers
- Model Developers

**Tasks**:
- Executable Spatial Plan Generation
- Spatial Understanding
- Spatial Reasoning
- Creativity
- Spatial Commonsense

**Limitations**: N/A

## 💾 Data

**Source**: Curated from various player-generated content on the Internet, including GrabCraft and Minecraft Official Wiki.

**Size**: 4,000 tasks

**Format**: JSON

**Annotation**: Annotated by human reviewers and MLLMs

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Accuracy
- Creativity Score
- Completeness Score

**Calculation**: Scores are calculated based on weighted formulas that consider various evaluation dimensions.

**Interpretation**: The final scores reflect the ability of AI agents to execute spatial planning and reasoning in a 3D environment.

**Baseline Results**: Performance details for several MLLM-based agents provided.

**Validation**: Tasks were validated through testing against existing MLLM models and various parameters were adjusted to ensure reliability.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness
- Robustness

**Atlas Risks**:
No specific atlas risks defined

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: CC BY-NC-SA 4.0

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
