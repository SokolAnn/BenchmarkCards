# VAT-KG (Visual-Audio-Text Knowledge Graph)

## 📊 Benchmark Details

**Name**: VAT-KG (Visual-Audio-Text Knowledge Graph)

**Overview**: VAT-KG is the first concept-centric and knowledge-intensive multimodal knowledge graph that comprehensively covers visual, audio, and text modalities, designed to provide explicit cross-modal knowledge to MLLMs.

**Data Type**: multimodal triplets

**Domains**:
- Natural Language Processing
- Computer Vision

**Languages**:
- English

**Similar Benchmarks**:
- VTKG
- M2ConceptBase
- Wikidata

**Resources**:
- [Resource](https://huggingface.co/datasets/vatkg/VATKG_DATASET)
- [Resource](https://huggingface.co/vatkg/VATKG_CODE)

## 🎯 Purpose and Intended Users

**Goal**: To provide a comprehensive multimodal knowledge graph for enhancing Retrieval-Augmented Generation tasks in multimodal large language models.

**Target Audience**:
- ML Researchers
- Industry Practitioners
- Model Developers

**Tasks**:
- Question Answering
- Multimodal Retrieval

**Limitations**: The diversity of VAT-KG is inherently dependent on the underlying multimodal datasets used during construction.

## 💾 Data

**Source**: Constructed from multimodal corpora including InternVid-FLT, AudioCaps, A VQA, and VALOR datasets.

**Size**: 110,786 triplets

**Format**: N/A

**Annotation**: Multimodal alignment filtering and knowledge-intensive recaptioning utilizing advanced LLMs.

## 🔬 Methodology

**Methods**:
- Multimodal Alignment Filtering
- Knowledge-Intensive Recaptioning
- Multimodal Triplet Grounding
- Cross-Modal Description Alignment

**Metrics**:
- Accuracy

**Calculation**: Performance measured through Model-as-Judge scores and human evaluation.

**Interpretation**: Higher scores indicate better performance on the task of multimodal question answering.

**Baseline Results**: N/A

**Validation**: Validated through comprehensive human assessment and statistical tests.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Safety
- Privacy

**Atlas Risks**:
- **Fairness**: Data bias
- **Privacy**: Personal information in data

**Demographic Analysis**: N/A

**Potential Harm**: Mitigates hallucinations in multimodal large language models.

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Ensured by excluding any private or deleted content and using only publicly available datasets.

**Data Licensing**: CC BY-NC 4.0 license for non-commercial use.

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Adheres to YouTube’s Terms of Service.
