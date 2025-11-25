# CAMPHOR Dataset

## 📊 Benchmark Details

**Name**: CAMPHOR Dataset

**Overview**: The CAMPHOR dataset contains multi-agent execution trajectories focused on mobile assistant use cases, annotated to demonstrate how a multi-agent system fetches personal information to solve user queries by breaking down tasks into smaller actions.

**Data Type**: prompt-completion pairs

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Resources**:
- [Resource](N/A)

## 🎯 Purpose and Intended Users

**Goal**: To provide a dataset for training and evaluating on-device Small Language Models (SLMs) in multi-agent planning and personalized query understanding.

**Target Audience**:
- ML Researchers
- Model Developers

**Tasks**:
- Task Completion

**Limitations**: The personalized user query parsing task is restricted to single interactions, oversimplifying the problem space.

## 💾 Data

**Source**: The data is generated using GPT-4o based on a device state and global function definitions to create user queries and their respective function call trajectories.

**Size**: 3,410 queries, resulting in 35,444 prompt-completion pairs

**Format**: N/A

**Annotation**: Annotated with human oversight and simulation of personal device states to capture task completion trajectories.

## 🔬 Methodology

**Methods**:
- End-to-end evaluation on task completion

**Metrics**:
- Tool F1
- Delexicalized Plan F1
- Plan F1

**Calculation**: Metrics are calculated based on the accuracy of function names and parameters in task completion calls.

**Interpretation**: Higher scores indicate better accuracy in executing function calls as per user intent.

**Baseline Results**: Fine-tuned SLMs outperform state-of-the-art LLMs in task completion metrics.

**Validation**: The dataset includes a validation set and metrics were evaluated against both LLM baselines and fine-tuned SLMs.

## ⚠️ Targeted Risks

**Risk Categories**:
- Privacy
- Accuracy

**Atlas Risks**:
- **Privacy**: Personal information in data
- **Accuracy**: Unrepresentative data

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
