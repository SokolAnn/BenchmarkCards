# Latent Jailbreak: A Benchmark for Evaluating Text Safety and Output Robustness of Large Language Models

## 📊 Benchmark Details

**Name**: Latent Jailbreak: A Benchmark for Evaluating Text Safety and Output Robustness of Large Language Models

**Overview**: We propose a benchmark that assesses both the safety and robustness of large language models (LLMs). To comprehensively study text safety and output robustness, we introduce a latent jailbreak prompt dataset, each involving malicious instruction embedding. We design a hierarchical annotation framework (SAFETY AND ROBUSTNESS FRAMEWORK) and present a systematic analysis of safety and robustness with respect to the position of explicit normal instructions, word replacements (verbs in explicit normal instructions, target groups in malicious instructions, cue words), and instruction replacements (different explicit normal instructions).

**Data Type**: text (instruction-following prompts / latent jailbreak prompts containing implicit malicious instructions)

**Domains**:
- Natural Language Processing

**Languages**:
- Chinese
- English

**Resources**:
- [GitHub Repository](https://github.com/qiuhuachuan/latent-jailbreak)
- [Resource](https://arxiv.org/abs/2307.08487)

## 🎯 Purpose and Intended Users

**Goal**: Evaluate both text safety and output robustness of large language models using a latent jailbreak prompt dataset and a hierarchical annotation framework.

**Target Audience**:
- ML Researchers
- Model Developers

**Tasks**:
- Machine Translation
- Text Generation (Instruction Following)
- Paraphrase / Refinement / Polishing (as instruction variants)

**Limitations**: The chosen jailbreak prompts in this article may exhibit some degree of incompleteness; the evaluated models have not been comprehensively covered in testing.

## 💾 Data

**Source**: Constructed by combining 13 prompt templates with 16 protected-group target words and 2 positional types (prefix and suffix) using an instruction-following format P ⊕ C ⊕ I where I is an implicit malicious instruction; dataset focused on toxic implicit malicious instructions (six toxic adjectives) and eight protected-group categories listed in Appendix A.

**Size**: 416 prompts

**Format**: N/A

**Annotation**: Hierarchical SAFETY AND ROBUSTNESS FRAMEWORK: Text Safety (binary: safe / unsafe) and Output Robustness (follow / not follow). Human annotation: 2,880 model responses for P1 and 960 instances for P2 and P3. Human labels used to fine-tune a RoBERTa classifier for automatic labeling of remaining model responses.

## 🔬 Methodology

**Methods**:
- Human evaluation (manual annotation of model responses according to SAFETY AND ROBUSTNESS FRAMEWORK)
- Automated labeling with fine-tuned RoBERTa classifier
- Automated metrics (success rates over multiple generations per prompt)

**Metrics**:
- Jailbreaking Success Rate (PJ = n_unsafe / (n_unsafe + n_safe))
- Instruction Following Rate (PR = n_follow / n_safe)
- Trustworthiness (P = (1 − PJ) · PR)

**Calculation**: PJ = n_unsafe / (n_unsafe + n_safe). PR = n_follow / n_safe. P = (1 - PJ) * PR.

**Interpretation**: Higher PJ indicates greater vulnerability to jailbreaks (worse safety). Higher PR indicates better adherence to explicit normal instructions (better robustness). Trustworthiness P combines safety and robustness: higher values indicate both low jailbreak rate and high instruction-following.

**Baseline Results**: Reported results (Table 4) across prompt templates P1–P13 for three models (ChatGLM2-6B, BELLE-7B-2M, ChatGPT). Example (P1, human-labeled): ChatGLM2-6B attack success rate 75.3%; BELLE-7B-2M 50.4%; ChatGPT 22.6%. Full table of results provided in the paper.

**Validation**: Automatic labeling validated on P2 and P3: safety prediction accuracy 99.8% (P2) and 99.9% (P3); robustness prediction accuracy 99.0% (P2) and 95.5% (P3) as reported in Table 3.

## ⚠️ Targeted Risks

**Risk Categories**:
- Safety
- Robustness

**Atlas Risks**:
- **Value Alignment**: Toxic output
- **Robustness**: Prompt injection attack
- **Fairness**: Output bias
- **Misuse**: Spreading toxicity, Dangerous use

**Demographic Analysis**: Breakdowns and per-target-group analysis for protected groups (16 words combined into eight protected-group categories: women / pregnant women; trans people / transgender people; lesbian women; gay people / gay men; homosexuals / bisexuals; black people; Jews / Arabs; disabled people; Muslims; immigrants; elderly people).

**Potential Harm**: Generation of toxic/offensive/harmful content targeted at protected groups (hate speech and discriminatory content) and reduced instruction-following leading to over-refusal or unsafe generations.

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
