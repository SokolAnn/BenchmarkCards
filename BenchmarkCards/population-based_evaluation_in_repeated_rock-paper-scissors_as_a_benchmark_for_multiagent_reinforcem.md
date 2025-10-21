# Population-based Evaluation in Repeated Rock-Paper-Scissors as a Benchmark for Multiagent Reinforcement Learning

## 📊 Benchmark Details

**Name**: Population-based Evaluation in Repeated Rock-Paper-Scissors as a Benchmark for Multiagent Reinforcement Learning

**Overview**: We propose a benchmark for multiagent learning based on repeated play of the simple game Rock, Paper, Scissors along with a population of forty-three tournament entries, some of which are intentionally sub-optimal. We describe metrics to measure the quality of agents based both on average returns and exploitability, and provide a population-based evaluation using head-to-head matches, exploitability approximations, and aggregate scoring.

**Data Type**: time-series (game trajectories / joint action sequences)

**Domains**:
- Reinforcement Learning
- Game Theory
- Multiagent Systems

**Similar Benchmarks**:
- OpenSpiel
- The Hanabi challenge
- Arcade Learning Environment

**Resources**:
- [Resource](https://openreview.net/forum?id=gQnJ7ODIAx)
- [GitHub Repository](https://github.com/google-deepmind/open_spiel/tree/master/open_spiel/data/paper_data/pbe_rrps)
- [Resource](https://arxiv.org/abs/2303.03196)

## 🎯 Purpose and Intended Users

**Goal**: To propose repeated Rock, Paper, Scissors (RRPS), a population of previous tournament bots, and population-based evaluation (PBE) as a new challenge in sequential decision-making with multiple agents that evaluates both average return and exploitability.

**Target Audience**:
- Multiagent Reinforcement Learning researchers
- Machine Learning researchers
- Reinforcement Learning practitioners

**Tasks**:
- Policy Evaluation
- Opponent Modeling
- Robustness Evaluation
- Sequential Decision-Making

**Limitations**: The benchmark requires a bot population and the approximation quality of within-population-exploitability depends on there being bots that can exploit population mistakes. The specific benchmark and bot population are restricted to the domain of RRPS. The proposed aggregate score addresses only the combination of maximizing reward and minimizing exploitability and may not generalize to other domains. The authors explicitly state they are not proposing PBE as a general evaluation methodology for all multiagent RL problems.

**Out of Scope Uses**:
- Using PBE as an evaluation methodology for comparing multiagent RL algorithms more generally (the paper states it is not proposing PBE for general MARL evaluation)

## 💾 Data

**Source**: Population of forty-three openly-available hand-crafted tournament bots (25 entrant bots and 18 seed bots, including greenberg and iocainepowder) integrated into OpenSpiel; RRPS environment implementation available within OpenSpiel (Lanctot et al., 2019).

**Size**: 43 bots; evaluations typically use 1,000 episodes per profile; each episode has K = 1000 plays (default K=1000); recall R default = 1 (unless otherwise noted).

**Format**: OpenSpiel data files (provided via the OpenSpiel repository; specific file format not specified in the paper).

**Annotation**: N/A

## 🔬 Methodology

**Methods**:
- Automated metrics: Population Return, Within-Population Exploitability, External-learned approximate exploitability
- Head-to-head pairwise evaluation (cross-table averaged over 1000 episodes)
- Approximate best-response estimation via running learning algorithms (e.g., Q-learning, IMPALA, DQN, BDQN, A2C) and taking maximum achieved opponent return
- Action prediction experiments using LSTM behavioral cloning (predictability analysis)
- Population-based training (PopRL) mixing self-play and population opponents with opponent-identification auxiliary task

**Metrics**:
- Population Return (average return per episode against a bot drawn uniformly at random)
- Within-Population Exploitability (WithinPopExpl: maximum opponent return taken over the bot population)
- External-learned approximate exploitability (maximum return achieved by learning algorithms used as exploiters)
- AggregateScore (AggregateScore = PopulationReturn - WithinPopExpl)
- Average return per episode
- Action prediction accuracy (proportion of time predicted action matched bot's action)

**Calculation**: PopulationReturn(π_i) = average return per episode when opponent is sampled uniformly from population. Exploitability Expl(π_i) = G0,-i,(π_i,b(π_i)) where b(π_i) is a best response (exact computation may be approximated by running learning algorithms). WithinPopExpl(π_i) = max_{π_-i in Population} E_{a~(π_i,π_-i)}[G0,-i]. AggregateScore(π_i) = PopulationReturn(π_i) - WithinPopExpl(π_i). Action prediction accuracy is proportion of times predicted action equals actual action.

**Interpretation**: Exploitability is non-negative and equals zero when an agent is not exploitable. Higher Population Return is better. AggregateScore balances maximizing return and minimizing exploitability; higher AggregateScore indicates a better balance. Action prediction accuracy > chance indicates learnable structure in bot behaviors.

**Baseline Results**: Selected results reported in the paper (averages over seeds/runs as reported): Top hand-crafted bots: greenberg — Population Return 288.15, Within-Population Exploitability 3.65, AggregateScore 284.50; iocainebot — Population Return 255.00, AggregateScore ~249.997. Top learning agents: PopRL — Population Return 258.00, Within-Population Exploitability 10.98, AggregateScore 247.02; LLM (Chinchilla 70B, zero-shot) — Population Return 201.00, AggregateScore 155.20; best independent RL baseline QL (R=10) — AggregateScore 8.10. (Values taken from Tables 1, 3, 4, and 7 in the paper.)

**Validation**: Approximate exploitability validated by training multiple learning algorithms (e.g., Q-learning, IMPALA) and taking the maximum achieved opponent return; within-population exploitability compared to external-learned exploitability and found to achieve on average 75.2% of external-learned exploitability. IMPALA generalization evaluated via cross-validation: train on 33 bots, evaluate on 10 held-out bots, averaged over 50 distinct held-out splits. Action prediction experiments used k-fold splits (30 train / 13 test) repeated experiments to assess generalization.

## ⚠️ Targeted Risks

**Atlas Risks**:
No specific atlas risks defined

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
