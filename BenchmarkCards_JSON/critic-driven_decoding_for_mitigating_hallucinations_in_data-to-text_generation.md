# Critic-Driven Decoding for Mitigating Hallucinations in Data-to-text Generation

## 📊 Benchmark Details

**Name**: Critic-Driven Decoding for Mitigating Hallucinations in Data-to-text Generation

**Overview**: The paper presents a novel critic-driven decoding approach that combines the probabilistic output of a generator language model with a specialized text critic classifier. This method mitigates hallucinations in neural data-to-text generation without altering the model architecture or requiring additional training data. Experimental results demonstrate improvements on the WebNLG and OpenDialKG benchmarks.

**Data Type**: Text generation

**Domains**:
- Natural Language Generation
- Data-to-text generation

**Languages**:
- English

**Similar Benchmarks**:
- WebNLG
- OpenDialKG

**Resources**:
- [GitHub Repository](https://github.com/langus0/critic-aware-decoding)

## 🎯 Purpose and Intended Users

**Goal**: To mitigate hallucinations in data-to-text generation without modifying existing models.

**Target Audience**:
- Researchers in Natural Language Processing
- Developers working on text generation systems

**Tasks**:
- Data-to-text generation
- Mitigating hallucinations in generated text

**Limitations**: The performance is limited by the base language model and its ability to predict the most likely next tokens.

**Out of Scope Uses**:
- Tasks unrelated to data-to-text generation
- Other forms of text generation not involving hallucination issues

## 💾 Data

**Source**: WebNLG and OpenDialKG datasets

**Size**: N/A

**Format**: Text and RDF triples

**Annotation**: Data-to-text pairs annotated for evaluating hallucination

## 🔬 Methodology

**Methods**:
- Greedy decoding
- Critic-driven decoding

**Metrics**:
- BLEU
- METEOR
- BERTScore
- NLI
- BLEURT

**Calculation**: Incorporates probabilistic outputs from both a language model and a critic classifier into the text generation probability.

**Interpretation**: Evaluation of text quality and hallucinations based on generated outputs compared to reference texts.

**Baseline Results**: The proposed method achieved improvements over baseline language models on multiple metrics.

**Validation**: Experimental validation on the WebNLG and OpenDialKG datasets.

## ⚠️ Targeted Risks

**Risk Categories**:
- Misuse
- Fairness
- Robustness
- Accuracy

**Atlas Risks**:
- **Robustness**: Evasion attack, Hallucination
- **Fairness**: Data bias, Output bias
- **Accuracy**: Poor model accuracy

**Demographic Analysis**: N/A

**Potential Harm**: Potential for hallucinations leading to misinformation

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
