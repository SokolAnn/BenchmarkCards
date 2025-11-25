# PromptCBLUE (Chinese Biomedical Language Understanding Prompt Tuning Benchmark)

## 📊 Benchmark Details

**Name**: PromptCBLUE (Chinese Biomedical Language Understanding Prompt Tuning Benchmark)

**Overview**: PromptCBLUE is a large-scale multi-task prompt tuning benchmark dataset designed for evaluating the multi-task capabilities of Chinese medical language models across various biomedical tasks such as medical entity recognition, text classification, natural language inference, dialogue understanding, and content generation.

**Data Type**: text

**Domains**:
- Natural Language Processing
- Healthcare

**Languages**:
- Chinese

**Similar Benchmarks**:
- CBLUE (Chinese Biomedical Language Understanding Evaluation)

**Resources**:
- [Resource](https://tianchi.aliyun.com/competition/entrance/532084/introduction)
- [GitHub Repository](https://github.com/michael-wzhu/PromptCBLUE)

## 🎯 Purpose and Intended Users

**Goal**: To provide a comprehensive evaluation platform for Chinese biomedical language models and to facilitate the development of applications in the medical domain.

**Target Audience**:
- ML Researchers
- Domain Experts

**Tasks**:
- Medical Entity Recognition
- Medical Text Classification
- Medical Natural Language Inference
- Medical Dialogue Understanding
- Medical Content Generation

**Limitations**: N/A

## 💾 Data

**Source**: The dataset is built by transforming traditional biomedical NLU tasks from the CBLUE benchmark into a prompt-response format.

**Size**: 82,600 examples in total (with specific splits for each task)

**Format**: JSON

**Annotation**: Annotated by human experts, with prompt templates validated by both NLP and medical professionals.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Micro-F1 Score
- Macro-F1 Score
- ROUGE-L

**Calculation**: Metrics are calculated based on the generated outputs compared to the ground truth for each task.

**Interpretation**: Higher scores indicate better performance in extracting information and generating content according to provided tasks.

**Baseline Results**: The evaluation included results from popular Chinese LLMs under different fine-tuning techniques, with comparative performance reported.

**Validation**: The dataset was validated through expert reviews and random sampling of annotations to ensure quality.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Accuracy
- Robustness

**Atlas Risks**:
- **Fairness**: Data bias
- **Accuracy**: Poor model accuracy
- **Robustness**: Hallucination

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
