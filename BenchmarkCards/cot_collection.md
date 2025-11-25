# COT COLLECTION

## 📊 Benchmark Details

**Name**: COT COLLECTION

**Overview**: An instruction-tuning dataset that augments the Flan Collection with 1.84 million chain-of-thought rationales generated across 1,060 tasks to enable chain-of-thought (CoT) fine-tuning of smaller language models and improve their zero-shot and few-shot reasoning.

**Data Type**: text (instruction-instance-answer pairs with chain-of-thought rationales)

**Domains**:
- Natural Language Processing

**Languages**:
- English
- French
- Japanese
- Korean
- Russian
- Chinese

**Similar Benchmarks**:
- Flan Collection
- P3
- Super-NaturalInstructions
- BIG-Bench-Hard (BBH)
- MGSM
- QASC
- AQuA
- GSM8K
- QED
- StrategyQA
- SenseMaking
- CREAK
- e-SNLI
- ECQA

**Resources**:
- [GitHub Repository](https://github.com/kaistAI/)
- [GitHub Repository](https://github.com/kaistAI/CoT-Collection)
- [Resource](https://arxiv.org/abs/2305.14045v2)

## 🎯 Purpose and Intended Users

**Goal**: To equip smaller language models (under 100B parameters) with step-by-step chain-of-thought reasoning ability by instruction tuning using a large-scale dataset of generated rationales (1.84M instances across 1,060 tasks).

**Target Audience**:
- ML Researchers
- Model Developers
- Industry Practitioners

**Tasks**:
- Multiple Choice Question Answering
- Extractive Question Answering
- Closed-book Question Answering
- Natural Language Inference
- Arithmetic Reasoning
- Formal Logic
- Dialogue Generation
- Text Classification
- Text Generation

**Limitations**: COT-T5 (models fine-tuned on COT COLLECTION) is not trained to engage in long-form dialogue/chat applications; smaller LMs still show near-zero accuracy on some non-English math tasks and the paper limits multilingual experiments to single-language adaptation; reproducibility concerns due to reliance on proprietary LLMs (OpenAI Codex) used for rationale augmentation; dataset quality could be improved using stronger LLMs and better prompting techniques.

**Out of Scope Uses**:
- Chat applications / long-form dialogue

## 💾 Data

**Source**: Augmented from the Flan Collection (including P3, Super-NaturalInstructions, Flan, and additional dialogue & code datasets). Rationales were generated via in-context learning using OpenAI Codex with demonstrations manually created by the authors and subsequent filtering.

**Size**: 1.84 million instances (rationales) across 1,060 tasks

**Format**: N/A

**Annotation**: Rationales automatically generated via in-context learning with OpenAI Codex using task-group demonstrations (6–8 examples per task group) manually created by authors; generated outputs filtered via stated criteria (answer inclusion, length <512 tokens, deduplication, repetition and code filters); for a multilingual experiment, 60K–80K instances were translated using ChatGPT.

## 🔬 Methodology

**Methods**:
- Direct Evaluation
- CoT Evaluation (requires generated rationale of minimum 8 tokens)
- Zero-shot evaluation
- Few-shot evaluation
- CoT fine-tuning
- Full fine-tuning
- LoRA (parameter-efficient) fine-tuning
- Rationale quality evaluation with ROSCOE

**Metrics**:
- Accuracy
- Exact Match (EM)
- ROSCOE suite (semantic alignment, semantic similarity, logical inference, language coherence)

**Calculation**: For classification tasks under Direct Evaluation, select the option with highest probability via verbalizers and report Accuracy. For generation tasks under Direct Evaluation, compare prediction with reference and report Exact Match (EM). For CoT Evaluation, require the model to generate a rationale of at least 8 tokens before producing the answer; in classification tasks verbalizers are applied after the generated rationale (indicator token '[ANSWER]') and Accuracy is measured; for generation tasks extract output after the indicator phrase and measure EM.

**Interpretation**: Higher Accuracy and EM indicate better zero-shot or few-shot task performance. Improvements reported in the paper (e.g., average percentage-point gains on BBH, P3, MGSM, and domain-specific few-shot tasks) are used to compare CoT fine-tuning effects. CoT Evaluation specifically measures the model's ability to produce intermediate rationales plus correct answers.

**Baseline Results**: On BIG-Bench-Hard (27 datasets) CoT-T5 (Flan-T5 fine-tuned on COT COLLECTION) reports average zero-shot accuracy improvements of +4.34% (Flan-T5 3B) and +2.60% (Flan-T5 11B) compared to Flan-T5. CoT fine-tuning T0 (3B) on a 163-task subset yields +8.65% average on 11 P3 evaluation datasets. Multilingual CoT fine-tuning (60K–80K translated instances) yields ~2x–10x improvements on MGSM in low-resource languages. In few-shot adaptation on 4 domain-specific datasets, CoT-T5 + LoRA achieves +2.24% (3B) and +2.37% (11B) improvements over Flan-T5 baselines, and outperforms ChatGPT with demonstrations by up to +13.98% on the reported setting.

**Validation**: Dataset and approach validated via ablation studies: training on subsets (163 tasks / 644K instances), sampling experiments (10K, 100K, 1.84M instances) to study task vs. instance scaling, multilingual adaptation experiments (translated 60K–80K instances per language), rationale quality assessment using ROSCOE metrics, and filtering heuristics to remove low-quality/degenerated rationales.

## ⚠️ Targeted Risks

**Risk Categories**:
- Robustness
- Governance

**Atlas Risks**:
- **Governance**: Lack of system transparency

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
