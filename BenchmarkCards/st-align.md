# ST-Align

## 📊 Benchmark Details

**Name**: ST-Align

**Overview**: ST-Align is a dataset proposed for fine-grained spatial-temporal multimodal understanding tasks, containing 4.3 million training samples to evaluate the capabilities of MLLMs on tasks like Spatial-Temporal Video Grounding (STVG), Event Localization and Captioning (ELC), and Spatial Video Grounding (SVG).

**Data Type**: multimodal

**Domains**:
- Natural Language Processing
- Computer Vision

**Languages**:
- English

**Similar Benchmarks**:
- GroundingGPT
- VTimeLLM
- Grounded-VideoLLM

**Resources**:
- [GitHub Repository](https://github.com/appletea233/LLaVA-ST)

## 🎯 Purpose and Intended Users

**Goal**: To evaluate the capabilities of MLLMs in fine-grained spatial-temporal understanding tasks.

**Target Audience**:
- ML Researchers
- Industry Practitioners
- Model Developers

**Tasks**:
- Spatial-Temporal Video Grounding
- Event Localization and Captioning
- Spatial Video Grounding

**Limitations**: N/A

## 💾 Data

**Source**: ST-Align dataset composed of 4.3 million training samples, created and curated for fine-grained spatial-temporal multimodal understanding.

**Size**: 4.3 million samples

**Format**: N/A

**Annotation**: Annotated using a combination of existing datasets and newly created examples for specific fine-grained tasks.

## 🔬 Methodology

**Methods**:
- Evaluation on various tasks like Spatial-Temporal Video Grounding and Event Localization.
- Progressive multi-task training.

**Metrics**:
- Mean Average Precision (MAP)
- Accuracy
- F1 Score

**Calculation**: Metrics are calculated based on task-specific performance evaluations.

**Interpretation**: Higher scores indicate better performance in accurately locating spatial-temporal events in videos.

**Baseline Results**: LLaVA-ST achieved state-of-the-art performance across multiple benchmarks.

**Validation**: N/A

## ⚠️ Targeted Risks

**Risk Categories**:
- Fairness
- Accuracy
- Privacy
- Robustness

**Atlas Risks**:
- **Fairness**: Data bias
- **Accuracy**: Poor model accuracy

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
