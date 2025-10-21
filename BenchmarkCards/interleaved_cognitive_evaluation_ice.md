# Interleaved Cognitive Evaluation (ICE)

## 📊 Benchmark Details

**Name**: Interleaved Cognitive Evaluation (ICE)

**Overview**: The Interleaved Cognitive Evaluation (ICE) benchmark systematically manipulates cognitive load factors on multi-hop reasoning tasks to measure the impact of extraneous load on model performance.

**Data Type**: question-answering pairs

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- MMLU

**Resources**:
- [GitHub Repository](https://github.com/imsaitejareddy/computational-cognitive-load)

## 🎯 Purpose and Intended Users

**Goal**: To evaluate the impact of cognitive load on the reasoning capabilities of large language models in a structured manner.

**Target Audience**:
- ML Researchers
- AI Safety Practitioners

**Tasks**:
- Multi-Hop Question Answering

**Limitations**: N/A - Not discussed

## 💾 Data

**Source**: Derived from curated datasets including U.S. SEC filings, FanOutQA, and MINTQA.

**Size**: 200 questions

**Format**: N/A

**Annotation**: N/A

## 🔬 Methodology

**Methods**:
- Automated metrics

**Metrics**:
- Exact-Match accuracy

**Calculation**: Exact-Match accuracy is calculated based on the proportion of correct answers provided by models across various conditions.

**Interpretation**: Higher Exact-Match accuracy indicates better reasoning capability under varying cognitive load conditions.

**Baseline Results**: Gemini-2.0-Flash-001 achieved 0.85 EM in Control conditions; Llama-3-8B-Instruct, Llama-3-70B-Instruct, Mistral-7B-Instruct-v0.2 achieved 0% EM across conditions.

**Validation**: Performance was validated through repeated tests under standardized conditions.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Robustness

**Atlas Risks**:
- **Accuracy**: Poor model accuracy
- **Robustness**

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
