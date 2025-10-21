# Ontology Completion Benchmark

## 📊 Benchmark Details

**Name**: Ontology Completion Benchmark

**Overview**: This paper introduces a benchmark for evaluating ontology completion methods, designed to include manually validated hard negatives, and thoroughly analyses the strengths and weaknesses of Natural Language Inference (NLI) and concept embedding approaches.

**Data Type**: rule pairs

**Domains**:
- Artificial Intelligence

**Languages**:
- English

**Resources**:
- [Resource](https://huggingface.co/meta-llama/Llama-2-7b-hf)
- [Resource](https://huggingface.co/meta-llama/Llama-2-7b-chat-hf)
- [Resource](https://huggingface.co/meta-llama/Llama-2-13b-hf)
- [Resource](https://huggingface.co/meta-llama/Llama-2-13b-chat-hf)
- [Resource](https://huggingface.co/togethercomputer/Llama-2-7B-32K-Instruct)
- [Resource](https://huggingface.co/mistralai/Mistral-7B-v0.1)
- [Resource](https://huggingface.co/mistralai/Mistral-7B-Instruct-v0.2)
- [Resource](https://huggingface.co/lmsys/vicuna-13b-v1.5)
- [Resource](https://huggingface.co/lmsys/vicuna-13b-v1.5-16k)

## 🎯 Purpose and Intended Users

**Goal**: To evaluate and compare ontology completion methods, specifically analyzing NLI and concept embedding approaches.

**Target Audience**:
- AI Researchers
- Ontology Engineers

**Tasks**:
- Ontology Completion

**Limitations**: The area of ontology completion is considerably less mature than related areas, and the methods analyzed should be seen as baselines for future work.

## 💾 Data

**Source**: Seven well-known ontologies including Wine, Economy, Olympics, Transport, SUMO, FoodOn, and Gene Ontology.

**Size**: 103,184 positive examples, 494,708 negative examples in total

**Format**: N/A

**Annotation**: Manual annotation for negative examples

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- F1 Score
- Accuracy

**Calculation**: Metrics are calculated based on the accuracy of identifying valid ontology rules.

**Interpretation**: Higher F1 scores indicate better performance in identifying valid rules and their classifications.

**Baseline Results**: Results achieved by various models are provided, showing performance across tasks.

**Validation**: The benchmark is validated through comparative analysis of NLI and concept embedding methods.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Accuracy

**Atlas Risks**:
- **Accuracy**
- **Fairness**

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
