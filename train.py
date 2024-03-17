{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "WARNING:tensorflow:From C:\\Users\\Amlan\\AppData\\Local\\Programs\\Python\\Python310\\lib\\site-packages\\keras\\src\\losses.py:2976: The name tf.losses.sparse_softmax_cross_entropy is deprecated. Please use tf.compat.v1.losses.sparse_softmax_cross_entropy instead.\n",
      "\n"
     ]
    }
   ],
   "source": [
    "import wandb\n",
    "import os\n",
    "os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'\n",
    "from sklearn.model_selection import train_test_split\n",
    "import numpy as np\n",
    "from keras.datasets import fashion_mnist, mnist\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "CLASS_NAMES = ['T-shirt/top', 'Trouser', 'Pullover', 'Dress', 'Coat', 'Sandal', 'Shirt', 'Sneaker', 'Bag', 'Ankle boot']"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [],
   "source": [
    "WANDB_PROJECT = \"myprojectname\"\n",
    "WANDB_ENTITY = \"myname\"\n",
    "DATASET = \"fashion_mnist\"\n",
    "EPOCHS = 10\n",
    "BATCH_SIZE = 32\n",
    "LOSS = \"mean_squared_error\"\n",
    "OPTIMIZER = \"sgd\"\n",
    "LEARNING_RATE = 0.001\n",
    "MOMENTUM = 0.8\n",
    "BETA = 0.5\n",
    "BETA1 = 0.9\n",
    "BETA2 = 0.999\n",
    "EPSILON = 1e-8\n",
    "WEIGHT_DECAY = 0.001\n",
    "WEIGHT_INIT = \"random\"\n",
    "NUM_LAYERS = 4\n",
    "HIDDEN_SIZE = 128\n",
    "ACTIVATION = \"sigmoid\""
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "wandb.login(key='8cd670a52fc28bf254ff6ff2b01f010982869e8d')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [],
   "source": [
    "class_names = ['T-shirt/top', 'Trouser', 'Pullover', 'Dress', 'Coat',\n",
    "               'Sandal', 'Shirt', 'Sneaker', 'Bag', 'Ankle boot']"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "(x_train, y_train), (x_test, y_test) = fashion_mnist.load__data()\n",
    "\n",
    "def log_examples():\n",
    "    wandb.init(project=\"cs6910-assignment-1\", entity='ge22m012')\n",
    "    # Log one image of each class\n",
    "    for i in range(10):\n",
    "        \n",
    "        idx = next(idx for idx, label in enumerate(y_train) if label == i)\n",
    "        \n",
    "        wandb.log({\"class_photos\": [wandb.Image(x_train[idx], caption=CLASS_NAMES[i])]})\n",
    "    wandb.finish()\n",
    "\n",
    "log_examples()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "wandb.finish()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "class FeedFNetwork():\n",
    "    def __init__(self, \n",
    "                Output_size=10,\n",
    "                hidden_layers=4, \n",
    "                input_size=784,\n",
    "                neurons=128,\n",
    "                out_act_function=\"softmax\", \n",
    "                weight_init=\"random\", \n",
    "                act_func=\"sigmoid\",\n",
    "                init_toggle=True):\n",
    "        self.output_activation_function = out_act_function\n",
    "        self.weights, self.biases = [],[] \n",
    "        self.input_size, self.Output_size = input_size, Output_size\n",
    "        self.activation_function, self.weight_init = act_func, weight_init\n",
    "        self.neurons, self.hidden_layers = neurons, hidden_layers\n",
    "\n",
    "        if init_toggle:\n",
    "            self.initialize_weights()\n",
    "            self.int_biases()\n",
    "\n",
    "    def initialize_weights(self):\n",
    "        self.weights.append(np.random.randn(self.input_size, self.neurons))\n",
    "        for _ in range(self.hidden_layers - 1):\n",
    "            self.weights.append(np.random.randn(self.neurons, self.neurons))\n",
    "        self.weights.append(np.random.randn(self.neurons, self.Output_size))\n",
    "\n",
    "        if self.weight_init == \"xavier\":\n",
    "            for i in range(len(self.weights)):\n",
    "                self.weights[i] = self.weights[i] * np.sqrt(1 / self.weights[i].shape[0])\n",
    "\n",
    "    def int_biases(self):\n",
    "        for _ in range(self.hidden_layers):\n",
    "            self.biases.append(np.zeros(self.neurons))\n",
    "        self.biases.append(np.zeros(self.Output_size))\n",
    "    \n",
    "    def activation(self, x):\n",
    "        if self.activation_function == \"sigmoid\":\n",
    "            return 1 / (1 + np.exp(-x))\n",
    "        elif self.activation_function == \"relu\":\n",
    "            return np.maximum(0, x)\n",
    "        elif self.activation_function == \"identity\":\n",
    "            return x\n",
    "        elif self.activation_function == \"tanh\":\n",
    "            return np.tanh(x)\n",
    "        \n",
    "        else:\n",
    "            raise Exception(\"Invalid Activation-Function\")\n",
    "    \n",
    "    def output_activation(self, x):\n",
    "        if self.output_activation_function == \"softmax\":\n",
    "            max_x = np.max(x, axis=1)\n",
    "            \n",
    "            max_x = max_x.reshape(max_x.shape[0], 1)\n",
    "            \n",
    "            exp_x = np.exp(x - max_x)\n",
    "            softmax_mat = exp_x / np.sum(exp_x, axis=1).reshape(exp_x.shape[0], 1)\n",
    "            return softmax_mat\n",
    "        else:\n",
    "            raise Exception(\"Output activation function : Invalid \")\n",
    "    \n",
    "    def forward(self, x):\n",
    "        self.pre_activation, self.post_activation = [x], [x]\n",
    "\n",
    "        for i in range(self.hidden_layers):\n",
    "            self.pre_activation.append(np.matmul(self.post_activation[-1], self.weights[i]) + self.biases[i])\n",
    "            self.post_activation.append(self.activation(self.pre_activation[-1]))\n",
    "            \n",
    "        self.pre_activation.append(np.matmul(self.post_activation[-1], self.weights[-1]) + self.biases[-1])\n",
    "        self.post_activation.append(self.output_activation(self.pre_activation[-1]))\n",
    "\n",
    "        return self.post_activation[-1]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "def loss(loss, y, y_pred):\n",
    "    if loss == \"cross_entropy\": # Cross Entropy\n",
    "        return -np.sum(y * np.log(y_pred))\n",
    "    elif loss == \"mean_squared_error\": # Mean Squared Error\n",
    "        return np.sum((y - y_pred) ** 2) / 2\n",
    "    else:\n",
    "        raise Exception(\"Invalid-loss-function\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "class back_propagation():\n",
    "    def __init__(self, \n",
    "                 nnetwork: FeedFNetwork, \n",
    "                 loss=\"cross_entropy\", \n",
    "                 act_func=\"sigmoid\"):\n",
    "        \n",
    "        self.nnetwork, self.loss, self.activation_function = nnetwork, loss, act_func\n",
    "        \n",
    "    def activation__derivatives(self, x):\n",
    "        \n",
    "        if self.activation_function == \"sigmoid\":\n",
    "            return x * (1 - x)\n",
    "        elif self.activation_function == \"tanh\":\n",
    "            return 1 - x ** 2\n",
    "        elif self.activation_function == \"relu\":\n",
    "            return (x > 0).astype(int)\n",
    "        elif self.activation_function == \"identity\":\n",
    "            return np.ones(x.shape)\n",
    "        else:\n",
    "            raise Exception(\"Invalid activation function\")\n",
    "        \n",
    "    \n",
    "    def loss_derivative(self, y, y_pred):\n",
    "        if self.loss == \"cross_entropy\":\n",
    "            return -y / (y_pred +(1e-6) )\n",
    "        elif self.loss == \"mean_squared_error\":\n",
    "            return (y_pred - y)\n",
    "        else:\n",
    "            raise Exception(\"Invalid loss function\")\n",
    "        \n",
    "\n",
    "    def output_activation__derivatives(self, y, y_pred):\n",
    "        if self.nnetwork.output_activation_function == \"softmax\":\n",
    "            # softmax derivative\n",
    "            return np.diag(y_pred) - np.outer(y_pred, y_pred)\n",
    "        else:\n",
    "            raise Exception(\"Invalid output activation function\")\n",
    "\n",
    "    def backward(self, y, y_pred):\n",
    "        self.D_weights, self.D_biases = [], []\n",
    "        self.d_h, self.d_a = [], []\n",
    "\n",
    "        self.d_h.append(self.loss_derivative(y, y_pred))\n",
    "        output_derivative_matrix = []\n",
    "        for i in range(y_pred.shape[0]):\n",
    "            output_derivative_matrix.append(np.matmul(self.loss_derivative(y[i], y_pred[i]), self.output_activation__derivatives(y[i], y_pred[i])))\n",
    "        self.d_a.append(np.array(output_derivative_matrix))\n",
    "\n",
    "        for i in range(self.nnetwork.hidden_layers, 0, -1):\n",
    "            self.D_weights.append(np.matmul(self.nnetwork.post_activation[i].T, self.d_a[-1]))\n",
    "            self.D_biases.append(np.sum(self.d_a[-1], axis=0))\n",
    "            self.d_h.append(np.matmul(self.d_a[-1], self.nnetwork.weights[i].T))\n",
    "            self.d_a.append(self.d_h[-1] * self.activation__derivatives(self.nnetwork.post_activation[i]))\n",
    "\n",
    "        self.D_weights.append(np.matmul(self.nnetwork.post_activation[0].T, self.d_a[-1]))\n",
    "        self.D_biases.append(np.sum(self.d_a[-1], axis=0))\n",
    "\n",
    "        self.D_weights.reverse()\n",
    "        self.D_biases.reverse()\n",
    "        for i in range(len(self.D_weights)):\n",
    "            self.D_weights[i] = self.D_weights[i] / y.shape[0]\n",
    "            self.D_biases[i] = self.D_biases[i] / y.shape[0]\n",
    "\n",
    "        return self.D_weights, self.D_biases"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "class Optimizer():\n",
    "    def __init__(self, \n",
    "                 nnetwork: FeedFNetwork, \n",
    "                 bp:back_propagation, \n",
    "                 lr=0.001, \n",
    "                 optimizer=\"sgd\", \n",
    "                 momentum=0.9,\n",
    "                 epsilon=1e-8,\n",
    "                 beta=0.9,\n",
    "                 beta1=0.9,\n",
    "                 beta2=0.999, \n",
    "                 t=0,\n",
    "                 decay=0):\n",
    "        \n",
    "        self.nnetwork, self.bp, self.lr, self.optimizer = nnetwork, bp, lr, optimizer\n",
    "        self.momentum, self.epsilon, self.beta1, self.beta2, self.beta = momentum, epsilon, beta1, beta2, beta\n",
    "        self.hweights = [np.zeros_like(w) for w in self.nnetwork.weights]\n",
    "        self.h_biases = [np.zeros_like(b) for b in self.nnetwork.biases]\n",
    "        self.hm_weights = [np.zeros_like(w) for w in self.nnetwork.weights]\n",
    "        self.hm_biases = [np.zeros_like(b) for b in self.nnetwork.biases]\n",
    "        self.t = t\n",
    "        self.decay = decay\n",
    "\n",
    "    def run(self, D_weights, D_biases):\n",
    "        if(self.optimizer == \"sgd\"):\n",
    "            self.sgd(D_weights, D_biases)\n",
    "        elif(self.optimizer == \"momentum\"):\n",
    "            self.momentum_gd(D_weights, D_biases)\n",
    "        elif(self.optimizer == \"nag\"):\n",
    "            self.nag(D_weights, D_biases)\n",
    "        elif(self.optimizer == \"rmsprop\"):\n",
    "            self.RMSProp(D_weights, D_biases)\n",
    "        elif(self.optimizer == \"adam\"):\n",
    "            self.Adam(D_weights, D_biases)\n",
    "        elif (self.optimizer == \"nadam\"):\n",
    "            self.NAdam(D_weights, D_biases)\n",
    "        else:\n",
    "            raise Exception(\"Invalid optimizer\")\n",
    "    \n",
    "\n",
    "\n",
    "    def momentum_gd(self, D_weights, D_biases):\n",
    "        \n",
    "        for i in range(self.nnetwork.hidden_layers + 1):\n",
    "            self.hweights[i] = self.momentum * self.hweights[i] + D_weights[i]\n",
    "            self.h_biases[i] = self.momentum * self.h_biases[i] + D_biases[i]\n",
    "\n",
    "            self.nnetwork.weights[i] -= self.lr * (self.hweights[i] + self.decay * self.nnetwork.weights[i])\n",
    "            self.nnetwork.biases[i] -= self.lr * (self.h_biases[i] + self.decay * self.nnetwork.biases[i])\n",
    "\n",
    "    def nag(self, D_weights, D_biases):        \n",
    "        for i in range(self.nnetwork.hidden_layers + 1):\n",
    "            self.h_biases[i] = self.momentum * self.h_biases[i] + D_biases[i]\n",
    "            self.hweights[i] = self.momentum * self.hweights[i] + D_weights[i]\n",
    "            \n",
    "\n",
    "            self.nnetwork.weights[i] -= self.lr * (self.momentum * self.hweights[i] + D_weights[i] + self.decay * self.nnetwork.weights[i])\n",
    "            self.nnetwork.biases[i] -= self.lr * (self.momentum * self.h_biases[i] + D_biases[i] + self.decay * self.nnetwork.biases[i])\n",
    "    def sgd(self, D_weights, D_biases):\n",
    "        for i in range(self.nnetwork.hidden_layers + 1):\n",
    "            self.nnetwork.biases[i] -= self.lr * (D_biases[i] + self.decay * self.nnetwork.biases[i])\n",
    "            self.nnetwork.weights[i] -= self.lr * (D_weights[i] + self.decay * self.nnetwork.weights[i])\n",
    "\n",
    "    def RMSProp(self, D_weights, D_biases):\n",
    "        for i in range(self.nnetwork.hidden_layers + 1):\n",
    "            self.hweights[i] =   self.momentum * self.hweights[i] + (1 - self.momentum) * D_weights[i]**2\n",
    "            self.h_biases[i] = self.momentum * self.h_biases[i] + (1 - self.momentum) * D_biases[i]**2\n",
    "\n",
    "            self.nnetwork.weights[i] -= (self.lr / (np.sqrt(self.hweights[i]) + self.epsilon)) * D_weights[i] + self.decay * self.nnetwork.weights[i] * self.lr\n",
    "            self.nnetwork.biases[i] -= (self.lr / (np.sqrt(self.h_biases[i]) + self.epsilon)) * D_biases[i] + self.decay * self.nnetwork.biases[i] * self.lr\n",
    "\n",
    "    def Adam(self, D_weights, D_biases):\n",
    "        for i in range(self.nnetwork.hidden_layers + 1):\n",
    "            self.hm_weights[i] = self.beta1 * self.hm_weights[i] + (1 - self.beta1) * D_weights[i]\n",
    "            self.hm_biases[i] = self.beta1 * self.hm_biases[i] + (1 - self.beta1) * D_biases[i]\n",
    "\n",
    "            self.hweights[i] = self.beta2 * self.hweights[i] + (1 - self.beta2) * D_weights[i]**2\n",
    "            self.h_biases[i] = self.beta2 * self.h_biases[i] + (1 - self.beta2) * D_biases[i]**2\n",
    "\n",
    "            self.hm_weights_hat = self.hm_weights[i] / (1 - self.beta1**(self.t + 1))\n",
    "            self.hm_biases_hat = self.hm_biases[i] / (1 - self.beta1**(self.t + 1))\n",
    "\n",
    "            self.hweights_hat = self.hweights[i] / (1 - self.beta2**(self.t + 1))\n",
    "            self.h_biases_hat = self.h_biases[i] / (1 - self.beta2**(self.t + 1))\n",
    "\n",
    "            self.nnetwork.weights[i] -= self.lr * (self.hm_weights_hat / ((np.sqrt(self.hweights_hat)) + self.epsilon)) + self.decay * self.nnetwork.weights[i] * self.lr\n",
    "            self.nnetwork.biases[i] -= self.lr * (self.hm_biases_hat / ((np.sqrt(self.h_biases_hat)) + self.epsilon)) + self.decay * self.nnetwork.biases[i] * self.lr\n",
    "\n",
    "    def NAdam(self, D_weights, D_biases):\n",
    "        for i in range(self.nnetwork.hidden_layers + 1):\n",
    "            self.hm_weights[i] = self.beta1 * self.hm_weights[i] + (1 - self.beta1) * D_weights[i]\n",
    "            self.hm_biases[i] = self.beta1 * self.hm_biases[i] + (1 - self.beta1) * D_biases[i]\n",
    "\n",
    "            self.hweights[i] = self.beta2 * self.hweights[i] + (1 - self.beta2) * D_weights[i]**2\n",
    "            self.h_biases[i] = self.beta2 * self.h_biases[i] + (1 - self.beta2) * D_biases[i]**2\n",
    "\n",
    "            self.hm_weights_hat = self.hm_weights[i] / (1 - self.beta1 ** (self.t + 1))\n",
    "            self.hm_biases_hat = self.hm_biases[i] / (1 - self.beta1 ** (self.t + 1))\n",
    "\n",
    "            self.hweights_hat = self.hweights[i] / (1 - self.beta2 ** (self.t + 1))\n",
    "            self.h_biases_hat = self.h_biases[i] / (1 - self.beta2 ** (self.t + 1))\n",
    "\n",
    "            temp_update_w = self.beta1 * self.hm_weights_hat + ((1 - self.beta1) / (1 - self.beta1 ** (self.t + 1))) * D_weights[i]\n",
    "            temp_update_b = self.beta1 * self.hm_biases_hat + ((1 - self.beta1) / (1 - self.beta1 ** (self.t + 1))) * D_biases[i]\n",
    "\n",
    "            self.nnetwork.weights[i] -= self.lr * (temp_update_w / ((np.sqrt(self.hweights_hat)) + self.epsilon)) + self.decay * self.nnetwork.weights[i] * self.lr\n",
    "            self.nnetwork.biases[i] -= self.lr * (temp_update_b / ((np.sqrt(self.h_biases_hat)) + self.epsilon)) + self.decay * self.nnetwork.biases[i] * self.lr\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "wandb.login()\n",
    "wandb.WANDB_NOTEBOOK_NAME = \"Assignment1.ipynb\""
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "import argparse\n",
    "\n",
    "# Parse arguments\n",
    "parser = argparse.ArgumentParser()\n",
    "parser.add_argument(\"-wp\", \"--wandb_project\", type=str, default=WANDB_PROJECT, help=\"Wandb project name\", required=True)\n",
    "parser.add_argument(\"-we\", \"--wandb_entity\", type=str, default=WANDB_ENTITY, help=\"Wandb entity name\", required=True)\n",
    "parser.add_argument(\"-d\", \"--dataset\", type=str, default=DATASET, help=\"Dataset to use choices=['fashion_mnist', 'mnist']\")\n",
    "parser.add_argument(\"-e\", \"--epochs\", type=int, default=EPOCHS, help=\"Number of epochs\")\n",
    "parser.add_argument(\"-b\", \"--batch_size\", type=int, default=BATCH_SIZE, help=\"Batch size\")\n",
    "parser.add_argument(\"-l\", \"--loss\", type=str, default=LOSS, help=\"Loss function to use choices=['cross_entropy', 'mean_squared_error']\")\n",
    "parser.add_argument(\"-o\", \"--optimizer\", type=str, default=OPTIMIZER, help=\"Optimizer to use choices=['sgd', 'momentum', 'nag', 'rmsprop', 'adam', 'nadam']\")\n",
    "parser.add_argument(\"-lr\", \"--learning_rate\", type=float, default=LEARNING_RATE, help=\"Learning rate\")\n",
    "parser.add_argument(\"-m\", \"--momentum\", type=float, default=MOMENTUM, help=\"Momentum for Momentum and NAG\")\n",
    "parser.add_argument(\"-beta\", \"--beta\", type=float, default=BETA, help=\"Beta for RMSProp\")\n",
    "parser.add_argument(\"-beta1\", \"--beta1\", type=float, default=BETA1, help=\"Beta1 for Adam and Nadam\")\n",
    "parser.add_argument(\"-beta2\", \"--beta2\", type=float, default=BETA2, help=\"Beta2 for Adam and Nadam\")\n",
    "parser.add_argument(\"-eps\", \"--epsilon\", type=float, default=EPSILON, help=\"Epsilon for Adam and Nadam\")\n",
    "parser.add_argument(\"-w_d\", \"--weight_decay\", type=float, default=WEIGHT_DECAY, help=\"Weight decay\")\n",
    "parser.add_argument(\"-w_i\", \"--weight_init\", type=str, default=WEIGHT_INIT, help=\"Weight initialization choices=['random', 'xavier']\")\n",
    "parser.add_argument(\"-nhl\", \"--num_layers\", type=int, default=NUM_LAYERS, help=\"Number of hidden layers\")\n",
    "parser.add_argument(\"-sz\", \"--hidden_size\", type=int, default=HIDDEN_SIZE, help=\"Hidden size\")\n",
    "parser.add_argument(\"-a\", \"--activation\", type=str, default=ACTIVATION, help=\"Activation function choices=['sigmoid', 'tanh', 'relu']\")\n",
    "\n",
    "args = parser.parse_args()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [
    {
     "ename": "SyntaxError",
     "evalue": "invalid syntax. Perhaps you forgot a comma? (56583639.py, line 10)",
     "output_type": "error",
     "traceback": [
      "\u001b[1;36m  Cell \u001b[1;32mIn [2], line 10\u001b[1;36m\u001b[0m\n\u001b[1;33m    'parameters': {\u001b[0m\n\u001b[1;37m                  ^\u001b[0m\n\u001b[1;31mSyntaxError\u001b[0m\u001b[1;31m:\u001b[0m invalid syntax. Perhaps you forgot a comma?\n"
     ]
    }
   ],
   "source": [
    "wandb.login()\n",
    "wandb.WANDB_NOTEBOOK_NAME = \"Assignment1.ipynb\"\n",
    "sweep_configuration = {\n",
    "    'method': 'random',\n",
    "    'name': 'sweep -3nd',\n",
    "    'metric': {\n",
    "        'goal': 'maximize',\n",
    "        'name': 'val_accuracy'\n",
    "    },\n",
    "    # 'parameters': {\n",
    "    #             'input_size': {\n",
    "    #                 'value': 784\n",
    "    #             },\n",
    "    #             'weight_init': {\n",
    "    #                 'values': ['xavier', 'random']\n",
    "    #             },\n",
    "    #             'learning_rate': {\n",
    "    #                 'values': [0.0001, 0.0005, 0.001, 0.005, 0.01, 0.05, 0.1]\n",
    "    #             },\n",
    "    #             'loss': {\n",
    "    #                 'value': 'cross_entropy'\n",
    "    #             },\n",
    "    #             'neurons': {\n",
    "    #                 'values': [16, 32, 64, 128]\n",
    "    #             },\n",
    "    #             'hidden_layers': {\n",
    "    #                 'values': [1, 2, 3, 4]\n",
    "    #             },\n",
    "    #             'beta1': {\n",
    "    #                 'value': 0.9\n",
    "    #             },\n",
    "    #             'beta2': {\n",
    "    #                 'value': 0.999\n",
    "    #             },\n",
    "    #             'output_activation': {\n",
    "    #                 'value': 'softmax'\n",
    "    #             },\n",
    "    #             'momentum': {\n",
    "    #                 'values': [0.7, 0.8, 0.9]\n",
    "    #             },\n",
    "    #             'epsilon': {\n",
    "    #                 'value': 1e-8\n",
    "    #             },\n",
    "    #             'epochs': {\n",
    "    #                 'value': 10\n",
    "    #             },\n",
    "    #             'dataset': {\n",
    "    #                 'value': 'fashion_mnist'\n",
    "    #             },\n",
    "    #             'activation': {\n",
    "    #                 'values': ['relu', 'tanh', 'sigmoid', 'identity']\n",
    "    #             },\n",
    "    #             'optimizer': {\n",
    "    #                 'values': ['sgd', 'momentum', 'nag', 'rmsprop', 'adam', 'nadam']\n",
    "    #             },\n",
    "    #             'decay': {\n",
    "    #                 'values': [0, 0.5, 0.0005]\n",
    "    #             },\n",
    "    #             'batch_size': {\n",
    "    #                 'values': [16, 32, 64, 128]\n",
    "    #             },\n",
    "    #             'Output_size': {\n",
    "    #                 'value': 10\n",
    "    #             }\n",
    "    # }\n",
    "    parameters_dict = {\n",
    "    'input_size': {\n",
    "        'value': args.input_size\n",
    "    },\n",
    "    'weight_init': {\n",
    "        'values': args.weight_init\n",
    "    },\n",
    "    'learning_rate': {\n",
    "        'values': args.learning_rate\n",
    "    },\n",
    "    'loss': {\n",
    "        'value': args.loss\n",
    "    },\n",
    "    'neurons': {\n",
    "        'values': args.neurons\n",
    "    },\n",
    "    'hidden_layers': {\n",
    "        'values': args.hidden_layers\n",
    "    },\n",
    "    'beta1': {\n",
    "        'value': args.beta1\n",
    "    },\n",
    "    'beta2': {\n",
    "        'value': args.beta2\n",
    "    },\n",
    "    'output_activation': {\n",
    "        'value': args.output_activation\n",
    "    },\n",
    "    'momentum': {\n",
    "        'values': args.momentum\n",
    "    },\n",
    "    'epsilon': {\n",
    "        'value': args.epsilon\n",
    "    },\n",
    "    'epochs': {\n",
    "        'value': args.epochs\n",
    "    },\n",
    "    'dataset': {\n",
    "        'value': args.dataset\n",
    "    },\n",
    "    'activation': {\n",
    "        'values': args.activation\n",
    "    },\n",
    "    'optimizer': {\n",
    "        'values': args.optimizer\n",
    "    },\n",
    "    'decay': {\n",
    "        'values': args.decay\n",
    "    },\n",
    "    'batch_size': {\n",
    "        'values': args.batch_size\n",
    "\n",
    "}"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "def load__data(type, dataset=DATASET):\n",
    "\n",
    "    x, y, x_test, y_test = None, None, None, None\n",
    "    \n",
    "    if dataset == 'mnist':\n",
    "        (x, y), (x_test, y_test) = mnist.load__data()\n",
    "    elif dataset == 'fashion_mnist':\n",
    "        (x, y), (x_test, y_test) = fashion_mnist.load__data()\n",
    "\n",
    "    if type == 'train':        \n",
    "        y = np.eye(10)[y]\n",
    "        x_shape= x.reshape(x.shape[0], 784) / 255\n",
    "        x=x_shape\n",
    "        return x, y\n",
    "    elif type == 'test':\n",
    "        xtest_reshape = x_test.reshape(x_test.shape[0], 784) / 255\n",
    "        x_test=xtest_reshape\n",
    "        y_test = np.eye(10)[y_test]\n",
    "        return x_test, y_test"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "def train(parameters):\n",
    "    x_train, y_train = load__data('train', dataset=parameters['dataset'])\n",
    "    \n",
    "    nnetwork = FeedFNetwork(input_size=parameters['input_size'], \n",
    "                         hidden_layers=parameters['hidden_layers'], \n",
    "                         neurons=parameters['neurons'], \n",
    "                         Output_size=parameters['Output_size'], \n",
    "                         act_func=parameters['activation'], \n",
    "                         ut_act_function=parameters['output_activation'],\n",
    "                         weight_init=parameters['weight_init'])\n",
    "    bp = back_propagation(nnetwork=nnetwork, \n",
    "                         loss=parameters['loss'],\n",
    "                         act_func=parameters['activation'])\n",
    "    opt = Optimizer(nnetwork=nnetwork,\n",
    "                    optimizer=parameters['optimizer'],\n",
    "                    beta=parameters['beta'],\n",
    "                    beta2=parameters['beta2'],\n",
    "                    momentum=parameters['momentum'],\n",
    "                    epsilon=parameters['epsilon'],\n",
    "                    decay=parameters['decay'],\n",
    "                    lr=parameters['learning_rate'],\n",
    "                    bp=bp,\n",
    "                    beta1=parameters['beta1'],)\n",
    "\n",
    "    batch_size = parameters['batch_size']\n",
    "    x_train_act, x_val, y_train_act, y_val = train_test_split(x_train, y_train, test_size=0.1)\n",
    "\n",
    "    print(\"Initial Accuracy: {}\".format(np.sum(np.argmax(nnetwork.forward(x_train), axis=1) == np.argmax(y_train, axis=1)) / y_train.shape[0]))\n",
    "\n",
    "    for epoch in range(parameters['epochs']):\n",
    "        for i in range(0, x_train_act.shape[0], batch_size):\n",
    "            y_batch = y_train_act[i:i+batch_size]\n",
    "            x_batch = x_train_act[i:i+batch_size]\n",
    "\n",
    "            y_pred = nnetwork.forward(x_batch)\n",
    "            D_weights, D_biases = bp.backward(y_batch, y_pred)\n",
    "            opt.run(D_weights, D_biases)\n",
    "        \n",
    "        opt.t += 1\n",
    "\n",
    "        y_pred = nnetwork.forward(x_train_act)\n",
    "        print(\"Epoch: {}, Loss: {}\".format(epoch + 1, loss(parameters['loss'], y_train_act, y_pred)))\n",
    "        print(\"Accuracy: {}\".format(np.sum(np.argmax(y_pred, axis=1) == np.argmax(y_train_act, axis=1)) / y_train_act.shape[0]))\n",
    "\n",
    "        val_accuracy = np.sum(np.argmax(nnetwork.forward(x_val), axis=1) == np.argmax(y_val, axis=1)) / y_val.shape[0]\n",
    "        print(\"Validation Accuracy: {}\".format(val_accuracy))\n",
    "\n",
    "    return nnetwork"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "parameters = {\n",
    "    'batch_size': 64,\n",
    "    'learning_rate': 0.005,\n",
    "    'neurons': 256,\n",
    "    'hidden_layers': 1,\n",
    "    'activation': 'sigmoid',\n",
    "    'weight_init': 'xavier',\n",
    "    'optimizer': 'nadam',\n",
    "    'momentum': 0.8,\n",
    "    'input_size': 784,\n",
    "    'Output_size': 10,\n",
    "    'loss': 'mean_squared_error',\n",
    "    'epochs': 10,\n",
    "    'beta1': 0.9,\n",
    "    'beta2': 0.999,\n",
    "    'output_activation': 'softmax',\n",
    "    'epsilon': 1e-8,\n",
    "    'decay': 0.0005,\n",
    "    'beta': 0.9,\n",
    "    'dataset': 'fashion_mnist'\n",
    "}\n",
    "\n",
    "# nnetwork = train(parameters)\n",
    "\n",
    "# x_test, y_test = load__data('test', dataset=parameters['dataset'])\n",
    "# y_pred = nnetwork.forward(x_test)\n",
    "# print(\"Test Accuracy: {}\".format(np.sum(np.argmax(y_pred, axis=1) == np.argmax(y_test, axis=1)) / y_test.shape[0]))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "def train_sweep():\n",
    "    run = wandb.init()\n",
    "    parameters = wandb.config\n",
    "    run.name = f\"{parameters['activation']}_neurons={parameters['neurons']}_layers={parameters['hidden_layers']}_lr={parameters['learning_rate']}_batch={parameters['batch_size']}_opt={parameters['optimizer']}_mom={parameters['momentum']}_init={parameters['weight_init']}\"\n",
    "    x_test, y_test = load__data('test', dataset=parameters['dataset'])\n",
    "    x_train, y_train = load__data('train', dataset=parameters['dataset'])\n",
    "    \n",
    "    nnetwork = FeedFNetwork(input_size=parameters['input_size'], \n",
    "                         hidden_layers=parameters['hidden_layers'], \n",
    "                         neurons=parameters['neurons'], \n",
    "                         Output_size=parameters['Output_size'], \n",
    "                         act_func=parameters['activation'], \n",
    "                         out_act_function=parameters['output_activation'],\n",
    "                         weight_init=parameters['weight_init'])\n",
    "    bp = back_propagation(nnetwork=nnetwork, \n",
    "                         loss=parameters['loss'],\n",
    "                         act_func=parameters['activation'])\n",
    "    opt = Optimizer(nnetwork=nnetwork,\n",
    "                    bp=bp,\n",
    "                    lr=parameters['learning_rate'],\n",
    "                    optimizer=parameters['optimizer'],\n",
    "                    momentum=parameters['momentum'],\n",
    "                    epsilon=parameters['epsilon'],\n",
    "                    beta1=parameters['beta1'],\n",
    "                    beta2=parameters['beta2'],\n",
    "                    decay=parameters['decay'])\n",
    "    \n",
    "    batch_size = parameters['batch_size']\n",
    "    x_train_act, x_val, y_train_act, y_val = train_test_split(x_train, y_train, test_size=0.1, random_state=42)\n",
    "\n",
    "    print(\"Initial Accuracy: {}\".format(np.sum(np.argmax(nnetwork.forward(x_train), axis=1) == np.argmax(y_train, axis=1)) / y_train.shape[0]))\n",
    "\n",
    "    for epoch in range(parameters['epochs']):\n",
    "        for i in range(0, x_train_act.shape[0], batch_size):\n",
    "            x_batch = x_train_act[i:i+batch_size]\n",
    "            y_batch = y_train_act[i:i+batch_size]\n",
    "\n",
    "            y_pred = nnetwork.forward(x_batch)\n",
    "            D_weights, D_biases = bp.backward(y_batch, y_pred)\n",
    "            # opt.run(D_weights, D_biases, y_batch, x_batch)\n",
    "            opt.run(D_weights, D_biases)\n",
    "            \n",
    "        \n",
    "        opt.t += 1\n",
    "\n",
    "        y_pred = nnetwork.forward(x_train_act)\n",
    "        wandb.log({'Epoch': epoch + 1, 'Loss': loss(parameters['loss'], y_train_act, y_pred)})\n",
    "        wandb.log({'Accuracy': np.sum(np.argmax(y_pred, axis=1) == np.argmax(y_train_act, axis=1)) / y_train_act.shape[0]})\n",
    "\n",
    "        train_loss = loss(\"cross_entropy\", y_train_act, y_pred)\n",
    "        train_accuracy = np.sum(np.argmax(y_pred, axis=1) == np.argmax(y_train_act, axis=1)) / y_train_act.shape[0]\n",
    "        val_loss = loss(\"cross_entropy\", y_val, nnetwork.forward(x_val))\n",
    "        val_accuracy = np.sum(np.argmax(nnetwork.forward(x_val), axis=1) == np.argmax(y_val, axis=1)) / y_val.shape[0]\n",
    "        # print(x_val.shape)\n",
    "        # print(x_test.shape)\n",
    "        \n",
    "\n",
    "        wandb.log({\n",
    "            \"epoch\": epoch + 1,\n",
    "            \"train_loss\": train_loss,\n",
    "            \"train_accuracy\": train_accuracy,\n",
    "            \"val_loss\": val_loss,\n",
    "            \"val_accuracy\": val_accuracy\n",
    "            \n",
    "        })\n",
    "        \n",
    "    accuracy = np.sum(np.argmax(nnetwork.forward(x_test), axis=1) == np.argmax(y_test, axis=1)) / y_test.shape[0]\n",
    "    wandb.log({\"accuracy\": accuracy})\n",
    "    \n",
    "    return nnetwork"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "def sweep(count=100, project=\"cs6910-assignment-1\"):\n",
    "    wandb_id = wandb.sweep(sweep_configuration, project=project)\n",
    "\n",
    "    wandb.agent(wandb_id, function=train_sweep, count=count)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "sweep()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "parameters = {\n",
    "    'activation': 'sigmoid',\n",
    "    'loss': 'cross_entropy',\n",
    "    'weight_init': 'xavier',\n",
    "    'epsilon': 1e-8,\n",
    "    'epochs': 10,\n",
    "    'neurons': 256,\n",
    "    'beta1': 0.9,\n",
    "    'optimizer': 'nadam',\n",
    "    'momentum': 0.8,\n",
    "    'input_size': 784,\n",
    "    'Output_size': 10,\n",
    "    'decay': 0.0005,\n",
    "    'dataset': 'fashion_mnist',\n",
    "    'output_activation': 'softmax',\n",
    "    'beta': 0.9,\n",
    "    'beta2': 0.999,\n",
    "    'hidden_layers': 1,\n",
    "    'learning_rate': 0.005,\n",
    "    'batch_size': 64,\n",
    "\n",
    "}\n",
    "\n",
    "def log_config_matrix():\n",
    "    wandb.init(project=\"cs6910-assignment-1\")\n",
    "    wandb.config.update(parameters)\n",
    "\n",
    "    nnetwork = train(parameters)\n",
    "    x_train, y_train = load__data('train', dataset=parameters['dataset'])\n",
    "    x_test, y_test = load__data('test', dataset=parameters['dataset'])\n",
    "\n",
    "    y_pred_train = nnetwork.forward(x_train)\n",
    "    wandb.log({'Train Accuracy': np.sum(np.argmax(y_pred_train, axis=1) == np.argmax(y_train, axis=1)) / y_train.shape[0]})\n",
    "\n",
    "    y_pred = nnetwork.forward(x_test)\n",
    "    wandb.log({'Test Accuracy' :np.sum(np.argmax(y_pred, axis=1) == np.argmax(y_test, axis=1)) / y_test.shape[0]})\n",
    "\n",
    "    wandb.log({'conf_mat_train': wandb.plot.confusion_matrix(probs=None, y_true=np.argmax(y_train, axis=1), preds=np.argmax(y_pred_train, axis=1), class_names=CLASS_NAMES)})\n",
    "    wandb.log({'conf_mat': wandb.plot.confusion_matrix(probs=None, y_true=np.argmax(y_test, axis=1), preds=np.argmax(y_pred, axis=1), class_names=CLASS_NAMES)})\n",
    "\n",
    "    wandb.log({'conf_mat_sklearn': wandb.sklearn.plot_confusion_matrix(np.argmax(y_test, axis=1), np.argmax(y_pred, axis=1), CLASS_NAMES)})\n",
    "    wandb.finish()\n",
    "\n",
    "log_config_matrix()\n",
    "\n",
    "\n",
    " #omlange22m012"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.10.11"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
