# GUIDE (Graphical User Interface Data for Execution)

## 📊 Benchmark Details

**Name**: GUIDE (Graphical User Interface Data for Execution)

**Overview**: GUIDE is a novel dataset tailored for the advancement of Multimodal Large Language Model (MLLM) applications, particularly focusing on Robotic Process Automation (RPA) use cases. It includes diverse data from various websites, each data entry containing an image, a task description, the last action taken, CoT, and the next action to be performed.

**Data Type**: multimodal

**Domains**:
- Natural Language Processing
- Robotics

**Languages**:
- English

**Resources**:
- [Resource](https://huggingface.co/datasets/SuperAGI/GUIDE)
- [GitHub Repository](https://github.com/superagi/GUIDE)

## 🎯 Purpose and Intended Users

**Goal**: To facilitate research and development in the realm of LLMs for graphical user interfaces, particularly in tasks related to RPA.

**Target Audience**:
- ML Researchers
- Industry Practitioners
- Model Developers
- Domain Experts

**Tasks**:
- Next Action Prediction
- Action Grounding

**Limitations**: LIMITED DOMAIN SCOPE; ANNOTATION BIAS; INTERFACE DYNAMICS AND UPDATES; SIMULATED ENVIRONMENT LIMITATIONS; REAL-WORLD INTERACTION COMPLEXITY; EXCEPTION AND ERROR HANDLING; SCALABILITY OF DATA COLLECTION.

## 💾 Data

**Source**: Data collected from various websites including Apollo, Gmail, Calendar, and Canva using the NEXTAG tool.

**Size**: N/A

**Format**: N/A

**Annotation**: Annotated by multiple annotators using an in-house tool to ensure diverse design representation and accurate action grounding.

## 🔬 Methodology

**Methods**:
- Automated metrics
- Human evaluation

**Metrics**:
- Accuracy
- Grounding accuracy

**Calculation**: Metrics are calculated based on the model's performance in task prediction and grounding tasks compared to baseline models.

**Interpretation**: A higher accuracy indicates better predictive and grounding capabilities of the RPA models.

**Baseline Results**: V-Zen achieved an accuracy of 93.2% in next action prediction and 89.7% in grounding tasks.

**Validation**: Validated through rigorous quality checks and comparisons against baseline models.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Safety
- Privacy
- Robustness
- Fairness
- Accuracy

**Atlas Risks**:
- **Accuracy**: Unrepresentative data
- **Fairness**: Data bias
- **Privacy**: Personal information in data

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
