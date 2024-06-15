import pickle
import ndjson
import json
import tiktoken
from prompt_message import system_message, generate_user_message, generate_assistant_message

data = pickle.load(open('data/cached_nuscenes_info.pkl', 'rb'))
split = json.load(open('data/split.json', 'r'))

'''
NuScenes 是一个用于自动驾驶和机器人领域的开源数据集，由位于美国马萨诸塞州剑桥市的公司 nuTonomy 创建。
该数据集提供了大量在城市环境中采集的传感器数据，包括相机、激光雷达（LiDAR）、雷达和全球定位系统（GPS）等。
NuScenes 数据集的主要作用是用于开发和评估自动驾驶车辆和机器人的感知、定位、路径规划等功能。
具体来说，NuScenes 数据集可用于以下方面：
一、 训练和评估感知系统：通过提供大规模的真实世界场景数据，
    可以用于训练和评估自动驾驶车辆和机器人的感知系统，如目标检测、目标跟踪、语义分割等。
二、 测试和验证路径规划算法：NuScenes 数据集中包含丰富的车辆轨迹信息，
    可以用于测试和验证自动驾驶车辆和机器人的路径规划算法，以确保其在复杂城市环境中的有效性和鲁棒性。
三、 开发和评估定位系统：由于NuScenes 数据集提供了高精度的全球定位系统（GPS）数据以及激光雷达等传感器数据，
    因此可用于开发和评估车辆和机器人的定位系统。
四、 研究和开发新技术：NuScenes 数据集为研究人员和开发者提供了一个标准的基准，
    可以用于比较不同算法的性能，并促进自动驾驶和机器人领域的技术创新。
'''

train_tokens = split["train"]
val_tokens = split["val"]
num_train_samples = len(train_tokens)
train_ratio = 1

encoding = tiktoken.encoding_for_model("gpt-3.5-turbo")

num_language_tokens = 0
num_system_tokens = 0
num_user_tokens = 0
num_assistant_tokens = 0

traj_only = False

train_messages = []
for token_i, token in enumerate(train_tokens):
    if token_i >= train_ratio * num_train_samples:
        break 
    user_message = generate_user_message(data, token)
    assitant_message = generate_assistant_message(data, token, traj_only=traj_only)
    if len(assitant_message.split("\n")) > 6:
        print()
        print(token)
        print(system_message)
        print(user_message)
        print(assitant_message)
    num_language_tokens += len(encoding.encode(system_message))
    num_system_tokens += len(encoding.encode(system_message))
    num_language_tokens += len(encoding.encode(user_message))
    num_user_tokens += len(encoding.encode(user_message))
    num_language_tokens += len(encoding.encode(assitant_message))
    num_assistant_tokens += len(encoding.encode(assitant_message))


    train_message = {"messages": 
        [
            {"role": "system", "content": system_message},
            {"role": "user", "content": user_message}, 
            {"role": "assistant", "content": assitant_message}
        ]
    }
    train_messages.append(train_message)

print("#### Cost Summarization ####")
print(f"Number of system tokens: {num_system_tokens}")
print(f"Number of user tokens: {num_user_tokens}")
print(f"Number of assistant tokens: {num_assistant_tokens}")
print(f"Number of total tokens: {num_language_tokens}")

with open("data/train.json", "w") as f:
    ndjson.dump(train_messages, f)