# JaFIn (Japanese Financial Instruction Dataset)

## 📊 Benchmark Details

**Name**: JaFIn (Japanese Financial Instruction Dataset)

**Overview**: JaFIn is a manually constructed instruction dataset specifically designed for domain adaptation in Japanese finance models. It aims to enhance the performance of large language models (LLMs) through instruction tuning.

**Data Type**: question-answering pairs

**Domains**:
- Natural Language Processing
- Finance

**Languages**:
- Japanese

**Resources**:
- [Resource](https://huggingface.co/collections/tokyotech-llm/swallow-65d2bf12f8ab7fc669881082)
- [Resource](https://huggingface.co/collections/rinna/nekomata-6582b5134ee85531becbb9a9)
- [Resource](https://huggingface.co/elyza/ELYZA-japanese-Llama-2-13b)
- [Resource](https://huggingface.co/line-corporation/japanese-large-lm-3.6b)
- [Resource](https://huggingface.co/pfnet/plamo-13b)
- [Resource](https://huggingface.co/llm-jp/llm-jp-13b-v1.0)
- [Resource](https://huggingface.co/cyberagent/calm2-7b)

## 🎯 Purpose and Intended Users

**Goal**: To provide an instruction dataset specialized for the financial domain, facilitating training and evaluation of large language models (LLMs) to enhance their performance in responding to finance-related queries.

**Target Audience**:
- ML Researchers
- Industry Practitioners
- Model Developers
- Domain Experts

**Tasks**:
- Question Answering

**Limitations**: N/A

## 💾 Data

**Source**: Constructed from frequently asked questions, explanatory materials related to finance from Japanese government websites, Wikipedia, etc.

**Size**: 1,490 samples

**Format**: N/A

**Annotation**: Manual annotation based on financial knowledge and instruction tuning methodology.

## 🔬 Methodology

**Methods**:
- Instruction tuning using JaFIn
- Quantitative evaluation using specified tasks

**Metrics**:
- Accuracy

**Calculation**: Metrics calculated based on the performance on predefined financial tasks.

**Interpretation**: Higher accuracy indicates better performance of LLMs in responding to finance instructions compared to baseline models.

**Baseline Results**: N/A

**Validation**: 85% training and 15% validation split for instruction tuning.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Accuracy
- Privacy

**Atlas Risks**:
- **Fairness**: Data bias
- **Accuracy**: Unrepresentative data

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
