# MVPBench (Multi-path Visual Physics benchmark)

## 📊 Benchmark Details

**Name**: MVPBench (Multi-path Visual Physics benchmark)

**Overview**: MVPBench is a benchmark designed to rigorously evaluate visual physical reasoning through the lens of visual chain-of-thought (CoT). Each example features interleaved multi-image inputs and demands coherent reasoning paths grounded in evolving visual cues.

**Data Type**: question-answering pairs

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- PhysBench
- Physion
- PhysReason

**Resources**:
- [GitHub Repository](https://github.com/CSU-JPG/MVPBench)
- [Resource](https://huggingface.co/datasets/CSU-JPG/MVPBench)

## 🎯 Purpose and Intended Users

**Goal**: To evaluate the visual reasoning capabilities of multimodal large language models (MLLMs) in understanding physical concepts through rigorous assessment of visual chain-of-thought reasoning.

**Target Audience**:
- ML Researchers
- Industry Practitioners
- Model Developers
- Physics Educators

**Tasks**:
- Visual Reasoning
- Physics Problem Solving
- Spatial Reasoning

**Limitations**: N/A

## 💾 Data

**Source**: Publicly available physics videos, curated questions from physics examinations, and image-based spatial reasoning tasks.

**Size**: 1,211 samples

**Format**: JSON

**Annotation**: Manually annotated by experts in physics and visual cognition.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics
- Multi-path reasoning evaluation

**Metrics**:
- Step Accuracy Score (SAS)
- Path Validity Rate (PVR)
- Path Coverage Score (PCS)
- Key Step Coverage (KSC)

**Calculation**: Metrics are calculated based on the correctness and coherence of reasoning steps provided by the model.

**Interpretation**: High scores on SAS and PVR indicate effective reasoning and understanding of physical laws.

**Baseline Results**: To be determined with model evaluations.

**Validation**: Benchmarked against established models such as GPT-4o and OpenAI o3.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness
- Robustness

**Atlas Risks**:
- **Accuracy**: Unrepresentative data
- **Fairness**: Data bias
- **Robustness**: Evasion attack

**Demographic Analysis**: N/A

**Potential Harm**: ['Inaccurate reasoning leading to misconceptions in physics education.']

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
