# Concept-Reversed Winograd Schema Challenge (CR-WSC)

## 📊 Benchmark Details

**Name**: Concept-Reversed Winograd Schema Challenge (CR-WSC)

**Overview**: We propose a new evaluation dataset, the Concept-Reversed Winograd Schema Challenge (CR-WSC), designed to evaluate and improve the reasoning capabilities of Large Language Models (LLMs) by utilizing adversarial examples that confuse standard semantic associations.

**Data Type**: question-answering pairs

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Resources**:
- [GitHub Repository](https://github.com/HKUST-KnowComp/Adv-WSC)

## 🎯 Purpose and Intended Users

**Goal**: To evaluate the robustness of reasoning in language models using a dataset that presents challenging adversarial examples.

**Target Audience**:
- ML Researchers
- Model Developers

**Tasks**:
- Coreference Resolution

**Limitations**: One limitation of the work is the reliance on human labour for the dataset construction. Annotators need to examine the entities and ensure they are reasonable to be included in the CR-WSC dataset.

## 💾 Data

**Source**: Data constructed using annotated pairs and generated adversarial examples, manually verified by experts.

**Size**: 410 examples

**Format**: JSON

**Annotation**: Manual annotation by experts in natural language processing.

## 🔬 Methodology

**Methods**:
- Automated metrics
- Human evaluation

**Metrics**:
- Single Accuracy
- Pair Accuracy

**Calculation**: Metrics are calculated based on the ability of the QA system to provide correct answers to the challenges posed in the dataset.

**Interpretation**: Higher accuracy rates indicate better reasoning capabilities in LLMs when faced with adversarial inputs.

**Validation**: The dataset was validated by employing different models and comparing their performance on CR-WSC and WSC.

## ⚠️ Targeted Risks

**Risk Categories**:
- Fairness
- Accuracy

**Atlas Risks**:
No specific atlas risks defined

**Demographic Analysis**: The dataset construction process avoided perpetuating stereotypes, although some traits might be perceived as stereotypical.

**Potential Harm**: ['Potential reinforcement of stereotypes and biases in language processing tasks.']

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
