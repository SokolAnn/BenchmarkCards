# MM-Vet (Multimodal Veterinarian)

## 📊 Benchmark Details

**Name**: MM-Vet (Multimodal Veterinarian)

**Overview**: MM-Vet is an evaluation benchmark that examines large multimodal models (LMMs) on complicated multimodal tasks by defining six core vision-language (VL) capabilities and evaluating 16 capability integrations. MM-Vet also proposes an LLM-based evaluator (GPT-4 few-shot prompt) to score open-ended model outputs with a unified scoring metric.

**Data Type**: image-question-answer pairs (images with open-ended questions and answers)

**Domains**:
- Natural Language Processing
- Computer Vision

**Languages**:
- English

**Similar Benchmarks**:
- MME
- MM-Bench
- VQA
- COCO
- TextCaps
- GQA
- VCR

**Resources**:
- [GitHub Repository](https://github.com/yuweihao/MM-Vet)
- [Resource](https://huggingface.co/spaces/whyu/MM-Vet_Evaluator)

## 🎯 Purpose and Intended Users

**Goal**: To evaluate large multimodal models (LMMs) on complicated multimodal tasks that require integration of multiple core vision-language capabilities, and to provide per-capability insights via a unified LLM-based evaluator for open-ended outputs.

**Target Audience**:
- ML Researchers
- Model Developers
- Industry Practitioners

**Tasks**:
- Question Answering
- Visual Question Answering
- Optical Character Recognition
- Image Captioning
- Spatial Reasoning
- Mathematical Problem Solving
- Knowledge-based Reasoning
- Language Generation

**Limitations**: MM-Vet focuses on image-text input/output modalities (does not cover other modalities). The LLM-based evaluator relies on GPT-4 (incurs usage fees), and the evaluator alignment is reported primarily for GPT-4.

## 💾 Data

**Source**: Collected 187 images from various online sources and 205 questions (initially); ground truths for 155 questions were annotated by the authors and answers for 50 questions were gathered from the Internet. Additionally collected ten extra images with high-quality questions from VCR and three images from ChestX-ray14. Paper reports that in total MM-Vet contains 200 images and 218 questions (samples).

**Size**: 200 images; 218 questions (samples)

**Format**: N/A

**Annotation**: Ground truths for 155 questions annotated by the authors; answers for 50 questions gathered from the Internet; remaining annotation sourcing not specified.

## 🔬 Methodology

**Methods**:
- LLM-based evaluation using GPT-4 with few-shot prompting
- Automated metrics (LLM-generated soft score per sample)
- Evaluation of multiple model paradigms: end-to-end tuned LMMs and LLM-tool-using systems
- Comparison of LLM evaluators against human annotations (validation)

**Metrics**:
- Per-sample correctness score in [0.0, 1.0] produced by GPT-4 evaluator
- Aggregate percentage score S = (sum of per-sample scores) / N × 100%
- Capability-wise aggregate score Sc = (sum of scores for samples in capability set) / Nc × 100%
- Averaged absolute difference (Δ) between evaluator scores and human-annotated scores for validation

**Calculation**: Per-sample score si ∈ {0.0,0.1,...,1.0} produced by GPT-4 evaluator. Total score S = (Σ_{i=1..N} si) / N × 100%. Capability score Sc = (Σ_{i ∈ C} si) / Nc × 100%, where C is the set of samples requiring that capability.

**Interpretation**: Per-sample scores range from 0 to 1; aggregated scores are reported as percentages (0%–100%). Higher aggregated percentages indicate better model performance; full score is 100%.

**Baseline Results**: Representative total scores reported: GPT-4V: 67.7% (±0.3); MM-ReAct-GPT-4: 44.6% (±0.2); LLaV A-13B (LLaMA-2): 32.9% (±0.1); LLaMA-Adapter v2-7B: 31.4% (±0.1). (Results and per-capability breakdowns provided in Tables 2-5.)

**Validation**: Validated LLM-based evaluator against human annotations using 138 objective questions from MM-ReAct-GPT-4 outputs, computing averaged absolute differences (Δ). GPT-4 (0613) showed the closest agreement with human scores (Δ = 0.0423). Additional Δ values for other LLM evaluators and combinations are reported in Tables 6 and 7.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Evaluation reliability

**Atlas Risks**:
- **Fairness**: Data bias

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
