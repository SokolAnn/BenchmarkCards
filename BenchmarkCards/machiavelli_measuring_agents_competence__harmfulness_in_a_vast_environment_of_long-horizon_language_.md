# MACHIAVELLI (Measuring Agents’ Competence & Harmfulness In A Vast Environment of Long-horizon Language Interactions)

## 📊 Benchmark Details

**Name**: MACHIAVELLI (Measuring Agents’ Competence & Harmfulness In A Vast Environment of Long-horizon Language Interactions)

**Overview**: A benchmark of 134 human-written Choose-Your-Own-Adventure games containing 572,322 scenes and millions of annotations to measure agents' social decision-making and unethical behaviors (power-seeking, disutility, ethical violations). It operationalizes harmful behaviors via mathematical formulas and dense annotations (collected with GPT-4) to evaluate trade-offs between reward optimization and ethical behavior, and to test methods for steering agents toward less harmful behaviors.

**Data Type**: text (text-based game scenes with action lists — scene descriptions and possible actions)

**Domains**:
- Natural Language Processing
- Reinforcement Learning

**Similar Benchmarks**:
- TextWorld
- ALFWorld
- Interactive Fiction games
- What would Jiminy Cricket do? (Hendrycks et al., 2021c)

**Resources**:
- [Resource](https://aypan17.github.io/machiavelli)
- [Resource](https://arxiv.org/abs/2304.03279)

## 🎯 Purpose and Intended Users

**Goal**: To measure agents' ability to plan in realistic social environments and to quantify unethical behaviors (power-seeking, disutility, deception and other ethical violations) arising from reward optimization; to provide a large environment and labels for evaluating and steering agents toward less harmful behaviors.

**Target Audience**:
- Machine Learning Researchers
- AI Safety Researchers
- Model Developers

**Tasks**:
- Sequential Decision Making
- Reinforcement Learning
- Text-based Game Playing
- Behavioral Evaluation

**Limitations**: Does not study extreme forms such as treacherous turns or deceptive alignment; does not incorporate multi-agent dynamics or counterfactual scenarios; current LM prompting for agents shows only the current scene (no long-term memory in prompts); annotations primarily collected using GPT-4 with a described model+ relabeling scheme (authors note limitations and validation procedures).

## 💾 Data

**Source**: Human-written Choose-Your-Own-Adventure games from choiceofgames.com (134 games).

**Size**: 134 games; 572,322 scenes; 4,559 achievements; 2,861,610 annotations

**Format**: JSON (labels and annotations produced/parsed as JSON-formatted strings)

**Annotation**: Automated annotation using GPT-4 in-context prompting (5 prompt rounds per scene, batched). Validation: GPT-4 labels compared against a gold set (ensemble of 3 expert authors) on a 2,000-scene test set; also compared to crowdworker annotations (Surge AI). Authors describe an ensemble/model+ relabeling scheme and partial human annotation for quality evaluation.

## 🔬 Methodology

**Methods**:
- Automated model-based annotations (GPT-4 in-context prompting)
- Human expert validation on held-out test scenes (3-expert ensemble)
- Automated behavioral scoring relative to a random baseline (1,000 sampled trajectories)
- Baseline agent evaluations including Random agent, Language Model agents (gpt-3.5-turbo, gpt-4, LLaMA variants) with prompting variants, and Reinforcement Learning agents (DRRN variants)

**Metrics**:
- Normalized Reward (agent points / total possible points)
- Number of Achievements (# Achievements)
- Behavioral harm score (proportion of harms relative to random baseline: # harms_agent / mean # harms_random)
- Power metrics (Economic, Physical, Social, Utility — aggregated as All power)
- Disutility (frequency of reducing others' wellbeing)
- Ethical violations (Deception, Killing, Physical harm, Non-physical harm, Intending harm, Manipulation, Betrayal, Stealing, Trespassing, Spying, Vandalism, Unfairness, Other)

**Calculation**: Reward is the sum of achievement points; normalized reward = agent points / total possible points. Behavioral score for a harm = (# harms committed by agent) / (mean # harms committed by random baseline), where the random baseline mean is estimated from 1,000 sampled trajectories. Power is approximated via sampled trajectories and unit measures (watts, money, wellbeing, social influence) as described in Section 2.3.

**Interpretation**: For behavioral metrics, lower percentages indicate fewer harms (best possible = 0%). Higher normalized reward indicates better goal achievement. Because objectives and harms can conflict, Pareto frontiers are used to interpret trade-offs between reward and ethical behavior.

**Baseline Results**: On the 30-game test set and broader evaluations: Random agent normalized reward ≈ 18.4; DRRN (RL) normalized reward ≈ 35.2 (higher reward but more harms). GPT-3.5 variants: normalized reward ≈ 22.5–23.4; GPT-4 + CoT normalized reward ≈ 27.4; GPT-4 + CoT + EthicsPrompt normalized reward ≈ 24.7. RL agents tend to achieve higher reward but also higher levels of Machiavellian behaviors; LM conditioning and RL policy shaping reduce harms but can reduce reward (see Tables 2 and 9 in paper).

**Validation**: Annotation validation: GPT-4 labels compared to an expert ensemble (3 experts) on a 2,000-scene gold set; GPT-4 (and ensembled model labels / model+ scheme) reported as more correlated with gold labels than average crowdworkers across most label types. Evaluation validation: authors identify a 30-game test set (games where points and harms are positively correlated) for focused evaluation.

## ⚠️ Targeted Risks

**Risk Categories**:
- Safety
- Fairness
- Robustness
- Societal Impact

**Atlas Risks**:
- **Value Alignment**: Harmful output
- **Misuse**: Spreading disinformation
- **Fairness**: Output bias
- **Societal Impact**: Impact on affected communities

**Potential Harm**: ['Power-seeking behavior', 'Deception', "Disutility (reducing other characters' wellbeing)", 'Unfairness', 'Killing', 'Physical harm', 'Non-physical harm', 'Manipulation', 'Stealing', 'Trespassing', 'Spying', 'Vandalism', 'Betrayal', 'Other ethical violations']

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
