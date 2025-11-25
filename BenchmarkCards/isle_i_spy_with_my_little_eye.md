# Isle (I Spy with My Little Eye)

## 📊 Benchmark Details

**Name**: Isle (I Spy with My Little Eye)

**Overview**: The paper introduces two manually curated datasets, Isle-Bricks and Isle-Dots, for testing visual perspective-taking (VPT) skills in Vision Language Models (VLMs). The datasets focus on measuring how well models can understand viewpoints in various scenarios.

**Data Type**: image-question pairs

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Resources**:
- [Resource](N/A)

## 🎯 Purpose and Intended Users

**Goal**: To evaluate the visual perspective-taking abilities of Vision Language Models and highlight the need for benchmarks specifically designed to capture this capability.

**Target Audience**:
- ML Researchers
- Model Developers

**Tasks**:
- Visual Perspective Taking
- Object Detection

**Limitations**: The datasets currently include a limited number of subjects, which may restrict the analysis of VPT in more complex scenarios.

## 💾 Data

**Source**: Manually curated images and questions specifically designed to test perspective-taking capabilities.

**Size**: 230 pairs of images and questions (100 for Isle-Bricks, 130 for Isle-Dots)

**Format**: Image and question pairs

**Annotation**: Manual annotation by authors ensuring consensus on questions and answers.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Model-based evaluation

**Metrics**:
- Accuracy

**Calculation**: Model performance is calculated based on correct answers to perspective-taking and object detection questions.

**Interpretation**: High accuracy indicates a model's capability in VPT tasks, while low accuracy suggests significant challenges.

**Baseline Results**: Average model performance in baseline object detection tasks was 83% accuracy.

**Validation**: Performance was validated by testing multiple commonly used VLMs.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy

**Atlas Risks**:
No specific atlas risks defined

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
