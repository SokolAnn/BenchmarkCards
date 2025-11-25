# MathChat

## 📊 Benchmark Details

**Name**: MathChat

**Overview**: MathChat is a comprehensive benchmark specifically designed to evaluate LLMs across a broader spectrum of mathematical tasks, focusing on multi-turn interactions and instruction-following abilities in conversations.

**Data Type**: question-answering pairs

**Domains**:
- Natural Language Processing
- Education

**Languages**:
- English

**Similar Benchmarks**:
- GSM8K
- MATH
- SVAMP
- MAWPS
- ASDiv
- MathVista

**Resources**:
- [GitHub Repository](https://github.com/Zhenwen-NLP/MathChat)

## 🎯 Purpose and Intended Users

**Goal**: To advance the development of a more generalized reasoner and assistant in mathematical contexts, particularly focusing on multi-turn mathematical reasoning and instruction-following.

**Target Audience**:
- ML Researchers
- Educators
- AI Developers

**Tasks**:
- Follow-Up Question Answering
- Error Correction
- Error Analysis
- Problem Generation

**Limitations**: N/A

## 💾 Data

**Source**: The MathChat benchmark contains tasks sourced from the testing set of GSM8K, which were expanded using GPT-4 to suit specific requirements.

**Size**: 1,319 examples per task

**Format**: JSON

**Annotation**: Automatically generated and verified with GPT-4 and other LLMs for accuracy.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Accuracy
- Instruction Following Score
- Error Diagnosis Score
- Solution Accuracy
- Problem Quality

**Calculation**: Metrics are calculated based on the ground truth values for problem-solving accuracy and scores assigned for instruction-following tasks.

**Interpretation**: Higher scores correspond to better understanding and adherence to instructions.

**Baseline Results**: The performance is compared against various state-of-the-art LLMs.

**Validation**: Empirical validation through extensive testing on multiple models trained on the benchmark.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Accuracy
- Safety
- Robustness

**Atlas Risks**:
- **Accuracy**: Unrepresentative data
- **Fairness**: Data bias

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
