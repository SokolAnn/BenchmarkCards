# CrystalGym

## 📊 Benchmark Details

**Name**: CrystalGym

**Overview**: CrystalGym is an open-source reinforcement learning environment for crystalline material discovery that benchmarks various RL algorithms based on DFT-calculated properties like band gap, bulk modulus, and density.

**Data Type**: reinforcement learning environment

**Domains**:
- Materials Science

**Languages**:
- English

**Resources**:
- [GitHub Repository](https://github.com/chandar-lab/crystal-gym/)

## 🎯 Purpose and Intended Users

**Goal**: To serve as a test bed for reinforcement learning researchers and material scientists to address real-world design problems in materials discovery using DFT signals.

**Target Audience**:
- Material Scientists
- Reinforcement Learning Researchers

**Tasks**:
- Material Optimization

**Limitations**: N/A

## 💾 Data

**Source**: Specific datasets from the Materials Project database.

**Size**: 7 different cubic crystal structures

**Format**: N/A

**Annotation**: N/A

## 🔬 Methodology

**Methods**:
- Reinforcement Learning Algorithms
- Proximal Policy Optimization (PPO)
- Soft Actor-Critic (SAC)
- Rainbow
- DQN

**Metrics**:
- Sample Efficiency
- Learning Convergence

**Calculation**: Metrics are calculated based on the reward outcome from DFT simulations.

**Interpretation**: The agent's performance is evaluated based on its ability to achieve target property values.

**Validation**: The benchmark assesses performance based on multiple RL algorithms across different crystal configurations.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness

**Atlas Risks**:
- **Accuracy**: Unrepresentative data, Poor model accuracy
- **Fairness**: Data bias

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
