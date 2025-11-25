# ATLAS: Benchmarking and Adapting LLMs for Global Trade via Harmonized Tariff Code Classification

## 📊 Benchmark Details

**Name**: ATLAS: Benchmarking and Adapting LLMs for Global Trade via Harmonized Tariff Code Classification

**Overview**: We introduce the first benchmark for HTS code classification, derived from the U.S. Customs Rulings Online Search System (CROSS).

**Data Type**: text

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Resources**:
- [Resource](https://huggingface.co/datasets/flexifyai/cross_rulings_hts_dataset_for_tariffs)
- [Resource](https://huggingface.co/flexifyai/atlas-llama3.3-70b-hts-classification)
- [Resource](https://flexifyai-atlas-llama3-3-70b-hts-demo.hf.space/?logs=container&__theme=system&deep_link=FFJuTJsv_fM)

## 🎯 Purpose and Intended Users

**Goal**: To establish tariff classification as a challenging new frontier for LLM evaluation.

**Target Audience**:
- ML Researchers
- Industry Practitioners
- Model Developers

**Tasks**:
- Hierarchical Classification
- Reasoning

**Limitations**: N/A

## 💾 Data

**Source**: U.S. Customs Rulings Online Search System (CROSS)

**Size**: 18,731 rulings

**Format**: Structured text format

**Annotation**: Automated information extraction from legal rulings

## 🔬 Methodology

**Methods**:
- Supervised Fine-Tuning

**Metrics**:
- Fully correct classification
- Partially correct classification
- Average digit-level accuracy

**Calculation**: Metrics calculated based on correctness of HTS US code matches.

**Interpretation**: Higher percentages in fully and partially correct classifications indicate better model performance in HTS code classification.

**Validation**: Random split of dataset into training (18,254), validation (200), and test (200) sets.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness

**Atlas Risks**:
- **Accuracy**: Unrepresentative data
- **Fairness**

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
