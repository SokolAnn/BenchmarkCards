# Custom Dataset for Long-Horizon Robotic Stacking with Multimodal Large Language Models

## 📊 Benchmark Details

**Name**: Custom Dataset for Long-Horizon Robotic Stacking with Multimodal Large Language Models

**Overview**: This paper proposes a custom dataset focused on stacking preferences including weight, stability, size, and footprint for fine-tuning large language models (LLMs) in long-horizon robotic stacking tasks involving multimodal inputs.

**Data Type**: multimodal data for robotic stacking tasks

**Domains**:
- Robotics

**Languages**:
- English

**Resources**:
- [Resource](N/A)

## 🎯 Purpose and Intended Users

**Goal**: To utilize multimodal information and large language models for planning long-horizon robotic stacking tasks with latent characteristics.

**Target Audience**:
- Roboticists
- AI Researchers
- ML Practitioners

**Tasks**:
- Robotic Stacking

**Limitations**: N/A

## 💾 Data

**Source**: Physics simulation based on PyBullet

**Size**: Thousands of training examples generated from simulated stacking scenarios

**Format**: N/A

**Annotation**: The data is generated through simulations considering various stacking preferences.

## 🔬 Methodology

**Methods**:
- Simulation-based evaluation
- Fine-tuning on custom dataset
- Real robotic evaluation

**Metrics**:
- Success Rate
- Preference Score
- Success-scaled Score

**Calculation**: Success Rate calculated by the proportion of successful stacking tasks; Preference Score based on compliance with optimal stacking orders; Success-scaled Score is the product of Success Rate and Preference Score.

**Interpretation**: A higher score indicates better performance in successfully completing stacking tasks with consideration for user-defined preferences.

**Baseline Results**: Results compared against prompt-tuned models, showing improvements for fine-tuned models.

**Validation**: Evaluation performed in simulation and on a real robotic system to assess capabilities.

## ⚠️ Targeted Risks

**Risk Categories**:
- Safety
- Accuracy
- Robustness

**Atlas Risks**:
No specific atlas risks defined

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
