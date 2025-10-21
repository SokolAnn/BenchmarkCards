# MM-S OC

## 📊 Benchmark Details

**Name**: MM-S OC

**Overview**: MM-S OC is a comprehensive benchmark designed to evaluate MLLMs’ understanding of multimodal social media content through various tasks, including misinformation detection, hate speech detection, and social context generation.

**Data Type**: multimodal

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- PolitiFact
- GossipCop
- Hateful Memes
- Memotion

**Resources**:
- [GitHub Repository](https://github.com/claws-lab/MMSoc.git)

## 🎯 Purpose and Intended Users

**Goal**: To rigorously assess the capabilities of MLLMs (Multimodal Large Language Models) across ten multimodal tasks derived from social media environments.

**Target Audience**:
- ML Researchers
- Industry Practitioners
- Model Developers

**Tasks**:
- Misinformation Detection
- Hate Speech Detection
- Humor Detection
- Sarcasm Detection
- Sentiment Analysis
- Offensiveness Detection
- Tagging
- Image Description
- Social Context Description
- Optical Character Recognition

**Limitations**: N/A

## 💾 Data

**Source**: Combines prominent multimodal datasets including a novel large-scale YouTube tagging dataset.

**Size**: 1,963,697 videos

**Format**: N/A

**Annotation**: Annotated via crowdsourcing and institutionally approved methods.

## 🔬 Methodology

**Methods**:
- Zero-shot evaluation
- Fine-tuning with explanations
- Human evaluation for tagging performance

**Metrics**:
- Accuracy
- F1 Score
- Precision
- Recall
- ROUGE-L

**Calculation**: Metrics are calculated based on the performance of models on benchmark tasks, averaged across various experiments.

**Interpretation**: Higher scores indicate better performance in accurately categorizing and generating responses relevant to multifaceted social media scenarios.

**Baseline Results**: Comparisons made against various models including fully fine-tuned state-of-the-art models.

**Validation**: End-to-end evaluation of MLLMs was conducted using established datasets reflecting real-world applicability.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Accuracy
- Safety

**Atlas Risks**:
- **Fairness**: Data bias, Output bias
- **Accuracy**: Unrepresentative data, Poor model accuracy
- **Societal Impact**: Impact on affected communities

**Demographic Analysis**: The benchmark includes considerations for the diversity of perspectives needed to interpret social media appropriately.

**Potential Harm**: The benchmark identifies and mitigates the risk of misinformation and harmful content propagation in model outputs.

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Distributed under the Apache 2.0 License.

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
