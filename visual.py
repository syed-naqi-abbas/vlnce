from vlnce_baselines.config.default import get_config
from habitat import Env
import imageio
import os

config = get_config("vlnce_baselines/config/r2r_baselines/cma.yaml")

config.TASK_CONFIG.defrost()
config.TASK_CONFIG.DATASET.SPLIT = "val_unseen"
config.TASK_CONFIG.TASK.TYPE = "Nav-v0"
config.TASK_CONFIG.TASK.SENSORS = ["SHORTEST_PATH_SENSOR"]
config.TASK_CONFIG.TASK.MEASUREMENTS = ["DISTANCE_TO_GOAL", "SUCCESS", "SPL", "PATH_LENGTH"]
config.TASK_CONFIG.freeze()

env = Env(config=config.TASK_CONFIG)

os.makedirs("data/videos", exist_ok=True)

for ep in range(3):
    obs = env.reset()
    frames = []

    while not env.episode_over:
        frame = env.sim.render(mode="rgb")
        frames.append(frame)

        obs = env.step({"action": 1})  # MOVE_FORWARD

    imageio.mimsave(f"data/videos/ep_{ep}.mp4", frames, fps=10)