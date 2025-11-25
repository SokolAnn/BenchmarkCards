# Winogender schemas

## 📊 Benchmark Details

**Name**: Winogender schemas

**Overview**: A Winograd schema-style evaluation set of minimal pair sentences that differ only by pronoun gender, designed to reveal and measure systematic gender bias in coreference resolution systems by testing pronoun resolution to occupational mentions across gender variants.

**Data Type**: text (hand-written Winograd-style sentence templates / minimal pair sentences)

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- Winograd Schema Challenge
- WinoBias

**Resources**:
- [GitHub Repository](https://github.com/rudinger/winogender-schemas)
- [Resource](https://arxiv.org/abs/1804.09301)

## 🎯 Purpose and Intended Users

**Goal**: To introduce Winogender schemas, a pronoun resolution diagnostic in the style of Winograd schemas, to uncover and analyze gender bias in coreference resolution systems and to correlate observed system bias with real-world and textual gender statistics.

**Target Audience**:
- Natural Language Processing researchers
- Model developers

**Tasks**:
- Coreference Resolution
- Bias Evaluation (diagnostic evaluation)

**Limitations**: The authors view the schemas as having high positive predictive value and low negative predictive value; they may demonstrate the presence of gender bias in a system, but not prove its absence. The work is focused on occupational gender bias and may not generalize to all manifestations of gender bias.

## 💾 Data

**Source**: 120 hand-written sentence templates instantiated using a list of 60 one-word occupations (from Caliskan et al., 2017, with three occupations added by the authors) and variations of participant and pronoun gender; uses Bergsma and Lin (2006) noun gender statistics and U.S. Bureau of Labor Statistics employment percentages for analysis.

**Size**: 720 sentences

**Format**: N/A

**Annotation**: Human validation via Amazon Mechanical Turk with 10-way redundancy per sentence; raw agreement 94.9% over 7,200 annotations; majority-vote agreement with intended answers for 718 of 720 sentences (99.7%).

## 🔬 Methodology

**Methods**:
- Automated evaluation of coreference resolution systems using the Winogender schemas
- Comparison across three off-the-shelf system architectures: rule-based (RULE), statistical (STAT), and neural (NEURAL)
- Human validation via Amazon Mechanical Turk

**Metrics**:
- Accuracy
- Percentage of differing resolutions between male-female minimal pairs
- Pearson correlation (r) between system gender preference scores and external gender statistics (Bureau of Labor Statistics and Bergsma & Lin)

**Calculation**: Percentages computed as proportion of test sentences where system predictions differ across pronoun gender (e.g., percent of male-female minimal pair sentences resolved differently). System gender preference per occupation computed as difference in percent resolving female pronouns to OCCUPATION minus percent resolving male pronouns to OCCUPATION (range -100 to 100). Pearson r computed between these system preference scores and percent female by occupation from Bureau of Labor Statistics and from Bergsma & Lin (2006).

**Interpretation**: Non-zero differences in resolution across pronoun genders indicate gender sensitivity/bias in systems. Positive correlation with external gender statistics indicates system preferences align with real-world/textual gender distributions and can amplify those distributions in predictions.

**Baseline Results**: Across male-female minimal pair test sentences, percent resolved differently: RULE 68%, STAT 28%, NEURAL 13%. Male pronouns resolved as OCCUPATION vs female vs neutral: RULE 72% male / 29% female / 1% neutral; STAT 71% male / 63% female / 50% neutral; NEURAL 87% male / 80% female / 36% neutral. Systems perform worse on so-called "gotcha" sentences where pronoun gender conflicts with occupation majority gender (see Table 2). Correlations (Pearson r) between system bias scores and Bergsma & Lin and BLS statistics reported (example: B&L correlation 0.87 for RULE in Table 1).

**Validation**: All 720 sentences were validated on Amazon Mechanical Turk with 10 annotators per sentence; raw annotator agreement 94.9% (7,200 binary-choice annotations), and majority-vote matched intended answers for 718 of 720 sentences (99.7%).

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Fairness
- Accuracy

**Atlas Risks**:
- **Fairness**: Data bias, Output bias
- **Accuracy**: Poor model accuracy

**Demographic Analysis**: Per-occupation analysis correlating system gender preference with percent female by occupation from the U.S. Bureau of Labor Statistics and percent female in text from Bergsma & Lin (2006); identification of "gotcha" sentences and occupation-level breakdowns.

**Potential Harm**: Detects and aims to highlight gender-based overgeneralization and systematic gender bias in coreference systems that can lead to erroneous predictions and amplification of real-world and textual occupational gender disparities.

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
