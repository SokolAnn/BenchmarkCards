# Visual CounterFact

## 📊 Benchmark Details

**Name**: Visual CounterFact

**Overview**: Visual CounterFact is a dataset designed to study world knowledge priors related to visual attributes in Multimodal Large Language Models (MLLMs) through visually-realistic counterfactuals that introduce conflicts between memorized facts and visual input.

**Data Type**: image

**Domains**:
- Computer Vision
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- VL-Checklist
- VALSE
- FOIL-COCO
- SVO-Probes
- Winoground
- COCO-Counterfactuals

**Resources**:
- [GitHub Repository](https://github.com/rsinghlab/pixels_vs_priors)

## 🎯 Purpose and Intended Users

**Goal**: To provide a benchmark for studying how multimodal large language models reconcile memorized world knowledge and visual input.

**Target Audience**:
- ML Researchers
- Industry Practitioners
- Model Developers

**Tasks**:
- Visual Question Answering
- Image Classification

**Limitations**: The framework focuses on three state-of-the-art models and may not represent the full spectrum of multimodal architectures.

## 💾 Data

**Source**: Images created through a four-step pipeline involving sourcing objects, retrieving images, and generating counterfactual relations.

**Size**: 2,904 visually grounded examples

**Format**: Image files

**Annotation**: Automatically generated counterfactuals using model-based approaches.

## 🔬 Methodology

**Methods**:
- Early decoding
- Activation-level intervention

**Metrics**:
- Accuracy

**Calculation**: Accuracy is calculated by evaluating how well models predict answers based on visual input and world knowledge.

**Interpretation**: High accuracy indicates that models effectively utilize visual input over memorized prior knowledge.

**Baseline Results**: Majority of models show above 80% accuracy on visual-based prompts.

**Validation**: Evaluated through experiments comparing performance with and without steering interventions.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Safety

**Atlas Risks**:
- **Fairness**: Data bias
- **Robustness**: Prompt injection attack

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
