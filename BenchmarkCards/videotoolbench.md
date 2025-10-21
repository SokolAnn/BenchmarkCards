# VideoToolBench

## 📊 Benchmark Details

**Name**: VideoToolBench

**Overview**: VideoToolBench is a tool-using instruction-following dataset designed to probe the abilities of video LLMs in invoking tools for video understanding tasks.

**Data Type**: instruction-following samples

**Domains**:
- Natural Language Processing
- Computer Vision

**Languages**:
- English

**Resources**:
- [GitHub Repository](https://github.com/JaidedAI/EasyOCR)

## 🎯 Purpose and Intended Users

**Goal**: To enhance video LLMs' tool usage capabilities and facilitate continual learning in real-world scenarios dealing with dynamic tool data.

**Target Audience**:
- ML Researchers
- Model Developers

**Tasks**:
- Video Understanding
- Instruction Following

**Limitations**: N/A

## 💾 Data

**Source**: Instruction following data generated via GPT-3.5-turbo for various tool functions in the context of video understanding.

**Size**: 5,000 samples per tool

**Format**: JSON

**Annotation**: Automatically generated with semantic verification.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Accuracy
- Average accuracy

**Calculation**: Metrics calculated based on the correct invocation of tools and responses by LLMs.

**Interpretation**: Higher average accuracy indicates better performance in invoking tools correctly.

**Validation**: Tested on both established benchmarks and VideoToolBench dataset.

## ⚠️ Targeted Risks

**Risk Categories**:
- Fairness
- Privacy
- Accuracy

**Atlas Risks**:
- **Fairness**: Data bias
- **Privacy**: Personal information in data
- **Accuracy**: Poor model accuracy

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: User data handled according to standard privacy practices.

**Data Licensing**: Publicly available upon publication with restrictions on commercial usage.

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
