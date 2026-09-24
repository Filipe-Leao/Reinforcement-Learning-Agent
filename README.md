# Reinforcement Learning Wrapper Evaluation and Hyperparameter Optimization

A reinforcement learning research project focused on evaluating environment wrappers and optimizing Proximal Policy Optimization (PPO) hyperparameters in the Gymnasium `LunarLander-v3` environment.

The project investigates how reward shaping, environmental disturbances, observation noise, action smoothing, and randomized initial conditions affect training and evaluation performance.

## Overview

This project provides an experimental pipeline for:

- Training PPO agents in the `LunarLander-v3` environment.
- Applying and comparing different environment wrappers.
- Optimizing PPO hyperparameters through Random Search and Grid Search.
- Validating selected configurations across multiple random seeds.
- Evaluating trained agents using reward and success-rate metrics.
- Visualizing training curves and episode-level performance.
- Applying statistical analysis to compare wrapper configurations.

The overall workflow is organized into four main stages:

```text
Random Search
      |
      v
Grid Search Refinement
      |
      v
Multi-Seed Validation
      |
      v
Final Evaluation and Analysis
```

## Research Objective

The main objective is to analyze whether environment modifications and wrapper-based interventions influence the learning behavior and performance of PPO agents.

The project compares a baseline environment against configurations that introduce:

- Reward shaping
- Wind forces
- Observation noise
- Action smoothing
- Randomized spawn conditions
- A combined configuration containing multiple wrappers

Performance is assessed using episode rewards, success rates, reward distributions, and statistical comparisons.

## Environment and Algorithm

### Environment

- **Environment:** `LunarLander-v3`
- **Framework:** Gymnasium
- **Maximum episode length:** 1,200 steps in the visualization workflow
- **Success threshold:** Episode reward greater than or equal to 200

### Reinforcement Learning Algorithm

The project uses Proximal Policy Optimization (PPO), loaded and trained through Stable-Baselines3.

The optimization process explores several PPO hyperparameters, including:

| Hyperparameter | Search Strategy |
|---|---|
| `learning_rate` | Log-uniform sampling and local refinement |
| `n_steps` | Discrete choices |
| `batch_size` | Discrete choices |
| `n_epochs` | Integer sampling |
| `gamma` | Uniform sampling |
| `gae_lambda` | Uniform sampling |
| `ent_coef` | Uniform sampling |
| `clip_range` | Uniform sampling |
| `vf_coef` | Uniform sampling |

## Wrapper Configurations

The notebook implements an evaluation workflow for comparing the following configurations:

| Configuration | Description |
|---|---|
| `none` | Baseline environment without additional wrappers |
| `all` | Combined wrapper configuration |
| `action_smoothing` | Uses action smoothing |
| `windforce` | Adds wind-related environmental forces |
| `random_spawn` | Randomizes initial spawn conditions |
| `observationwrapper` | Adds noise to environment observations |

The wrapper implementation includes the following components:

- `RewardShapingWrapper`
- `WindForceWrapper`
- `ObservationNoiseWrapper`
- `ActionSmoothingWrapper`
- `RandomSpawnWrapper`

The exact wrapper parameters should be reviewed in the notebook before reproducing or extending the experiments.

## Hyperparameter Optimization Pipeline

### Phase 1: Random Search

Random Search explores a broad hyperparameter space by sampling parameter combinations from predefined distributions.

The default pipeline supports early stopping based on:

- Mean reward
- Success rate

The implementation evaluates each sampled configuration and calculates a combined score:

```python
score = mean_reward + success_rate * 100
```

This score is used to track and compare candidate configurations during the search.

### Phase 2: Grid Search Refinement

Grid Search refines the best candidates found during Random Search.

The refinement process creates a local search space around selected parameters, including:

- Learning rate variations
- Neighboring `n_steps` values
- Neighboring batch sizes
- Gamma variations
- Entropy coefficient variations

The optimized grid search tracks the top-performing configurations and supports early stopping when the configured thresholds are reached.

### Phase 3: Multi-Seed Validation

The selected hyperparameters are evaluated using multiple random seeds:

```python
seeds = [42, 123, 777]
```

Multi-seed validation is intended to assess the consistency of the selected configuration and reduce dependence on a single random initialization.

### Phase 4: Final Analysis

The final stage consolidates the experimental results and supports comparisons between wrapper configurations.

The analysis includes reward statistics, success rates, visualizations, and non-parametric statistical testing.

## Evaluation Metrics

The project uses the following evaluation metrics:

### Mean Reward

The average episode reward over the evaluation episodes.

### Success Rate

The proportion of episodes in which the agent reaches the defined success threshold.

In the notebook, success is defined as:

```python
episode_reward >= 200
```

### Reward Distribution

The project analyzes reward distributions using:

- Boxplots
- Violin plots
- Mean reward with 95% confidence intervals
- Median reward
- Standard deviation
- Interquartile range (IQR)

