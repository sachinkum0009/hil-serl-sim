# hil-serl-sim
LeRobot Global Hackathon Challenge


## Commands

```bash

# to record
python lerobot/scripts/rl/gym_manipulator.py --config_path gym_hil_env_record.json

# to train 
python lerobot/scripts/rl/actor.py --config_path gym_hil_env_train_eval.json

python lerobot/scripts/rl/learner.py --config_path gym_hil_env_train.json

# to evaluate
python lerobot/scripts/rl/eval_policy.py --config_path=gym_hil_env_new.json


```