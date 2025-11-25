# TRUST GPT: A Benchmark for Trustworthy and Responsible Large Language Models

## 📊 Benchmark Details

**Name**: TRUST GPT: A Benchmark for Trustworthy and Responsible Large Language Models

**Overview**: TRUST GPT provides a comprehensive evaluation of large language models (LLMs) from three ethical perspectives—toxicity, bias, and value-alignment—using prompt templates derived from social norms, toxicity scoring via the PERSPECTIVE API, and active and passive value-alignment tasks.

**Data Type**: text (social norm prompts and model-generated responses)

**Domains**:
- Natural Language Processing
- AI Ethics

**Similar Benchmarks**:
- REALTOXICITY PROMPTS
- BOLD
- HELM
- BIG-Bench HHH E VAL

**Resources**:
- [GitHub Repository](https://github.com/HowieHwong/TrustGPT)
- [Resource](https://www.perspectiveapi.com/)
- [Resource](https://maxwellforbes.com/social-chemistry/)
- [Resource](https://arxiv.org/abs/2306.11507)

## 🎯 Purpose and Intended Users

**Goal**: To evaluate the ethical implications of LLMs by measuring toxicity, quantifying bias across demographic groups, and assessing value-alignment via active (AVA) and passive (PVA) tasks.

**Target Audience**:
- ML Researchers
- Model Developers
- AI Ethics Researchers

**Tasks**:
- Toxicity evaluation (model-generated responses to toxic/bad/harmful prompt templates)
- Bias evaluation (measuring toxicity differences across demographic groups)
- Value-Alignment evaluation — Active Value-Alignment (AVA: option selection)
- Value-Alignment evaluation — Passive Value-Alignment (PVA: Refuse to Answer / RtA)

**Limitations**: Explicit limitations stated by the authors: (1) model capability differences can influence evaluation results and cause low-quality or irrelevant outputs; (2) sensitivity to prompt template design is possible and more diverse prompt templates may be needed; (3) evaluation used a single dataset (Social Chemistry 101) and a limited set of models due to resource constraints, which may undermine confidence in generality; (4) online/open-source LLMs and APIs change over time, potentially affecting reproducibility.

## 💾 Data

**Source**: SOCIAL CHEMISTRY 101 dataset (social norms with crowd-sourced human judgment labels) used as prompts; model-generated responses collected via prompt templates; toxicity scoring via PERSPECTIVE API.

**Size**: Social Chemistry 101: 292,000 social norms; Experimental test sample counts used in the paper: Toxicity: 12,000 generated responses (500 samples × 8 models × 3 prompt templates); Bias: 32,000 generated responses (500 samples × 8 models × 8 groups); Value-alignment AVA: 4,000 generated responses (500 × 8 models); PV A: 4,000 generated responses (500 × 8 models).

**Format**: N/A

**Annotation**: Crowdsourced human evaluation labels (rot-judgment) in Social Chemistry 101 mapped to three basic labels: "it's good", "it's wrong", and "it's okay".

## 🔬 Methodology

**Methods**:
- Prompt-based automated evaluation of LLMs with predefined prompt templates
- Toxicity scoring using PERSPECTIVE API
- Statistical analysis including standard deviation across groups and Mann-Whitney U test for bias
- Active value-alignment (AVA) using option selection evaluated by hard and soft accuracy
- Passive value-alignment (PVA) using RtA (Refuse to Answer) metric based on refusal-detection templates

**Metrics**:
- Average toxicity score
- Standard deviation (toxicity across demographic groups)
- Mann-Whitney U test p-value (toxicity distributions between groups)
- Hard accuracy (AVA)
- Soft accuracy (AVA)
- RtA (Refuse to Answer) (PVA)

**Calculation**: Average toxicity: mean of PERSPECTIVE API toxicity scores (range 0–1) for generated responses after excluding refusal responses per refusal templates (Appendix 6.2). Bias: compute average toxicity per group, standard deviation across groups, and perform Mann-Whitney U test on toxicity distributions. AVA: hard accuracy is strict 3-class classification accuracy; soft accuracy counts 'it's okay' as acceptable for 'it's good' or 'it's wrong' labels (formulas in Appendix 6.6). RtA: proportion of responses classified as refusal based on explicit refusal indicators (Appendix 6.2).

**Interpretation**: Higher average toxicity indicates more toxic outputs. Larger standard deviation across groups and small Mann-Whitney U p-values indicate greater bias. Higher hard/soft accuracy indicates better active value-alignment. Higher RtA indicates stronger passive value-alignment (greater tendency to refuse norm-violating prompts).

**Baseline Results**: Empirical findings reported in the paper: FastChat exhibited the highest overall toxicity among evaluated models (e.g., average toxicity scores up to ~0.384 in some settings) while Alpaca exhibited the lowest toxicity (majority of toxicity scores < 0.1). ChatGPT achieved the highest soft accuracy in AVA (soft accuracy > 0.9). RtA results show Alpaca with very low RtA (< 0.1) and varied RtA across models and demographic groups (detailed per-model per-group values are provided in Table 6 of the paper).

**Validation**: Validation via statistical significance testing (Mann-Whitney U) for bias; experiments run with predefined sample sizes per section (Appendix 6.1); refusals filtered using explicit refusal-detection templates; toxicity scores obtained from PERSPECTIVE API. Detailed experimental settings and filtering procedures provided in Appendices.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Toxicity
- Value Alignment
- Fairness
- Robustness
- Misuse
- Transparency
- Societal Impact

**Atlas Risks**:
- **Fairness**: Output bias
- **Robustness**: Prompt injection attack
- **Misuse**: Spreading toxicity, Dangerous use
- **Value Alignment**: Toxic output, Harmful output
- **Transparency**: Lack of training data transparency
- **Governance**: Lack of model transparency, Lack of testing diversity
- **Societal Impact**: Impact on affected communities

**Demographic Analysis**: Benchmark includes demographic breakdowns across GENDER, RACE, and RELIGION; analysis uses average toxicity per group, standard deviation across groups, and Mann-Whitney U test to detect distributional differences.

**Potential Harm**: ['Detection of toxic outputs generated by LLMs', 'Detection of biased outputs that disproportionately target demographic groups', 'Detection of misaligned or harmful values in model outputs (both active choices and passive responses)']

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
