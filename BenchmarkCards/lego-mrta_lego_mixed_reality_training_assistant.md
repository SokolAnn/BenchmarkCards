# LEGO-MRTA (LEGO Mixed Reality Training Assistant)

## 📊 Benchmark Details

**Name**: LEGO-MRTA (LEGO Mixed Reality Training Assistant)

**Overview**: This dataset comprises multimodal instruction manuals, conversations, and vision question answering, created for fine-grained training in a mixed reality (MR) environment focused on LEGO brick assembly.

**Data Type**: multimodal instruction manuals and conversation pairs

**Domains**:
- Natural Language Processing
- Computer Vision
- Education

**Languages**:
- English

**Resources**:
- [GitHub Repository](https://github.com/Jiahuan-Pei/AutonomousDialogAgent4AugmentedReality)

## 🎯 Purpose and Intended Users

**Goal**: To facilitate fine-grained training in a mixed reality environment for LEGO assembly tasks using AI agents.

**Target Audience**:
- ML Researchers
- Industry Practitioners
- Model Developers
- Domain Experts

**Tasks**:
- Dialogue Generation
- Instruction Following

**Limitations**: The dataset and user requirements generation rely on a simulated process, which may not fully capture real-world complexity.

## 💾 Data

**Source**: Crawled instruction manuals from the LEGO official website.

**Size**: 1,423 conversations

**Format**: Multimodal (Text and Images)

**Annotation**: Automatically generated through interactions guided by LLMs.

## 🔬 Methodology

**Methods**:
- Automated metrics for evaluation and fine-tuning
- Model-based evaluation using existing LLMs

**Metrics**:
- BLEU Score
- ROUGE-L
- Tool Accuracy
- Theme Accuracy

**Calculation**: Evaluation is based on n-grams overlap (BLEU, ROUGE) and entity mention accuracy (ToolACC, ThemeACC).

**Interpretation**: Higher scores indicate better performance in generating human-like responses and successful task execution.

**Validation**: Benchmarking against various open-source LLMs before and after fine-tuning.

## ⚠️ Targeted Risks

**Risk Categories**:
- Fairness
- Accuracy
- Privacy

**Atlas Risks**:
- **Fairness**: Data bias
- **Accuracy**: Unrepresentative data
- **Privacy**: Personal information in data

**Demographic Analysis**: Analysis not explicitly mentioned.

**Potential Harm**: The dependence on simulated data may limit nuanced understanding of real user interactions.

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Users are informed about the use of their data for training and receive consent forms prior to participation.

**Data Licensing**: Not Applicable

**Consent Procedures**: Users must sign consent forms before participating in the MR training.

**Compliance With Regulations**: Not Applicable
