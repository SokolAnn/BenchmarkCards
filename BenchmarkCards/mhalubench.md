# MHaluBench

## 📊 Benchmark Details

**Name**: MHaluBench

**Overview**: A meta-evaluation benchmark designed for the assessment of hallucination detection methods in multimodal large language models.

**Data Type**: Multi-modal

**Domains**:
- Image-to-Text
- Text-to-Image

**Similar Benchmarks**:
- FactCC
- QAGS
- HaluEval
- POPE
- HaELM
- AMBER

**Resources**:
- [GitHub Repository](https://github.com/zjunlp/EasyDetect)
- [Resource](http://easydetect.openkg.cn)

## 🎯 Purpose and Intended Users

**Goal**: To facilitate evaluation of hallucination detection capabilities in multimodal large language models.

**Target Audience**:
- Researchers
- AI developers
- Data scientists

**Tasks**:
- Detect multimodal hallucinations
- Conduct meta-evaluation of detection frameworks

**Limitations**: None

## 💾 Data

**Source**: Generated outputs from leading multimodal models

**Size**: 200 instances for Image Captioning, 200 for Visual Question Answering, and 220 for Text-to-Image Generation.

**Format**: Image and text pairs

**Annotation**: Claims labeled as hallucinatory or non-hallucinatory based on claim extraction.

## 🔬 Methodology

**Methods**:
- Claim extraction
- Autonomous tool selection
- Parallel tool execution
- Hallucination verification

**Metrics**:
- Precision
- Recall
- F1 Score
- Accuracy
- Macro F1 Score

**Calculation**: Metrics calculated based on detection outcomes from the benchmark.

**Interpretation**: Quantitative assessment of model performance against hallucination detection tasks.

**Validation**: Validated through extensive evaluation on the MHaluBench benchmark.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Privacy
- Fairness

**Atlas Risks**:
- **Accuracy**: Poor model accuracy
- **Privacy**: Personal information in data
- **Fairness**: Data bias

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: All data used complies with privacy regulations.

**Data Licensing**: The dataset is constructed from publicly available sources.

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Adheres to applicable data privacy laws.
