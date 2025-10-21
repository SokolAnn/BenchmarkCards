# LatEval (Lateral Thinking Evaluation Benchmark)

## 📊 Benchmark Details

**Name**: LatEval (Lateral Thinking Evaluation Benchmark)

**Overview**: LatEval is a novel evaluation benchmark that assesses the lateral thinking capabilities of large language models (LLMs) within an interactive framework, specifically utilizing Lateral Thinking Puzzles. The benchmark challenges models to pose high-quality questions that enable puzzle-solving and to integrate information to deduce the truth.

**Data Type**: puzzle-solving interactions

**Domains**:
- Natural Language Processing

**Languages**:
- English
- Chinese

**Similar Benchmarks**:
- MMLU
- C-Eval
- GSM8K

**Resources**:
- [GitHub Repository](https://github.com/THUKElab/LatEval)

## 🎯 Purpose and Intended Users

**Goal**: To evaluate the lateral thinking ability of large language models in a structured and interactive environment.

**Target Audience**:
- ML Researchers
- Model Developers
- AI Practitioners

**Tasks**:
- Lateral Thinking Puzzle
- Interactive Question Answering

**Limitations**: N/A

## 💾 Data

**Source**: Collected from various Lateral Thinking Puzzles websites

**Size**: 325 entries

**Format**: N/A

**Annotation**: Annotated using a combined approach of manual annotation and LLM assistance.

## 🔬 Methodology

**Methods**:
- Interactive questioning
- Automated metrics evaluation

**Metrics**:
- Answer Consistency
- Question Relevance
- Question Divergence
- Average Turns

**Calculation**: Metrics calculated based on interactions between the model and the host.

**Interpretation**: Higher scores indicate better lateral thinking capability and problem-solving skills.

**Baseline Results**: Experimental results show that most LLMs struggle significantly with tasks requiring lateral thinking.

**Validation**: Evaluation was performed using mainstream LLMs such as GPT-4 and GPT-3.5 as hosts.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Accuracy

**Atlas Risks**:
- **Accuracy**: Unrepresentative data, Poor model accuracy
- **Fairness**: Data bias

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: All samples collected from publicly accessible and legitimate websites with no sensitive information.

**Data Licensing**: Reviewed licenses of sources to ensure usability for non-profit academic research.

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
