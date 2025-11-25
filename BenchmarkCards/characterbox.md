# CharacterBox

## 📊 Benchmark Details

**Name**: CharacterBox

**Overview**: CharacterBox is a simulation sandbox designed to generate situational fine-grained character behavior trajectories to evaluate the role-playing capabilities of Large Language Models (LLMs) more comprehensively. It consists of a character agent, grounded in psychological and behavioral science, and a narrator agent that coordinates interactions between character agents and environmental changes.

**Data Type**: behavior trajectories

**Domains**:
- Natural Language Processing

**Languages**:
- English
- Chinese

**Similar Benchmarks**:
- RoleBench
- CharacterEval
- InCharacter
- RoleInteract

**Resources**:
- [GitHub Repository](https://github.com/Paitesanshi/CharacterBox)

## 🎯 Purpose and Intended Users

**Goal**: To provide a dynamic, multi-agent interactive virtual world for evaluating the role-playing capabilities of LLMs.

**Target Audience**:
- ML Researchers
- Model Developers

**Tasks**:
- Role-Playing Evaluation

**Limitations**: Runtime efficiency needs improvement for large-scale evaluations.

## 💾 Data

**Source**: Utilizes diverse scenes from well-known novels and scripts for role-playing evaluations.

**Size**: 100 scenes

**Format**: N/A

**Annotation**: Human experts annotate character trajectories based on detailed evaluation criteria.

## 🔬 Methodology

**Methods**:
- Automated evaluation
- Trajectory analysis

**Metrics**:
- Knowledge Accuracy
- Behavioral Accuracy
- Emotional Expression
- Personality Traits
- Immersion
- Adaptability
- Behavioral Coherence

**Calculation**: Each metric is scored from 1 to 5 based on evaluator assessments.

**Interpretation**: Higher scores indicate stronger role-playing performance.

**Baseline Results**: Performance results indicate varying abilities across different LLMs evaluated.

**Validation**: Validated through correlations with expert evaluations.

## ⚠️ Targeted Risks

**Risk Categories**:
- Fairness
- Accuracy

**Atlas Risks**:
- **Fairness**: Data bias
- **Accuracy**: Poor model accuracy

**Demographic Analysis**: Includes evaluations across different character profiles.

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
