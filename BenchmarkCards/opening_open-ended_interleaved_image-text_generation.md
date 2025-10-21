# OpenING (Open-ended Interleaved Image-Text Generation)

## 📊 Benchmark Details

**Name**: OpenING (Open-ended Interleaved Image-Text Generation)

**Overview**: OpenING is a comprehensive benchmark for evaluating open-ended interleaved image-text generation, comprising 5,400 high-quality human-annotated instances across 56 real-world tasks, aimed at challenging and improving interleaved generation methods and supporting the development of judge models for assessing multimodal generation.

**Data Type**: interleaved image-text instances

**Domains**:
- Natural Language Processing
- Computer Vision

**Languages**:
- English

**Similar Benchmarks**:
- OpenLEAF
- InterleavedBench

**Resources**:
- [Resource](https://opening-benchmark.github.io)

## 🎯 Purpose and Intended Users

**Goal**: Evaluate and benchmark open-ended interleaved image-text generation methods, providing a robust platform for challenging generation techniques and model assessments.

**Target Audience**:
- ML Researchers
- Model Developers
- AI Practitioners

**Tasks**:
- Interleaved Image-Text Generation
- Multimodal Reasoning
- Content Creation

**Limitations**: By design, OpenING is limited in scope to primarily 23 meta-topics and 56 tasks, which may not represent every real-world scenario and requires more task diversity.

## 💾 Data

**Source**: Collected from over 20 sources including social media, video sharing sites, and open dataset platforms, with instances annotated by human experts.

**Size**: 5,400 instances

**Format**: JSONL

**Annotation**: Manual annotation by 28 professional annotators and 14 expert supervisors.

## 🔬 Methodology

**Methods**:
- Pairwise evaluation using human judges
- Automated evaluation with IntJudge
- Comparison with GPT-based evaluators

**Metrics**:
- Win Rate
- Agreement
- FDT (Force Dividing Tie)

**Calculation**: Win rate represents how often a model wins in pairwise comparisons against others.

**Interpretation**: Higher win rates indicate superior performance in generating coherent interleaved content, while agreement measures evaluator consistency across different evaluation methods.

**Baseline Results**: GPT-4o+DALL-E3 and Gemini1.5+Flux are top-performing baselines evaluated against IntJudge.

**Validation**: Validation procedures involved pairwise comparisons conducted by multiple evaluators including humans and AI models.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness
- Robustness

**Atlas Risks**:
- **Accuracy**: Unrepresentative data
- **Fairness**: Data bias
- **Robustness**: Evasion attack

**Demographic Analysis**: The benchmark includes demographic fairness across model outputs but is primarily evaluated based on performance metrics.

**Potential Harm**: ['Content incoherence', 'Image-Text mismatch', 'Poor image quality']

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
