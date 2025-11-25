# PerInstruct

## 📊 Benchmark Details

**Name**: PerInstruct

**Overview**: PerInstruct is a novel benchmark composed of personalized instructions spanning diverse daily scenarios, specifically designed to evaluate the personalization capabilities of VLM-based mobile agents.

**Data Type**: text

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- MobileAgentBench
- AndroidArena
- Mobile-Bench

**Resources**:
- [GitHub Repository](https://github.com/xinwang-nwpu/PerPilot)

## 🎯 Purpose and Intended Users

**Goal**: To evaluate the personalization capabilities of VLM-based mobile agents.

**Target Audience**:
- ML Researchers
- Industry Practitioners
- Model Developers

**Tasks**:
- Personalized Task Execution
- Instruction Understanding

**Limitations**: N/A

## 💾 Data

**Source**: Human-annotated dataset constructed from authentic user-generated requests and LLM-based generation.

**Size**: 75 examples

**Format**: N/A

**Annotation**: Manual annotation by experts

## 🔬 Methodology

**Methods**:
- Human evaluation

**Metrics**:
- Accuracy

**Calculation**: Measurements of success rates, element perception accuracy, and exploration accuracy.

**Interpretation**: Higher scores indicate better performance in handling personalized instructions.

**Baseline Results**: UI-TARS improved success rates from 12.0% to 68.0%; MobileAgent from 9.3% to 49.3%; AppAgent from 10.7% to 46.7%.

**Validation**: Extensive experiments conducted across multiple mobile agents.

## ⚠️ Targeted Risks

**Risk Categories**:
- Fairness
- Accuracy

**Atlas Risks**:
- **Fairness**: Output bias
- **Accuracy**: Poor model accuracy

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
