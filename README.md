# CS6910_Assignment1
CS6910_Assignment1
Sure, here's a README interaction for using the Neural Network model implemented in `train.py`:

---

# Neural Network Model Training

## Overview
This repository contains a Python script `train.py` that facilitates training a Neural Network model using hyperparameter sweeps. The script supports various image datasets and provides functionality to check class distribution, compute validation, test, and train accuracies.

## Requirements
- Python 3.x
- Install required dependencies using:
  ```
  pip install -r requirements.txt
  ```

## Usage
1. Clone the repository:
   ```
   git clone <repository-url>
   cd <repository-directory>
   ```

2. Prepare your dataset:
   - Ensure your dataset is properly formatted and split into train, validation, and test sets.
   - Supported datasets: MNIST, Fashion MNIST, and other image datasets.

3. Run the training script:
   - Execute `train.py` with the required arguments:
     ```
     python train.py -d <dataset> -e <epochs> -b <batch_size> -l <loss> -o <optimizer> -lr <learning_rate> -m <momentum> -beta <beta> -beta1 <beta1> -beta2 <beta2> -eps <epsilon> -w_i <weight_init> -nhl <num_layers> -sz <hidden_size> -a <activation>
     ```
     Replace `<dataset>` with your dataset name and provide values for other hyperparameters as required.

4. View results:
   - Upon completion, the script will display the validation, test, and train accuracies of the trained model.
   - Additionally, Wandb logs will provide detailed information about the training process and hyperparameter sweeps.

## Example
```bash
python train.py -d fashion_mnist -e 10 -b 32 -l cross_entropy -o adam -lr 0.001 -m 0.9 -beta 0.999 -beta1 0.9 -beta2 0.999 -eps 1e-8 -w_i xavier -nhl 3 -sz 128 -a relu
```

## Notes
- The `train.py` script supports hyperparameter sweeps using the Wandb library.
- Ensure your dataset is properly formatted and available in the specified directory.
- Experiment with different hyperparameter configurations to optimize model performance.
