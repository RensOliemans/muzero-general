import datetime
import os

import torch


class MuZeroConfig:
    def __init__(self):
        self.seed = 0
        self.max_num_gpus = None

        ### Game
        self.observation_shape = (7, 7, 7)
        self.action_space = list(range(7 * 7 * 4))
        self.players = list(range(2))
        self.stacked_observations = 0
        # Evaluate
        self.muzero_player = 0
        self.opponent = "random"

        ### Self-Play
        # todo: tune params
        self.num_workers = 1
        self.selfplay_on_gpu = False
        self.max_moves = 500
        self.num_simulations = 50
        self.discount = 0.997
        self.temperature_threshold = None

        # Root prior exploration noise
        self.root_dirichlet_alpha = 0.25
        self.root_exploration_fraction = 0.25

        # UCB formula
        self.pb_c_base = 19652
        self.pb_c_init = 1.25

        ### Network
        self.network = "fullyconnected"
        self.support_size = 10

        # Residual Network
        self.downsample = False
        self.blocks = 1
        self.channels = 2
        self.reduced_channels_reward = 2
        self.reduced_channels_value = 2
        self.reduced_channels_policy = 2
        self.resnet_fc_reward_layers = []
        self.resnet_fc_value_layers = []
        self.resnet_fc_policy_layers = []

        # Fully Connected Network
        # todo: change nn?
        self.encoding_size = 8
        self.fc_representation_layers = []
        self.fc_dynamics_layers = [16]
        self.fc_reward_layers = [16]
        self.fc_value_layers = [16]
        self.fc_policy_layers = [16]

        ### Training
        self.results_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "../results",
                                         os.path.basename(__file__)[:-3], datetime.datetime.now().strftime(
                "%Y-%m-%d--%H-%M-%S"))  # Path to store the model weights and TensorBoard logs
        self.save_model = True
        self.training_steps = 10000
        self.batch_size = 128
        self.checkpoint_interval = 10
        self.value_loss_weight = 1
        self.train_on_gpu = torch.cuda.is_available()

        self.optimizer = "SGD"
        self.weight_decay = 1e-4
        self.momentum = 0.9

        # Exponential learning rate schedule
        self.lr_init = 0.02
        self.lr_decay_rate = 0.9
        self.lr_decay_steps = 1000

        ### Replay Buffer
        self.replay_buffer_size = 500
        self.num_unroll_steps = 10
        self.td_steps = 50
        self.PER = True
        self.PER_alpha = 0.5

        # Reanalyze (See paper appendix Reanalyse)
        self.use_last_model_value = True
        self.reanalyse_on_gpu = False

        ### Adjust the self play / training ratio to avoid over/underfitting
        self.self_play_delay = 0
        self.training_delay = 0
        self.ratio = None

    def visit_softmax_temperature_fn(self, trained_steps):
        return 1