### Statistical Testing

The notebook includes the Mann–Whitney U test to compare reward samples between two wrapper configurations.

The test is non-parametric and is used to assess whether the reward distributions differ statistically under the selected comparison setup.

## Visualization

The project includes functionality for:

- Plotting raw reward curves
- Plotting smoothed reward curves
- Comparing multiple configurations
- Visualizing trained agents in the environment
- Summarizing episode rewards and episode lengths

The visualization workflow supports:

- `human` rendering for interactive visualization
- `rgb_array` rendering for programmatic video or frame-based workflows

## Experimental Workflow

The final wrapper comparison follows this general process:

1. Define or load optimized PPO hyperparameters.
2. Train a model for each wrapper configuration.
3. Save the trained model and monitoring data.
4. Locate the trained model checkpoint.
5. Evaluate the model over multiple episodes.
6. Record reward and success-rate metrics.
7. Visualize selected episodes.
8. Compare the results across configurations.
9. Apply statistical analysis when required.

The notebook uses 250,000 training timesteps and seed `42` in the final wrapper comparison workflow.

## Project Structure

The notebook generates experiment outputs using directories similar to the following structure:

```text
experiments/
├── <experiment_name>/
│   ├── none/
│   │   └── seed42/
│   │       ├── monitor.csv
│   │       └── model files
│   ├── all/
│   │   └── seed42/
│   ├── action_smoothing/
│   │   └── seed42/
│   ├── windforce/
│   │   └── seed42/
│   ├── random_spawn/
│   │   └── seed42/
│   └── observationwrapper/
│       └── seed42/
│
└── hpo_pipeline_<experiment_name>/
    ├── phase1_random_search/
    ├── phase2_grid_refinement/
    └── phase3_multi_seed_validation/
```

The exact directory structure may vary depending on the selected experiment name and output configuration.

## Installation

The notebook relies on Python-based reinforcement learning, simulation, data analysis, and visualization libraries.

A typical environment can be prepared with:

```bash
python -m venv .venv
```

Activate the virtual environment:

### Linux and macOS

```bash
source .venv/bin/activate
```

### Windows

```powershell
.venv\Scripts\activate
```

Install the dependencies used by the project:

```bash
pip install gymnasium
pip install stable-baselines3
pip install numpy pandas matplotlib seaborn scipy
pip install "gymnasium[box2d]"
```

Depending on the local system and Gymnasium version, additional Box2D-related dependencies may be required.

## Running the Project

The project is implemented as a Jupyter Notebook.

Start Jupyter:

```bash
jupyter notebook
```

Open the notebook and execute the cells in the intended order.

The general execution sequence is:

1. Import dependencies and define wrappers.
2. Define training and evaluation functions.
3. Configure the experiment.
4. Run hyperparameter optimization.
5. Extract the selected hyperparameters.
6. Train the wrapper configurations.
7. Evaluate the trained models.
8. Generate visualizations and statistical summaries.

## Reproducibility Considerations

The notebook uses explicit seeds in several stages of the experimental workflow, including training, evaluation, and multi-seed validation.

However, complete reproducibility may depend on:

- Python version
- Library versions
- Operating system
- Environment implementation
- Hardware and numerical operations
- Randomness introduced by the environment and wrappers
- Training configuration and execution order

For reliable comparisons, document the software versions, hardware configuration, selected seeds, and complete hyperparameter settings for each experiment.

## Limitations

The notebook is an experimental research workflow rather than a packaged production library.

Before reproducing the experiments, verify the following:

- All wrapper classes are defined and available.
- The required environment dependencies are installed.
- The PPO model and environment configurations are compatible.
- The output directories have sufficient storage.
- The selected hyperparameters match the intended experiment.
- The evaluation protocol is consistent across configurations.
- Results are interpreted together with their random seeds and statistical uncertainty.

The notebook contains training and evaluation workflows, but the README does not claim a specific performance improvement because the final experimental results are not summarized here.

## Future Improvements

Potential improvements to the project include:

- Adding a dedicated `requirements.txt` or `pyproject.toml`.
- Separating wrappers, training utilities, evaluation functions, and plotting utilities into Python modules.
- Adding automated experiment configuration through YAML or JSON files.
- Recording library versions and hardware information.
- Extending multi-seed experiments for stronger statistical reliability.
- Adding automated result aggregation and experiment tracking.
- Exporting final plots and summary tables to a dedicated results directory.
- Adding unit tests for wrapper behavior and evaluation functions.
- Including confidence intervals and effect-size measurements in the statistical analysis.

## License

No license is specified in the provided notebook.

If this project is intended for public distribution, add an appropriate license file, such as an MIT License, before publishing.

## Acknowledgements

This project builds on the Gymnasium reinforcement learning environment ecosystem and Stable-Baselines3 PPO implementations.
