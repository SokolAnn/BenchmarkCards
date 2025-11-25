# VSP (Visual Spatial Planning)

## 📊 Benchmark Details

**Name**: VSP (Visual Spatial Planning)

**Overview**: VSP is introduced to evaluate the spatial planning capabilities of vision language models (VLMs), focusing on tasks that require understanding spatial arrangements of objects and devising action plans in visual scenes.

**Data Type**: question-answering pairs

**Domains**:
- Natural Language Processing
- Computer Vision

**Languages**:
- English

**Similar Benchmarks**:
- MME
- MMMU
- MathVision
- SeedBench
- MM-Vet

**Resources**:
- [GitHub Repository](https://github.com/UCSB-NLP-Chang/Visual-Spatial-Planning)

## 🎯 Purpose and Intended Users

**Goal**: To evaluate and diagnose the spatial planning capabilities of vision language models.

**Target Audience**:
- ML Researchers
- Model Developers

**Tasks**:
- Spatial Planning
- Single Object Perception
- Spatial Relation Perception
- Environment Perception
- Spatial Reasoning

**Limitations**: N/A

## 💾 Data

**Source**: The images and tasks are based on simulations of maze navigation and block-moving tasks developed with tools such as OpenAI Gym and sampled images from the BIRD dataset.

**Size**: 4,400 questions

**Format**: N/A

**Annotation**: N/A

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Accuracy

**Calculation**: Metrics calculated based on correct and incorrect responses to the questions posed in the VSP tasks.

**Interpretation**: A high accuracy indicates better spatial understanding and planning capabilities of the model.

**Baseline Results**: Previous state-of-the-art models were evaluated against the VSP benchmark and demonstrated considerable deficiencies.

**Validation**: The benchmark was validated by testing with multiple models, highlighting their performance across various tasks.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Robustness

**Atlas Risks**:
- **Accuracy**: Poor model accuracy
- **Robustness**

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: MIT License

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
