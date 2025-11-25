# AutoEval-Video

## 📊 Benchmark Details

**Name**: AutoEval-Video

**Overview**: AutoEval-Video is a comprehensive and challenging benchmark designed to evaluate the video understanding capabilities of large vision-language models in open-ended video question answering. It includes 327 open-ended video-question instances across nine skill dimensions and utilizes an LLM-based evaluation approach with instance-specific rules.

**Data Type**: question-answering pairs

**Domains**:
- Natural Language Processing
- Computer Vision

**Languages**:
- English

**Resources**:
- [GitHub Repository](https://github.com/Xiuyuan-Chen/AutoEval-Video)

## 🎯 Purpose and Intended Users

**Goal**: To provide a rigorous evaluation framework for assessing the capabilities of large vision-language models in comprehensively understanding and answering open-ended video questions.

**Target Audience**:
- ML Researchers
- Model Developers

**Tasks**:
- Video Question Answering

**Limitations**: N/A

## 💾 Data

**Source**: Videos collected from YouTube covering over 40 distinct themes.

**Size**: 327 instances

**Format**: N/A

**Annotation**: Annotated by human evaluators, incorporating adversarial annotation for robustness.

## 🔬 Methodology

**Methods**:
- LLM-based evaluation
- Human evaluation

**Metrics**:
- Accuracy

**Calculation**: Accuracy is determined using an LLM evaluator based on instance-specific rules annotated for each video-question pair.

**Interpretation**: An accuracy rate of around 97% was achieved by the GPT-4 evaluator compared to human evaluators.

**Validation**: Validation through rigorous annotation and adversarial evaluation mechanisms.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Accuracy

**Atlas Risks**:
- **Accuracy**: Unrepresentative data

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Videos comply with Creative Commons License.

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
