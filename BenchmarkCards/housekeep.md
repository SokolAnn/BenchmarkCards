# Housekeep

## 📊 Benchmark Details

**Name**: Housekeep

**Overview**: Housekeep is a benchmark to evaluate common-sense reasoning in the home for embodied AI. In Housekeep, an embodied agent must tidy a house by rearranging misplaced objects without explicit instructions specifying which objects need to be rearranged. The authors collect a dataset of where humans typically place objects in tidy and untidy houses (1799 objects, 268 object categories, 585 placements, and 105 rooms) and use it to generate initializations of unclean houses and define evaluation criteria for tidy houses. Housekeep evaluates how an agent is able to rearrange novel objects not seen during training and is instantiated in the Habitat simulator using iGibson scenes.

**Data Type**: multimodal (egocentric RGBD observations and human preference annotations / object-receptacle pairs)

**Domains**:
- Robotics
- Computer Vision
- Natural Language Processing

**Similar Benchmarks**:
- Transport Challenge
- Habitat 2.0
- Behavior
- VRR
- Taniguchi et al.
- Jiang et al.
- My House, My Rules

**Resources**:
- [Resource](https://yashkant.github.io/housekeep/)
- [Resource](https://www.youtube.com/watch?v=BcHmSzoNBYw)
- [Resource](https://www.youtube.com/watch?v=XccBpQNGN1Q)
- [Resource](https://app.ignitionrobotics.org/GoogleResearch/fuel/collections/Google%20Scanned%20Objects)
- [Resource](http://fetchrobotics.com/)
- [Resource](https://aihabitat.org/challenge/2021/)

## 🎯 Purpose and Intended Users

**Goal**: To benchmark the ability of embodied AI agents to use physical commonsense reasoning and infer rearrangement goals that mimic human-preferred placements of objects in indoor environments (tidying a house by rearranging misplaced objects without explicit instructions).

**Target Audience**:
- Embodied AI researchers
- Robotics researchers
- Machine Learning researchers

**Tasks**:
- Object Rearrangement
- Navigation
- Exploration
- Manipulation (Pick-and-Place)
- Commonsense Reasoning (physical/embodied)

**Limitations**: Housekeep provides additional sensors for the baseline (semantic and instance segmentation masks, relationship sensor, receptacle-room map) to scope the problem toward planning and commonsense reasoning; the authors note replacing these additional sensors with learned counterparts is future work to make baselines more realistic. The benchmark is instantiated in simulated iGibson/Habitat scenes (i.e., simulation-based).

## 💾 Data

**Source**: Human preference annotations collected via Amazon Mechanical Turk; objects and receptacles sourced from Amazon-Berkeley Objects, YCB Objects, Google Scanned Objects, ReplicaCAD (iGibson), and iGibson scenes; episodes instantiated in the Habitat simulator using iGibson scenes.

**Size**: 1799 objects; 268 object categories; 585 placements; 105 rooms; 395 unique receptacles over 32 categories; 14 interactive iGibson scenes; 128 distinct room-receptacles; 372 annotators; 1,633 hours of annotation reported in Appendix (paper also states 1500+ hours of effort). Episode splits: train: 9,000 episodes; val-seen: 200 episodes; val-unseen: 200 episodes; test-seen: 800 episodes; test-unseen: 800 episodes.

**Format**: N/A

**Annotation**: Crowdsourced via Amazon Mechanical Turk with 10 annotations per object-room pair. Annotators classify receptacles for an object-room pair into 'misplaced', 'correct', or 'implausible' and rank receptacles within 'misplaced' and 'correct' categories. Agreement measured using Fleiss' kappa; 8/10 highest-agreement annotations used in some analyses.

## 🔬 Methodology

**Methods**:
- Simulation-based evaluation in Habitat with iGibson scenes
- Automated metrics computed from episode start/end states
- Human annotation-based ground truth (for object-receptacle preferences)
- Ranking-based evaluation (language model-based and contrastive finetuning)

**Metrics**:
- Episode Success (ES)
- Object Success (OS)
- Soft Object Success (SOS)
- Rearrange Quality (RQ)
- Map Coverage (MC)
- Misplaced Objects Coverage (MOC)
- Pick and Place Efficiency (PPE)
- Mean Average Precision (mAP)
- Mean Reciprocal Rank (mrr)
- F1 Score

**Calculation**: Episode Success (ES): strict binary (all-or-none) metric = 1 iff all objects in episode are correctly placed at episode end. Object Success (OS): fraction of objects (initially misplaced or interacted) placed correctly at episode end. Soft Object Success (SOS): average fraction of annotators who agree an object is placed correctly. Rearrangement Quality (RQ): normalized value in [0,1] via mean reciprocal rank of the placed receptacle among correct receptacles (0 if misplaced). Map Coverage (MC): percentage of navigable map area explored. Misplaced Objects Coverage (MOC): fraction of misplaced objects discovered (object appears in FoV). Pick and Place Efficiency (PPE): minimum number of picks/places required divided by actual picks/places performed by agent. mAP computed across objects to compare ranked list of rooms/receptacles to annotator-provided correct lists. Threshold sL for classification chosen by grid search to maximize F1 on validation episodes.

**Interpretation**: Higher metric values indicate better performance. ES is strict and often low due to compounding errors; SOS is more lenient as it reflects annotator agreement; higher mAP indicates correct items are ranked higher. RQ ranges between 0 and 1 (higher is better).

**Baseline Results**: Ranking (ORR/OR) mAP (RoBERTa+CM): ORR train 0.81, val-unseen 0.79, test-unseen 0.81; OR train 1.0, val-unseen 0.65, test-unseen 0.65. Modular baseline (RoBERTa+CM ranking + frontier exploration) results: test-seen Object Success (OS) = 0.30; test-unseen OS = 0.23. Non-oracle episode success for non-oracle baseline is very low (e.g., ES ≈ 0.01 for the LM+FRT baseline in both test-seen and test-unseen splits). Oracle upper bounds show ES and OS = 1.00 when using oracle ranker and oracle exploration.

**Validation**: Human annotation quality validated using Fleiss' kappa (FK) agreement; authors report about 90% of collected data has fair to moderate agreement. The classification threshold sL for identifying correct receptacles is tuned on validation episodes by maximizing F1. Five non-overlapping object/scene splits provided for evaluation to test generalization.

## ⚠️ Targeted Risks

**Atlas Risks**:
No specific atlas risks defined

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
