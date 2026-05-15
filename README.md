# Vision-and-Language Navigation using CMA Policy in Habitat Simulator

> Vision-and-Language Navigation (VLN) agent built using Habitat-Lab, CMA Policy, Matterport3D, and R2R-VLNCE datasets for embodied AI navigation tasks.

---

# Overview

This project implements and evaluates a Vision-and-Language Navigation (VLN) agent using the Cross-Modal Attention (CMA) policy architecture in Habitat Simulator.

The agent learns to navigate realistic indoor 3D environments from natural language instructions by combining:

- Visual perception
- Language understanding
- Cross-modal attention
- Sequential decision making
- Imitation learning

The implementation is based on the VLN-CE framework using Habitat-Lab.

---

# Features

- CMA-based VLN agent
- Habitat-Lab + Habitat-Sim integration
- Matterport3D environment support
- LSTM instruction encoder
- ResNet visual encoder
- Cross-modal attention fusion
- DAgger imitation learning
- Evaluation using SR and SPL metrics
- Ablation and generalization studies

---

# Repository Structure

```text
.
├── habitat_extensions/
├── sbatch_scripts/
├── scripts/
├── vlnce_baselines/
├── LICENSE
├── README.md
├── pyproject.toml
├── requirements.txt
├── run.py
├── stats_RandomAgent_val_unseen.json
├── train.log
└── visual.py
````

---

# System Architecture

```text
Instruction
    ↓
Language Encoder (LSTM)

RGB/Depth Observations
    ↓
Visual Encoder (ResNet)

Cross-Modal Attention (CMA)
    ↓
RNN State Encoder
    ↓
Policy Head
    ↓
Navigation Action
```

---

# Datasets Used

## Matterport3D (MP3D)

Realistic indoor 3D scans containing:

* Multiple room layouts
* Navigation meshes
* RGB and depth observations
* Diverse scene structures

## R2R_VLNCE_v1-3_preprocessed

Vision-and-Language Navigation dataset containing:

* Natural language instructions
* Expert trajectories
* Continuous navigation environments

---

# Action Space

| Action       | Description    |
| ------------ | -------------- |
| MOVE_FORWARD | Move ahead     |
| TURN_LEFT    | Rotate left    |
| TURN_RIGHT   | Rotate right   |
| STOP         | End navigation |

---

# Model Components

## Visual Encoder

A pretrained ResNet-based encoder extracts:

* Semantic scene information
* Spatial layouts
* Navigational cues
* Object features

---

## Language Encoder

An LSTM-based encoder converts instructions into contextual embeddings.

Example instruction:

```text
"Turn right near the kitchen"
```

---

## Cross-Modal Attention (CMA)

The CMA module aligns:

* Visual observations
* Language instructions

This enables grounding of instruction words to relevant visual regions.

Example:

```text
"Turn left at the staircase"
```

The model focuses attention on:

* Staircase-related words
* Staircase regions in the environment

---

## Recurrent State Encoder

Maintains temporal memory for:

* Navigation history
* Previous observations
* Instruction progress tracking

---

## Policy Head

Predicts the next navigation action:

* FORWARD
* LEFT
* RIGHT
* STOP

---

# Training Pipeline

The agent is trained using DAgger imitation learning.

```text
Environment Rollout
    ↓
Expert Action Collection
    ↓
Trajectory Aggregation
    ↓
Policy Training
    ↓
Updated Policy
```

---

# Hyperparameters

| Hyperparameter | Value  |
| -------------- | ------ |
| Learning Rate  | 2.5e-4 |
| Batch Size     | 5      |
| Epochs         | 45     |
| Optimizer      | Adam   |
| Hidden Size    | 256    |

---

# Evaluation Metrics

## Success Rate (SR)

Measures whether the agent reaches the goal successfully.

```math
SR = Successful Episodes / Total Episodes
```

## Success weighted by Path Length (SPL)

Measures both success and trajectory efficiency.

```math
SPL = (1/N) Σ Si * (li / max(pi, li))
```

Where:

* `Si` = Success indicator
* `li` = Shortest path length
* `pi` = Agent path length

---

# Results

| Metric            | Seen   | Unseen |
| ----------------- | ------ | ------ |
| Success Rate (SR) | 0.3000 | 0.3600 |
| SPL               | 0.2583 | 0.3393 |

---

# Generalization Study

## Unseen Environment Evaluation

Observations:

* Performance decreases on unseen scenes
* CMA improves robustness
* Scene diversity affects navigation efficiency

---

## Paraphrased Instructions

Example:

```text
Original:
"Turn left at the sofa"

Paraphrased:
"Take a left near the couch"
```

Observations:

* Minor degradation in performance
* Semantic similarity preserved navigation quality

---

## Reduced Training Data

Observations:

* Smaller datasets reduce SR and SPL
* Larger datasets improve generalization

---

# Ablation Study

## Frozen Visual Encoder

Only the following modules were trained:

* Cross-modal attention
* RNN encoder
* Policy head

Observations:

* Faster convergence
* Lower SR and SPL
* Reduced adaptability

This highlights the importance of visual feature fine-tuning.

---

# Challenges Faced

* High GPU memory usage
* Large DAgger trajectory storage
* Long training times
* Habitat-Sim dependency conflicts
* Difficulty balancing SR and SPL
* Generalization gap between seen and unseen environments

---

# Limitations

* Computationally expensive training
* Dependence on pretrained visual encoders
* Difficulty handling ambiguous instructions
* Reduced robustness in unseen environments

---

# Future Work

* Transformer-based multimodal fusion
* Larger language models
* Better exploration strategies
* Memory-augmented navigation
* Reinforcement learning fine-tuning

---

# Installation

## Clone Repository

```bash
git clone <your-repo-link>
cd <repo-name>
```

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

# Download Checkpoints

Download pretrained CMA weights from the following Google Drive link:

```text
https://drive.google.com/drive/folders/1KeUseBAxJlHwUd20EzZlZHpuyCZg615T?usp=sharing
```

Place the downloaded weights inside:

```text
data/checkpoints/cma/
```

Example:

```text
data/checkpoints/cma/ckpt.11.pth
```

---

# Training

```bash
python run.py \
  --exp-config vlnce_baselines/config/r2r_baselines/cma.yaml \
  --run-type train
```

---

# Evaluation

```bash
python run.py \
  --exp-config vlnce_baselines/config/r2r_baselines/cma.yaml \
  --run-type eval
```

---

# TensorBoard

```bash
tensorboard --logdir data/tensorboard_dirs/
```

Open:

```text
http://localhost:6006
```

---

# Acknowledgements

* Habitat-Lab
* Habitat-Sim
* VLN-CE
* Matterport3D
* PyTorch
* Facebook AI Research

---

# References

1. Habitat-Lab: A Platform for Embodied AI Research
2. VLN-CE: Vision-and-Language Navigation in Continuous Environments
3. Matterport3D Dataset
4. Room-to-Room (R2R) Dataset
5. Cross-Modal Attention for Vision-Language Navigation
6. DAgger: Dataset Aggregation for Imitation Learning
