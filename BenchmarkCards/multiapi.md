# MultiAPI

## 📊 Benchmark Details

**Name**: MultiAPI

**Overview**: MultiAPI is a pioneering comprehensive large-scale API benchmark dataset aimed at expanding LLMs’ proficiency in multimodal contexts. It consists of 235 diverse API calls and 2,038 contextual prompts, providing a unique platform for evaluating tool-augmented LLMs handling multimodal tasks.

**Data Type**: API function and prompt pairs

**Domains**:
- Natural Language Processing
- Computer Vision

**Languages**:
- English

**Resources**:
- [GitHub Repository](https://github.com/HaroldLiuJ/MultiAPI)

## 🎯 Purpose and Intended Users

**Goal**: To evaluate Large Language Models' ability to handle multimodal tasks using external API functions and to enhance LLMs' capabilities.

**Target Audience**:
- ML Researchers
- Industry Practitioners
- Model Developers

**Tasks**:
- API Function Matching
- Multimodal Task Execution

**Limitations**: N/A

## 💾 Data

**Source**: Constructed from the HuggingFace instruction-code dataset.

**Size**: 235 API functions and 2,038 prompts

**Format**: N/A

**Annotation**: Human refinement and verification of model descriptions and generated instructions.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Invocation Accuracy
- Domain Match
- Function Match
- Argument Match

**Calculation**: Metrics are calculated based on function calls selected by LLMs in response to user instructions.

**Interpretation**: Higher accuracy values indicate better performance in correctly identifying the necessary API functions and their arguments.

**Baseline Results**: N/A

**Validation**: Evaluated through comprehensive experiments involving both API-based and open-source LLMs.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Safety
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
