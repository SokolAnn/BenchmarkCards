# EMBODIED CITY: A BENCHMARK PLATFORM FOR EMBODIED AGENT IN REAL-WORLD CITY ENVIRONMENT

## 📊 Benchmark Details

**Name**: EMBODIED CITY: A BENCHMARK PLATFORM FOR EMBODIED AGENT IN REAL-WORLD CITY ENVIRONMENT

**Overview**: This paper constructs a benchmark platform for evaluating embodied intelligence in real-world city environments, extending capabilities of existing embodied intelligence to higher levels. It includes a highly realistic 3D simulation environment based on a real city and a set of evaluation tasks covering various embodied intelligence abilities.

**Data Type**: embodied task cases

**Domains**:
- Robotics
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- MetaUrban
- GRUtopia
- CityNav

**Resources**:
- [Resource](https://embodied-city.fiblab.net)

## 🎯 Purpose and Intended Users

**Goal**: To provide a systematic benchmark platform for embodied intelligence in urban environments, facilitating development and evaluation of embodied agents.

**Target Audience**:
- ML Researchers
- Industry Practitioners
- Robotics Developers

**Tasks**:
- Scene Understanding
- Question Answering
- Dialogue
- Visual Language Navigation
- Task Planning

**Limitations**: N/A

## 💾 Data

**Source**: 3D simulation environment based on a real city in China, using historical traffic data and simulation algorithms.

**Size**: 87.1k cases

**Format**: JSON

**Annotation**: Human efforts with ground-truth data obtained through various refinement processes.

## 🔬 Methodology

**Methods**:
- Automated metrics evaluation
- Human evaluation

**Metrics**:
- BLEU Score
- ROUGE
- METEOR
- CIDEr

**Calculation**: Metrics are calculated based on generated responses to embodied tasks, comparing them to ground truth.

**Interpretation**: Higher scores indicate better performance in generating responses for embodied tasks.

**Baseline Results**: Various multi-modal large language models like GPT-4 Turbo and Claude 3 are evaluated and compared.

**Validation**: N/A

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness

**Atlas Risks**:
- **Accuracy**: Unrepresentative data
- **Fairness**: Data bias

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
