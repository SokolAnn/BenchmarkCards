# SeeGULL (Stereotypes Generated Using LLMs in the Loop)

## 📊 Benchmark Details

**Name**: SeeGULL (Stereotypes Generated Using LLMs in the Loop)

**Overview**: SeeGULL is a broad-coverage stereotype dataset created by leveraging the generative capabilities of large language models (PaLM, GPT-3, T0) to generate stereotype candidates and a geographically diverse human rater pool to validate prevalence. The dataset is in English and contains stereotypes about identity groups spanning 178 countries across 8 geo-political regions and 6 continents, as well as state-level identities within the United States and India. The dataset includes fine-grained offensiveness scores and comparative in-region vs out-region annotations.

**Data Type**: text (identity-attribute stereotype tuples)

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- StereoSet (Nadeem et al., 2021)
- CrowS-Pairs (Nangia et al., 2020)
- French CrowS-Pairs (Névéol et al., 2022)
- Bhatt et al. (2022)
- UNESCO (Klineberg, 1951)

**Resources**:
- [GitHub Repository](https://github.com/google-research-datasets/seegull)
- [GitHub Repository](https://github.com/google-research-datasets/seegull/seegull_datacard)
- [Resource](https://arxiv.org/abs/2305.11840)

## 🎯 Purpose and Intended Users

**Goal**: Create a broad geo-culturally covered stereotype benchmark in English to detect and measure stereotyping harms in NLP models and provide offensiveness ratings and socially situated (in-region vs out-region) annotations.

**Target Audience**:
- ML Researchers
- Natural Language Processing Researchers
- Model Developers

**Tasks**:
- Natural Language Inference
- Question Answering
- Document Similarity
- Bias / Fairness Evaluation

**Limitations**: The dataset is only in English and not exhaustive. Generation depends on seed selection which can skew coverage. Annotations are subjective and annotators may have limited world views. Some stereotypes require contextual information which is not captured. Out-region annotators were recruited from North America only. The dataset is not a replacement for participatory community-engaged methods.

**Out of Scope Uses**:
- SeeGULL should be used only for diagnostic and research purposes, and not as benchmarks to prove lack of bias.

## 💾 Data

**Source**: Stereotype candidates were generated using large language models PaLM 540B, GPT-3, and T0 prompted with few-shot examples drawn from seed sets (sources include StereoSet, UNESCO/Klineberg 1951, Koch et al., Borude 1966, Bhatt et al. 2022). Generated candidates were post-processed and validated by human annotators recruited from geographically diverse regions for in-region and out-region annotations. Offensiveness annotations for attribute terms were collected separately from annotators.

**Size**: 7,750 annotated stereotypes (Global axis) and 80,977 unique generated stereotype candidates (pre-validation). Covers 179 identity groups across 178 countries, plus state-level identities for 50 US states and 31 Indian states/union territories.

**Format**: N/A

**Annotation**: Prevalence annotation: each candidate annotated by 3 annotators with labels Stereotypical (S), Non-Stereotypical (N), or Unsure (U). Stereotype thresholds reported for k=1..3 (number of annotators labeling as stereotype). Offensiveness annotation: top 1,800 attribute terms annotated by 3 annotators on a Likert scale from -1 (Not offensive) to +4 (Extremely Offensive). Annotator pool: 89 annotators across 8 regions and 16 countries for prevalence annotations; offensiveness annotations recruited from North America (annotators proficient in English). Annotators were professional contractors and compensated above market/local minimum wage; total annotation spend reported as USD 23,100 (~USD 0.50 per tuple on average).

## 🔬 Methodology

**Methods**:
- LLM-based generation using few-shot prompting (PaLM 540B, GPT-3, T0)
- Post-processing (regex extraction, deduplication, demonym/adjectival mapping)
- Salience scoring using a modified tf-idf
- Candidate selection (top 1000 candidates per region while maintaining country distribution)
- Human validation with geographically situated annotators (in-region and out-region)
- Offensiveness annotation via Likert scale ratings for attribute terms
- Downstream evaluation in Natural Language Inference (NLI) to measure embedded stereotypes

**Metrics**:
- Mean entailment (M(E))
- Percent Entailed (%Entailed, %E)
- Salience score (modified tf-idf)
- Mean offensiveness score (mean of 3 annotator Likert ratings)
- Annotator agreement / stereotype thresholds (k = number of annotators labeling Stereotypical)

**Calculation**: Salience score computed as salience = tf(attr; c) * idf(attr; R), where tf(attr; c) is the smoothed relative frequency of attribute in country c and idf(attr; R) is the inverse document frequency of the attribute across regions R. Mean entailment M(E) computed as P(entail)/|D| over the constructed NLI dataset. Mean offensiveness is the arithmetic mean of three annotator ratings on a Likert scale (-1 to +4).

**Interpretation**: Higher mean entailment (M(E)) and higher %Entailed indicate stronger embedded stereotyping harms in evaluated NLI models. Higher salience indicates a more uniquely associated attribute for an identity group as generated by LLMs. Higher mean offensiveness scores indicate more offensive stereotypes.

**Baseline Results**: SeeGULL compared against a neutral baseline (NB), StereoSet (SS), and CrowS-Pairs (CP) on three pre-trained NLI models (ELMo, XLNet, ELECTRA). Example (ELMo, Global): NB M(E)=0.74, SS M(E)=0.79, CP M(E)=0.69, SeeGULL (SG) M(E)=0.81. SeeGULL yields higher M(E) and %Entailed across models and many regions (detailed results in Table 3).

**Validation**: Candidates selected by salience and top-1000 per region to ensure balanced distribution; each selected candidate annotated by 3 in-region annotators (and additionally 3 out-region annotators for regional-sensitivity analysis). No majority voting enforced; dataset releases individual annotator labels so end users can choose thresholds. Offensiveness annotations obtained from 3 annotators per attribute term (top 1,800 attributes).

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Fairness
- Societal Impact
- Offensiveness

**Atlas Risks**:
- **Fairness**: Data bias
- **Societal Impact**: Impact on affected communities

**Demographic Analysis**: Includes annotator demographic breakdown (89 annotators across 8 regions and 16 countries for prevalence annotations; additional details in Appendix A.6) and analysis of regional sensitivity comparing in-region vs out-region annotators.

**Potential Harm**: ['Stereotyping harms (models reinforcing societal stereotypes)', 'Offensive content leading to hate, prejudice and negative impacts on affected communities']

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Annotator compensation respected local regulations regarding minimum wage in respective countries; annotators were professional contractors and were compensated above prevalent market rates. Dataset release will include trigger warnings for offensive content.
