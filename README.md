made by ChatGPT

# Reinforcement Learning for Carnival Atari Game

This project implements a Deep Q-Network (DQN) agent with a Convolutional Neural Network (CNN) policy to play the Carnival game from the Atari 2600 platform using the Gymnasium (formerly OpenAI Gym) environment.

## Game Description

Carnival is a "shoot 'em up" game where:
- Targets move horizontally across the screen
- The player controls a gun that can be moved horizontally
- The objective is to shoot the targets
- Ammunition is limited
- Chickens can steal bullets if not hit in time
- Rewards are given for successful hits

## Environment Details

- Game: `gymnasium.make("ALE/Carnival-v5")`
- Action Space: `Discrete(6)`
- Observation Space: `Box(0, 255, (214, 160, 3), uint8)`
  - Converted to grayscale: `(84, 84, 1)`

## Implementation Details

- Algorithm: Deep Q-Network (DQN)
- Policy: Convolutional Neural Network (CNN)
- Preprocessing: Convert observations to grayscale and resize to 84x84
- Reward: Printed after each episode

## Action Space

Carnival has an action space of `Discrete(6)`. To enable all 18 possible actions that can be performed on an Atari 2600, specify `full_action_space=True` during initialization or by passing `full_action_space=True` to `gymnasium.make`.

## Requirements

- Python 3.7+
- gymnasium[atari]
- numpy
- tensorflow
- opencv-python

## Installation

1. Clone this repository:

git clone https://github.com/Mariuscheng/carnival-rl.git
cd carnival-rl

2. Install the required packages:

pip install gymnasium[atari] numpy tensorflow opencv-python

The script will train the agent for 1000 episodes by default. The total reward for each episode will be printed, and the model will be saved every 10 episodes.

## Customization

You can modify the following parameters in the `carnival_rl.py` file:

- `n_episodes`: Number of episodes to train
- `batch_size`: Size of the batch for replay memory
- Epsilon decay parameters
- Learning rate
- Network architecture

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Gymnasium (formerly OpenAI Gym) for providing the Atari environment
- The Atari 2600 Carnival game creators



